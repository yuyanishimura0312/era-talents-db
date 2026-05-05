#!/usr/bin/env python3
"""
Phase 4: 関係ネットワーク構築
- 人物関係テーブル設計（師弟・メンター・思想継承・所属）
- 既存データから関係抽出（mentors JSON配列、education_path、source_team等）
- Great Figures DB の person_relations を取り込み
- gap_insights テーブル充填（L1とL2のズレから新知見を生成）
"""
import sqlite3
import json
from pathlib import Path
from collections import defaultdict

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"
GREAT_FIGURES_DB = Path.home() / "projects/research/great-figures-db/great_figures.db"


def setup_relations_schema(dst):
    """関係テーブルとネットワーク分析用のテーブルを追加"""
    dst.executescript("""
        CREATE TABLE IF NOT EXISTS person_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_id INTEGER NOT NULL REFERENCES achievers(id),
            to_id INTEGER REFERENCES achievers(id),
            to_name_ja TEXT,        -- 関係先がDBに未登録の場合の文字列名
            relation_type TEXT NOT NULL,  -- mentor, disciple, influenced_by, colleague, family, succession, opposed
            strength INTEGER CHECK(strength BETWEEN 1 AND 10),
            cross_era INTEGER DEFAULT 0,
            description TEXT,
            source TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_relations_from ON person_relations(from_id);
        CREATE INDEX IF NOT EXISTS idx_relations_to ON person_relations(to_id);
        CREATE INDEX IF NOT EXISTS idx_relations_type ON person_relations(relation_type);

        CREATE TABLE IF NOT EXISTS network_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            achiever_id INTEGER NOT NULL REFERENCES achievers(id) UNIQUE,
            in_degree INTEGER DEFAULT 0,
            out_degree INTEGER DEFAULT 0,
            betweenness REAL,
            era_bridges INTEGER DEFAULT 0,
            domain_bridges INTEGER DEFAULT 0,
            updated_at TEXT DEFAULT (datetime('now'))
        );
    """)
    dst.commit()


def extract_relations_from_mentors(dst):
    """mentors フィールド（JSON配列）から関係を抽出"""
    rows = dst.execute("""
        SELECT id, name_ja, mentors FROM achievers
        WHERE mentors IS NOT NULL AND mentors != '' AND mentors != '[]'
    """).fetchall()

    inserted = 0
    for aid, name, mentors_json in rows:
        try:
            mentors = json.loads(mentors_json) if mentors_json.startswith('[') else [mentors_json]
        except Exception:
            mentors = [m.strip() for m in mentors_json.split(',')]

        for mentor_name in mentors:
            if not mentor_name or len(mentor_name) < 2:
                continue
            mentor_name = mentor_name.strip().strip('"').strip("'")

            # メンターがDBに登録されているか
            mentor_row = dst.execute(
                "SELECT id FROM achievers WHERE name_ja=? OR name_en=? LIMIT 1",
                (mentor_name, mentor_name)
            ).fetchone()
            mentor_id = mentor_row[0] if mentor_row else None

            try:
                dst.execute("""
                    INSERT INTO person_relations
                    (from_id, to_id, to_name_ja, relation_type, strength, source)
                    VALUES (?, ?, ?, 'mentor', 7, 'extracted_from_mentors_field')
                """, (aid, mentor_id, mentor_name))
                inserted += 1
            except Exception:
                pass

    dst.commit()
    return inserted


def import_great_figures_relations(dst):
    """Great Figures DBの person_relations から日本人関連を取り込み"""
    if not GREAT_FIGURES_DB.exists():
        return 0

    src = sqlite3.connect(GREAT_FIGURES_DB)
    src.row_factory = sqlite3.Row

    tables = [r[0] for r in src.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]

    if "person_relations" not in tables:
        src.close()
        return 0

    cols = [r[1] for r in src.execute("PRAGMA table_info(person_relations)").fetchall()]

    # 名前ベースでマッチング
    name_id_map = {}
    rows = dst.execute("SELECT id, name_ja FROM achievers WHERE name_ja IS NOT NULL").fetchall()
    for aid, name in rows:
        name_id_map[name] = aid

    # GF DBの関係取得
    rel_rows = src.execute(f"SELECT * FROM person_relations LIMIT 5000").fetchall()

    inserted = 0
    for r in rel_rows:
        d = dict(r)
        # スキーマに依存しない柔軟な取り扱い
        from_name = None
        to_name = None
        rel_type = d.get("relation_type") or d.get("type") or "influenced_by"

        # from/to 取得（id→name の解決が必要）
        from_pid = d.get("from_person_id") or d.get("person_a_id") or d.get("from_id")
        to_pid = d.get("to_person_id") or d.get("person_b_id") or d.get("to_id")

        if from_pid:
            try:
                pname = src.execute(
                    "SELECT name_ja FROM persons WHERE id=?", (from_pid,)
                ).fetchone()
                if pname:
                    from_name = pname[0]
            except Exception:
                pass
        if to_pid:
            try:
                pname = src.execute(
                    "SELECT name_ja FROM persons WHERE id=?", (to_pid,)
                ).fetchone()
                if pname:
                    to_name = pname[0]
            except Exception:
                pass

        if not from_name:
            continue

        from_id = name_id_map.get(from_name)
        to_id = name_id_map.get(to_name) if to_name else None

        if not from_id and not to_id:
            continue  # 両方未登録なら scrap

        try:
            # from が登録済みなら from→to で投入
            if from_id:
                dst.execute("""
                    INSERT INTO person_relations
                    (from_id, to_id, to_name_ja, relation_type, strength, source)
                    VALUES (?, ?, ?, ?, 6, 'great_figures_db')
                """, (from_id, to_id, to_name, rel_type))
                inserted += 1
            elif to_id:
                # to が登録済みで from が未登録 → from を to_name に入れて反転
                dst.execute("""
                    INSERT INTO person_relations
                    (from_id, to_id, to_name_ja, relation_type, strength, source)
                    VALUES (?, NULL, ?, ?, 6, 'great_figures_db_reversed')
                """, (to_id, from_name, "influenced_by"))
                inserted += 1
        except Exception:
            pass

    dst.commit()
    src.close()
    return inserted


def compute_network_metrics(dst):
    """各人物の入次数・出次数を計算"""
    dst.execute("DELETE FROM network_metrics")

    # 入次数（参照される回数）
    in_rows = dst.execute("""
        SELECT to_id, COUNT(*) FROM person_relations
        WHERE to_id IS NOT NULL GROUP BY to_id
    """).fetchall()
    in_map = {r[0]: r[1] for r in in_rows}

    # 出次数（参照する回数）
    out_rows = dst.execute("""
        SELECT from_id, COUNT(*) FROM person_relations GROUP BY from_id
    """).fetchall()
    out_map = {r[0]: r[1] for r in out_rows}

    # 時代を跨ぐエッジ数
    cross_era_rows = dst.execute("""
        SELECT pr.from_id, COUNT(*) FROM person_relations pr
        JOIN achievers a1 ON pr.from_id=a1.id
        JOIN achievers a2 ON pr.to_id=a2.id
        WHERE a1.primary_era_id != a2.primary_era_id
        GROUP BY pr.from_id
    """).fetchall()
    cross_era_map = {r[0]: r[1] for r in cross_era_rows}

    # ドメインを跨ぐエッジ数
    domain_bridge_rows = dst.execute("""
        SELECT pr.from_id, COUNT(*) FROM person_relations pr
        JOIN achievers a1 ON pr.from_id=a1.id
        JOIN achievers a2 ON pr.to_id=a2.id
        WHERE a1.domain != a2.domain
        GROUP BY pr.from_id
    """).fetchall()
    domain_bridge_map = {r[0]: r[1] for r in domain_bridge_rows}

    all_ids = set(in_map.keys()) | set(out_map.keys())
    for aid in all_ids:
        try:
            dst.execute("""
                INSERT OR REPLACE INTO network_metrics
                (achiever_id, in_degree, out_degree, era_bridges, domain_bridges)
                VALUES (?, ?, ?, ?, ?)
            """, (aid,
                  in_map.get(aid, 0), out_map.get(aid, 0),
                  cross_era_map.get(aid, 0), domain_bridge_map.get(aid, 0)))
        except Exception:
            pass

    dst.commit()
    return len(all_ids)


def generate_gap_insights(dst):
    """L1（当時言説）とL2（事後評価）のギャップから知見を抽出"""
    dst.execute("DELETE FROM gap_insights")

    # 各時代×各能力の言説と事後評価を集約
    insights = []

    # 1. 「明治期に重視されなかったが現代から振り返ると重要だった」パターン
    for era in ["meiji", "taisho", "showa_pre", "showa_post", "heisei"]:
        # L2で頻出だがL1で言及少ない能力を抽出
        l2_findings = dst.execute("""
            SELECT capability_id, COUNT(*) c FROM era_retrospectives
            WHERE era_id=? AND capability_id IS NOT NULL
            GROUP BY capability_id ORDER BY c DESC LIMIT 5
        """, (era,)).fetchall()
        l1_findings = dst.execute("""
            SELECT capability_id, COUNT(*) c FROM era_discourses
            WHERE era_id=? AND capability_id IS NOT NULL
            GROUP BY capability_id
        """, (era,)).fetchall()
        l1_map = {r[0]: r[1] for r in l1_findings}

        for cap_id, l2_count in l2_findings:
            l1_count = l1_map.get(cap_id, 0)
            if l1_count == 0 and l2_count >= 2:
                cap_name = dst.execute(
                    "SELECT name_ja FROM capability_dimensions WHERE id=?", (cap_id,)
                ).fetchone()
                if cap_name:
                    insights.append({
                        "type": "l1_l2_gap",
                        "title": f"{era}に「{cap_name[0]}」は事後重視されたが当時は言及少",
                        "desc": f"{era}期において、現代の研究は「{cap_name[0]}」の重要性を{l2_count}件指摘しているが、当時の言説では明示されていなかった。これは時代の盲点を示唆する。",
                        "eras": [era],
                        "caps": [cap_id],
                        "edu": f"現代の教育では、{cap_name[0]}を意識的にカリキュラムに組み込むことで、当時の盲点を補完できる",
                        "hire": f"採用要件として{cap_name[0]}を明示的に評価することで、見落とされがちな潜在力を発掘できる",
                        "org": f"組織設計では{cap_name[0]}を発揮できる場と評価制度の設計が不可欠",
                        "conf": 6
                    })

    # 2. 時代を跨いで一貫して重要な能力
    consistent = dst.execute("""
        SELECT capability_id, COUNT(DISTINCT era_id) era_count, COUNT(*) total
        FROM era_retrospectives
        WHERE capability_id IS NOT NULL
        GROUP BY capability_id
        HAVING era_count >= 3
        ORDER BY total DESC
        LIMIT 5
    """).fetchall()
    for cap_id, era_count, total in consistent:
        cap_row = dst.execute("SELECT name_ja FROM capability_dimensions WHERE id=?", (cap_id,)).fetchone()
        if not cap_row:
            continue
        insights.append({
            "type": "cross_era",
            "title": f"「{cap_row[0]}」は時代を跨いで一貫して重要",
            "desc": f"事後評価において「{cap_row[0]}」は{era_count}時代にわたり計{total}件言及されており、時代を超えた普遍的能力と言える。",
            "eras": ["all"],
            "caps": [cap_id],
            "edu": f"普遍的能力として{cap_row[0]}は基礎教育の柱に据えるべき",
            "hire": f"{cap_row[0]}は時代を超えて評価される能力なので、長期キャリア形成の核",
            "org": f"組織の継続的価値創造には{cap_row[0]}を持つ人材の安定確保が不可欠",
            "conf": 8
        })

    # 3. 未来予測で頻出する能力（過去になかった）
    future_caps = dst.execute("""
        SELECT capability_id, COUNT(*) c FROM future_demands
        WHERE capability_id IS NOT NULL
        GROUP BY capability_id ORDER BY c DESC LIMIT 5
    """).fetchall()
    for cap_id, count in future_caps:
        past_count = dst.execute("""
            SELECT COUNT(*) FROM era_retrospectives
            WHERE capability_id=? AND era_id IN ('meiji','taisho','showa_pre','showa_post')
        """, (cap_id,)).fetchone()[0]
        if past_count == 0 and count >= 5:
            cap_row = dst.execute("SELECT name_ja FROM capability_dimensions WHERE id=?", (cap_id,)).fetchone()
            if not cap_row:
                continue
            insights.append({
                "type": "era_to_future",
                "title": f"未来固有能力「{cap_row[0]}」",
                "desc": f"未来予測で{count}件言及されているが、過去には事後評価でも見当たらない新しい能力次元。{cap_row[0]}は未来固有の要求である。",
                "eras": ["future_2030", "future_2050", "future_2100"],
                "caps": [cap_id],
                "edu": f"既存教育パラダイムには存在しない{cap_row[0]}を新規カリキュラムとして設計する必要がある",
                "hire": f"{cap_row[0]}の評価は既存の採用基準では不可能。新たな評価フレームが必要",
                "org": f"{cap_row[0]}を発揮できる組織形態の刷新が、未来適応の鍵になる",
                "conf": 7
            })

    # 投入
    for ins in insights:
        try:
            dst.execute("""
                INSERT INTO gap_insights
                (insight_type, title_ja, description_ja, related_eras, related_capabilities,
                 implications_education, implications_hiring, implications_org, confidence)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (ins["type"], ins["title"], ins["desc"],
                  json.dumps(ins["eras"], ensure_ascii=False),
                  json.dumps(ins["caps"], ensure_ascii=False),
                  ins["edu"], ins["hire"], ins["org"], ins["conf"]))
        except Exception as e:
            pass

    dst.commit()
    return len(insights)


def main():
    dst = sqlite3.connect(ERA_DB)

    print("=== Phase 4: 関係ネットワーク構築 ===\n")

    print("[1] 関係テーブル・スキーマ準備")
    setup_relations_schema(dst)
    print("  完了\n")

    print("[2] mentors フィールドから関係抽出")
    n = extract_relations_from_mentors(dst)
    print(f"  抽出: {n} 関係\n")

    print("[3] Great Figures DB から関係取り込み")
    try:
        n = import_great_figures_relations(dst)
        print(f"  取り込み: {n} 関係\n")
    except Exception as e:
        print(f"  ERROR: {e}\n")

    print("[4] ネットワークメトリクス計算")
    n = compute_network_metrics(dst)
    print(f"  計算対象: {n} 人\n")

    print("[5] gap_insights 生成（L1×L2×L4 ギャップ知見）")
    n = generate_gap_insights(dst)
    print(f"  生成: {n} 知見\n")

    # 最終
    print("=== Phase 4 完了状態 ===")
    for table in ["achievers", "achiever_capabilities", "era_discourses",
                  "era_retrospectives", "future_demands", "academic_references",
                  "data_sources", "person_relations", "network_metrics", "gap_insights"]:
        try:
            c = dst.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"  {table}: {c:,}")
        except Exception:
            pass

    # トップ影響力人物
    print("\n=== ネットワーク中心性 TOP 15 ===")
    top = dst.execute("""
        SELECT a.name_ja, a.primary_era_id, a.domain,
               nm.in_degree, nm.out_degree, nm.era_bridges, nm.domain_bridges
        FROM network_metrics nm
        JOIN achievers a ON nm.achiever_id = a.id
        ORDER BY (nm.in_degree + nm.out_degree) DESC
        LIMIT 15
    """).fetchall()
    print(f"  {'名前':<20} {'時代':<10} {'分野':<15} in out era_b dom_b")
    for r in top:
        print(f"  {(r[0] or '?')[:18]:<20} {r[1]:<10} {(r[2] or '?'):<15} {r[3]:>3} {r[4]:>3} {r[5]:>5} {r[6]:>5}")

    dst.close()


if __name__ == "__main__":
    main()

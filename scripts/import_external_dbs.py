#!/usr/bin/env python3
"""
miratuku-news-v2 統合DB群（30DB・15.2M+レコード）から
era-talents-db への構造化インポートパイプライン

対象DB:
- experts-db (3,995人 政府委員・有識者) → L3 政治・行政
- great-figures-db (9,178人物 + 568概念 + 10,033イベント) → L3 横断
- investment-signal-radar v2 (4,180組織) → L3 令和起業家
- foresight-knowledge-base (309機関 / 45,323レポート / 23,272予測) → L4
- futures-studies-db (448研究者 / 507概念) → L4
- academic-knowledge-db (8,212知識単位) → L2
- innovation-theory-db → L2
- management-concepts-db → L2
- pestle-signal-db (196,714記事) → L1
- cla-db (91,550レコード 127年統合CLA) → L1
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"

# 既存DBのパス
EXTERNAL = {
    "experts": Path.home() / "projects/research/experts-db/data/experts.db",
    "great_figures": Path.home() / "projects/research/great-figures-db/great_figures.db",
    "investment_v2": Path.home() / "projects/research/investment-signal-radar/data/investment_signal_v2.db",
    "foresight_kb": Path.home() / "projects/research/foresight-knowledge-base/data/foresight_knowledge.db",
    "foresight_legacy": Path.home() / "projects/research/foresight-knowledge-base/foresight.db",
    "futures": Path.home() / "projects/research/futures-studies-db/data/futures_studies.db",
    "academic_knowledge": Path.home() / "projects/research/academic-knowledge-db/academic_knowledge.db",
    "policy": Path.home() / "projects/apps/policy-db/data/policy_new.db",
}


def determine_era(birth_year):
    """生年から時代区分を決定"""
    if not birth_year or birth_year < 1850:
        return None
    # 主要活躍時期は概ね30-60歳と仮定 → 生年+45を活躍中年
    active = birth_year + 45
    if active < 1912:
        return "meiji"
    if active < 1926:
        return "taisho"
    if active < 1946:
        return "showa_pre"
    if active < 1989:
        return "showa_post"
    if active < 2019:
        return "heisei"
    return "reiwa"


def map_category_to_domain(category_primary):
    """great-figures の category_primary を era-talents-db の domain にマッピング"""
    mapping = {
        "monarch": "politics",
        "statesman": "politics",
        "military": "military",
        "merchant": "business",
        "thinker": "education_thought",
        "religious": "religion",
        "revolutionary": "social_movement",
        "explorer": "exploration",
        "inventor": "science_tech",
        "scientist": "science_tech",
        "economist": "business",
        "manager": "business",
        "diplomat": "politics",
        "legal": "professional",
        "social_reformer": "social_movement",
        "cultural": "culture_arts",
        "spy": "other",
        "other": "other",
    }
    return mapping.get(category_primary, "other")


def import_great_figures():
    """great-figures-db の日本人持ち込み（明治以降）"""
    src = sqlite3.connect(EXTERNAL["great_figures"])
    dst = sqlite3.connect(ERA_DB)
    src.row_factory = sqlite3.Row

    rows = src.execute("""
        SELECT name_ja, name_en, birth_year, death_year, category_primary,
               summary_ja, entrepreneur_score, region_primary, country_modern, era
        FROM persons
        WHERE (country_modern LIKE '%Japan%' OR country_modern LIKE '%日本%')
          AND birth_year >= 1840
          AND era IN ('modern', 'contemporary', 'early_modern')
    """).fetchall()

    inserted = 0
    skipped_dup = 0
    for r in rows:
        era_id = determine_era(r["birth_year"])
        if not era_id:
            continue
        domain = map_category_to_domain(r["category_primary"])

        # 重複チェック
        existing = dst.execute(
            "SELECT id FROM achievers WHERE name_ja=? AND birth_year IS ?",
            (r["name_ja"], r["birth_year"])
        ).fetchone()
        if existing:
            skipped_dup += 1
            continue

        dst.execute("""
            INSERT INTO achievers (name_ja, name_en, birth_year, death_year,
                primary_era_id, domain, achievement_summary, is_traditional_great,
                source_team, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, 1, 'import_great_figures', ?)
        """, (
            r["name_ja"], r["name_en"], r["birth_year"], r["death_year"],
            era_id, domain,
            r["summary_ja"] or f"{r['category_primary']}として活動",
            f"category_primary={r['category_primary']}, region={r['region_primary']}"
        ))
        inserted += 1

    dst.commit()
    src.close()
    dst.close()
    return inserted, skipped_dup


def import_experts_db():
    """experts-db (3,995人 政府委員) の取り込み（令和期 政治・行政）"""
    src = sqlite3.connect(EXTERNAL["experts"])
    dst = sqlite3.connect(ERA_DB)
    src.row_factory = sqlite3.Row

    rows = src.execute("""
        SELECT canonical_name, name_kana, field, org_position, org_name, notes
        FROM persons
        WHERE canonical_name IS NOT NULL AND canonical_name != ''
    """).fetchall()

    inserted = 0
    skipped_dup = 0
    for r in rows:
        # 政府委員・有識者は基本「令和」で投入（Phase 3で時代調整）
        existing = dst.execute(
            "SELECT id FROM achievers WHERE name_ja=?",
            (r["canonical_name"],)
        ).fetchone()
        if existing:
            skipped_dup += 1
            continue

        domain = "politics"  # 大半が政府関連
        if r["field"]:
            field = r["field"].lower()
            if "経済" in field or "産業" in field:
                domain = "business"
            elif "科学" in field or "技術" in field or "医" in field:
                domain = "science_tech"
            elif "文化" in field or "芸術" in field:
                domain = "culture_arts"
            elif "教育" in field:
                domain = "education_thought"

        achievement = f"{r['org_position'] or ''} ({r['org_name'] or ''}); {r['field'] or ''}"

        dst.execute("""
            INSERT INTO achievers (name_ja, name_kana, primary_era_id, domain,
                achievement_summary, is_traditional_great, is_local_excellent,
                source_team, notes)
            VALUES (?, ?, 'reiwa', ?, ?, 0, 1, 'import_experts', ?)
        """, (
            r["canonical_name"], r["name_kana"], domain, achievement, r["notes"] or ""
        ))
        inserted += 1

    dst.commit()
    src.close()
    dst.close()
    return inserted, skipped_dup


def import_investment_signal():
    """investment_signal_v2 の起業家・組織情報を令和期実業として取り込み"""
    src = sqlite3.connect(EXTERNAL["investment_v2"])
    dst = sqlite3.connect(ERA_DB)
    src.row_factory = sqlite3.Row

    # 組織を「実業」として取り込み（人物名でなく組織名だが、創業者プールとして残す）
    rows = src.execute("""
        SELECT name, name_en, founded_date, description, region, city, website
        FROM organizations
        WHERE primary_role IN ('company', 'accelerator')
          AND status = 'active'
          AND name IS NOT NULL
        LIMIT 1500
    """).fetchall()

    inserted = 0
    skipped_dup = 0
    for r in rows:
        # 「組織名」なので achievers ではなく notes 経由で活用
        # ここでは entry を skip し、別途人物データを抽出する仕組みを作る
        pass

    src.close()
    dst.close()
    return 0, 0  # 組織データは別途専用テーブルで管理推奨


def import_foresight_kb_l4():
    """foresight-knowledge-base から未来予測 L4 拡張"""
    candidates = [EXTERNAL["foresight_kb"], EXTERNAL["foresight_legacy"]]
    src_path = next((p for p in candidates if p.exists()), None)
    if not src_path:
        return 0, 0

    src = sqlite3.connect(src_path)
    src.row_factory = sqlite3.Row

    # テーブル確認
    tables = [r[0] for r in src.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]

    if not tables:
        src.close()
        return 0, 0

    dst = sqlite3.connect(ERA_DB)
    inserted = 0

    # 予測テーブルがあれば取り込み
    pred_tables = [t for t in tables if "predict" in t.lower() or "forecast" in t.lower() or "trend" in t.lower()]
    for tbl in pred_tables[:1]:  # 最初の予測テーブルのみ
        try:
            rows = src.execute(f"SELECT * FROM {tbl} LIMIT 100").fetchall()
            for r in rows:
                d = dict(r)
                title = d.get("title") or d.get("name") or d.get("trend_name") or "未来予測"
                content = d.get("description") or d.get("content") or d.get("summary") or ""
                year = d.get("target_year") or d.get("year") or 2030

                era_id = "future_2030"
                if year >= 2080:
                    era_id = "future_2100"
                elif year >= 2040:
                    era_id = "future_2050"

                if not content or len(content) < 30:
                    continue

                dst.execute("""
                    INSERT INTO future_demands (era_id, scenario, source_title, source_org,
                        source_year, finding_ja, confidence, is_unique_to_era)
                    VALUES (?, 'baseline', ?, 'Foresight Knowledge Base', ?, ?, 6, 0)
                """, (era_id, title[:200], year, content[:500]))
                inserted += 1
        except Exception as e:
            print(f"  Skip {tbl}: {e}")

    dst.commit()
    src.close()
    dst.close()
    return inserted, 0


def import_data_source_registry():
    """30DB全体をdata_sources参照テーブルとして登録"""
    dst = sqlite3.connect(ERA_DB)

    # data_sources テーブル作成（外部DBとの紐付け）
    dst.execute("""
        CREATE TABLE IF NOT EXISTS data_sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id TEXT UNIQUE,
            name_ja TEXT NOT NULL,
            name_en TEXT,
            layer TEXT,
            stat TEXT,
            repo TEXT,
            dashboard TEXT,
            local_path TEXT,
            relevance_layers TEXT,  -- JSON: ["L1", "L3"]
            integration_status TEXT,  -- imported, pending, n/a
            notes TEXT
        )
    """)

    registry = json.load(open(Path.home() / "projects/apps/miratuku-news-v2/data/db-registry.json"))

    inserted = 0
    for layer in registry["layers"]:
        for db in layer["databases"]:
            sid = db.get("id") or db.get("name")
            try:
                dst.execute("""
                    INSERT OR REPLACE INTO data_sources
                    (source_id, name_ja, name_en, layer, stat, repo, dashboard, integration_status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    sid, db.get("nameJa") or db.get("name"), db.get("name"),
                    layer["id"], db.get("stat"), db.get("repo"), db.get("dashboard"),
                    "pending"
                ))
                inserted += 1
            except Exception as e:
                pass

    for sup in registry["supplementary"]:
        sid = sup.get("id") or sup.get("name")
        try:
            dst.execute("""
                INSERT OR REPLACE INTO data_sources
                (source_id, name_ja, name_en, layer, stat, repo, dashboard, integration_status)
                VALUES (?, ?, ?, 'supplementary', ?, ?, ?, ?)
            """, (
                sid, sup.get("nameJa") or sup.get("name"), sup.get("name"),
                sup.get("stat"), sup.get("repo"), sup.get("dashboard"), "pending"
            ))
            inserted += 1
        except Exception as e:
            pass

    dst.commit()
    dst.close()
    return inserted


def main():
    print(f"=== era-talents-db 外部DB統合インポート開始 ===")
    print(f"  実行時刻: {datetime.now().isoformat()}\n")

    # 1. 30DBレジストリ登録
    print("[1] 30DBデータソース・レジストリ登録")
    n = import_data_source_registry()
    print(f"  登録: {n} DB\n")

    # 2. great-figures からの取り込み
    print("[2] great-figures-db (日本人・明治以降) 取り込み")
    try:
        inserted, dup = import_great_figures()
        print(f"  新規: {inserted} 人 / 重複スキップ: {dup}\n")
    except Exception as e:
        print(f"  ERROR: {e}\n")

    # 3. experts-db からの取り込み
    print("[3] experts-db (政府委員・有識者 3,995人) 取り込み")
    try:
        inserted, dup = import_experts_db()
        print(f"  新規: {inserted} 人 / 重複スキップ: {dup}\n")
    except Exception as e:
        print(f"  ERROR: {e}\n")

    # 4. foresight-kb からのL4取り込み
    print("[4] foresight-knowledge-base L4 未来予測 取り込み")
    try:
        inserted, _ = import_foresight_kb_l4()
        print(f"  新規: {inserted} 件\n")
    except Exception as e:
        print(f"  ERROR: {e}\n")

    # 最終状態
    dst = sqlite3.connect(ERA_DB)
    print("=== インポート後の合計 ===")
    for table in ["achievers", "achiever_capabilities", "era_discourses",
                  "era_retrospectives", "future_demands", "academic_references", "data_sources"]:
        try:
            c = dst.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"  {table}: {c}")
        except Exception:
            pass
    dst.close()


if __name__ == "__main__":
    main()

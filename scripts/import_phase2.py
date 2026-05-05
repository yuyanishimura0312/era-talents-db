#!/usr/bin/env python3
"""
Phase 2: 学術理論・PESTLE言説・CLA構造の取り込み
- academic-knowledge-db: humanities_concept (1,385), social_theory (936) → L2 事後評価
- pestle-signal-db: cla_analyses, articles → L1 当時言説
- innovation-theory-db (academic.db内): innovation_theories
"""
import sqlite3
import json
from pathlib import Path

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"
ACADEMIC_DB = Path.home() / "projects/research/academic-knowledge-db/academic.db"
PESTLE_DB = Path.home() / "projects/research/pestle-signal-db/data/pestle.db"
CLA_DB = Path.home() / "projects/research/pestle-signal-db/data/cla.db"


def map_era_from_year(year):
    if not year:
        return None
    if year < 1912:
        return "meiji"
    if year < 1926:
        return "taisho"
    if year < 1946:
        return "showa_pre"
    if year < 1989:
        return "showa_post"
    if year < 2019:
        return "heisei"
    return "reiwa"


def import_social_theories():
    """social_theory (936件) を era_retrospectives へ取り込み"""
    src = sqlite3.connect(ACADEMIC_DB)
    src.row_factory = sqlite3.Row
    dst = sqlite3.connect(ERA_DB)

    # 人材論・教育論・能力論・社会階層論に関連するものを優先
    keywords = ['人材', '能力', '教育', '才能', '卓越', 'タレント',
                'リーダー', 'エリート', '知性', '知能', '創造', 'スキル',
                '階層', 'メリトクラシー', '学歴', '社会移動', '威信',
                '労働', '就業', 'キャリア', '生涯学習',
                'leadership', 'talent', 'meritocracy', 'mobility', 'gift',
                'creativity', 'expertise', 'skill', 'competence']
    where_clauses = " OR ".join(
        [f"keywords_ja LIKE '%{k}%' OR name_ja LIKE '%{k}%' OR definition LIKE '%{k}%'" for k in keywords]
    )

    rows = src.execute(f"""
        SELECT name_ja, name_en, definition, impact_summary, subfield,
               school_of_thought, era_start, era_end, keywords_ja
        FROM social_theory
        WHERE {where_clauses}
        LIMIT 500
    """).fetchall()

    inserted = 0
    for r in rows:
        # era_start から時代を決定
        era_id = map_era_from_year(r["era_start"])
        if not era_id:
            era_id = "showa_post"  # デフォルト

        finding = (r["impact_summary"] or r["definition"] or "")[:500]
        if not finding:
            continue

        try:
            dst.execute("""
                INSERT INTO era_retrospectives
                (era_id, perspective, source_title, source_author, source_year,
                 finding_ja, relevance_score, diverges_from_l1)
                VALUES (?, 'social_theory', ?, ?, ?, ?, 7, 0)
            """, (
                era_id, r["name_ja"][:200], r["school_of_thought"] or "academic-knowledge-db",
                r["era_start"], finding
            ))
            inserted += 1
        except Exception as e:
            pass

    dst.commit()
    src.close()
    dst.close()
    return inserted


def import_humanities_concepts():
    """humanities_concept (1,385件) から人物・教育関連を era_retrospectives 補強"""
    src = sqlite3.connect(ACADEMIC_DB)
    src.row_factory = sqlite3.Row
    dst = sqlite3.connect(ERA_DB)

    # スキーマ確認
    cols = [r[1] for r in src.execute("PRAGMA table_info(humanities_concept)").fetchall()]

    # 人物・能力関連のキーワードを含むもの
    rows = src.execute("""
        SELECT * FROM humanities_concept
        WHERE name_ja LIKE '%人%' OR name_ja LIKE '%教育%' OR name_ja LIKE '%能力%'
           OR name_ja LIKE '%才%' OR name_ja LIKE '%学%' OR name_ja LIKE '%教養%'
        LIMIT 200
    """).fetchall()

    inserted = 0
    for r in rows:
        d = dict(r)
        finding = (d.get("impact_summary") or d.get("definition") or "")[:500]
        if not finding or len(finding) < 30:
            continue

        era_start = d.get("era_start")
        era_id = map_era_from_year(era_start) or "showa_post"

        try:
            dst.execute("""
                INSERT INTO era_retrospectives
                (era_id, perspective, source_title, source_year,
                 finding_ja, relevance_score)
                VALUES (?, 'humanities_concept', ?, ?, ?, 6)
            """, (era_id, d.get("name_ja", "")[:200], era_start, finding))
            inserted += 1
        except Exception:
            pass

    dst.commit()
    src.close()
    dst.close()
    return inserted


def import_cla_analyses():
    """cla.db の CLA 分析（127年・年次/四半期）を era_discourses に取り込み"""
    if not CLA_DB.exists():
        return 0

    src = sqlite3.connect(CLA_DB)
    src.row_factory = sqlite3.Row

    # cla_analyses の存在確認
    tables = [r[0] for r in src.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]

    if "cla_analyses" not in tables:
        src.close()
        return 0

    # スキーマ確認
    cols = [r[1] for r in src.execute("PRAGMA table_info(cla_analyses)").fetchall()]

    # year, litany, systemic, worldview, myth など想定
    year_col = "year" if "year" in cols else None
    if not year_col:
        for c in cols:
            if "year" in c.lower():
                year_col = c
                break

    if not year_col:
        src.close()
        return 0

    # 各時代から代表的なCLAを最大80件
    rows = src.execute(f"""
        SELECT * FROM cla_analyses
        WHERE {year_col} >= 1900
        ORDER BY {year_col}
        LIMIT 200
    """).fetchall()

    dst = sqlite3.connect(ERA_DB)
    inserted = 0
    for r in rows:
        d = dict(r)
        year = d.get(year_col)
        era_id = map_era_from_year(year)
        if not era_id:
            continue

        # litany / systemic / worldview / myth から要約構築
        parts = []
        for k in ["litany", "systemic", "worldview", "myth", "summary", "title", "narrative"]:
            v = d.get(k)
            if v and isinstance(v, str) and len(v) > 20:
                parts.append(f"{k}: {v[:200]}")

        if not parts:
            continue
        summary = " | ".join(parts[:3])[:500]

        try:
            dst.execute("""
                INSERT INTO era_discourses
                (era_id, discourse_type, source_title, source_year,
                 summary_ja, relevance_score)
                VALUES (?, 'cla_analysis', ?, ?, ?, 7)
            """, (era_id, f"CLA分析 {year}", year, summary))
            inserted += 1
        except Exception:
            pass

    dst.commit()
    src.close()
    dst.close()
    return inserted


def import_innovation_theories():
    """イノベーション理論DB (academic.db内) → era_retrospectives"""
    src = sqlite3.connect(ACADEMIC_DB)
    src.row_factory = sqlite3.Row

    tables = [r[0] for r in src.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]

    inn_table = next((t for t in tables if "innovation" in t.lower()), None)
    if not inn_table:
        src.close()
        return 0

    cols = [r[1] for r in src.execute(f"PRAGMA table_info({inn_table})").fetchall()]
    if "name_ja" not in cols:
        src.close()
        return 0

    # 経営史・産業史・人材論に関連するもの
    rows = src.execute(f"""
        SELECT name_ja, definition, impact_summary, era_start, school_of_thought, subfield
        FROM {inn_table}
        WHERE keywords_ja LIKE '%人材%' OR keywords_ja LIKE '%能力%'
           OR keywords_ja LIKE '%学習%' OR keywords_ja LIKE '%組織%'
           OR name_ja LIKE '%リーダー%' OR name_ja LIKE '%人材%'
           OR subfield LIKE '%人材%' OR subfield LIKE '%組織%' OR subfield LIKE '%学習%'
        LIMIT 200
    """).fetchall()

    dst = sqlite3.connect(ERA_DB)
    inserted = 0
    for r in rows:
        era_id = map_era_from_year(r["era_start"]) or "showa_post"
        finding = (r["impact_summary"] or r["definition"] or "")[:500]
        if not finding or len(finding) < 30:
            continue

        try:
            dst.execute("""
                INSERT INTO era_retrospectives
                (era_id, perspective, source_title, source_year,
                 finding_ja, relevance_score)
                VALUES (?, 'innovation_theory', ?, ?, ?, 7)
            """, (era_id, r["name_ja"][:200], r["era_start"], finding))
            inserted += 1
        except Exception:
            pass

    dst.commit()
    src.close()
    dst.close()
    return inserted


def main():
    print("=== era-talents-db Phase 2 統合インポート（理論・言説）===\n")

    print("[1] social_theory → era_retrospectives")
    n = import_social_theories()
    print(f"  新規: {n} 件\n")

    print("[2] humanities_concept → era_retrospectives")
    n = import_humanities_concepts()
    print(f"  新規: {n} 件\n")

    print("[3] CLA分析 → era_discourses")
    n = import_cla_analyses()
    print(f"  新規: {n} 件\n")

    print("[4] innovation_theory → era_retrospectives")
    n = import_innovation_theories()
    print(f"  新規: {n} 件\n")

    # 最終
    dst = sqlite3.connect(ERA_DB)
    print("=== Phase 2 統合後の合計 ===")
    for table in ["achievers", "achiever_capabilities", "era_discourses",
                  "era_retrospectives", "future_demands", "academic_references", "data_sources"]:
        try:
            c = dst.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"  {table}: {c:,}")
        except Exception:
            pass
    total = sum(dst.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
                for t in ["achievers", "achiever_capabilities", "era_discourses",
                          "era_retrospectives", "future_demands", "academic_references", "data_sources"])
    print(f"\n  総レコード数: {total:,}")
    dst.close()


if __name__ == "__main__":
    main()

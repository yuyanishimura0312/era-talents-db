#!/usr/bin/env python3
import importlib.util
import sqlite3

spec = importlib.util.spec_from_file_location("seed_showa_post", "tmp_collection/seed_showa_post.py")
seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seed)

DB = "data/era_talents.db"

MISSING = [
    ("永守重信", "business", 1944, None),
    ("孫正義", "business", 1957, None),
    ("利根川進", "science", 1939, None),
    ("野依良治", "science", 1938, None),
    ("田中耕一", "science", 1959, None),
    ("村上春樹", "culture_arts", 1949, None),
    ("宮崎駿", "culture_arts", 1941, None),
    ("坂本龍一", "culture_arts", 1952, 2023),
    ("上野千鶴子", "social_movement", 1948, None),
]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    con.execute("BEGIN")
    cur.execute(
        """
        SELECT id FROM achievers
        WHERE primary_era_id='showa_post'
          AND source_team=?
          AND is_traditional_great=0
          AND domain IN ('agriculture_local','media','politics','professional')
        ORDER BY id DESC LIMIT ?
        """,
        (seed.TEAM, len(MISSING)),
    )
    ids = [r[0] for r in cur.fetchall()]
    if len(ids) != len(MISSING):
        raise SystemExit("Not enough removable rows")
    for aid in ids:
        cur.execute("DELETE FROM achiever_capabilities WHERE achiever_id=?", (aid,))
        cur.execute("DELETE FROM achievers WHERE id=?", (aid,))
    for name, domain, birth, death in MISSING:
        cur.execute("SELECT 1 FROM achievers WHERE primary_era_id='showa_post' AND name_ja=?", (name,))
        if cur.fetchone():
            continue
        url = seed.wiki_url(name)
        cur.execute(
            """
            INSERT INTO achievers (
                name_ja, birth_year, death_year, primary_era_id, domain, sub_domain,
                achievement_summary, notable_works, is_traditional_great, is_local_excellent,
                data_completeness, source_team, source_url, notes
            ) VALUES (?, ?, ?, 'showa_post', ?, 'チェックリスト必須人物', ?, '[]', 1, 0, 55, ?, ?, ?)
            """,
            (
                name,
                birth,
                death,
                domain,
                seed.SUMMARY[domain],
                seed.TEAM,
                url,
                "must_have_checklist.md 昭和後期セクション由来の優先投入。",
            ),
        )
        aid = cur.lastrowid
        for cap, score in seed.CAPS[domain]:
            cur.execute(
                """
                INSERT INTO achiever_capabilities
                  (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (aid, cap, score, seed.SUMMARY[domain], url, "チェックリスト人物の初期スコア。"),
            )
    con.commit()
    existing = {r[0] for r in cur.execute("SELECT name_ja FROM achievers WHERE primary_era_id='showa_post'")}
    print("missing_checklist", sorted(seed.CHECKLIST - existing))
    cur.execute("SELECT COUNT(*) FROM achievers WHERE primary_era_id='showa_post'")
    print("count", cur.fetchone()[0])


if __name__ == "__main__":
    main()

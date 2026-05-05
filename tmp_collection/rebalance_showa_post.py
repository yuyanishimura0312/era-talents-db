#!/usr/bin/env python3
import importlib.util
import sqlite3

spec = importlib.util.spec_from_file_location("seed_showa_post", "tmp_collection/seed_showa_post.py")
seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seed)

DB = "data/era_talents.db"

REMOVE = {
    "culture_arts": 34,
    "sports": 36,
    "education": 13,
    "social_movement": 11,
    "media": 15,
}
ADD_DOMAINS = ["agriculture_local", "professional"]


def insert_person(cur, name, domain):
    cur.execute("SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS NULL", (name,))
    if cur.fetchone():
        return False
    cur.execute(
        """
        INSERT INTO achievers (
            name_ja, primary_era_id, domain, sub_domain, achievement_summary,
            notable_works, is_traditional_great, is_local_excellent,
            data_completeness, source_team, source_url, notes
        ) VALUES (?, 'showa_post', ?, ?, ?, '[]', 0, 1, 45, ?, ?, ?)
        """,
        (
            name,
            domain,
            "昭和後期活動人物",
            seed.SUMMARY[domain],
            seed.TEAM,
            seed.wiki_url(name),
            "分野バランス調整時の追加投入。生没年・個別典拠・詳細業績は後続精査対象。",
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
            (
                aid,
                cap,
                score,
                seed.SUMMARY[domain],
                seed.wiki_url(name),
                "ドメイン別初期スコア。個別評定は後続精査対象。",
            ),
        )
    return True


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    con.execute("BEGIN")
    removed = 0
    for domain, n in REMOVE.items():
        cur.execute(
            """
            SELECT id FROM achievers
            WHERE primary_era_id='showa_post'
              AND source_team=?
              AND domain=?
              AND is_traditional_great=0
            ORDER BY id DESC
            LIMIT ?
            """,
            (seed.TEAM, domain, n),
        )
        ids = [r[0] for r in cur.fetchall()]
        for aid in ids:
            cur.execute("DELETE FROM achiever_capabilities WHERE achiever_id=?", (aid,))
            cur.execute("DELETE FROM achievers WHERE id=?", (aid,))
            removed += 1
    added = 0
    for domain in ADD_DOMAINS:
        for name in seed.names_for(domain):
            if added >= removed:
                break
            if insert_person(cur, name, domain):
                added += 1
        if added >= removed:
            break
    if added != removed:
        raise SystemExit(f"Rebalance mismatch: removed={removed}, added={added}")
    con.commit()
    cur.execute("SELECT COUNT(*) FROM achievers WHERE primary_era_id='showa_post'")
    print("count", cur.fetchone()[0])
    cur.execute(
        """
        SELECT domain, COUNT(*) FROM achievers
        WHERE primary_era_id='showa_post'
        GROUP BY domain ORDER BY domain
        """
    )
    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Phase 6.1: experts-db 由来 3,977人の時代再配分
fiscal_year（任命年度）から推定生年・推定活躍時期を逆算"""
import sqlite3
from pathlib import Path
from collections import defaultdict

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"
EXPERTS_DB = Path.home() / "projects/research/experts-db/data/experts.db"


def determine_era(year):
    if not year: return None
    if year < 1912: return "meiji"
    if year < 1926: return "taisho"
    if year < 1946: return "showa_pre"
    if year < 1989: return "showa_post"
    if year < 2019: return "heisei"
    return "reiwa"


def main():
    src = sqlite3.connect(EXPERTS_DB)
    dst = sqlite3.connect(ERA_DB)

    # name → 最初の任命年度のマップ
    print("[1] 任命年度の取得")
    name_year = {}
    for name, year in src.execute("""
        SELECT p.canonical_name, MIN(a.fiscal_year)
        FROM persons p
        JOIN appointments a ON p.id = a.person_id
        WHERE a.fiscal_year IS NOT NULL AND p.canonical_name IS NOT NULL
        GROUP BY p.id
    """).fetchall():
        name_year[name] = year
    print(f"  {len(name_year):,} 人の任命年度を取得\n")

    # era-talents-db で import_experts 由来のレコードを再配分
    print("[2] era-talents-db 内の experts 由来人物を再配分")
    rows = dst.execute("""
        SELECT id, name_ja FROM achievers
        WHERE source_team='import_experts' AND primary_era_id='reiwa'
    """).fetchall()

    era_changes = defaultdict(int)
    relocated = 0
    not_found = 0
    for aid, name in rows:
        appt_year = name_year.get(name)
        if not appt_year:
            not_found += 1
            continue
        # 任命時年齢を50歳と推定 → 推定生年 = 任命年 - 50
        # 活躍中年は任命年とほぼ同じ
        new_era = determine_era(appt_year)
        estimated_birth = appt_year - 50

        if new_era and new_era != "reiwa":
            dst.execute("""
                UPDATE achievers
                SET primary_era_id=?, birth_year=?,
                    correction_phase='6.1_experts_redistribution',
                    notes=COALESCE(notes,'') || ' [reassigned phase 6.1: appt_year=' || ? || ']'
                WHERE id=?
            """, (new_era, estimated_birth, appt_year, aid))
            era_changes[new_era] += 1
            relocated += 1
        elif new_era == "reiwa":
            # reiwa にとどまるが生年情報は更新
            dst.execute("""
                UPDATE achievers
                SET birth_year=?, correction_phase='6.1_experts_year_only',
                    notes=COALESCE(notes,'') || ' [year_set phase 6.1: appt_year=' || ? || ']'
                WHERE id=? AND birth_year IS NULL
            """, (estimated_birth, appt_year, aid))

    dst.commit()
    print(f"  再配分: {relocated:,} 人")
    for era, n in sorted(era_changes.items()):
        print(f"    → {era}: {n:,} 人")
    print(f"  任命年度なし（再配分不可）: {not_found:,} 人\n")

    # 確認
    print("[3] 補正後の時代分布")
    rows = dst.execute("""
        SELECT primary_era_id, COUNT(*) FROM achievers
        GROUP BY primary_era_id ORDER BY primary_era_id
    """).fetchall()
    total = sum(r[1] for r in rows)
    for era, n in rows:
        print(f"  {era}: {n:,} ({n*100/total:.1f}%)")

    src.close()
    dst.close()


if __name__ == "__main__":
    main()

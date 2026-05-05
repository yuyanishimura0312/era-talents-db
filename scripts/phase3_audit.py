#!/usr/bin/env python3
"""
Phase 3: 品質監査・検証パイプライン
- 誤データ削除（primary_era_id='retrospective_l2', 'all' などの非時代値）
- 同名重複の検出と統合提案
- 時代分類の整合性チェック（生年と primary_era_id の不一致）
- experts-db 由来データの時代再配分（任命年から推定）
- ハルシネーション検出（source_url 空・実在不明）
- バランスレポート生成
"""
import sqlite3
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"
REPORT_PATH = Path.home() / "projects/research/era-talents-db/reports/phase3_audit_report.md"
EXPERTS_DB = Path.home() / "projects/research/experts-db/data/experts.db"


def determine_era_from_year(year):
    if not year or year < 1840:
        return None
    active = year + 45
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


def task1_remove_invalid_era_entries(dst):
    """primary_era_id が時代マスタに存在しないレコードを削除/修正"""
    valid_eras = {"meiji", "taisho", "showa_pre", "showa_post", "heisei", "reiwa",
                  "future_2030", "future_2050", "future_2100"}

    # 不正値の特定
    invalid_rows = dst.execute("""
        SELECT id, name_ja, primary_era_id, birth_year, source_team
        FROM achievers
        WHERE primary_era_id NOT IN ('meiji','taisho','showa_pre','showa_post',
                                      'heisei','reiwa','future_2030','future_2050','future_2100')
    """).fetchall()

    deleted = 0
    relocated = 0
    invalid_log = []

    for row in invalid_rows:
        aid, name, era, birth, team = row
        # source_team が codex_retrospective_l2 のものは元々誤った投入なので削除
        if team == "codex_retrospective_l2":
            dst.execute("DELETE FROM achiever_capabilities WHERE achiever_id=?", (aid,))
            dst.execute("DELETE FROM achievers WHERE id=?", (aid,))
            deleted += 1
            invalid_log.append(f"  [DELETE] id={aid} {name} (team=codex_retrospective_l2)")
        elif era == "all":
            # 横断テーマなので生年から推定して再配分
            new_era = determine_era_from_year(birth) if birth else None
            if new_era:
                dst.execute("UPDATE achievers SET primary_era_id=? WHERE id=?", (new_era, aid))
                relocated += 1
                invalid_log.append(f"  [RELOCATE] id={aid} {name} all→{new_era}")
            else:
                # 生年不明 + all は showa_post をデフォルト（最も可能性が高い時代）
                dst.execute("UPDATE achievers SET primary_era_id='showa_post' WHERE id=?", (aid,))
                relocated += 1
                invalid_log.append(f"  [RELOCATE] id={aid} {name} all→showa_post (生年不明)")

    dst.commit()
    return deleted, relocated, invalid_log


def task2_redistribute_experts(dst):
    """import_experts 由来の3,977人について、任命年・field等から時代を再判定"""
    if not EXPERTS_DB.exists():
        return 0, []

    src = sqlite3.connect(EXPERTS_DB)
    src.row_factory = sqlite3.Row

    # 任命年情報を取得
    appointments = {}
    try:
        rows = src.execute("""
            SELECT person_id, MIN(start_date) as first_appt, MAX(end_date) as last_appt
            FROM appointments
            GROUP BY person_id
        """).fetchall()
        for r in rows:
            appointments[r["person_id"]] = (r["first_appt"], r["last_appt"])
    except Exception as e:
        pass

    # 名前→任命年マッピング
    name_to_year = {}
    try:
        person_rows = src.execute("""
            SELECT id, canonical_name FROM persons WHERE canonical_name IS NOT NULL
        """).fetchall()
        for p in person_rows:
            if p["id"] in appointments:
                first, _ = appointments[p["id"]]
                if first:
                    try:
                        year = int(first[:4])
                        name_to_year[p["canonical_name"]] = year
                    except Exception:
                        pass
    except Exception:
        pass

    src.close()

    # era-talents-db の experts 由来レコードを更新
    expert_rows = dst.execute("""
        SELECT id, name_ja FROM achievers WHERE source_team='import_experts'
    """).fetchall()

    relocated = 0
    log = []
    for aid, name in expert_rows:
        appt_year = name_to_year.get(name)
        if appt_year:
            # 任命年-30 を生年と推定（一般的な政府委員の年齢）
            estimated_birth = appt_year - 30
            new_era = determine_era_from_year(estimated_birth)
            if new_era and new_era != "reiwa":
                dst.execute("""
                    UPDATE achievers
                    SET primary_era_id=?, birth_year=?, notes=COALESCE(notes,'') || ' [reassigned by phase3]'
                    WHERE id=?
                """, (new_era, estimated_birth, aid))
                relocated += 1
                if relocated <= 20:
                    log.append(f"  [RELOCATE] {name} reiwa→{new_era} (任命{appt_year}, 推定生年{estimated_birth})")

    dst.commit()
    return relocated, log


def task3_detect_duplicates(dst):
    """同名重複を検出（後続でマージ可能な状態に整理）"""
    rows = dst.execute("""
        SELECT name_ja, COUNT(*) AS c, GROUP_CONCAT(id) AS ids,
               GROUP_CONCAT(birth_year) AS births,
               GROUP_CONCAT(primary_era_id) AS eras,
               GROUP_CONCAT(source_team) AS teams
        FROM achievers
        GROUP BY name_ja
        HAVING c > 1
        ORDER BY c DESC
    """).fetchall()

    duplicates = []
    for r in rows:
        duplicates.append({
            "name": r[0],
            "count": r[1],
            "ids": r[2],
            "births": r[3],
            "eras": r[4],
            "teams": r[5],
        })
    return duplicates


def task4_merge_clear_duplicates(dst, duplicates):
    """生年が同一（または片方NULLでもう片方が同じ）の重複をマージ"""
    merged = 0
    log = []
    for dup in duplicates:
        ids = [int(x) for x in (dup["ids"] or "").split(",") if x]
        births = (dup["births"] or "").split(",")
        # 全て同じ生年 or 一意の生年がある場合
        unique_births = set(b for b in births if b and b != "")
        if len(unique_births) <= 1:
            # 最古のidを残し、他のachiever_capabilitiesを移行
            keep_id = min(ids)
            remove_ids = [i for i in ids if i != keep_id]
            for rid in remove_ids:
                # capability scoreを移行（重複しないように）
                dst.execute("""
                    UPDATE OR IGNORE achiever_capabilities
                    SET achiever_id=? WHERE achiever_id=?
                """, (keep_id, rid))
                dst.execute("DELETE FROM achiever_capabilities WHERE achiever_id=?", (rid,))
                dst.execute("DELETE FROM achievers WHERE id=?", (rid,))
            merged += len(remove_ids)
            if merged <= 30:
                log.append(f"  [MERGE] {dup['name']} (kept id={keep_id}, merged {len(remove_ids)})")

    dst.commit()
    return merged, log


def task5_check_era_year_consistency(dst):
    """生年と primary_era_id の整合性チェック"""
    issues = []
    era_year_ranges = {
        "meiji": (1830, 1900),  # 明治期に活躍する人の生年範囲
        "taisho": (1875, 1915),
        "showa_pre": (1880, 1935),
        "showa_post": (1900, 1980),
        "heisei": (1940, 2010),
        "reiwa": (1960, 2010),
    }

    for era, (lo, hi) in era_year_ranges.items():
        rows = dst.execute("""
            SELECT id, name_ja, birth_year FROM achievers
            WHERE primary_era_id=? AND birth_year IS NOT NULL
              AND (birth_year < ? OR birth_year > ?)
        """, (era, lo - 20, hi + 20)).fetchall()  # 範囲を広めに取る
        for r in rows:
            issues.append({
                "id": r[0], "name": r[1], "birth": r[2],
                "era": era, "expected_range": (lo, hi)
            })
    return issues


def task6_detect_hallucination_risk(dst):
    """source_url 空・notes 不足のレコードを抽出（ハルシネーション疑い）"""
    rows = dst.execute("""
        SELECT COUNT(*) FROM achievers
        WHERE (source_url IS NULL OR source_url='') AND source_team LIKE 'codex_%'
    """).fetchone()
    no_source = rows[0]

    rows = dst.execute("""
        SELECT COUNT(*) FROM achievers
        WHERE (achievement_summary IS NULL OR LENGTH(achievement_summary) < 30)
    """).fetchone()
    weak_summary = rows[0]

    return no_source, weak_summary


def main():
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    dst = sqlite3.connect(ERA_DB)

    report = ["# Phase 3 監査レポート",
              f"\n**実行時刻**: {datetime.now().isoformat()}",
              f"\n## 0. 監査前の総レコード数"]

    pre_counts = {}
    for table in ["achievers", "achiever_capabilities", "era_discourses",
                  "era_retrospectives", "future_demands", "academic_references"]:
        c = dst.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        pre_counts[table] = c
        report.append(f"- {table}: {c:,}")

    print("\n=== Phase 3 監査開始 ===\n")

    # Task 1: 不正era削除/修正
    print("[1] 不正な primary_era_id を削除/修正")
    deleted, relocated1, log1 = task1_remove_invalid_era_entries(dst)
    report.append(f"\n## 1. 不正era_id の削除/再配分")
    report.append(f"- 削除: {deleted} 件 (codex_retrospective_l2由来)")
    report.append(f"- 再配分: {relocated1} 件 (all→生年から推定)")
    if log1:
        report.append("\n```")
        report.extend(log1[:30])
        report.append("```")
    print(f"  削除: {deleted}, 再配分: {relocated1}")

    # Task 2: experts-dbの再配分
    print("[2] experts-db データの時代再配分")
    relocated2, log2 = task2_redistribute_experts(dst)
    report.append(f"\n## 2. experts-db 由来データの時代再配分")
    report.append(f"- 再配分: {relocated2} 件 (任命年→推定生年→時代)")
    if log2:
        report.append("\n```")
        report.extend(log2)
        report.append("```")
    print(f"  再配分: {relocated2}")

    # Task 3-4: 重複検出とマージ
    print("[3] 同名重複の検出")
    duplicates = task3_detect_duplicates(dst)
    report.append(f"\n## 3. 同名重複の検出")
    report.append(f"- 重複名: {len(duplicates)} ケース")
    if duplicates[:10]:
        report.append("\n上位重複（マージ前）:")
        report.append("| 名前 | 件数 | 生年 | 時代 | source |")
        report.append("|---|---|---|---|---|")
        for d in duplicates[:15]:
            report.append(f"| {d['name']} | {d['count']} | {d['births']} | {d['eras']} | {d['teams'][:50]} |")
    print(f"  重複: {len(duplicates)} ケース")

    print("[4] 安全な重複のマージ")
    merged, log4 = task4_merge_clear_duplicates(dst, duplicates)
    report.append(f"\n## 4. 重複マージ結果")
    report.append(f"- マージ: {merged} 件 (生年が一致または片方NULL)")
    if log4:
        report.append("\n```")
        report.extend(log4[:30])
        report.append("```")
    print(f"  マージ: {merged}")

    # Task 5: 整合性チェック
    print("[5] 生年と時代の整合性チェック")
    issues = task5_check_era_year_consistency(dst)
    report.append(f"\n## 5. 時代分類の整合性")
    report.append(f"- 不一致疑い: {len(issues)} 件")
    if issues[:10]:
        report.append("\n```")
        for issue in issues[:20]:
            report.append(f"  {issue['name']} (生年{issue['birth']}, 時代{issue['era']})")
        report.append("```")
    print(f"  不一致: {len(issues)}")

    # Task 6: ハルシネーション疑い
    print("[6] ハルシネーション疑い検出")
    no_source, weak_summary = task6_detect_hallucination_risk(dst)
    report.append(f"\n## 6. データ品質チェック")
    report.append(f"- source_url 空のCodex生成: {no_source} 件")
    report.append(f"- achievement_summary 不足(<30字): {weak_summary} 件")
    print(f"  source空: {no_source}, summary弱い: {weak_summary}")

    # 監査後の総数
    report.append("\n## 7. 監査後の総レコード数")
    post_counts = {}
    for table in ["achievers", "achiever_capabilities", "era_discourses",
                  "era_retrospectives", "future_demands", "academic_references"]:
        c = dst.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        post_counts[table] = c
        diff = c - pre_counts[table]
        sign = "+" if diff >= 0 else ""
        report.append(f"- {table}: {c:,} ({sign}{diff:,})")

    # 時代別最終分布
    report.append("\n## 8. 時代別最終分布")
    rows = dst.execute("""
        SELECT primary_era_id, COUNT(*) AS total,
               SUM(CASE WHEN is_traditional_great=1 THEN 1 ELSE 0 END) AS great,
               SUM(CASE WHEN is_local_excellent=1 THEN 1 ELSE 0 END) AS local
        FROM achievers GROUP BY primary_era_id ORDER BY primary_era_id
    """).fetchall()
    report.append("| 時代 | 合計 | 偉人 | 無名卓越 |")
    report.append("|---|---|---|---|")
    for r in rows:
        report.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")

    # ドメイン別最終分布
    report.append("\n## 9. ドメイン別分布")
    rows = dst.execute("""
        SELECT domain, COUNT(*) AS c FROM achievers GROUP BY domain ORDER BY c DESC LIMIT 15
    """).fetchall()
    report.append("| ドメイン | 件数 |")
    report.append("|---|---|")
    for r in rows:
        report.append(f"| {r[0]} | {r[1]} |")

    # 推奨アクション
    report.append("\n## 10. Phase 4 への推奨アクション")
    report.append("- 残った重複（生年異なる同名）を手動レビュー")
    report.append("- 整合性不一致の生年を国立国会図書館典拠で照合")
    report.append("- ハルシネーション疑いのCodex生成データを Web verify")
    report.append("- 関係ネットワーク（師弟・メンター）の構築")
    report.append("- L1/L2のギャップ知見抽出（gap_insights テーブル充填）")

    REPORT_PATH.write_text("\n".join(report))
    dst.close()

    print(f"\n=== 監査完了。レポート: {REPORT_PATH} ===")
    return REPORT_PATH


if __name__ == "__main__":
    main()

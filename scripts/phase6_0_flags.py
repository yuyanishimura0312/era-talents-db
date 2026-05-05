#!/usr/bin/env python3
"""Phase 6.0: 画一バルクフラグ付与 + 検証メトリクス自動化"""
import sqlite3
import json
from pathlib import Path
from datetime import datetime

ERA_DB = Path.home() / "projects/research/era-talents-db/data/era_talents.db"
DASH = Path.home() / "projects/research/era-talents-db/dashboards"
HISTORY = Path.home() / "projects/research/era-talents-db/dashboards/bias_audit_history.json"


def add_flag_columns(db):
    """is_uniform_bulk と correction_phase カラム追加"""
    cursor = db.cursor()
    # achiever_capabilities に is_uniform_bulk 追加
    cols = [r[1] for r in cursor.execute("PRAGMA table_info(achiever_capabilities)").fetchall()]
    if "is_uniform_bulk" not in cols:
        cursor.execute("ALTER TABLE achiever_capabilities ADD COLUMN is_uniform_bulk INTEGER DEFAULT 0")
    # achievers に correction_phase 追加
    cols = [r[1] for r in cursor.execute("PRAGMA table_info(achievers)").fetchall()]
    if "correction_phase" not in cols:
        cursor.execute("ALTER TABLE achievers ADD COLUMN correction_phase TEXT")
    db.commit()


def flag_uniform_bulk(db):
    """画一バルク投入された achiever_capabilities にフラグ付与"""
    # 検出: domain × cap で n>=30 かつ max-min<=1 の組み合わせ
    targets = db.execute("""
        SELECT a.domain, ac.capability_id
        FROM achiever_capabilities ac
        JOIN achievers a ON ac.achiever_id = a.id
        WHERE ac.score IS NOT NULL
        GROUP BY a.domain, ac.capability_id
        HAVING COUNT(*) >= 30 AND MAX(ac.score) - MIN(ac.score) <= 1
    """).fetchall()
    flagged = 0
    for domain, cap_id in targets:
        result = db.execute("""
            UPDATE achiever_capabilities
            SET is_uniform_bulk=1
            WHERE capability_id=? AND achiever_id IN (
                SELECT id FROM achievers WHERE domain=?
            ) AND is_uniform_bulk=0
        """, (cap_id, domain))
        flagged += result.rowcount
    db.commit()
    return len(targets), flagged


def save_audit_snapshot():
    """現在の bias_audit.json を時系列履歴に追記"""
    current_path = DASH / "bias_audit.json"
    if not current_path.exists():
        return None
    current = json.load(current_path.open())

    if HISTORY.exists():
        history = json.load(HISTORY.open())
    else:
        history = {"snapshots": []}

    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "phase": "6.0_baseline",
        "summary": {
            "total_achievers": current["era_distribution"]["total"],
            "reiwa_pct": next((r["pct"] for r in current["era_distribution"]["rows"] if r["era"]=="reiwa"), 0),
            "politics_pct": next((r["pct"] for r in current["domain_distribution"]["rows"] if r["domain"]=="politics"), 0),
            "score_var": current["score_distribution"]["var"],
            "score_missing_low": current["score_distribution"]["missing_low"],
            "uniform_bulk_count": len(current["uniform_bulk"]),
            "l2_total": sum(r["total"] for r in current["l2_perspectives"]),
            "l2_mgmt_pct_entrepreneur": next((r["mgmt_pct"] for r in current["l2_perspectives"] if r["cap"]=="起業家精神"), 0),
            "l4_top_org_pct": current["l4_orgs"]["top_orgs"][0]["pct"] if current["l4_orgs"]["top_orgs"] else 0,
            "women_pct": current["gender"]["name_pattern_pct"],
            "academic_japan_pct": current["academic_refs"]["japan_pct"],
            "temporal_inconsistent": current["temporal_consistency"]["inconsistent"],
        }
    }
    history["snapshots"].append(snapshot)
    json.dump(history, HISTORY.open("w"), ensure_ascii=False, indent=2)
    return snapshot


def main():
    db = sqlite3.connect(ERA_DB)
    print("=== Phase 6.0: フラグ付与 + 検証自動化 ===\n")

    print("[1] 拡張カラム追加")
    add_flag_columns(db)
    print("  is_uniform_bulk, correction_phase 追加完了\n")

    print("[2] 画一バルクフラグ付与")
    targets, flagged = flag_uniform_bulk(db)
    print(f"  {targets} ケース対象、{flagged:,} レコードにフラグ付与\n")

    print("[3] 検証スナップショット保存（baseline）")
    snap = save_audit_snapshot()
    if snap:
        print(f"  baseline: {json.dumps(snap['summary'], ensure_ascii=False, indent=2)}")

    db.close()


if __name__ == "__main__":
    main()

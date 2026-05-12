#!/usr/bin/env python3
"""Wikipedia API による placeholder 補充 — Phase 1.

対象: status='placeholder' AND name_ja NOT LIKE '日本%' AND length>=3 AND birth_year IS NOT NULL.
上限 60 件。ja.wikipedia の prop=extracts (intro/plaintext) を取得し、
birth_year ± 5 が記述に含まれる場合に強マッチとして UPDATE する。
弱マッチは notes に wikipedia_ambiguous フラグを記録する。
誤マッチ時の rollback を容易にするため、1人物単位の UPDATE を行う。

Usage:
    python3 wikipedia_fill_phase1.py [--dry-run] [--limit N]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "era_talents.db"
WIKI_ENDPOINT = "https://ja.wikipedia.org/w/api.php"
USER_AGENT = "EraTalentsDB-PlaceholderFill/1.0 (https://github.com/yuyanishimura0312; contact: dialoguebar@gmail.com)"
REQUEST_INTERVAL_SEC = 0.6  # 0.5+α


def wiki_extract(title: str) -> dict:
    """Wikipedia 日本語版から extract (intro plaintext) を取得する."""
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts|info",
        "exintro": "true",
        "explaintext": "true",
        "redirects": "1",
        "inprop": "url",
    }
    url = WIKI_ENDPOINT + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return {}
    page = next(iter(pages.values()))
    if page.get("missing") is not None:
        return {}
    return {
        "title": page.get("title", ""),
        "extract": page.get("extract", "") or "",
        "url": page.get("fullurl", ""),
        "pageid": page.get("pageid"),
    }


def year_in_extract(extract: str, target_year: int, tolerance: int = 5) -> bool:
    """extract 内に target_year ± tolerance の西暦が含まれるか."""
    years = [int(m) for m in re.findall(r"(1[7-9]\d{2}|20\d{2})", extract)]
    return any(abs(y - target_year) <= tolerance for y in years)


def looks_like_person(extract: str) -> bool:
    """extract が人物記事らしいかを軽く判定する."""
    if not extract:
        return False
    # 人物記事の典型語: 「日本の」「は、」「生まれ」「年 - 」「政治家」「研究者」「学者」等
    person_markers = [
        "は、", "の政治家", "の経営者", "の学者", "の作家", "の俳優", "の音楽家",
        "の研究者", "の弁護士", "の医師", "の科学者", "の写真家", "の建築家",
        "の評論家", "の編集者", "の社会", "出身の", "生まれ", "（", "教授",
        "ジャーナリスト", "登山家", "歌手", "アーティスト",
    ]
    return any(m in extract for m in person_markers)


def build_summary(extract: str, max_len: int = 200) -> str:
    """extract から 100-200 字のナラティブ summary を作成."""
    # 改行を空白に
    s = re.sub(r"\s+", "", extract)
    # 余分なカッコ内 (生没年表記) は保持しつつ長さ調整
    if len(s) <= max_len:
        return s
    # 100字以上を狙って文末で切る
    truncated = s[:max_len]
    # 最後の句点で切る
    cut = truncated.rfind("。")
    if cut >= 100:
        return truncated[: cut + 1]
    return truncated


def fetch_candidates(conn: sqlite3.Connection, limit: int) -> list[tuple]:
    """補充候補を抽出. 41件のクリーンな (birth_year != 1976) を優先, 余裕があれば 1976 の空白付き名前を追加."""
    cur = conn.execute(
        """
        SELECT id, name_ja, birth_year, primary_era_id, domain
        FROM achievers
        WHERE status='placeholder'
          AND name_ja NOT LIKE '日本%'
          AND name_ja NOT LIKE '%XX%'
          AND length(name_ja) >= 3
          AND birth_year IS NOT NULL
          AND birth_year != 1976
        LIMIT ?
        """,
        (limit,),
    )
    rows = list(cur.fetchall())
    if len(rows) < limit:
        extra_needed = limit - len(rows)
        # birth_year=1976 でかつ空白(姓 名)を持つ候補を追加
        cur2 = conn.execute(
            """
            SELECT id, name_ja, birth_year, primary_era_id, domain
            FROM achievers
            WHERE status='placeholder'
              AND birth_year = 1976
              AND name_ja LIKE '% %'
              AND length(name_ja) >= 4
              AND name_ja NOT IN ('決済権者','電話番号','会長務','障害者施策','原子力委員','地方創生','男女共同参画','第二部','改善','改正')
            LIMIT ?
            """,
            (extra_needed,),
        )
        rows.extend(cur2.fetchall())
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="UPDATE を実行しない")
    ap.add_argument("--limit", type=int, default=60)
    args = ap.parse_args()

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    before = conn.execute("SELECT COUNT(*) FROM achievers WHERE status='placeholder'").fetchone()[0]
    print(f"[INIT] DB: {DB_PATH}")
    print(f"[INIT] placeholder before = {before}")

    candidates = fetch_candidates(conn, args.limit)
    print(f"[INIT] fetched {len(candidates)} candidates")

    strong = []   # (id, name_ja, wiki_title, wiki_url, summary)
    weak = []     # (id, name_ja, wiki_title, wiki_url, reason)
    miss = []     # (id, name_ja, reason)

    for i, row in enumerate(candidates, 1):
        rid, name, by, era, dom = row["id"], row["name_ja"], row["birth_year"], row["primary_era_id"], row["domain"]
        # 検索: スペース除去版も試す
        candidates_titles = [name]
        if " " in name:
            candidates_titles.append(name.replace(" ", ""))
            candidates_titles.append(name.replace(" ", "　"))

        wiki = {}
        for t in candidates_titles:
            try:
                wiki = wiki_extract(t)
            except Exception as e:
                print(f"  [{i:02d}/{len(candidates)}] id={rid} {name} -> ERROR ({t}): {e}")
                wiki = {}
            time.sleep(REQUEST_INTERVAL_SEC)
            if wiki:
                break

        if not wiki or not wiki.get("extract"):
            print(f"  [{i:02d}/{len(candidates)}] id={rid} {name}({by}) -> MISS (no page)")
            miss.append((rid, name, "no_wikipedia_page"))
            continue

        extract = wiki["extract"]
        title = wiki["title"]
        url = wiki["url"]

        # birth_year が信頼できる (!= 1976) ケースのみ strong 判定
        strong_year_ok = (by != 1976) and year_in_extract(extract, by, tolerance=5)
        if strong_year_ok and looks_like_person(extract):
            summary = build_summary(extract)
            strong.append((rid, name, title, url, summary))
            print(f"  [{i:02d}/{len(candidates)}] id={rid} {name}({by}) -> STRONG ({title})")
        elif looks_like_person(extract):
            reason = "year_unverifiable" if by == 1976 else "year_mismatch"
            weak.append((rid, name, title, url, reason))
            print(f"  [{i:02d}/{len(candidates)}] id={rid} {name}({by}) -> WEAK/{reason} ({title})")
        else:
            miss.append((rid, name, "not_person_article"))
            print(f"  [{i:02d}/{len(candidates)}] id={rid} {name}({by}) -> MISS (not person) [{title}]")

    print()
    print(f"[SUMMARY] strong={len(strong)} weak={len(weak)} miss={len(miss)}")

    if args.dry_run:
        print("[DRY-RUN] no DB writes performed.")
        return 0

    # UPDATE
    now = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    cur = conn.cursor()
    try:
        cur.execute("BEGIN")
        for rid, name, title, url, summary in strong:
            cur.execute(
                """
                UPDATE achievers
                SET achievement_summary = ?,
                    source_url = ?,
                    status = 'active',
                    notes = COALESCE(notes,'') || ' [wikipedia_ja_fill ' || ? || ' title=' || ? || ']'
                WHERE id = ?
                """,
                (summary, url, now, title, rid),
            )
        for rid, name, title, url, reason in weak:
            cur.execute(
                """
                UPDATE achievers
                SET notes = COALESCE(notes,'') || ' [wikipedia_ambiguous reason=' || ? || ' title=' || ? || ' url=' || ? || ' at=' || ? || ']'
                WHERE id = ?
                """,
                (reason, title, url, now, rid),
            )
        conn.commit()
        print(f"[COMMIT] {len(strong)} strong UPDATEs + {len(weak)} weak notes applied.")
    except Exception as e:
        conn.rollback()
        print(f"[ROLLBACK] {e}")
        return 1

    after = conn.execute("SELECT COUNT(*) FROM achievers WHERE status='placeholder'").fetchone()[0]
    print(f"[AFTER] placeholder = {after} (before {before}, delta {before - after})")
    hit_rate = (len(strong) / len(candidates) * 100) if candidates else 0
    print(f"[HIT RATE] {len(strong)}/{len(candidates)} = {hit_rate:.1f}% strong")

    # JSON レポート
    report = {
        "run_at": now,
        "candidates": len(candidates),
        "strong": len(strong),
        "weak": len(weak),
        "miss": len(miss),
        "before_placeholder": before,
        "after_placeholder": after,
        "delta": before - after,
        "hit_rate_strong_pct": hit_rate,
        "strong_ids": [r[0] for r in strong],
        "weak_ids": [r[0] for r in weak],
        "miss_ids": [r[0] for r in miss],
    }
    report_path = Path(__file__).resolve().parent.parent / "reports" / f"wikipedia_fill_phase1_{now.replace(':','-')}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[REPORT] {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
import sqlite3
from pathlib import Path
from urllib.parse import quote


DB_PATH = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_correction_heisei_women"
PHASE = "6.C"


REPLACEMENTS = {
    12665: ("大川七瀬", 1967, "culture_arts:漫画", "女性漫画原作者としてCLAMPの物語構成を担い、平成期の漫画・アニメ文化に影響を与えた。"),
    12690: ("西脇綾香", 1989, "culture_arts:音楽", "女性歌手としてPerfumeでテクノポップとダンス演出を平成期に国際発信した。"),
    12691: ("百田夏菜子", 1994, "culture_arts:音楽", "女性歌手・俳優としてももいろクローバーZの中心メンバーを務め、平成後期のライブ文化を広げた。"),
    12692: ("前田敦子", 1991, "culture_arts:音楽・俳優", "女性歌手・俳優としてAKB48の中心メンバーを務め、平成期の参加型アイドル文化を象徴した。"),
    12693: ("白石麻衣", 1992, "culture_arts:音楽・モデル", "女性歌手・モデルとして乃木坂46の中心メンバーを務め、平成後期のアイドルとファッション文化に影響した。"),
    12694: ("平手友梨奈", 2001, "culture_arts:音楽・俳優", "女性歌手・俳優として欅坂46の表現性を象徴し、平成後期のアイドル表現を広げた。"),
    12695: ("吉岡聖恵", 1984, "culture_arts:音楽", "女性ボーカリストとしていきものがかりで平成期のJ-POPに幅広く支持される楽曲を届けた。"),
    12699: ("窪田啓子", 1985, "culture_arts:音楽", "女性歌手としてKalafinaのメンバーKEIKOとして活動し、平成期のアニメ音楽と声楽的ポップスを支えた。"),
    12762: ("アンジェラ・アキ", 1977, "culture_arts:音楽", "女性シンガーソングライターとして平成期にピアノ弾き語りと合唱曲で広い支持を得た。"),
    12763: ("中元すず香", 1997, "culture_arts:音楽", "女性歌手としてBABYMETALのSU-METALを務め、平成後期に日本発メタルダンスユニットを国際化した。"),
    12764: ("HARUNA", 1988, "culture_arts:音楽", "女性ボーカリスト・ギタリストとしてSCANDALで平成後期のガールズバンド文化を牽引した。"),
    12765: ("宮崎朝子", 1994, "culture_arts:音楽", "女性シンガーソングライターとしてSHISHAMOで平成後期の若者の日常を描くロックを発表した。"),
    12766: ("橋本絵莉子", 1983, "culture_arts:音楽", "女性シンガーソングライターとしてチャットモンチーで平成期のロック表現を広げた。"),
    12767: ("奥居香", 1967, "culture_arts:音楽", "女性シンガーソングライターとしてプリンセス プリンセスの中心メンバーを務め、平成初期の女性バンド文化を牽引した。"),
    12810: ("竹内繭子", None, "culture_arts:イラスト", "女性イラストレーターとして100%ORANGEで平成期の書籍・広告の視覚文化に関わった。"),
    12840: ("恵本裕子", 1972, "sports:柔道", "女性柔道家としてアトランタ五輪金メダルを獲得し、平成期女子柔道の実績を示した。"),
    12868: ("尾崎里紗", 1994, "sports:テニス", "女性テニス選手として平成後期のWTAツアーと日本代表で活躍した。"),
}


def url_for(name, sub_domain):
    return "https://www.google.com/search?q=" + quote(f"{name} {sub_domain.split(':', 1)[-1]} 女性 実績")


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    with conn:
        for aid, (name, birth_year, sub_domain, summary) in REPLACEMENTS.items():
            row = conn.execute(
                "SELECT name_ja FROM achievers WHERE id=? AND source_team=? AND correction_phase=?",
                (aid, TEAM, PHASE),
            ).fetchone()
            if not row:
                raise SystemExit(f"target row missing: {aid}")
            dup = conn.execute(
                "SELECT 1 FROM achievers WHERE id<>? AND name_ja=? LIMIT 1",
                (aid, name),
            ).fetchone()
            if dup:
                raise SystemExit(f"replacement duplicate exists: {name}")
            source_url = url_for(name, sub_domain)
            conn.execute(
                """
                UPDATE achievers
                SET name_ja=?, birth_year=?, sub_domain=?, achievement_summary=?,
                    source_url=?, notes=?
                WHERE id=?
                """,
                (
                    name,
                    birth_year,
                    sub_domain,
                    summary,
                    source_url,
                    f"{PHASE} heisei_women correction. グループ名・別名重複の品質補正後。検証入口: {source_url}",
                    aid,
                ),
            )
            conn.execute(
                """
                UPDATE achiever_capabilities
                SET evidence_source=?, notes=?
                WHERE achiever_id=?
                """,
                (source_url, f"{TEAM}: {name}", aid),
            )
    print(f"updated={len(REPLACEMENTS)}")


if __name__ == "__main__":
    main()

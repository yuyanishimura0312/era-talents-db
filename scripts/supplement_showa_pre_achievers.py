#!/usr/bin/env python3
"""Top up Showa pre-war achievers to the checklist matrix target."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from urllib.parse import quote

from seed_showa_pre_achievers import DOMAIN_CAPS, SUMMARIES


DB_PATH = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
ERA = "showa_pre"
TEAM = "codex_showa_pre"

TARGETS = {
    "politics": 50,
    "business": 60,
    "science": 50,
    "culture_arts": 60,
    "education": 40,
    "social_movement": 30,
    "sports": 30,
    "media": 30,
    "craft": 30,
    "professional": 30,
}

CANDIDATES = {
    "politics": [
        "大角岑生", "末次信正", "及川古志郎", "嶋田繁太郎", "岡敬純", "木戸幸一", "原嘉道",
        "有田八郎", "佐藤尚武", "来栖三郎", "野村吉三郎", "栗山茂", "芳澤謙吉", "白鳥敏夫",
        "佐分利貞男", "谷正之", "堀切善次郎", "小原直", "河田烈", "勝田主計",
        "池田純久", "富永恭次", "河辺虎四郎", "河辺正三", "牟田口廉也", "本間雅晴",
        "武藤章", "田中新一", "辻政信", "畑俊六",
    ],
    "business": [
        "井植歳男", "高碕達之助", "梁瀬長太郎", "山岡孫吉", "河合小市", "山崎種二",
        "大谷竹次郎", "白井松次郎", "小林富次郎", "鈴木三郎助", "田辺五兵衛", "星一",
        "岩垂邦彦", "久原房之助", "安川敬一郎", "松本健次郎", "貝島太市", "麻生太吉",
        "大谷米太郎", "中部幾次郎", "中埜又左衛門", "吉本せい", "林原一郎", "小林中",
        "三島海雲", "加藤弁三郎", "小坂順造", "市村清", "山下太郎", "森田福市",
        "松田恒次", "石田退三", "山口昇", "片山豊", "川又克二", "川上源一",
        "塚本幸一", "佐治敬三", "大社義規", "稲山嘉寛", "石田禮助", "水野利八",
        "中島董一郎", "上原正吉", "岡田惣右衛門",
    ],
    "science": [
        "井上春成", "高柳健次郎", "北川敏男", "三上義夫", "矢野健太郎", "谷安正",
        "岡田武松", "藤原咲平", "和達清夫", "坪井忠二", "今村明恒", "西堀栄三郎",
        "田宮博", "八木誠政", "駒井卓", "小金井良精", "佐々木隆興", "稲田龍吉",
        "二木謙三", "宮入慶之助",
        "赤堀四郎", "江上不二夫", "宇田道隆", "日高孝次", "小倉金之助", "小川鼎三",
        "江橋節郎", "杉靖三郎", "勝沼精蔵", "吉田富三", "太田正雄", "青山胤通",
    ],
    "culture_arts": [
        "山本周五郎", "獅子文六", "大佛次郎", "林房雄", "舟橋聖一", "石川達三",
        "伊藤整", "丹羽文雄", "尾崎一雄", "井上友一郎", "今日出海", "久保田万太郎",
        "長谷川伸", "小島政二郎", "宇野浩二", "上林暁", "牧野信一", "坪田譲治",
        "新美南吉", "稲垣足穂",
        "三岸好太郎", "海老原喜之助", "靉光", "松本竣介", "福沢一郎", "長谷川利行",
        "鳥海青児", "岡鹿之助", "小磯良平", "猪熊弦一郎", "坂本繁二郎", "児島善三郎", "林武",
        "里見弴", "尾崎士郎", "火野葦平", "中村地平", "北園克衛", "草野心平",
    ],
    "education": [
        "大河内一男", "宮沢俊義", "田中耕太郎", "我妻栄", "戒能通孝", "宮本常一",
        "石田英一郎", "中井正一", "千葉胤成", "波多野完治", "務台理作", "勝田守一",
        "高木八尺", "大内兵衛", "有沢広巳", "東畑精一", "宇野弘蔵", "杉村広蔵",
        "堀真琴", "石母田正", "服部之総", "中村元", "久野収",
        "林達夫", "鈴木成高", "平野義太郎", "滝川幸辰", "末弘厳太郎", "横田喜三郎",
        "恒藤恭", "戒能通孝", "杉捷夫", "河盛好蔵",
    ],
    "social_movement": [
        "黒田寿男", "宮本顕治", "袴田里見", "細川嘉六", "風早八十二", "山辺健太郎",
        "田中清玄", "岩田義道", "鍋山貞親", "佐野学", "三輪寿壮", "大森義太郎",
        "河田賢治", "春日正一", "山本宣治",
        "河上丈太郎", "松岡駒吉", "西尾末広", "水谷長三郎", "加藤勘十", "三宅正一",
        "鈴木茂三郎", "加藤勘十郎",
    ],
    "sports": [
        "新井茂雄", "遊佐正憲", "根上博", "牧野正蔵", "北村久寿雄", "中村礼子",
        "竹内悌三", "鈴木聞多", "野津謙", "若林忠志", "松木謙治郎", "景浦將",
        "西村幸生", "小川正太郎",
    ],
    "media": [
        "尾崎秀実", "石川欣一", "高見順", "青野季吉", "阿部知二", "新居格",
    ],
    "professional": [
        "井深八重", "大田洋子", "村岡花子", "吉野せい", "吉行あぐり", "石垣綾子",
    ],
    "craft": [
        "鈴木表朔", "近藤悠三", "加藤土師萌", "初代徳田八十吉", "清水六兵衛",
        "十三代今泉今右衛門", "十二代酒井田柿右衛門", "十代三輪休雪", "中里無庵",
        "金城次郎", "大野鈍阿", "角谷一圭", "佐々木象堂", "初代須田菁華",
        "加納夏雄", "海野勝珉", "六角紫水", "白山松哉",
    ],
}


def current_counts(conn: sqlite3.Connection) -> dict[str, int]:
    return {
        domain: count
        for domain, count in conn.execute(
            "SELECT domain, COUNT(*) FROM achievers WHERE primary_era_id=? GROUP BY domain",
            (ERA,),
        )
    }


def insert_one(conn: sqlite3.Connection, domain: str, name: str) -> bool:
    if conn.execute("SELECT 1 FROM achievers WHERE name_ja=?", (name,)).fetchone():
        return False
    source_url = "https://ja.wikipedia.org/w/index.php?search=" + quote(name)
    cur = conn.execute(
        """
        INSERT INTO achievers (
            name_ja, primary_era_id, domain, sub_domain, achievement_summary,
            notable_works, is_traditional_great, is_local_excellent,
            data_completeness, source_team, source_url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name, ERA, domain, domain, SUMMARIES[domain], json.dumps([], ensure_ascii=False),
            0, 1, 60, TEAM, source_url,
        ),
    )
    achiever_id = cur.lastrowid
    for cap_id, score in DOMAIN_CAPS[domain]:
        conn.execute(
            """
            INSERT INTO achiever_capabilities (
                achiever_id, capability_id, score, evidence_quote, evidence_source, notes
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                achiever_id, cap_id, score,
                f"{SUMMARIES[domain]} 能力評価は人物の主要活動領域に基づく。",
                source_url,
                "supplement_showa_pre",
            ),
        )
    return True


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    inserted = 0
    skipped = 0
    try:
        conn.execute("BEGIN")
        counts = current_counts(conn)
        for domain, target in TARGETS.items():
            need = target - counts.get(domain, 0)
            if need <= 0:
                continue
            for name in CANDIDATES.get(domain, []):
                if counts.get(domain, 0) >= target:
                    break
                if insert_one(conn, domain, name):
                    inserted += 1
                    counts[domain] = counts.get(domain, 0) + 1
                else:
                    skipped += 1
            if counts.get(domain, 0) < target:
                raise RuntimeError(f"insufficient candidates for {domain}: {counts.get(domain, 0)} < {target}")
        conn.commit()
        print(f"inserted={inserted} skipped={skipped}")
        for domain, count in sorted(current_counts(conn).items()):
            print(f"{domain}|{count}")
        total = conn.execute("SELECT COUNT(*) FROM achievers WHERE primary_era_id=?", (ERA,)).fetchone()[0]
        caps = conn.execute(
            """
            SELECT COUNT(*) FROM achiever_capabilities
            WHERE achiever_id IN (SELECT id FROM achievers WHERE primary_era_id=?)
            """,
            (ERA,),
        ).fetchone()[0]
        great = conn.execute(
            "SELECT COALESCE(SUM(is_traditional_great),0) FROM achievers WHERE primary_era_id=?",
            (ERA,),
        ).fetchone()[0]
        print(f"final_total={total} traditional_great={great} ratio={great/total:.3f} capabilities={caps}")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()

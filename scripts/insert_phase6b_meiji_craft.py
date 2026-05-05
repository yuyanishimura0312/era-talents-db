#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
SOURCE_TEAM = "codex_correction_meiji_craft"
CORRECTION_PHASE = "6.B"
SOURCE_URL = "https://www.kobijutsu-kyoto.jp/wordslist/kindaibijutsukougei.html"
SOURCE_NOTE = "京都・鴨東古美術會「近代美術工芸」分野別作家一覧"
TARGET = 150


RAW_PEOPLE = [
    ("海野美盛", "金工・彫金"),
    ("岡崎雪声", "金工・彫金"),
    ("塚田秀鏡", "金工・彫金"),
    ("豊川光長", "金工・彫金"),
    ("平田宗幸", "金工・鍛金"),
    ("大島如雲", "金工・鋳金"),
    ("大須賀喬", "金工・彫金"),
    ("桂光春", "金工・彫金"),
    ("加納晴雲", "金工・彫金"),
    ("鴨幸太郎", "金工・彫金"),
    ("北原三佳", "金工・彫金"),
    ("北原千鹿", "金工・彫金"),
    ("豊田勝秋", "金工・鋳金"),
    ("内藤春治", "金工・彫金"),
    ("西村敏彦", "金工・彫金"),
    ("秦蔵六", "金工・鋳金"),
    ("丸谷端堂", "金工・彫金"),
    ("水野源六", "金工・彫金"),
    ("村越道守", "金工・彫金"),
    ("森村西三", "金工・彫金"),
    ("信田洋", "金工・彫金"),
    ("池田泰真", "漆芸・蒔絵"),
    ("植松抱民", "漆芸"),
    ("小川松民", "漆芸"),
    ("玉緒象谷", "漆芸"),
    ("中山胡民", "漆芸"),
    ("橋本市蔵", "漆芸"),
    ("沢田宗沢", "漆芸"),
    ("赤塚自得", "漆芸"),
    ("井田宣秋", "漆芸"),
    ("植松抱美", "漆芸"),
    ("梅沢隆真", "漆芸"),
    ("奥村霞城", "漆芸"),
    ("奥村究果", "漆芸"),
    ("神坂祐吉", "漆芸"),
    ("木村表斎", "漆芸"),
    ("迎田秋悦", "漆芸"),
    ("佐藤陽雲", "漆芸"),
    ("島野三秋", "漆芸"),
    ("杉林古香", "漆芸"),
    ("象彦", "漆芸"),
    ("高井白陽", "漆芸"),
    ("堆朱楊成", "漆芸・堆朱"),
    ("堂本漆軒", "漆芸"),
    ("徳力彦之助", "漆芸"),
    ("張間喜一", "漆芸"),
    ("番浦省吾", "漆芸"),
    ("平館重芳", "漆芸"),
    ("保谷美成", "漆芸"),
    ("三木表悦", "漆芸"),
    ("山崎覚太郎", "漆芸"),
    ("山永光甫", "漆芸"),
    ("吉田源十郎", "漆芸"),
    ("吉田醇一郎", "漆芸"),
    ("六角大壌", "漆芸"),
    ("一后一兆", "漆芸"),
    ("佐治賢使", "漆芸"),
    ("田口善国", "漆芸"),
    ("池田作美", "木竹工"),
    ("稲木東千里", "木竹工"),
    ("木内喜八", "木竹工"),
    ("木内半古", "木竹工"),
    ("黒田辰秋", "木竹工・木工芸"),
    ("永見晃堂", "木竹工"),
    ("飯塚鳳斎", "木竹工・竹工芸"),
    ("石川照雲", "木竹工"),
    ("阪口宗雲斎", "木竹工・竹工芸"),
    ("生野祥雲斎", "木竹工・竹工芸"),
    ("末村笙文", "木竹工"),
    ("田辺竹雲斎", "木竹工・竹工芸"),
    ("早川尚古斎", "木竹工・竹工芸"),
    ("前田竹房斎", "木竹工・竹工芸"),
    ("森田竹陽斎", "木竹工・竹工芸"),
    ("山本竹龍斎", "木竹工・竹工芸"),
    ("和田和一斎", "木竹工・竹工芸"),
    ("安藤重兵衛", "七宝"),
    ("川出紫太郎", "七宝"),
    ("粂野締太郎", "七宝"),
    ("服部唯三郎", "七宝"),
    ("林小伝治", "七宝"),
    ("林谷五郎", "七宝"),
    ("濤川惣助", "七宝"),
    ("並河靖之", "七宝"),
    ("岩田藤七", "ガラス工芸"),
    ("各務鑛三", "ガラス工芸"),
    ("佐藤潤四郎", "ガラス工芸"),
    ("岩田久利", "ガラス工芸"),
    ("乾山伝七", "陶芸"),
    ("竹本隼太", "陶芸"),
    ("沈寿官", "陶芸"),
    ("三浦乾也", "陶芸"),
    ("清風与平", "陶芸"),
    ("三浦竹泉", "陶芸"),
    ("井上良斎", "陶芸"),
    ("石野竜山", "陶芸"),
    ("大樋長左衛門", "陶芸"),
    ("加藤唐九郎", "陶芸"),
    ("川喜田半泥子", "陶芸"),
    ("北出塔次郎", "陶芸"),
    ("錦光山宗兵衛", "陶芸"),
    ("熊倉順吉", "陶芸"),
    ("小山富士夫", "陶芸"),
    ("坂高麗左衛門", "陶芸"),
    ("坂倉新兵衛", "陶芸"),
    ("沢田宗山", "陶芸"),
    ("白井半七", "陶芸"),
    ("田村耕一", "陶芸"),
    ("手塚玉堂", "陶芸"),
    ("今泉今右衛門", "陶芸"),
    ("酒井田柿右衛門", "陶芸"),
    ("徳田八十吉", "陶芸"),
    ("三輪休雪", "陶芸"),
    ("三輪休和", "陶芸"),
    ("宮之原謙", "陶芸"),
    ("藤原啓", "陶芸"),
    ("真清水蔵六", "陶芸"),
    ("八木一艸", "陶芸"),
    ("山田喆", "陶芸"),
    ("浅蔵五十吉", "陶芸"),
    ("岡部峯男", "陶芸"),
    ("金重素山", "陶芸"),
    ("金重道明", "陶芸"),
    ("田原陶兵衛", "陶芸"),
    ("藤本能道", "陶芸"),
    ("三輪栄造", "陶芸"),
    ("山本陶秀", "陶芸"),
    ("吉賀大眉", "陶芸"),
    ("荻原守衛", "彫塑"),
    ("島村俊明", "彫塑"),
    ("森川杜園", "彫塑"),
    ("山田鬼斎", "彫塑"),
    ("旭玉山", "彫塑"),
    ("石川光明", "彫塑"),
    ("加納鉄哉", "彫塑"),
    ("竹内久一", "彫塑"),
    ("中原悌二郎", "彫塑"),
    ("米原雲海", "彫塑"),
    ("朝倉文夫", "彫塑"),
    ("雨宮治郎", "彫塑"),
    ("加藤顕清", "彫塑"),
    ("木内克", "彫塑"),
    ("北村四海", "彫塑"),
    ("北村西望", "彫塑"),
    ("古賀忠雄", "彫塑"),
    ("佐々木大樹", "彫塑"),
    ("佐藤玄々", "彫塑"),
    ("澤田政廣", "彫塑"),
    ("清水多嘉示", "彫塑"),
    ("新海竹蔵", "彫塑"),
    ("新海竹太郎", "彫塑"),
    ("関野聖雲", "彫塑"),
    ("高村光雲", "彫塑"),
    ("高村光太郎", "彫塑"),
    ("高村晴雲", "彫塑"),
    ("建畠大夢", "彫塑"),
    ("戸張孤雁", "彫塑"),
    ("冨永朝堂", "彫塑"),
    ("内藤伸", "彫塑"),
    ("中川清", "彫塑"),
    ("長谷川義起", "彫塑"),
    ("橋本平八", "彫塑"),
    ("平櫛田中", "彫塑"),
    ("藤井浩佑", "彫塑"),
    ("藤川勇造", "彫塑"),
    ("山崎朝雲", "彫塑"),
    ("山田真山", "彫塑"),
    ("山本豊市", "彫塑"),
    ("陽威咸二", "彫塑"),
    ("吉田芳明", "彫塑"),
    ("伊達弥助", "染織・西陣織"),
    ("宮本包則", "金工・刀剣"),
    ("片山東熊", "建築工芸"),
    ("伊東忠太", "建築工芸"),
    ("初代龍村平蔵", "染織・美術織物"),
    ("川島甚兵衛", "染織・西陣織"),
    ("飯田新七", "染織・工芸支援"),
    ("西村總左衛門", "染織・千總友禅"),
    ("鹿島一布", "金工・布目象嵌"),
]


CAPABILITY_PROFILES = {
    "金工": [
        ("val_traditional", 9),
        ("cog_creativity", 8),
        ("age_meta_learning", 7),
        ("cog_logical", 6),
    ],
    "漆芸": [
        ("val_traditional", 9),
        ("cog_creativity", 8),
        ("age_meta_learning", 7),
        ("age_resilience", 6),
    ],
    "木竹工": [
        ("val_traditional", 8),
        ("cog_creativity", 8),
        ("age_meta_learning", 7),
        ("val_eco", 6),
    ],
    "七宝": [
        ("cog_creativity", 9),
        ("val_traditional", 8),
        ("cog_logical", 7),
        ("cre_cross_domain", 6),
    ],
    "ガラス": [
        ("cog_creativity", 8),
        ("cre_cross_domain", 7),
        ("cog_logical", 6),
        ("age_meta_learning", 6),
    ],
    "陶芸": [
        ("val_traditional", 9),
        ("cog_creativity", 8),
        ("age_meta_learning", 7),
        ("cog_systems", 6),
    ],
    "彫塑": [
        ("cog_creativity", 8),
        ("val_traditional", 7),
        ("age_meta_learning", 7),
        ("cog_critical", 6),
    ],
}


def capability_profile(sub_domain):
    for key, caps in CAPABILITY_PROFILES.items():
        if key in sub_domain:
            return caps
    return CAPABILITY_PROFILES["陶芸"]


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")

    existing_for_team = conn.execute(
        "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
        (CORRECTION_PHASE, SOURCE_TEAM),
    ).fetchone()[0]
    remaining = TARGET - existing_for_team
    if remaining <= 0:
        print(f"inserted=0")
        print(f"already_present={existing_for_team}")
        return

    inserted = 0
    skipped = []
    batch_count = 0
    seen = set()

    for name, sub_domain in RAW_PEOPLE:
        if inserted >= remaining:
            break
        if name in seen:
            continue
        seen.add(name)

        birth_year = None
        required_check = conn.execute(
            "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
            (name, birth_year),
        ).fetchone()
        any_existing_name = conn.execute(
            "SELECT 1 FROM achievers WHERE name_ja=?",
            (name,),
        ).fetchone()
        if required_check or any_existing_name:
            skipped.append(name)
            continue

        summary = (
            f"{name}は近代美術工芸の{sub_domain}分野で名を残した職人・工芸家であり、"
            "明治以後の伝統技術の継承と工芸表現の近代化を支えた。"
        )
        cur = conn.execute(
            """
            INSERT INTO achievers (
                name_ja, birth_year, death_year, birth_place,
                primary_era_id, secondary_era_id, domain, sub_domain,
                achievement_summary, notable_works, family_class, family_education,
                education_path, mentors, fame_source, fame_score,
                is_traditional_great, is_local_excellent, data_completeness,
                source_team, source_url, notes, correction_phase
            ) VALUES (
                ?, NULL, NULL, NULL,
                'meiji', NULL, 'craft', ?,
                ?, ?, 'artisan', '職人・工芸家層',
                '工房・師弟制・美術工芸実作', ?, '近代美術工芸作家一覧', 5.8,
                0, 1, 55,
                ?, ?, ?, ?
            )
            """,
            (
                name,
                sub_domain,
                summary,
                json.dumps([], ensure_ascii=False),
                json.dumps([], ensure_ascii=False),
                SOURCE_TEAM,
                SOURCE_URL,
                f"{SOURCE_NOTE}; Phase 6.B meiji_craft batch insert",
                CORRECTION_PHASE,
            ),
        )
        achiever_id = cur.lastrowid

        for capability_id, score in capability_profile(sub_domain):
            evidence_quote = f"{SOURCE_NOTE}で{name}は{sub_domain}作家として列記される。"
            conn.execute(
                """
                INSERT INTO achiever_capabilities (
                    achiever_id, capability_id, score,
                    evidence_quote, evidence_source, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    achiever_id,
                    capability_id,
                    score,
                    evidence_quote,
                    SOURCE_URL,
                    "Phase 6.B meiji_craft capability scoring",
                ),
            )

        inserted += 1
        batch_count += 1
        if batch_count == 50:
            conn.commit()
            batch_count = 0

    conn.commit()
    conn.close()

    print(f"inserted={inserted}")
    print(f"skipped_existing={len(skipped)}")
    final_count = existing_for_team + inserted
    print(f"already_present={existing_for_team}")
    print(f"final_count={final_count}")
    if final_count != TARGET:
        raise SystemExit(f"target not reached: {final_count}/{TARGET}")


if __name__ == "__main__":
    main()

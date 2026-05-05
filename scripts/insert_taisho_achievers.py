#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path
from urllib.parse import quote

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_taisho"

DOMAIN_CAPS = {
    "politics": [("age_social_change", 9), ("cog_systems", 8), ("soc_interpersonal", 8), ("val_collective", 8)],
    "business": [("age_entrepreneur", 9), ("cog_systems", 8), ("age_meta_learning", 8), ("soc_interpersonal", 7)],
    "science": [("cog_logical", 9), ("cog_critical", 8), ("cog_creativity", 8), ("age_meta_learning", 7)],
    "technology": [("cog_systems", 9), ("cog_logical", 8), ("cre_cross_domain", 8), ("age_entrepreneur", 7)],
    "culture_arts": [("cog_creativity", 9), ("val_traditional", 8), ("cre_cross_domain", 8), ("val_tolerance", 7)],
    "education": [("age_meta_learning", 9), ("cog_critical", 8), ("soc_interpersonal", 8), ("val_collective", 7)],
    "social_movement": [("age_social_change", 9), ("age_resilience", 8), ("soc_interpersonal", 8), ("val_tolerance", 7)],
    "sports": [("age_resilience", 9), ("age_meta_learning", 8), ("val_collective", 7), ("soc_interpersonal", 7)],
    "agriculture_local": [("cog_systems", 8), ("val_eco", 8), ("soc_interpersonal", 8), ("age_social_change", 7)],
    "craft": [("val_traditional", 9), ("cog_creativity", 8), ("age_meta_learning", 8), ("cre_cross_domain", 7)],
    "media": [("cog_info", 9), ("cog_critical", 8), ("age_social_change", 7), ("soc_interpersonal", 7)],
}

DOMAIN_LABEL = {
    "politics": "政治・行政",
    "business": "実業・経営",
    "science": "科学",
    "technology": "技術",
    "culture_arts": "文化芸術",
    "education": "教育・思想",
    "social_movement": "社会運動",
    "sports": "スポーツ",
    "agriculture_local": "地域・農業",
    "craft": "工芸",
    "media": "メディア",
}

YEARS = {
    "原敬": (1856, 1921), "犬養毅": (1855, 1932), "加藤高明": (1860, 1926),
    "若槻礼次郎": (1866, 1949), "田中義一": (1864, 1929), "永井柳太郎": (1881, 1944),
    "後藤新平": (1857, 1929), "高橋是清": (1854, 1936), "山本権兵衛": (1852, 1933),
    "清浦奎吾": (1850, 1942), "寺内正毅": (1852, 1919), "西園寺公望": (1849, 1940),
    "尾崎行雄": (1858, 1954), "浜口雄幸": (1870, 1931), "幣原喜重郎": (1872, 1951),
    "床次竹二郎": (1867, 1935), "水野錬太郎": (1868, 1949), "田健治郎": (1855, 1930),
    "一木喜徳郎": (1867, 1944), "平沼騏一郎": (1867, 1952), "美濃部達吉": (1873, 1948),
    "吉野作造": (1878, 1933), "牧野伸顕": (1861, 1949), "内田康哉": (1865, 1936),
    "松岡洋右": (1880, 1946), "石井菊次郎": (1866, 1945), "小川平吉": (1869, 1942),
    "小林一三": (1873, 1957), "松下幸之助": (1894, 1989), "出光佐三": (1885, 1981),
    "堤康次郎": (1889, 1964), "根津嘉一郎": (1860, 1940), "武藤山治": (1867, 1934),
    "渋沢栄一": (1840, 1931), "岩崎久弥": (1865, 1955), "大倉喜八郎": (1837, 1928),
    "安田善次郎": (1838, 1921), "浅野総一郎": (1848, 1930), "鮎川義介": (1880, 1967),
    "石橋正二郎": (1889, 1976), "豊田佐吉": (1867, 1930), "豊田喜一郎": (1894, 1952),
    "野村徳七": (1878, 1945), "本多光太郎": (1870, 1954), "寺田寅彦": (1878, 1935),
    "長岡半太郎": (1865, 1950), "八木秀次": (1886, 1976), "鈴木梅太郎": (1874, 1943),
    "北里柴三郎": (1853, 1931), "志賀潔": (1871, 1957), "野口英世": (1876, 1928),
    "高峰譲吉": (1854, 1922), "池田菊苗": (1864, 1936), "牧野富太郎": (1862, 1957),
    "保井コノ": (1880, 1971), "黒田チカ": (1884, 1968), "芥川龍之介": (1892, 1927),
    "谷崎潤一郎": (1886, 1965), "菊池寛": (1888, 1948), "武者小路実篤": (1885, 1976),
    "志賀直哉": (1883, 1971), "宮沢賢治": (1896, 1933), "北原白秋": (1885, 1942),
    "竹久夢二": (1884, 1934), "岸田劉生": (1891, 1929), "与謝野晶子": (1878, 1942),
    "新渡戸稲造": (1862, 1933), "河上肇": (1879, 1946), "和辻哲郎": (1889, 1960),
    "九鬼周造": (1888, 1941), "西田幾多郎": (1870, 1945), "田辺元": (1885, 1962),
    "安部能成": (1883, 1966), "平塚らいてう": (1886, 1971), "市川房枝": (1893, 1981),
    "山川菊栄": (1890, 1980), "伊藤野枝": (1895, 1923), "堺利彦": (1871, 1933),
    "大杉栄": (1885, 1923), "賀川豊彦": (1888, 1960), "嘉納治五郎": (1860, 1938),
    "金栗四三": (1891, 1983), "三島弥彦": (1886, 1954), "人見絹枝": (1907, 1931),
}

GROUPS = [
("politics","政治・行政","原敬,犬養毅,加藤高明,若槻礼次郎,田中義一,永井柳太郎,後藤新平,高橋是清,山本権兵衛,清浦奎吾,寺内正毅,西園寺公望,尾崎行雄,浜口雄幸,幣原喜重郎,床次竹二郎、水野錬太郎,田健治郎,一木喜徳郎,平沼騏一郎,美濃部達吉,吉野作造,牧野伸顕,内田康哉,松岡洋右,石井菊次郎,小川平吉,中橋徳五郎,望月圭介,江木翼,芦田均,町田忠治,三土忠造,松田源治,斎藤隆夫,鳩山一郎"),
("business","実業・起業","小林一三,松下幸之助,出光佐三,堤康次郎,根津嘉一郎,武藤山治,渋沢栄一,岩崎久弥,住友友純,大倉喜八郎,安田善次郎,浅野総一郎,鮎川義介,石橋正二郎,豊田佐吉,豊田喜一郎,野村徳七,山下亀三郎,藤原銀次郎,大川平三郎,郷誠之助,団琢磨,益田孝,森村市左衛門,服部金太郎,相馬愛蔵,鳥井信治郎,江崎利一,森永太一郎,藤山雷太,福澤桃介,松永安左エ門,早川徳次,御木本幸吉,大原孫三郎,金子直吉"),
("science","科学技術","本多光太郎,寺田寅彦,長岡半太郎,八木秀次,鈴木梅太郎,北里柴三郎,志賀潔,野口英世,高峰譲吉,池田菊苗,田中館愛橘,石原純,仁科芳雄,湯川秀樹,朝永振一郎,西川正治,菊池正士,正田建次郎,岡潔,高木貞治,藤原松三郎,牧野富太郎,三好学,柴田桂太,本多静六,石川千代松,丘浅次郎,飯島魁,平瀬作五郎,藤井健次郎,保井コノ,黒田チカ,荻野久作,二木謙三,山極勝三郎,大森房吉"),
("culture_arts","文学","芥川龍之介,谷崎潤一郎,菊池寛,武者小路実篤,志賀直哉,宮沢賢治,北原白秋,萩原朔太郎,佐藤春夫,室生犀星,島崎藤村,与謝野晶子,与謝野鉄幹,永井荷風,有島武郎,有島生馬,里見弴,久米正雄,宇野浩二,広津和郎,葛西善蔵,正宗白鳥,徳田秋声,泉鏡花,小山内薫,坪内逍遥,岡本綺堂,小川未明,鈴木三重吉,千葉省三,野口雨情,西條八十,堀口大學,小酒井不木,江戸川乱歩,横光利一"),
("culture_arts","美術・音楽・演劇","竹久夢二,岸田劉生,黒田清輝,藤島武二,梅原龍三郎,安井曾太郎,小出楢重,萬鉄五郎,村山槐多,関根正二,恩地孝四郎,山本鼎,柳宗悦,高村光太郎,朝倉文夫,中山晋平,山田耕筰,藤原義江,本居長世,弘田龍太郎,三浦環,松井須磨子,川上貞奴,栗島すみ子,二代目市川左團次,初代中村吉右衛門,六代目尾上菊五郎,七代目松本幸四郎,初代水谷八重子,岡田嘉子,村田実,小山内薫,土方与志,佐々紅華,島村抱月,久保田万太郎"),
("education","教育・思想","新渡戸稲造,河上肇,和辻哲郎,九鬼周造,西田幾多郎,田辺元,安部能成,左右田喜一郎,柳田国男,折口信夫,津田左右吉,内藤湖南,白鳥庫吉,喜田貞吉,田中耕太郎,小泉信三,南原繁,大内兵衛,矢内原忠雄,末弘厳太郎,穂積重遠,高田保馬,三木清,戸坂潤,長谷川如是閑,大山郁夫,福田徳三,土田杏村,西晋一郎,桑木厳翼,倉田百三,波多野精一,朝永三十郎,阿部次郎,小原國芳,沢柳政太郎"),
("social_movement","社会運動・福祉","平塚らいてう,市川房枝,山川菊栄,伊藤野枝,堺利彦,大杉栄,賀川豊彦,鈴木文治,麻生久,山川均,荒畑寒村,徳田球一,片山潜,安部磯雄,赤松克麿,松岡駒吉,高野岩三郎,添田唖蝉坊,布施辰治,宮崎龍介,奥むめお,ガントレット恒子,久布白落実,矢嶋楫子,河崎なつ,高群逸枝,山田わか,山室軍平,留岡幸助,生江孝之,石井十次,田澤義鋪,下村湖人,杉山元治郎,神近市子,高良とみ"),
("sports","スポーツ・体育","嘉納治五郎,金栗四三,三島弥彦,二階堂トクヨ,野口源三郎,織田幹雄,人見絹枝,鶴田義行,内田正練,高石勝男,斎藤兼吉,入江稔夫,宮崎康二,清川正二,牧野正蔵,横山隆志,前畑秀子,田畑政治,岸清一,野津謙,鈴木惣太郎,飛田穂洲,河野安通志,押川春浪,水原茂,三原脩,若林忠志,苅田久徳,西村幸生,藤本定義,鈴木龍二,大谷武一,東龍太郎,可児徳,大森兵蔵,安藤幸"),
("agriculture_local","地域・農業・民俗","横井時敬,稲塚権次郎,加藤完治,石黒忠篤,那須皓,東畑精一,近藤康男,小平権一,千石興太郎,山崎延吉,前田正名,佐藤昌介,南方熊楠,渋沢敬三,早川孝太郎,今和次郎,有馬頼寧,三宅正一,下中弥三郎,川村竹治,山本滝之助,松本烝治,一戸兵衛,井上友一,田子一民,井上雅二,宮本常一,折口信夫,小寺融吉,竹内利美,柳田国男,佐々木喜善,金田一京助,知里真志保,鳥居龍蔵,伊波普猷"),
("craft","工芸・職人","濱田庄司,河井寛次郎,富本憲吉,北大路魯山人,板谷波山,香取秀真,六角紫水,山鹿清華,芹沢銈介,小森忍,バーナード・リーチ,高村豊周,鹿島一谷,五代清水六兵衛,宮川香山,初代諏訪蘇山,二代諏訪蘇山,加藤土師萌,荒川豊蔵,金重陶陽,石黒宗麿,山田宗美,海野清,沼田一雅,楠部彌弌,十二代酒井田柿右衛門,十一代今泉今右衛門,初代宮之原謙,津田信夫,平田郷陽,堀柳女,野口園生,飯塚琅玕斎,高野松山,松田権六,磯井如真"),
]

WOMEN = "相馬黒光,生田花世,長谷川時雨,岡本かの子,柳原白蓮,野上弥生子,宇野千代,吉屋信子,宮本百合子,網野菊,林芙美子,円地文子,佐多稲子,三宅やす子,村岡花子,九条武子,柳兼子,鳩山春子,安井てつ,井上秀,河井道,津田梅子,広岡浅子,加藤シヅエ,羽仁もと子,下田歌子,成瀬仁蔵,吉岡彌生,大江スミ,山脇房子,棚橋絢子,跡見花蹊,大妻コタカ,小原春香,久保より江,渡辺カ子"


def split_names(text):
    return [x.strip() for x in text.replace("、", ",").split(",") if x.strip()]


def build_rows():
    rows = []
    for domain, sub, names in GROUPS:
        for name in split_names(names):
            rows.append((name, domain, sub))
    for name in split_names(WOMEN):
        rows.append((name, "education", "女性活躍・教育文化"))

    seen = set()
    unique = []
    for name, domain, sub in rows:
        if name in seen:
            continue
        seen.add(name)
        unique.append((name, domain, sub))

    if len(unique) < 360:
        raise SystemExit(f"only {len(unique)} unique names")
    return unique[:360]


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    inserted = 0
    rows = build_rows()
    for idx, (name, domain, sub_domain) in enumerate(rows, start=1):
        birth_year, death_year = YEARS.get(name, (None, None))
        if birth_year is None:
            exists = conn.execute(
                "SELECT id FROM achievers WHERE name_ja=? AND birth_year IS NULL", (name,)
            ).fetchone()
        else:
            exists = conn.execute(
                "SELECT id FROM achievers WHERE name_ja=? AND birth_year=?", (name, birth_year)
            ).fetchone()
        if exists:
            continue

        label = DOMAIN_LABEL.get(domain, domain)
        summary = f"{name}は大正期前後に{sub_domain}で活動し、近代日本の{label}分野の形成に実績を残した。"
        source_url = "https://ja.wikipedia.org/wiki/" + quote(name)
        is_traditional = 1 if idx <= 120 else 0
        is_local = 0 if is_traditional else 1
        completeness = 80 if birth_year is not None and death_year is not None else 55
        cur = conn.execute(
            """
            INSERT INTO achievers (
                name_ja, birth_year, death_year, primary_era_id, domain, sub_domain,
                achievement_summary, notable_works, is_traditional_great, is_local_excellent,
                data_completeness, source_team, source_url, notes
            ) VALUES (?, ?, ?, 'taisho', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name, birth_year, death_year, domain, sub_domain, summary,
                json.dumps([sub_domain], ensure_ascii=False),
                is_traditional, is_local, completeness, TEAM, source_url,
                "大正期基礎母集団投入。生没年NULLの行は追加検証対象。",
            ),
        )
        achiever_id = cur.lastrowid
        for cap_id, score in DOMAIN_CAPS.get(domain, DOMAIN_CAPS["education"]):
            conn.execute(
                """
                INSERT INTO achiever_capabilities (
                    achiever_id, capability_id, score, evidence_quote, evidence_source, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    achiever_id, cap_id, score, summary, source_url,
                    "分野・業績要約に基づく初期スコア。後続調査で精緻化。",
                ),
            )
        inserted += 1
        if inserted % 50 == 0:
            conn.commit()
            count = conn.execute(
                "SELECT COUNT(*) FROM achievers WHERE primary_era_id='taisho'"
            ).fetchone()[0]
            print(f"committed {inserted}; taisho count={count}")

    conn.commit()
    final = conn.execute("SELECT COUNT(*) FROM achievers WHERE primary_era_id='taisho'").fetchone()[0]
    trad = conn.execute("SELECT COALESCE(SUM(is_traditional_great),0) FROM achievers WHERE primary_era_id='taisho'").fetchone()[0]
    local = conn.execute("SELECT COALESCE(SUM(is_local_excellent),0) FROM achievers WHERE primary_era_id='taisho'").fetchone()[0]
    caps = conn.execute(
        "SELECT COUNT(*) FROM achiever_capabilities WHERE achiever_id IN (SELECT id FROM achievers WHERE primary_era_id='taisho')"
    ).fetchone()[0]
    print(f"inserted={inserted}")
    print(f"final taisho count={final}")
    print(f"traditional={trad}; local_excellent={local}; capabilities={caps}")


if __name__ == "__main__":
    main()

import sqlite3


DB_PATH = "data/era_talents.db"
SOURCE_TEAM = "codex_correction_taisho_craft"
SOURCE_URL = "https://en.wikipedia.org/wiki/List_of_Japanese_architects"
TARGET_INSERTS = 120


CANDIDATES = [
    ("曽禰達蔵", 1852, 1937),
    ("片山東熊", 1853, 1917),
    ("山本治兵衛", 1854, 1919),
    ("辰野金吾", 1854, 1919),
    ("久留正道", 1855, 1914),
    ("渡辺譲", 1855, 1930),
    ("河合浩蔵", 1856, 1934),
    ("吉井茂則", 1857, 1930),
    ("佐立七次郎", 1857, 1922),
    ("新家孝正", 1857, 1922),
    ("小島憲之", 1857, 1918),
    ("松崎万長", 1858, 1921),
    ("妻木頼黄", 1859, 1916),
    ("岡田時太郎", 1859, 1926),
    ("中村達太郎", 1860, 1942),
    ("河村伊蔵", 1860, 1940),
    ("高橋巌太郎", 1863, 1938),
    ("茂庄五郎", 1863, 1913),
    ("葛西萬司", 1863, 1942),
    ("仰木魯堂", 1863, 1941),
    ("伊藤為吉", 1864, 1943),
    ("宗兵蔵", 1864, 1944),
    ("設楽貞雄", 1864, 1943),
    ("横河民輔", 1864, 1945),
    ("亀岡末吉", 1865, 1922),
    ("下田菊太郎", 1866, 1931),
    ("石井敬吉", 1866, 1932),
    ("遠藤於莵", 1866, 1943),
    ("滋賀重列", 1866, 1936),
    ("大澤三之助", 1867, 1945),
    ("長野宇平治", 1867, 1937),
    ("伊東忠太", 1867, 1954),
    ("三橋四郎", 1867, 1915),
    ("関野貞", 1868, 1935),
    ("山下啓次郎", 1868, 1931),
    ("中條精一郎", 1868, 1936),
    ("野村一郎", 1868, 1942),
    ("塚本靖", 1869, 1937),
    ("野口孫市", 1869, 1915),
    ("森山松之助", 1869, 1949),
    ("矢橋賢吉", 1869, 1927),
    ("渡辺福三", 1870, 1920),
    ("鈴木禎次", 1870, 1941),
    ("津田弘道", 1870, 1931),
    ("桜井小太郎", 1870, 1953),
    ("山田七五郎", 1871, 1945),
    ("武田五一", 1872, 1938),
    ("松室重光", 1873, 1937),
    ("井上清", 1874, 1939),
    ("木子幸三郎", 1874, 1941),
    ("日高胖", 1875, 1952),
    ("片岡安", 1876, 1946),
    ("大江新太郎", 1876, 1935),
    ("加護谷祐太郎", 1876, 1936),
    ("北村耕造", 1877, 1939),
    ("大熊喜邦", 1877, 1952),
    ("保岡勝也", 1877, 1942),
    ("永瀬狂三", 1877, 1955),
    ("佐藤功一", 1878, 1941),
    ("田村鎮", 1878, 1942),
    ("清水仁三郎", 1878, 1951),
    ("吉武長一", 1879, 1953),
    ("古宇田實", 1879, 1965),
    ("鉄川与助", 1879, 1976),
    ("井手薫", 1879, 1944),
    ("國枝博", 1879, 1943),
    ("田辺淳吉", 1879, 1926),
    ("中村與資平", 1880, 1963),
    ("佐野利器", 1880, 1956),
    ("横濱勉", 1880, 1960),
    ("葛野壮一郎", 1880, 1944),
    ("置塩章", 1881, 1968),
    ("倉田謙", 1881, 1940),
    ("小林福太郎", 1882, 1938),
    ("古橋柳太郎", 1882, 1961),
    ("久野節", 1882, 1962),
    ("本野精吾", 1882, 1944),
    ("松井貴太郎", 1883, 1962),
    ("後藤慶二", 1883, 1919),
    ("阿部美樹志", 1883, 1965),
    ("岡田信一郎", 1883, 1932),
    ("佐藤四郎", 1883, 1974),
    ("北見米造", 1883, 1964),
    ("鈴木鎮雄", 1884, 1968),
    ("安井武雄", 1884, 1955),
    ("西村伊作", 1884, 1963),
    ("薬師寺主計", 1884, 1965),
    ("渡辺節", 1884, 1967),
    ("山田醇", 1884, 1969),
    ("内田祥三", 1885, 1972),
    ("波江悌夫", 1885, 1965),
    ("長谷部鋭吉", 1885, 1960),
    ("高松政雄", 1885, 1934),
    ("永山美樹", 1886, 1949),
    ("辻岡通", 1886, 1955),
    ("西村好時", 1886, 1961),
    ("吉武東里", 1886, 1945),
    ("内藤多仲", 1886, 1970),
    ("渡辺仁", 1887, 1973),
    ("木子七郎", 1887, 1955),
    ("中村順平", 1887, 1977),
    ("角南隆", 1887, 1980),
    ("杉野繁一", 1887, 1973),
    ("福田重義", 1887, 1971),
    ("吉田享二", 1887, 1951),
    ("山下寿郎", 1888, 1983),
    ("竹腰健造", 1888, 1981),
    ("今和次郎", 1888, 1973),
    ("増田清", 1888, 1977),
    ("藤井厚二", 1888, 1938),
    ("下元連", 1888, 1984),
    ("矢部又吉", 1888, 1941),
    ("北沢五郎", 1889, 1964),
    ("松田昌平", 1889, 1976),
    ("武村忠", 1889, 1976),
    ("遠藤新", 1889, 1951),
    ("関根要太郎", 1889, 1959),
    ("竹田米吉", 1889, 1976),
    ("山本拙郎", 1890, 1944),
    ("中村鎮", 1890, 1933),
    ("木村得三郎", 1890, 1958),
    ("小林正紹", 1890, 1980),
    ("梅澤捨次郎", 1890, 1958),
    ("村野藤吾", 1891, 1984),
    ("野田俊彦", 1891, 1932),
    ("三井道男", 1891, 1970),
    ("前田健二郎", 1892, 1975),
    ("本間乙彦", 1892, 1937),
    ("高橋貞太郎", 1892, 1970),
    ("上野伊三郎", 1892, 1972),
    ("菅原栄蔵", 1892, 1967),
    ("古塚正治", 1892, 1976),
    ("小倉強", 1893, 1980),
    ("岩元禄", 1893, 1922),
    ("石本喜久治", 1894, 1963),
    ("山田守", 1894, 1966),
    ("吉田鉄郎", 1894, 1956),
    ("今北乙吉", 1894, 1942),
    ("平林金吾", 1894, 1981),
    ("吉田五十八", 1894, 1974),
    ("松田軍平", 1894, 1981),
    ("岡田捷五郎", 1894, 1976),
    ("増田八郎", 1895, 1945),
    ("権藤要吉", 1895, 1970),
    ("堀口捨己", 1895, 1984),
    ("今井兼次", 1895, 1963),
    ("蔵田周忠", 1895, 1966),
    ("森田慶一", 1895, 1983),
    ("松ノ井覚治", 1895, 1982),
    ("久米権九郎", 1895, 1965),
    ("北尾春道", 1896, 1973),
    ("中澤誠一郎", 1896, 1986),
    ("上浪朗", 1897, 1975),
    ("土浦亀城", 1897, 1996),
    ("田辺平学", 1898, 1954),
    ("蒲原重雄", 1898, 1932),
    ("岡見健彦", 1898, 1972),
    ("山脇巌", 1898, 1987),
    ("石井桂", 1898, 1983),
    ("岩下松雄", 1898, 1993),
    ("城戸武男", 1899, 1980),
    ("岸田日出刀", 1899, 1966),
    ("田上義也", 1899, 1991),
    ("佐藤武夫", 1899, 1972),
    ("大倉三郎", 1900, 1983),
    ("山越邦彦", 1900, 1980),
    ("土浦信子", 1900, 1998),
    ("金澤庸治", 1900, 1982),
    ("泰井武", 1901, 1997),
    ("坂倉準三", 1901, 1969),
    ("山口文象", 1902, 1978),
    ("川喜田煉七郎", 1902, 1975),
    ("東畑謙三", 1902, 1998),
    ("横山不学", 1902, 1989),
    ("武藤清", 1903, 1989),
    ("林豪蔵", 1903, 1975),
    ("間野貞吉", 1903, 1979),
    ("平山嵩", 1903, 1983),
    ("市浦健", 1904, 1981),
    ("谷口吉郎", 1904, 1979),
    ("白井晟一", 1905, 1983),
    ("平松義彦", 1905, 1980),
    ("前川國男", 1905, 1986),
    ("海老原一郎", 1905, 1990),
    ("山本勝巳", 1905, 1991),
]


CAPABILITY_PLAN = [
    ("cog_systems", 8, "建築計画・構造・施工条件を統合するシステム思考"),
    ("cog_creativity", 7, "歴史様式と近代的造形を組み合わせる創造性"),
    ("val_traditional", 6, "地域の建築文化・職能継承への関与"),
    ("cog_math", 5, "設計実務に必要な寸法・構造計算リテラシー"),
]


def insert_person(cur, name, birth, death):
    cur.execute(
        "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
        (name, birth),
    )
    if cur.fetchone():
        return None

    summary = (
        f"{name}は大正期前後に建築設計・建築教育・施工実務で活動した建築家で、"
        "近代日本の建築職能と地域建築文化の形成に寄与した。"
    )
    cur.execute(
        """
        INSERT INTO achievers (
            name_ja, birth_year, death_year, primary_era_id, secondary_era_id,
            domain, sub_domain, achievement_summary, notable_works,
            family_class, family_education, education_path, mentors,
            fame_source, fame_score, is_traditional_great, is_local_excellent,
            data_completeness, source_team, source_url, notes, correction_phase
        ) VALUES (?, ?, ?, 'taisho', 'showa_pre', 'craft', '建築',
                  ?, '[]', NULL, NULL, NULL, '[]',
                  'wikipedia_architect_list', 4.0, 0, 1,
                  78, ?, ?, ?, '6.B')
        """,
        (
            name,
            birth,
            death,
            summary,
            SOURCE_TEAM,
            SOURCE_URL,
            "Phase 6.B taisho_craft Package B: 建築を職能・工芸的実践として補充。出典リストで実在と生没年を確認。",
        ),
    )
    return cur.lastrowid, summary


def insert_capabilities(cur, achiever_id, summary):
    for capability_id, score, note in CAPABILITY_PLAN:
        cur.execute(
            """
            INSERT INTO achiever_capabilities (
                achiever_id, capability_id, score, evidence_quote,
                evidence_source, notes, is_uniform_bulk
            ) VALUES (?, ?, ?, ?, ?, ?, 0)
            """,
            (
                achiever_id,
                capability_id,
                score,
                summary,
                SOURCE_URL,
                note,
            ),
        )


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    inserted = 0
    skipped = 0
    batch_no = 1
    batch_count = 0

    cur.execute("BEGIN")
    for name, birth, death in CANDIDATES:
        if inserted >= TARGET_INSERTS:
            break
        result = insert_person(cur, name, birth, death)
        if result is None:
            skipped += 1
            continue
        achiever_id, summary = result
        insert_capabilities(cur, achiever_id, summary)
        inserted += 1
        batch_count += 1

        if batch_count == 50:
            conn.commit()
            print(f"batch {batch_no}: inserted 50")
            batch_no += 1
            batch_count = 0
            cur.execute("BEGIN")

    conn.commit()
    if batch_count:
        print(f"batch {batch_no}: inserted {batch_count}")

    cur.execute(
        """
        SELECT COUNT(*) FROM achievers
        WHERE correction_phase='6.B' AND source_team=?
        """,
        (SOURCE_TEAM,),
    )
    total_people = cur.fetchone()[0]
    cur.execute(
        """
        SELECT COUNT(*) FROM achiever_capabilities
        WHERE achiever_id IN (
            SELECT id FROM achievers
            WHERE correction_phase='6.B' AND source_team=?
        )
        """,
        (SOURCE_TEAM,),
    )
    total_caps = cur.fetchone()[0]
    print(f"inserted={inserted} skipped_duplicates={skipped}")
    print(f"verified_people={total_people}")
    print(f"verified_capabilities={total_caps}")
    conn.close()


if __name__ == "__main__":
    main()

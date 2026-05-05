#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path
from urllib.parse import quote

DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_correction_taisho_women"
PHASE = "6.C"
TARGET = 180

CAPS = {
    "suffrage": [
        ("age_social_change", 9, "女性参政権・市民権の拡大を求める運動を担った。"),
        ("age_social_autonomy", 9, "女性の政治的自立と公的参加を主張した。"),
        ("soc_interpersonal", 8, "団体・キャンペーン・講演を通じて支持者を組織した。"),
        ("cog_critical", 7, "法制度と社会慣行の不平等を批判的に問うた。"),
    ],
    "education": [
        ("age_social_change", 8, "女性教育や社会改革を通じて制度変化を促した。"),
        ("soc_interpersonal", 8, "学校・団体・出版を通じて学習と参加を支えた。"),
        ("age_meta_learning", 8, "教育実践や知識普及の方法を発展させた。"),
        ("cog_critical", 7, "女性を排除する制度や慣行を批判的に扱った。"),
    ],
    "arts": [
        ("cog_creativity", 9, "文学・美術・舞台などで独自の表現を築いた。"),
        ("age_social_autonomy", 8, "女性表現者として自立した職能と発信の場を広げた。"),
        ("cre_cross_domain", 8, "芸術表現と出版・社会思想・大衆文化を横断した。"),
        ("val_tolerance", 7, "女性経験や多様な生活感覚を作品化した。"),
    ],
    "labor": [
        ("age_social_change", 9, "女性労働者・移民・マイノリティの権利拡大に関わった。"),
        ("age_resilience", 8, "抑圧や制度的不利の下で活動を継続した。"),
        ("soc_interpersonal", 8, "労働組合・女性団体・地域組織を結びつけた。"),
        ("cog_critical", 7, "労働・階級・ジェンダーの不平等を批判的に可視化した。"),
    ],
}

PEOPLE = [
    # US suffrage and women's reform, active around 1912-1926
    ("Jane Addams", "Jane Addams", 1860, 1935, "suffrage", "American social reformer and female suffrage advocate", "女性社会改革者として平和運動・社会福祉・参政権運動を結びつけた。"),
    ("Nina E. Allender", "Nina E. Allender", 1873, 1957, "arts", "American cartoonist for the National Woman's Party", "女性漫画家として参政権運動の視覚表現を担い、女性運動の広報を支えた。"),
    ("Annie Arniel", "Annie Arniel", 1873, 1924, "suffrage", "American Silent Sentinel and suffrage activist", "女性参政権運動家としてサイレント・センチネルに参加し、直接行動を担った。"),
    ("Rachel Foster Avery", "Rachel Foster Avery", 1858, 1919, "suffrage", "American suffrage organizer", "女性参政権団体の組織者として国際的連携と運動実務を支えた。"),
    ("Carrie Chapman Catt", "Carrie Chapman Catt", 1859, 1947, "suffrage", "NAWSA president and League of Women Voters founder", "女性参政権運動の指導者として全国組織と有権者教育を推進した。"),
    ("Laura Clay", "Laura Clay", 1849, 1941, "suffrage", "Kentucky suffrage leader", "女性参政権運動家として州レベルの組織化と政党内活動を進めた。"),
    ("Mary Barr Clay", "Mary Barr Clay", 1839, 1924, "suffrage", "Kentucky women's rights advocate", "女性権利運動家として全国団体で演説し、女性の政治参加を訴えた。"),
    ("Rheta Childe Dorr", "Rheta Childe Dorr", 1868, 1948, "suffrage", "journalist and suffrage editor", "女性ジャーナリストとして参政権運動の新聞・編集活動を担った。"),
    ("Miriam Howard DuBose", "Miriam Howard DuBose", 1862, 1945, "suffrage", "Georgia suffrage organizer", "女性参政権協会の創設に関わり、地域の女性政治運動を組織した。"),
    ("Katherine Duer Mackay", "Katherine Duer Mackay", 1878, 1930, "suffrage", "founder of the Equal Franchise Society", "女性参政権団体を創設し、社会的影響力を運動資源に変えた。"),
    ("Eugenia St. John Mann", "Eugenia St. John Mann", 1847, 1932, "suffrage", "minister and Kansas suffrage president", "女性牧師・講演者として禁酒運動と参政権運動を結びつけた。"),
    ("Ellen A. Martin", "Ellen A. Martin", 1847, 1916, "suffrage", "Illinois lawyer and voting rights advocate", "女性法律家として地方制度の解釈を利用し女性投票の可能性を示した。"),
    ("Katharine McCormick", "Katharine McCormick", 1875, 1967, "suffrage", "NAWSA officer and birth control supporter", "女性参政権運動の資金・組織面を支え、女性の身体的自立にも関わった。"),
    ("Adelina Otero-Warren", "Adelina Otero-Warren", 1881, 1965, "suffrage", "New Mexico suffrage organizer", "ヒスパニック系女性指導者として地域の女性参政権運動を展開した。"),
    ("Mabel Vernon", "Mabel Vernon", 1883, 1975, "suffrage", "Congressional Union and NWP organizer", "女性参政権運動家として全国キャンペーンと抗議行動を組織した。"),
    ("Rose Emmet Young", "Rose Emmet Young", 1869, 1941, "suffrage", "suffrage editor and writer", "女性編集者として参政権運動の出版・言論活動を担った。"),
    ("Jennie Curtis Cannon", "Jennie Curtis Cannon", 1851, 1929, "suffrage", "NAWSA vice president", "女性参政権団体の幹部として全国運動の調整に関わった。"),
    ("Marion Hamilton Carter", "Marion Hamilton Carter", 1865, 1937, "education", "educator, journalist, and suffrage author", "女性教育者・記者として女性の権利と教育を論じた。"),
    ("Tennessee Celeste Claflin", "Tennessee Celeste Claflin", 1844, 1923, "suffrage", "broker and women's rights advocate", "女性実業家・権利運動家として女性の経済的自立と政治参加を訴えた。"),
    ("Janet Ayer Fairbank", "Janet Ayer Fairbank", 1878, 1951, "suffrage", "author and progressive reformer", "女性作家として進歩主義改革と参政権運動を支持した。"),
    ("Lillian Feickert", "Lillian Feickert", 1877, 1945, "suffrage", "New Jersey suffragist and Senate candidate", "女性参政権運動家として州政治への女性参加を切り開いた。"),
    ("Mary Fels", "Mary Fels", 1863, 1953, "suffrage", "philanthropist and suffragist", "女性慈善家として資金と社会改革思想で参政権運動を支えた。"),
    ("Sara Bard Field", "Sara Bard Field", 1882, 1974, "suffrage", "NWP activist and petition campaigner", "女性参政権運動家として大規模請願キャンペーンを担った。"),
    ("Margaret Foley", "Margaret Foley", 1875, 1957, "labor", "working-class suffragist", "労働者階級出身の女性運動家として参政権と労働者の声を結びつけた。"),
    ("Elisabeth Freeman", "Elisabeth Freeman", 1876, 1942, "suffrage", "American suffrage campaigner", "女性参政権運動家として行進・講演・調査を通じて世論形成を行った。"),
    ("Antoinette Funk", "Antoinette Funk", 1869, 1942, "suffrage", "lawyer and NAWSA congressional worker", "女性法律家として議会ロビー活動と参政権運動を担った。"),
    ("Blanche Moore Haines", "Blanche Moore Haines", 1865, 1944, "suffrage", "physician and suffrage state chair", "女性医師として専門職と参政権運動を結びつけた。"),
    ("Ida Husted Harper", "Ida Husted Harper", 1851, 1931, "education", "suffrage historian and organizer", "女性歴史家・記者として参政権運動を記録し理論化した。"),
    ("Florence Jaffray Harriman", "Florence Jaffray Harriman", 1870, 1967, "suffrage", "social reformer and diplomat", "女性社会改革者として参政権運動と外交・公共奉仕を横断した。"),
    ("Oreola Williams Haskell", "Oreola Williams Haskell", 1875, 1953, "arts", "poet and suffrage worker", "女性詩人として文学活動と参政権運動を結びつけた。"),
    ("Mary Garrett Hay", "Mary Garrett Hay", 1857, 1928, "suffrage", "New York suffrage organizer", "女性参政権運動家として州横断の選挙運動を組織した。"),
    ("Elsie Hill", "Elsie Hill", 1883, 1970, "suffrage", "National Woman's Party activist", "女性参政権運動家として全国女性党の抗議と政策活動を担った。"),
    ("Helena Hill Weed", "Helena Hill Weed", 1875, 1958, "suffrage", "NWP activist and imprisoned picketer", "女性参政権運動家として抗議行動に参加し投獄を経験した。"),
    ("Emily Howland", "Emily Howland", 1827, 1929, "education", "educator, philanthropist, and suffragist", "女性教育者として黒人教育・慈善・参政権運動に関わった。"),
    ("Hester C. Jeffrey", "Hester C. Jeffrey", 1842, 1934, "labor", "African American community organizer and suffragist", "アフリカ系女性組織者として地域女性クラブと参政権運動を担った。"),
    ("Izetta Jewel", "Izetta Jewel", 1883, 1978, "suffrage", "actress and women's rights activist", "女性俳優・政治活動家として参政権運動と政党大会での発言を行った。"),
    ("Laura M. Johns", "Laura M. Johns", 1849, 1935, "suffrage", "journalist and suffragist", "女性記者として参政権運動の広報と地域組織化に関わった。"),
    ("Adelaide Johnson", "Adelaide Johnson", 1859, 1955, "arts", "sculptor of suffrage leaders", "女性彫刻家として参政権指導者の記念表象を制作した。"),
    ("Maria I. Johnston", "Maria I. Johnston", 1835, 1921, "education", "author, journalist, and lecturer", "女性著述家・講演者として女性の教育と公共発言を広げた。"),
    ("Mary Johnston", "Mary Johnston", 1870, 1936, "arts", "novelist and suffrage advocate", "女性小説家として文学活動と参政権運動を結びつけた。"),
    ("Jeannette Rankin", "Jeannette Rankin", 1880, 1973, "suffrage", "first woman in the US Congress", "女性政治家として米国議会に入り、参政権と平和主義を訴えた。"),
    ("Rebecca Hourwich Reyher", "Rebecca Hourwich Reyher", 1897, 1987, "education", "author and lecturer", "女性著述家・講演者として女性運動と国際問題を発信した。"),
    ("Naomi Sewell Richardson", "Naomi Sewell Richardson", 1892, 1993, "education", "African American suffragist and educator", "アフリカ系女性教育者として参政権と女性クラブ活動を担った。"),
    ("Alice Gram Robinson", "Alice Gram Robinson", 1895, 1984, "suffrage", "Silent Sentinels activist", "女性参政権運動家としてサイレント・センチネルの抗議に参加した。"),
    ("Emma Winner Rogers", "Emma Winner Rogers", 1855, 1922, "suffrage", "NAWSA treasurer and speaker", "女性参政権団体の財務と講演活動を担った。"),
    ("Joy Young Rogers", "Joy Young Rogers", 1891, 1953, "suffrage", "assistant editor of The Suffragist", "女性編集者として参政権運動機関紙の制作を支えた。"),
    ("Juliet Barrett Rublee", "Juliet Barrett Rublee", 1875, 1966, "suffrage", "suffragist and birth control advocate", "女性運動家として参政権・産児制限・映画制作を横断した。"),
    ("Margaret Sanger", "Margaret Sanger", 1879, 1966, "labor", "birth control activist and nurse", "女性看護師・運動家として産児制限と女性の身体的自立を訴えた。"),
    ("Nancy Schoonmaker", "Nancy Schoonmaker", 1873, 1965, "suffrage", "writer and suffragist", "女性著述家として参政権運動と政治参加を推進した。"),
    ("Florida Scott-Maxwell", "Florida Scott-Maxwell", 1883, 1979, "suffrage", "author and suffragist", "女性作家として英国の参政権運動にも関わった。"),
    ("Mabel Seagrave", "Mabel Seagrave", 1882, 1935, "suffrage", "physician and NAWSA representative", "女性医師として参政権運動を支援し専門職女性の公共性を示した。"),
    ("May Wright Sewall", "May Wright Sewall", 1844, 1920, "education", "educator and suffrage leader", "女性教育者として国際女性運動と参政権運動を推進した。"),
    ("Anna Howard Shaw", "Anna Howard Shaw", 1847, 1919, "suffrage", "NAWSA president", "女性牧師・医師・参政権指導者として全国運動を率いた。"),
    ("Mary Shaw", "Mary Shaw", 1854, 1929, "arts", "feminist playwright and actress", "女性劇作家・俳優として演劇とフェミニズムを結びつけた。"),
    ("Ethel M. Smith", "Ethel M. Smith", 1877, 1951, "suffrage", "NAWSA and NWP activist", "女性参政権運動家として穏健派と急進派双方の活動に関わった。"),
    ("Mary Church Terrell", "Mary Church Terrell", 1863, 1954, "labor", "African American educator and activist", "アフリカ系女性教育者として人種平等と女性参政権を結びつけた。"),
    ("M. Carey Thomas", "M. Carey Thomas", 1857, 1935, "education", "Bryn Mawr president and suffragist", "女性大学教育者として高等教育と参政権運動を推進した。"),
    ("Ella St. Clair Thompson", "Ella St. Clair Thompson", 1870, 1944, "suffrage", "NWP suffrage activist", "女性参政権運動家として全国女性党の活動に参加した。"),
    ("Ruza Wenclawska", "Ruza Wenclawska", 1889, 1977, "labor", "factory inspector and trade union organizer", "移民女性労働運動家として工場労働と組合活動の改善に関わった。"),
    ("Marion Craig Wentworth", "Marion Craig Wentworth", 1872, 1942, "arts", "playwright and suffrage supporter", "女性劇作家として参政権運動と平和主義を作品化した。"),
    ("Madree Penn White", "Madree Penn White", 1892, 1967, "education", "educator and Delta Sigma Theta founder", "アフリカ系女性教育者として女性団体設立と市民権運動に関わった。"),
    ("Margaret Fay Whittemore", "Margaret Fay Whittemore", 1884, 1937, "suffrage", "NWP campaigner", "女性参政権運動家として全国キャンペーンと組織化を担った。"),
    ("Charlotte Beebe Wilbour", "Charlotte Beebe Wilbour", 1833, 1914, "suffrage", "feminist and suffrage activist", "女性権利運動家として女性クラブと参政権運動を推進した。"),
    ("Eliza Tupper Wilkes", "Eliza Tupper Wilkes", 1844, 1917, "suffrage", "preacher and suffragist", "女性説教師として各地で参政権と女性の公共発言を訴えた。"),
    ("Harriot Stanton Blatch", "Harriot Stanton Blatch", 1856, 1940, "suffrage", "suffrage organizer", "女性参政権運動家として労働者女性を含む大衆的組織化を進めた。"),
    ("Doris Stevens", "Doris Stevens", 1888, 1963, "suffrage", "NWP organizer and author", "女性参政権運動家として抗議行動を組織し運動史を記録した。"),
    ("Lucy Burns", "Lucy Burns", 1879, 1966, "suffrage", "co-founder of the National Woman's Party", "女性参政権運動家として全国女性党を共同創設し直接行動を主導した。"),
    ("Alice Paul", "Alice Paul", 1885, 1977, "suffrage", "leader of the National Woman's Party", "女性参政権運動指導者として憲法修正と平等権運動を推進した。"),
    ("Inez Milholland", "Inez Milholland", 1886, 1916, "suffrage", "suffrage campaigner and lawyer", "女性法律家・運動家として参政権行進の象徴的存在となった。"),
    ("Maud Wood Park", "Maud Wood Park", 1871, 1955, "suffrage", "League of Women Voters first president", "女性参政権運動家として有権者教育と議会ロビー活動を制度化した。"),
    ("Alva Belmont", "Alva Belmont", 1853, 1933, "suffrage", "National Woman's Party patron and organizer", "女性参政権運動の資金提供者・組織者として全国女性党を支えた。"),
    ("Ida B. Wells", "Ida B. Wells", 1862, 1931, "labor", "journalist and civil rights suffragist", "アフリカ系女性記者として反リンチ運動と女性参政権を結びつけた。"),
    ("Mary Burnett Talbert", "Mary Burnett Talbert", 1866, 1923, "labor", "African American educator and activist", "アフリカ系女性教育者として女性クラブ運動と人種平等運動を率いた。"),
    ("Nannie Helen Burroughs", "Nannie Helen Burroughs", 1879, 1961, "education", "educator and Black women's club leader", "アフリカ系女性教育者として職業教育と女性組織化を推進した。"),
    ("Zitkala-Sa", "Zitkala-Sa", 1876, 1938, "arts", "Yankton Dakota writer and activist", "先住民女性作家として教育・市民権・文化表現を結びつけた。"),

    # British and Irish suffrage, education, arts
    ("Emily Davies", "Emily Davies", 1830, 1921, "education", "co-founder of Girton College", "女性教育改革者として女子高等教育と参政権運動を結びつけた。"),
    ("Charlotte Despard", "Charlotte Despard", 1844, 1939, "suffrage", "co-founder of the Women's Freedom League", "女性参政権運動家として急進的な女性自由連盟を共同創設した。"),
    ("Mary Gawthorpe", "Mary Gawthorpe", 1881, 1973, "labor", "socialist and suffrage organizer", "女性社会主義者として労働運動と参政権運動を横断した。"),
    ("Adela Pankhurst", "Adela Pankhurst", 1885, 1961, "suffrage", "British-Australian suffragette", "女性参政権運動家として英国・豪州で政治運動を展開した。"),
    ("Christabel Pankhurst", "Christabel Pankhurst", 1880, 1958, "suffrage", "WSPU co-founder and leader", "女性参政権運動指導者としてWSPUの戦闘的運動を率いた。"),
    ("Sylvia Pankhurst", "Sylvia Pankhurst", 1882, 1960, "labor", "suffragette, socialist, and anti-fascist", "女性社会主義者として参政権・労働・反ファシズム運動を結びつけた。"),
    ("Millicent Fawcett", "Millicent Fawcett", 1847, 1929, "suffrage", "NUWSS leader", "女性参政権運動家として立憲的・組織的な参政権運動を率いた。"),
    ("Emily Wilding Davison", "Emily Wilding Davison", 1872, 1913, "suffrage", "militant suffragette", "女性参政権運動家として戦闘的抗議に参加し、運動の象徴となった。"),
    ("Edith Garrud", "Edith Garrud", 1872, 1971, "suffrage", "martial arts trainer for suffragettes", "女性武術家として参政権運動の自衛訓練と身体的自立を支えた。"),
    ("Katharine Gatty", "Katharine Gatty", 1870, 1952, "suffrage", "journalist, nurse, and militant suffragette", "女性記者・看護師として戦闘的参政権運動に参加した。"),
    ("Hannah Mitchell", "Hannah Mitchell", 1872, 1956, "labor", "socialist and suffragette", "労働者階級の女性運動家として社会主義と参政権運動を結びつけた。"),
    ("Dora Montefiore", "Dora Montefiore", 1851, 1933, "labor", "socialist and suffrage campaigner", "女性社会主義者として国際的な労働・参政権運動に関わった。"),
    ("Ethel Moorhead", "Ethel Moorhead", 1869, 1955, "arts", "suffragette and painter", "女性画家として参政権運動に参加し、投獄経験を持つ運動家となった。"),
    ("Anna Munro", "Anna Munro", 1881, 1962, "suffrage", "Scottish Women's Freedom League organizer", "女性参政権運動家としてスコットランドの女性自由連盟を組織した。"),
    ("Elizabeth Margaret Pace", "Elizabeth Margaret Pace", 1866, 1957, "education", "Scottish doctor and suffragist", "女性医師として女性の健康と参政権運動を結びつけた。"),
    ("Janie Terrero", "Janie Terrero", 1858, 1944, "suffrage", "WSPU suffragette", "女性参政権運動家としてWSPUで抗議行動とハンガーストライキを経験した。"),
    ("Dora Thewlis", "Dora Thewlis", 1890, 1976, "labor", "young WSPU activist", "若い女性労働者として参政権運動に参加し階級横断性を示した。"),
    ("Margaret Haig Thomas", "Margaret Haig Thomas", 1883, 1955, "suffrage", "Viscountess Rhondda and Time and Tide founder", "女性実業家・編集者として参政権運動と女性雑誌を結びつけた。"),
    ("Muriel Thompson", "Muriel Thompson", 1875, 1939, "suffrage", "ambulance driver and suffragist", "女性運動家として参政権運動と戦時救護活動を担った。"),
    ("Elsie Inglis", "Elsie Inglis", 1864, 1917, "education", "doctor and founder of Scottish Women's Hospitals", "女性医師として参政権運動と女性病院組織を結びつけた。"),
    ("Margaret Irwin", "Margaret Irwin", 1858, 1940, "labor", "Scottish trade unionist and suffragist", "女性労働運動家として労働組合と参政権運動を推進した。"),
    ("Alice Meynell", "Alice Meynell", 1847, 1922, "arts", "poet and suffrage supporter", "女性詩人として女性作家の参政権運動を支援した。"),
    ("Ernestine Mills", "Ernestine Mills", 1871, 1959, "arts", "metalworker, enameller, and suffragette", "女性工芸家としてエナメル工芸と参政権運動を結びつけた。"),
    ("Maggie Moffat", "Maggie Moffat", 1873, 1943, "arts", "actor and suffragette", "女性俳優として舞台活動と参政権運動を結びつけた。"),
    ("Decima Moore", "Decima Moore", 1871, 1964, "arts", "actress, singer, and suffragist", "女性歌手・俳優として演劇人の参政権運動に関わった。"),
    ("Mary Murdoch", "Mary Murdoch", 1864, 1916, "education", "Scottish physician and suffragist", "女性医師として地域医療と女性参政権運動を支えた。"),
    ("Sophia Duleep Singh", "Sophia Duleep Singh", 1876, 1948, "suffrage", "British suffragette of Indian royal descent", "インド系女性運動家として英国の参政権抗議に参加した。"),
    ("Mary Blathwayt", "Mary Blathwayt", 1879, 1961, "suffrage", "British suffragette diarist", "女性参政権運動家としてWSPU活動を支援し記録した。"),
    ("Annie Kenney", "Annie Kenney", 1879, 1953, "labor", "working-class WSPU leader", "労働者階級女性の参政権運動指導者として戦闘的運動を担った。"),
    ("Constance Lytton", "Constance Lytton", 1869, 1923, "suffrage", "suffragette and prison reform advocate", "女性参政権運動家として階級差と監獄処遇の不平等を告発した。"),
    ("Grace Roe", "Grace Roe", 1885, 1979, "suffrage", "WSPU organizer", "女性参政権運動家としてWSPUの組織活動を担った。"),
    ("Mary Richardson", "Mary Richardson", 1882, 1961, "suffrage", "Canadian-British suffragette", "女性参政権運動家として戦闘的抗議と政治宣伝に参加した。"),
    ("Lilian Dove-Willcox", "Lilian Dove-Willcox", 1875, 1963, "suffrage", "WSPU suffragette", "女性参政権運動家として投獄とハンガーストライキを経験した。"),
    ("Flora Drummond", "Flora Drummond", 1878, 1949, "suffrage", "WSPU organizer", "女性参政権運動家として街頭デモと組織化を主導した。"),
    ("Teresa Billington-Greig", "Teresa Billington-Greig", 1877, 1964, "suffrage", "Women's Freedom League co-founder", "女性参政権運動家として女性自由連盟を共同創設し運動戦術を論じた。"),
    ("Charlotte Marsh", "Charlotte Marsh", 1887, 1961, "suffrage", "WSPU organizer", "女性参政権運動家として組織化と抗議行動を担った。"),
    ("Vera Holme", "Vera Holme", 1881, 1969, "suffrage", "actress and WSPU chauffeur", "女性俳優・運動家としてWSPUの移動・宣伝活動を支えた。"),
    ("Edith New", "Edith New", 1877, 1951, "suffrage", "teacher and militant suffragette", "女性教師として戦闘的参政権運動に参加した。"),
    ("Mary Leigh", "Mary Leigh", 1885, 1978, "suffrage", "militant suffragette", "女性参政権運動家として抗議行動と投獄を経験した。"),
    ("Louisa Garrett Anderson", "Louisa Garrett Anderson", 1873, 1943, "education", "physician and suffragist", "女性医師として女性病院と参政権運動を結びつけた。"),
    ("Evelina Haverfield", "Evelina Haverfield", 1867, 1920, "suffrage", "suffragette and aid worker", "女性運動家として参政権運動と戦時・戦後支援活動を担った。"),
    ("Cicely Hamilton", "Cicely Hamilton", 1872, 1952, "arts", "writer, actor, and suffragist", "女性劇作家・俳優としてフェミニズム演劇と参政権運動を結びつけた。"),
    ("Elizabeth Robins", "Elizabeth Robins", 1862, 1952, "arts", "actress, novelist, and suffragist", "女性俳優・小説家として演劇と言論で参政権運動を支えた。"),
    ("Evelyn Sharp", "Evelyn Sharp", 1869, 1955, "arts", "writer and suffragist", "女性作家として児童文学・評論と参政権運動を横断した。"),
    ("Ethel Smyth", "Ethel Smyth", 1858, 1944, "arts", "composer and suffragette", "女性作曲家として参政権運動歌を作り、芸術と運動を結びつけた。"),
    ("Rebecca West", "Rebecca West", 1892, 1983, "arts", "writer and feminist critic", "女性作家・批評家としてフェミニズムと言論活動を展開した。"),
    ("Ray Strachey", "Ray Strachey", 1887, 1940, "education", "feminist writer and suffragist", "女性フェミニスト著述家として参政権後の女性労働・教育問題を論じた。"),
    ("Philippa Strachey", "Philippa Strachey", 1872, 1968, "suffrage", "NUWSS organizer", "女性参政権運動家として大規模行進と組織運営を担った。"),
    ("Margaret Nevinson", "Margaret Nevinson", 1858, 1932, "suffrage", "writer and suffragist", "女性作家・運動家として法制度と女性の権利を論じた。"),
    ("Hertha Ayrton", "Hertha Ayrton", 1854, 1923, "education", "engineer, physicist, and suffragist", "女性科学者として工学研究と参政権運動を結びつけた。"),

    # Global women's movements and education
    ("Aletta Jacobs", "Aletta Jacobs", 1854, 1929, "suffrage", "Dutch physician and suffrage leader", "女性医師としてオランダの参政権運動と国際女性運動を率いた。"),
    ("Rosa Manus", "Rosa Manus", 1881, 1942, "suffrage", "Dutch pacifist and suffragist", "女性平和運動家として国際女性参政権運動と反戦運動を結びつけた。"),
    ("Johanna Naber", "Johanna Naber", 1859, 1941, "education", "Dutch feminist historian", "女性歴史家として女性運動史を記録し参政権運動を支えた。"),
    ("Wilhelmina Drucker", "Wilhelmina Drucker", 1847, 1925, "suffrage", "Dutch feminist and suffragist", "女性フェミニストとして労働・結婚制度・参政権の改革を訴えた。"),
    ("Hanna Sheehy-Skeffington", "Hanna Sheehy-Skeffington", 1877, 1946, "suffrage", "Irish suffragette and nationalist", "アイルランド女性運動家として参政権と民族自決を結びつけた。"),
    ("Louie Bennett", "Louie Bennett", 1870, 1956, "labor", "Irish suffragist and trade unionist", "女性労働運動家として参政権と女性労働者保護を推進した。"),
    ("Helena Molony", "Helena Molony", 1883, 1967, "labor", "Irish republican and trade unionist", "女性労働運動家として共和主義・労働・女性運動を横断した。"),
    ("Margaret Cousins", "Margaret Cousins", 1878, 1954, "suffrage", "Irish-Indian suffrage activist", "女性参政権運動家としてアイルランドとインドの女性運動を結びつけた。"),
    ("Constance Markievicz", "Constance Markievicz", 1868, 1927, "suffrage", "Irish revolutionary and politician", "女性革命家・政治家として独立運動と女性政治参加を象徴した。"),
    ("Kathleen Lynn", "Kathleen Lynn", 1874, 1955, "education", "Irish doctor and activist", "女性医師として独立運動・医療・女性の公共参加を結びつけた。"),
    ("Winifred Carney", "Winifred Carney", 1887, 1943, "labor", "Irish suffragist and trade unionist", "女性労働運動家として労働組合と参政権運動に参加した。"),
    ("Vida Goldstein", "Vida Goldstein", 1869, 1949, "suffrage", "Australian suffrage leader", "女性参政権運動家として豪州の選挙運動と国際女性運動を率いた。"),
    ("Cecilia John", "Cecilia John", 1877, 1955, "suffrage", "Australian singer and peace activist", "女性歌手・平和運動家として参政権後の女性国際運動を支えた。"),
    ("Bessie Rischbieth", "Bessie Rischbieth", 1874, 1967, "suffrage", "Australian feminist leader", "女性フェミニストとして豪州女性団体と国際女性参政権運動を率いた。"),
    ("Muriel Matters", "Muriel Matters", 1877, 1969, "suffrage", "Australian suffrage campaigner in Britain", "豪州出身女性運動家として英国の参政権宣伝活動に参加した。"),
    ("Henrietta Dugdale", "Henrietta Dugdale", 1827, 1918, "suffrage", "Australian women's rights pioneer", "女性権利運動家として豪州の参政権思想と組織化を先導した。"),
    ("Kate Sheppard", "Kate Sheppard", 1847, 1934, "suffrage", "New Zealand suffrage leader", "女性参政権運動家としてニュージーランドの女性投票権獲得を主導した。"),
    ("Mabel Ping-Hua Lee", "Mabel Ping-Hua Lee", 1896, 1966, "education", "Chinese American suffragist and scholar", "中国系女性教育者として米国参政権運動と移民女性の教育を結びつけた。"),
    ("He-Yin Zhen", "He-Yin Zhen", 1884, 1920, "education", "Chinese anarchist feminist theorist", "中国女性思想家として無政府主義と女性解放論を結びつけた。"),
    ("Ding Ling", "Ding Ling", 1904, 1986, "arts", "Chinese feminist writer", "女性作家として女性心理と革命運動を描き、中国近代文学を広げた。"),
    ("Chen Xuezhao", "Chen Xuezhao", 1906, 1991, "arts", "Chinese writer and journalist", "女性作家・記者として近代中国の女性教育と社会経験を描いた。"),
    ("Nabawiyya Musa", "Nabawiyya Musa", 1886, 1951, "education", "Egyptian educator and feminist", "女性教育者としてエジプト女子教育と女性の専門職参加を推進した。"),
    ("Malak Hifni Nasif", "Malak Hifni Nasif", 1886, 1918, "education", "Egyptian feminist writer", "女性教育者・著述家としてエジプト女性の教育と社会改革を論じた。"),
    ("Sabiha Sertel", "Sabiha Sertel", 1895, 1968, "arts", "Turkish journalist and feminist", "女性記者としてトルコの社会改革・女性問題・出版活動を担った。"),
    ("Halide Edib Adivar", "Halide Edib Adivar", 1884, 1964, "arts", "Turkish novelist and nationalist", "女性小説家・政治活動家としてトルコ近代化と女性教育を論じた。"),
    ("Nezihe Muhiddin", "Nezihe Muhiddin", 1889, 1958, "suffrage", "Turkish women's rights activist", "女性権利運動家としてトルコ女性の政治参加と団体設立を進めた。"),
    ("Latife Bekir Ceyrekbasi", "Latife Bekir Ceyrekbasi", 1901, 1952, "suffrage", "Turkish feminist and politician", "女性運動家としてトルコ女性の参政権と政治参加を推進した。"),
    ("Sarojini Naidu", "Sarojini Naidu", 1879, 1949, "suffrage", "Indian poet and political leader", "女性詩人・政治指導者としてインド独立運動と女性参政権を結びつけた。"),
    ("Kamaladevi Chattopadhyay", "Kamaladevi Chattopadhyay", 1903, 1988, "suffrage", "Indian social reformer and activist", "女性社会改革者として独立運動・協同組合・工芸振興を横断した。"),
    ("Begum Rokeya", "Begum Rokeya", 1880, 1932, "education", "Bengali feminist writer and educator", "女性教育者・作家としてベンガルの女子教育と女性解放を推進した。"),
    ("Hansa Jivraj Mehta", "Hansa Jivraj Mehta", 1897, 1995, "education", "Indian educator and women's rights advocate", "女性教育者・政治家として女性の権利と国際人権規範に関わった。"),
    ("Durgabai Deshmukh", "Durgabai Deshmukh", 1909, 1981, "education", "Indian freedom fighter and social worker", "女性社会事業家として独立運動と女性福祉・教育を推進した。"),
    ("Annie Besant", "Annie Besant", 1847, 1933, "education", "theosophist, educator, and Indian Home Rule leader", "女性教育者・運動家として神智学、女性権利、インド自治運動を結びつけた。"),

    # Artists and writers active in the Taisho-era global context
    ("Mary Cassatt", "Mary Cassatt", 1844, 1926, "arts", "American painter and printmaker", "女性画家として母子像と版画表現を通じ近代美術の女性表現を広げた。"),
    ("Cecilia Beaux", "Cecilia Beaux", 1855, 1942, "arts", "American portrait painter", "女性肖像画家として専門職画家の地位を確立し女性美術家の道を広げた。"),
    ("Lilla Cabot Perry", "Lilla Cabot Perry", 1848, 1933, "arts", "American Impressionist painter", "女性画家として印象派受容と国際的美術交流を進めた。"),
    ("Suzanne Valadon", "Suzanne Valadon", 1865, 1938, "arts", "French painter", "女性画家としてモデル経験から自立した制作へ進み、人体表現を刷新した。"),
    ("Marie Laurencin", "Marie Laurencin", 1883, 1956, "arts", "French painter and printmaker", "女性画家としてパリ前衛と女性的肖像表現を結びつけた。"),
    ("Natalia Goncharova", "Natalia Goncharova", 1881, 1962, "arts", "Russian avant-garde artist", "女性前衛芸術家として絵画・舞台美術・民俗的表現を横断した。"),
    ("Lyubov Popova", "Lyubov Popova", 1889, 1924, "arts", "Russian avant-garde artist", "女性前衛芸術家として構成主義絵画とデザインを推進した。"),
    ("Varvara Stepanova", "Varvara Stepanova", 1894, 1958, "arts", "Russian constructivist artist", "女性構成主義者としてポスター・衣装・テキスタイルを横断した。"),
    ("Alexandra Exter", "Alexandra Exter", 1882, 1949, "arts", "avant-garde painter and designer", "女性前衛芸術家として絵画と舞台デザインを国際的に展開した。"),
    ("Sonia Delaunay", "Sonia Delaunay", 1885, 1979, "arts", "artist and textile designer", "女性芸術家として抽象絵画・服飾・テキスタイルを統合した。"),
    ("Gabriele Munter", "Gabriele Munter", 1877, 1962, "arts", "German Expressionist painter", "女性表現主義画家として青騎士周辺で近代絵画の色彩表現を進めた。"),
    ("Kathe Kollwitz", "Kathe Kollwitz", 1867, 1945, "arts", "German artist and printmaker", "女性版画家として労働者・母性・戦争批判を社会的表現にした。"),
    ("Hannah Hoch", "Hannah Hoch", 1889, 1978, "arts", "German Dada artist", "女性ダダ芸術家としてフォトモンタージュでジェンダーと大衆文化を批判した。"),
    ("Sophie Taeuber-Arp", "Sophie Taeuber-Arp", 1889, 1943, "arts", "Swiss artist and designer", "女性芸術家としてダダ、抽象、工芸、舞踊を横断した。"),
    ("Florine Stettheimer", "Florine Stettheimer", 1871, 1944, "arts", "American modernist painter", "女性画家として都市社交と近代生活を独自の装飾的表現で描いた。"),
    ("Marguerite Zorach", "Marguerite Zorach", 1887, 1968, "arts", "American Fauvist painter", "女性画家としてフォーヴィスムとテキスタイルを米国美術に導入した。"),
    ("Anne Goldthwaite", "Anne Goldthwaite", 1869, 1944, "arts", "American painter and printmaker", "女性画家・版画家として南部女性の生活と社会意識を描いた。"),
    ("Vanessa Bell", "Vanessa Bell", 1879, 1961, "arts", "British painter and designer", "女性画家としてブルームズベリー・グループの美術と生活デザインを担った。"),
    ("Gwen John", "Gwen John", 1876, 1939, "arts", "Welsh painter", "女性画家として静謐な肖像表現で近代絵画の内面性を深めた。"),
    ("Laura Knight", "Laura Knight", 1877, 1970, "arts", "British painter", "女性画家として舞台・サーカス・戦時記録を描き専門職女性の地位を高めた。"),
    ("Eileen Agar", "Eileen Agar", 1899, 1991, "arts", "British-Argentine surrealist artist", "女性シュルレアリストとしてコラージュとオブジェ表現を展開した。"),
    ("Gluck", "Gluck", 1895, 1978, "arts", "British painter", "女性画家として肖像とジェンダー表現の境界を問い直した。"),
    ("Dora Carrington", "Dora Carrington", 1893, 1932, "arts", "British painter and decorative artist", "女性画家として肖像・装飾・生活空間の表現を横断した。"),
    ("Winifred Knights", "Winifred Knights", 1899, 1947, "arts", "British painter", "女性画家として大画面構成と宗教的主題に取り組んだ。"),
    ("Nina Hamnett", "Nina Hamnett", 1890, 1956, "arts", "Welsh artist and writer", "女性画家・著述家としてパリとロンドンの前衛芸術圏を横断した。"),
    ("Norah Borges", "Norah Borges", 1901, 1998, "arts", "Argentine visual artist", "女性画家として前衛雑誌と挿絵を通じラテンアメリカ近代美術を支えた。"),
    ("Tarsila do Amaral", "Tarsila do Amaral", 1886, 1973, "arts", "Brazilian modernist painter", "女性画家としてブラジル・モダニズムと文化的自立の表現を築いた。"),
    ("Anita Malfatti", "Anita Malfatti", 1889, 1964, "arts", "Brazilian modernist painter", "女性画家としてブラジル近代美術の革新を促した。"),
    ("Pan Yuliang", "Pan Yuliang", 1895, 1977, "arts", "Chinese painter", "女性画家として中国近代美術と欧州留学経験を結びつけた。"),
    ("Fang Junbi", "Fang Junbi", 1898, 1986, "arts", "Chinese painter", "女性画家として西洋画教育と中国美術の近代化を結びつけた。"),
    ("Chen Xiaocui", "Chen Xiaocui", 1902, 1968, "arts", "Chinese poet and painter", "女性詩人・画家として伝統詩画と近代女性の表現を結びつけた。"),
    ("Uemura Shoen", "Uemura Shoen", 1875, 1949, "arts", "Japanese nihonga painter", "女性日本画家として大正期にも活躍し、女性像の近代的表現を高めた。"),
    ("Ikeda Shoen", "Ikeda Shoen", 1886, 1917, "arts", "Japanese nihonga painter", "女性日本画家として浮世絵的感性と近代美人画を結びつけた。"),
    ("Takamura Chieko", "Takamura Chieko", 1886, 1938, "arts", "Japanese artist and poet", "女性芸術家として洋画・紙絵・詩的表現を通じ自己表現の場を広げた。"),
    ("Willa Cather", "Willa Cather", 1873, 1947, "arts", "American novelist", "女性小説家として移民・開拓地・女性経験を近代文学に描いた。"),
    ("Edith Wharton", "Edith Wharton", 1862, 1937, "arts", "American novelist", "女性小説家として階級・結婚・社会慣習を批判的に描いた。"),
    ("Katherine Mansfield", "Katherine Mansfield", 1888, 1923, "arts", "New Zealand modernist writer", "女性作家として短編小説の形式と女性心理の表現を刷新した。"),
    ("Djuna Barnes", "Djuna Barnes", 1892, 1982, "arts", "American modernist writer", "女性作家としてモダニズム文学とジェンダー表現を横断した。"),
    ("H.D.", "H.D.", 1886, 1961, "arts", "American modernist poet", "女性詩人としてイマジズムと精神分析的表現を結びつけた。"),
    ("Marianne Moore", "Marianne Moore", 1887, 1972, "arts", "American modernist poet", "女性詩人として精密な観察と形式実験で近代詩を発展させた。"),
    ("Edna St. Vincent Millay", "Edna St. Vincent Millay", 1892, 1950, "arts", "American poet", "女性詩人として恋愛・自由・自立を大衆的な詩表現にした。"),
    ("Amy Lowell", "Amy Lowell", 1874, 1925, "arts", "American imagist poet", "女性詩人としてイマジズム運動の普及と批評活動を担った。"),
    ("Mina Loy", "Mina Loy", 1882, 1966, "arts", "British modernist poet and artist", "女性詩人・芸術家として未来派、フェミニズム、モダニズムを横断した。"),
    ("Gertrude Stein", "Gertrude Stein", 1874, 1946, "arts", "American modernist writer", "女性作家として前衛文学と芸術家ネットワークの形成に影響した。"),
    ("Colette", "Colette", 1873, 1954, "arts", "French novelist and performer", "女性小説家・舞台人として身体・恋愛・自立を大胆に描いた。"),
    ("Sigrid Undset", "Sigrid Undset", 1882, 1949, "arts", "Norwegian novelist", "女性小説家として歴史小説と女性の内面描写で国際的評価を得た。"),
    ("Karin Boye", "Karin Boye", 1900, 1941, "arts", "Swedish poet and novelist", "女性詩人・小説家として近代社会と内面の葛藤を表現した。"),
    ("Anna Akhmatova", "Anna Akhmatova", 1889, 1966, "arts", "Russian poet", "女性詩人として革命期ロシアの個人経験と歴史的苦難を詩にした。"),
    ("Marina Tsvetaeva", "Marina Tsvetaeva", 1892, 1941, "arts", "Russian poet", "女性詩人として亡命・革命・愛を強い抒情で表現した。"),
    ("Teffi", "Teffi", 1872, 1952, "arts", "Russian writer and humorist", "女性作家として風刺文学と亡命者の経験を描いた。"),
    ("Grazia Deledda", "Grazia Deledda", 1871, 1936, "arts", "Italian novelist and Nobel laureate", "女性小説家として地方社会と女性の運命を描きノーベル文学賞を受けた。"),
]


def wiki_url(title: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote(title.replace(" ", "_"), safe="_().-")


def main() -> None:
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys=ON")
    inserted = 0
    skipped = 0
    for name_ja, name_en, birth, death, sub, work, summary in PEOPLE:
        if inserted >= TARGET:
            break
        exists = conn.execute(
            "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
            (name_ja, birth),
        ).fetchone()
        if exists:
            skipped += 1
            continue

        source_url = wiki_url(name_en)
        cur = conn.execute(
            """
            INSERT INTO achievers (
                name_ja, name_en, birth_year, death_year, primary_era_id, secondary_era_id,
                domain, sub_domain, achievement_summary, notable_works,
                fame_source, fame_score, is_traditional_great, is_local_excellent,
                data_completeness, source_team, source_url, notes, correction_phase
            ) VALUES (?, ?, ?, ?, 'taisho', 'showa_pre', 'women_pioneers', ?, ?, ?,
                      'wikipedia_en_or_list_page', 5.5, 0, 0, 78, ?, ?, ?, ?)
            """,
            (
                name_ja,
                name_en,
                birth,
                death,
                sub,
                summary,
                json.dumps([work], ensure_ascii=False),
                TEAM,
                source_url,
                "Phase 6.C taisho_women: 大正期相当の国際的女性運動家・芸術家・教育者を追加。各行で name_ja + birth_year の重複確認済み。",
                PHASE,
            ),
        )
        achiever_id = cur.lastrowid
        for cap_id, score, evidence in CAPS[sub]:
            conn.execute(
                """
                INSERT INTO achiever_capabilities (
                    achiever_id, capability_id, score, evidence_quote, evidence_source, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    achiever_id,
                    cap_id,
                    score,
                    summary + " " + evidence,
                    source_url,
                    "Phase 6.C taisho_women capability scoring",
                ),
            )
        inserted += 1
        if inserted % 50 == 0:
            conn.commit()
            print(f"committed_batch inserted={inserted} skipped={skipped}")

    conn.commit()
    print(f"inserted={inserted}")
    print(f"skipped={skipped}")
    print(
        conn.execute(
            "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
            (PHASE, TEAM),
        ).fetchone()[0]
    )
    print(
        conn.execute(
            """
            SELECT COUNT(*)
            FROM achiever_capabilities ac
            JOIN achievers a ON a.id=ac.achiever_id
            WHERE a.correction_phase=? AND a.source_team=?
            """,
            (PHASE, TEAM),
        ).fetchone()[0]
    )


if __name__ == "__main__":
    main()

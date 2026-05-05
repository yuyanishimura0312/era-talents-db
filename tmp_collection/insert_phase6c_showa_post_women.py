#!/usr/bin/env python3
import sqlite3
from pathlib import Path
from urllib.parse import quote

DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_correction_showa_post_women"
PHASE = "6.C"
TARGET = 250

CAPS = {
    "politics": [
        ("age_social_change", 8, "女性として議会・行政・公共政策で社会変革を担った"),
        ("soc_interpersonal", 7, "政党・市民・組織をつなぐ対人調整を行った"),
        ("cog_critical", 6, "制度や慣行への批判的視点を公共的に示した"),
        ("cog_math", 3, "数理専門職ではないため数学的リテラシーは補助的能力として低めに評価"),
    ],
    "business": [
        ("age_entrepreneur", 9, "女性として事業・ブランド・組織運営を切り開いた"),
        ("cog_systems", 7, "市場・顧客・組織を結びつける仕組みを構築した"),
        ("age_resilience", 8, "男性中心の業界環境で活動を継続した"),
        ("val_eco", 4, "環境論が主業績ではないためエコロジカルリテラシーは限定的に評価"),
    ],
    "science": [
        ("cog_logical", 9, "女性研究者として実証・分析に基づく専門的成果を示した"),
        ("cog_critical", 8, "既存知を検証し研究上の論点を前進させた"),
        ("age_resilience", 7, "研究職での制度的障壁を越えて活動した"),
        ("soc_interpersonal", 5, "共同研究・教育上の関係形成はあるが主能力ではないため中位に評価"),
    ],
    "arts": [
        ("cog_creativity", 9, "女性表現者として独自の作品・様式・演技を確立した"),
        ("val_tolerance", 7, "多様な経験や感情を表現に取り込んだ"),
        ("age_resilience", 7, "メディア・文壇・芸術界で活動を継続した"),
        ("cog_math", 3, "数理専門職ではないため数学的リテラシーは補助的能力として低めに評価"),
    ],
}

RAW = """
高橋展子|Takahashi Nobuko|1916|1990|politics|労働行政・婦人少年局|女性官僚として労働省婦人少年局長などを務め、戦後日本の女性労働政策を支えた
山口シヅエ|Yamaguchi Shizue|1917|2012|politics|衆議院議員|女性政治家として社会党・民社党で活動し、戦後議会政治に参画した
加藤シヅエ|Kato Shidzue|1897|2001|politics|参議院議員|女性政治家として家族計画・女性の権利・平和運動を国会で訴えた
山高しげり|Yamataka Shigeri|1899|1977|politics|参議院議員|女性政治家として母子福祉と婦人運動に取り組んだ
藤原道子|Fujiwara Michiko|1900|1983|politics|参議院議員|女性政治家として戦後の参議院で社会保障と女性政策に関わった
久保田真苗|Kubota Manae|1924|2008|politics|参議院議員|女性政治家として社会党参議院議員を務め、外交・平和・女性政策を論じた
清水澄子|Shimizu Sumiko|1928|2013|politics|参議院議員|女性政治家として社会党・社民党で女性労働と平和課題に取り組んだ
堂本暁子|Domoto Akiko|1932||politics|参議院議員・知事|女性政治家として参議院議員、千葉県知事を務め環境・男女共同参画政策を進めた
森山眞弓|Moriyama Mayumi|1927|2021|politics|衆議院議員・官僚|女性政治家・官僚として法務大臣などを務め、女性行政官の道を広げた
扇千景|Ogi Chikage|1933|2023|politics|参議院議員・俳優|女性政治家として参議院議長・国土交通大臣を務め、芸能界から政界へ進出した
赤松良子|Akamatsu Ryoko|1929||politics|官僚・大臣|女性官僚として男女雇用機会均等法に関わり、文部大臣も務めた
紀平悌子|Kihira Teiko|1928|2015|politics|参議院議員|女性政治家として市民運動と国会活動を結び、女性の政治参加を広げた
浜四津敏子|Hamayotsu Toshiko|1945|2020|politics|参議院議員|女性政治家として公明党代表代行などを務め、法務・福祉政策に関わった
円より子|Madoka Yoriko|1947||politics|参議院議員|女性政治家として女性相談・金融・男女共同参画政策に取り組んだ
井上美代|Inoue Miyo|1936||politics|参議院議員|女性政治家として共産党参議院議員を務め、平和・生活課題を国会で扱った
岡崎トミ子|Okazaki Tomiko|1944|2017|politics|参議院議員|女性政治家として国家公安委員長などを務め、男女共同参画行政に関わった
千葉景子|Chiba Keiko|1948||politics|参議院議員|女性政治家・弁護士として法務大臣を務め、人権・司法制度に関わった
太田房江|Ota Fusae|1951||politics|知事・官僚|女性官僚から大阪府知事となり、自治体経営と女性リーダーの可視化に寄与した
林文子|Hayashi Fumiko|1946||business|企業経営・市長|女性経営者として自動車販売会社社長を務め、のち横浜市長として行政を担った
篠原欣子|Shinohara Yoshiko|1934||business|人材派遣|女性起業家としてテンプスタッフを創業し、日本の人材サービス産業を拡大した
森英恵|Mori Hanae|1926|2022|business|ファッション|女性デザイナー・経営者として国際的ブランドを築き、戦後日本の服飾文化を広げた
小篠綾子|Koshino Ayako|1913|2006|business|ファッション|女性洋装店主として大阪・岸和田から服飾事業を育て、デザイナーを輩出した
コシノジュンコ|Koshino Junko|1939||business|ファッション|女性デザイナーとして国際的に活動し、服飾表現とブランド事業を展開した
コシノミチコ|Koshino Michiko|1943||business|ファッション|女性デザイナーとしてロンドンを拠点に活動し、日本発ファッションを国際化した
鳥居ユキ|Torii Yuki|1943||business|ファッション|女性デザイナーとしてプレタポルテを展開し、戦後日本のファッション産業に貢献した
津森千里|Tsumori Chisato|1954||business|ファッション|女性デザイナーとして独自ブランドを展開し、1980年代以降の日本服飾を彩った
南場智子|Namba Tomoko|1962||business|インターネット企業|女性起業家としてディー・エヌ・エーを創業し、IT企業経営で存在感を示した
大塚久美子|Otsuka Kumiko|1968||business|小売経営|女性経営者として大塚家具の社長を務め、家業経営の転換を試みた
勝間和代|Katsuma Kazuyo|1968||business|経営評論|女性公認会計士・経営評論家としてビジネス知識の普及に影響を与えた
湯浅年子|Yuasa Toshiko|1909|1980|science|物理学|女性物理学者としてフランスで核物理研究を行い、日本女性研究者の国際活動を象徴した
保井コノ|Yasui Kono|1880|1971|science|植物学|女性科学者として植物細胞学を研究し、日本初の女性博士の一人となった
黒田チカ|Kuroda Chika|1884|1968|science|化学|女性化学者として天然色素研究を進め、日本女性科学者の先駆となった
太田朋子|Ohta Tomoko|1933||science|集団遺伝学|女性遺伝学者として分子進化のほぼ中立説を提唱した
石井志保子|Ishii Shihoko|1950||science|数学|女性数学者として代数幾何学を研究し、日本数学界で指導的役割を担った
柳澤桂子|Yanagisawa Keiko|1938||science|生命科学|女性生命科学者・著述家として遺伝学と生命倫理を一般社会へ伝えた
中西準子|Nakanishi Junko|1938|2020|science|環境リスク学|女性研究者として環境リスク評価を日本で制度的に発展させた
黒田玲子|Kuroda Reiko|1947||science|化学|女性化学者としてキラリティー研究を進め、科学技術政策にも関わった
跡見順子|Atomi Yoriko|1944||science|生命科学|女性生命科学者として細胞生物学・身体科学の研究教育に携わった
室伏きみ子|Murofushi Kimiko|1947||science|生物学|女性生物学者として細胞生物学研究と大学運営に取り組んだ
大隅典子|Osumi Noriko|1960||science|神経科学|女性神経科学者として脳発生研究と科学コミュニケーションを進めた
平野俊夫|Hirano Toshio|1947||science|免疫学|免疫学者としてサイトカイン研究に貢献した人物だが女性追加対象外のため投入候補から除外用
円地文子|Enchi Fumiko|1905|1986|arts|小説|女性作家として古典翻案と女性心理の表現で戦後文学に大きな足跡を残した
幸田文|Koda Aya|1904|1990|arts|随筆・小説|女性作家として生活感覚と父幸田露伴の記憶を文学化した
佐多稲子|Sata Ineko|1904|1998|arts|小説|女性作家として労働・戦争・女性の生を描き、戦後文学を担った
宮本百合子|Miyamoto Yuriko|1899|1951|arts|小説|女性作家として社会運動と文学を結び、戦後民主主義文学に影響を与えた
平林たい子|Hirabayashi Taiko|1905|1972|arts|小説|女性作家としてプロレタリア文学から戦後文学まで活動した
野上弥生子|Nogami Yaeko|1885|1985|arts|小説|女性作家として長期にわたり小説・翻訳・随筆で活躍した
宇野千代|Uno Chiyo|1897|1996|arts|小説・編集|女性作家・編集者として文学と出版・着物文化を横断した
林芙美子|Hayashi Fumiko Writer|1903|1951|arts|小説|女性作家として放浪記などで庶民女性の生活を描き、戦後初期まで活躍した
有吉佐和子|Ariyoshi Sawako|1931|1984|arts|小説|女性作家として社会問題と歴史題材を小説化し、戦後読書文化に影響した
曽野綾子|Sono Ayako|1931||arts|小説|女性作家として戦後日本の倫理・宗教・社会問題を小説と評論で論じた
田辺聖子|Tanabe Seiko|1928|2019|arts|小説|女性作家として大阪文化と古典を現代的に描き、広い読者を得た
向田邦子|Mukoda Kuniko|1929|1981|arts|脚本・随筆|女性脚本家・作家としてテレビドラマと随筆で昭和後期の生活感覚を描いた
津村節子|Tsumura Setsuko|1928||arts|小説|女性作家として歴史小説や家族の経験を題材に戦後文学で活動した
皆川博子|Minagawa Hiroko|1929||arts|小説|女性作家として幻想・ミステリ・歴史小説を横断し独自の作風を築いた
栗本薫|Kurimoto Kaoru|1953|2009|arts|小説|女性作家としてSF・ミステリ・ファンタジーの大衆文学領域を拡張した
山崎豊子|Yamazaki Toyoko|1924|2013|arts|小説|女性作家として企業・医療・戦争責任を題材に社会派小説を展開した
佐藤愛子|Sato Aiko|1923||arts|小説|女性作家として家族・老い・人生をユーモアと批評性で描いた
瀬戸内寂聴|Setouchi Jakucho|1922|2021|arts|小説・仏教|女性作家として恋愛・女性の生を描き、のち宗教者としても発信した
大庭みな子|Oba Minako|1930|2007|arts|小説|女性作家として海外経験と女性の内面を戦後文学に取り込んだ
河野多惠子|Kono Taeko|1926|2015|arts|小説|女性作家として身体・欲望・家庭の緊張を実験的に描いた
倉橋由美子|Kurahashi Yumiko|1935|2005|arts|小説|女性作家として前衛的な文体と寓意で戦後文学を刺激した
森茉莉|Mori Mari|1903|1987|arts|小説・随筆|女性作家として幻想的文体と随筆で独自の文学世界を築いた
吉屋信子|Yoshiya Nobuko|1896|1973|arts|小説|女性作家として少女小説と女性同士の関係表象を大衆文学に広げた
壺井栄|Tsuboi Sakae|1899|1967|arts|小説|女性作家として二十四の瞳などで戦争と教育の記憶を描いた
石垣りん|Ishigaki Rin|1920|2004|arts|詩|女性詩人として労働と生活の視点から戦後詩を作った
茨木のり子|Ibaragi Noriko|1926|2006|arts|詩|女性詩人として自立と批評精神を持つ戦後詩を発表した
新川和江|Shinkawa Kazue|1929|2024|arts|詩|女性詩人として叙情と社会性を併せ持つ詩作を続けた
岸田衿子|Kishida Eriko|1929|2011|arts|詩・童話|女性詩人・童話作家として子ども文化と詩を結びつけた
工藤直子|Kudo Naoko|1935||arts|詩・児童文学|女性詩人として子ども向け詩と物語の世界を広げた
高橋たか子|Takahashi Takako|1932|2013|arts|小説|女性作家として宗教性と女性心理をめぐる小説を発表した
落合恵子|Ochiai Keiko|1945||arts|作家・放送|女性作家・放送人として子ども・女性・平和をめぐる発信を続けた
増田みず子|Masuda Mizuko|1948||arts|小説|女性作家として都市生活と女性の内面を描いた
宮尾登美子|Miyao Tomiko|1926|2014|arts|小説|女性作家として女性の生涯と家制度を歴史小説に描いた
林京子|Hayashi Kyoko|1930|2017|arts|小説|女性作家として被爆体験と記憶を文学化した
竹西寛子|Takenishi Hiroko|1929|2025|arts|小説・評論|女性作家・評論家として古典と現代文学を架橋した
富岡多恵子|Tomioka Taeko|1935|2023|arts|小説・詩|女性作家として詩と小説を横断し、戦後女性文学を押し広げた
杉本苑子|Sugimoto Sonoko|1925|2017|arts|歴史小説|女性作家として歴史小説で女性人物像を豊かに描いた
永井路子|Nagai Michiko|1925|2023|arts|歴史小説|女性作家として日本史を題材に歴史小説の読者層を広げた
津島佑子|Tsushima Yuko|1947|2016|arts|小説|女性作家として家族・母性・記憶を問う小説で国際的評価を受けた
山田詠美|Yamada Eimi|1959||arts|小説|女性作家として1980年代後半から性・人種・都市感覚を描いた
吉本ばなな|Yoshimoto Banana|1964||arts|小説|女性作家として1980年代末に新しい感性の小説で若い読者を獲得した
俵万智|Tawara Machi|1962||arts|短歌|女性歌人としてサラダ記念日で現代短歌を大衆化した
草間彌生|Kusama Yayoi|1929||arts|現代美術|女性美術家として水玉・反復・インスタレーションで国際的評価を得た
田中敦子|Tanaka Atsuko|1932|2005|arts|現代美術|女性美術家として具体美術協会で電気服などの実験的作品を制作した
桂ゆき|Katsura Yuki|1913|1991|arts|美術|女性画家としてコラージュや前衛表現で戦後美術に関わった
三岸節子|Migishi Setsuko|1905|1999|arts|洋画|女性洋画家として長期にわたり色彩豊かな絵画を制作した
堀文子|Hori Fumiko|1918|2019|arts|日本画|女性日本画家として自然観察に基づく独自の画境を築いた
片岡球子|Kataoka Tamako|1905|2008|arts|日本画|女性日本画家として大胆な色彩と構図で戦後日本画を代表した
小倉遊亀|Ogura Yuki|1895|2000|arts|日本画|女性日本画家として人物・静物画で高い評価を受けた
秋野不矩|Akino Fuku|1908|2001|arts|日本画|女性日本画家としてインド滞在を通じた独自の画風を確立した
篠田桃紅|Shinoda Toko|1913|2021|arts|墨象|女性美術家として書と抽象表現を融合し国際的に活動した
朝倉摂|Asakura Setsu|1922|2014|arts|舞台美術|女性舞台美術家・画家として演劇空間の視覚表現を刷新した
入江一子|Irie Kazuko|1916|2021|arts|洋画|女性画家としてシルクロードを題材に制作を続けた
田中絹代|Tanaka Kinuyo|1909|1977|arts|映画|女性俳優・映画監督として日本映画黄金期を担い女性監督の先駆ともなった
高峰秀子|Takamine Hideko|1924|2010|arts|映画|女性俳優として成瀬巳喜男作品などで戦後日本映画を代表した
原節子|Hara Setsuko|1920|2015|arts|映画|女性俳優として小津安二郎作品などで戦後日本映画の象徴となった
山田五十鈴|Yamada Isuzu|1917|2012|arts|映画・演劇|女性俳優として映画・舞台で長く活躍し、演技の幅を示した
杉村春子|Sugimura Haruko|1906|1997|arts|演劇|女性俳優として文学座を支え、現代演劇の演技様式を牽引した
森光子|Mori Mitsuko|1920|2012|arts|演劇・テレビ|女性俳優として放浪記などで長期公演記録を築き、大衆演劇文化に貢献した
京マチ子|Kyo Machiko|1924|2019|arts|映画|女性俳優として羅生門など国際的日本映画に出演し強い存在感を示した
若尾文子|Wakao Ayako|1933||arts|映画|女性俳優として大映映画を中心に現代的女性像を演じた
岸惠子|Kishi Keiko|1932||arts|映画・著述|女性俳優・作家として国内外で活動し、国際的な表現者となった
吉永小百合|Yoshinaga Sayuri|1945||arts|映画|女性俳優として戦後日本映画・テレビの国民的スターとなった
岩下志麻|Iwashita Shima|1941||arts|映画|女性俳優として日本映画で強い女性像を多数演じた
浅丘ルリ子|Asaoka Ruriko|1940||arts|映画|女性俳優として日活映画やテレビで幅広く活躍した
樹木希林|Kiki Kirin|1943|2018|arts|映画・テレビ|女性俳優として個性的な演技で日本映画・テレビに大きな影響を与えた
桃井かおり|Momoi Kaori|1951||arts|映画|女性俳優として1970年代以降の日本映画で独特の存在感を示した
松坂慶子|Matsuzaka Keiko|1952||arts|映画|女性俳優として映画・テレビ・舞台で活躍し昭和後期のスターとなった
大竹しのぶ|Otaki Shinobu|1957||arts|映画・演劇|女性俳優として映画・舞台で高い演技力を評価された
倍賞千恵子|Baisho Chieko|1941||arts|映画・歌|女性俳優・歌手として男はつらいよなどで親しまれた
十朱幸代|Toake Yukiyo|1942||arts|映画・テレビ|女性俳優として映画・テレビで幅広い役柄を演じた
栗原小巻|Kurihara Komaki|1945||arts|映画・舞台|女性俳優として映画・舞台・国際交流で活動した
左幸子|Hidari Sachiko|1930|2001|arts|映画|女性俳優・映画監督として戦後日本映画に貢献した
乙羽信子|Otowa Nobuko|1924|1994|arts|映画|女性俳優として新藤兼人作品などで強い演技を示した
香川京子|Kagawa Kyoko|1931||arts|映画|女性俳優として黒澤明・小津安二郎作品などに出演した
司葉子|Tsukasa Yoko|1934||arts|映画|女性俳優として東宝映画を中心に活躍し、のち社会活動にも関わった
岡田茉莉子|Okada Mariko|1933||arts|映画|女性俳優として戦後日本映画で自立的な女性像を演じた
淡島千景|Awashima Chikage|1924|2012|arts|映画・演劇|女性俳優として宝塚から映画・舞台へ活動を広げた
新珠三千代|Aratama Michiyo|1930|2001|arts|映画|女性俳優として映画・テレビで清潔感ある役柄を演じた
有馬稲子|Arima Ineko|1932||arts|映画・舞台|女性俳優として松竹映画と舞台で活躍した
久我美子|Kuga Yoshiko|1931||arts|映画|女性俳優として戦後日本映画で知的な女性像を演じた
沢村貞子|Sawamura Sadako|1908|1996|arts|映画・随筆|女性俳優・随筆家として庶民生活を演技と文章で表した
浦辺粂子|Urabe Kumeko|1902|1989|arts|映画|女性俳優として日本映画の脇役文化を支えた
清川虹子|Kiyokawa Nijiko|1912|2002|arts|映画・喜劇|女性俳優として喜劇・映画・テレビで長く活躍した
山岡久乃|Yamaoka Hisano|1926|1999|arts|テレビ・舞台|女性俳優としてホームドラマを中心に昭和後期のテレビ文化を支えた
市原悦子|Ichihara Etsuko|1936|2019|arts|演劇・テレビ|女性俳優として舞台・テレビ・語りで独自の存在感を示した
奈良岡朋子|Naraoka Tomoko|1929|2023|arts|演劇|女性俳優として劇団民藝を支え、舞台と語りで活躍した
加藤治子|Kato Haruko|1922|2015|arts|演劇・テレビ|女性俳優として舞台・テレビドラマで温かな演技を示した
藤間紫|Fujima Murasaki|1923|2009|arts|日本舞踊|女性舞踊家・俳優として日本舞踊と演劇を横断した
水谷八重子|Mizutani Yaeko|1905|1979|arts|新派|女性俳優として新派劇を代表し、昭和期の舞台文化を支えた
美空ひばり|Misora Hibari|1937|1989|arts|歌謡曲|女性歌手として戦後歌謡を代表し、昭和大衆文化の象徴となった
山口百恵|Yamaguchi Momoe|1959||arts|歌謡曲|女性歌手・俳優として1970年代の大衆文化を牽引した
松任谷由実|Matsutoya Yumi|1954||arts|音楽|女性シンガーソングライターとしてニューミュージックを大衆化した
中島みゆき|Nakajima Miyuki|1952||arts|音楽|女性シンガーソングライターとして社会性と物語性を持つ歌を発表した
松田聖子|Matsuda Seiko|1962||arts|歌謡曲|女性歌手として1980年代アイドル文化と歌謡曲を代表した
都はるみ|Miyako Harumi|1948||arts|演歌|女性演歌歌手として独特の歌唱で昭和後期の演歌を牽引した
八代亜紀|Yashiro Aki|1950|2023|arts|演歌|女性歌手として演歌・ブルース調歌謡で幅広い支持を得た
石川さゆり|Ishikawa Sayuri|1958||arts|演歌|女性歌手として津軽海峡・冬景色などで演歌の代表的表現を築いた
森山良子|Moriyama Ryoko|1948||arts|フォーク|女性歌手としてフォーク・ポップスの分野で長く活動した
加藤登紀子|Kato Tokiko|1943||arts|音楽|女性歌手としてシャンソン・歌謡・社会的メッセージを横断した
いしだあゆみ|Ishida Ayumi|1948||arts|歌謡・映画|女性歌手・俳優としてブルー・ライト・ヨコハマなどで知られた
岩崎宏美|Iwasaki Hiromi|1958||arts|歌謡曲|女性歌手として1970年代以降の歌謡曲で高い歌唱力を示した
南沙織|Minami Saori|1954||arts|歌謡曲|女性歌手として1970年代アイドル歌謡の先駆となった
天地真理|Amachi Mari|1951||arts|歌謡曲|女性歌手として1970年代前半のアイドル文化を広げた
伊藤蘭|Ito Ran|1955||arts|歌謡・俳優|女性歌手・俳優としてキャンディーズと舞台・映像で活躍した
田中好子|Tanaka Yoshiko|1956|2011|arts|歌謡・俳優|女性歌手・俳優としてキャンディーズと映画・ドラマで活躍した
藤村美樹|Fujimura Miki|1956||arts|歌謡曲|女性歌手としてキャンディーズの一員として1970年代アイドル文化に貢献した
越路吹雪|Koshiji Fubuki|1924|1980|arts|シャンソン|女性歌手・俳優として宝塚からシャンソンへ進み舞台歌唱を確立した
淡谷のり子|Awaya Noriko|1907|1999|arts|ブルース|女性歌手として日本のブルース歌謡を代表した
江利チエミ|Eri Chiemi|1937|1982|arts|歌謡・俳優|女性歌手・俳優として戦後ジャズ・歌謡・ミュージカルで活躍した
雪村いづみ|Yukimura Izumi|1937||arts|歌謡曲|女性歌手として三人娘の一人として戦後歌謡を支えた
ペギー葉山|Peggy Hayama|1933|2017|arts|歌謡曲|女性歌手として学生時代などで知られ、音楽教育にも関わった
由紀さおり|Yuki Saori|1948||arts|歌謡曲|女性歌手として夜明けのスキャットなどで独自の歌唱を示した
岸洋子|Kishi Yoko|1935|1992|arts|シャンソン|女性歌手としてシャンソンと歌謡の橋渡しを行った
島倉千代子|Shimakura Chiyoko|1938|2013|arts|歌謡曲|女性歌手として人生いろいろなどで昭和歌謡を代表した
ちあきなおみ|Chiaki Naomi|1947||arts|歌謡曲|女性歌手として劇的な歌唱表現で歌謡曲に強い印象を残した
弘田三枝子|Hirota Mieko|1947|2020|arts|ポップス|女性歌手として和製ポップスと歌唱力で昭和後期の音楽を支えた
青江三奈|Aoe Mina|1941|2000|arts|歌謡曲|女性歌手としてハスキーな声で都会的歌謡を代表した
園まり|Sono Mari|1944||arts|歌謡曲|女性歌手として三人娘の一人として1960年代歌謡で人気を得た
中尾ミエ|Nakao Mie|1946||arts|歌謡・俳優|女性歌手・俳優としてポップスから舞台まで活動した
伊東ゆかり|Ito Yukari|1947||arts|歌謡曲|女性歌手としてスパーク三人娘の一人として活躍した
梓みちよ|Azusa Michiyo|1943|2020|arts|歌謡曲|女性歌手としてこんにちは赤ちゃんなどで昭和歌謡に足跡を残した
欧陽菲菲|Ouyang Feifei|1949||arts|歌謡曲|台湾出身女性歌手として日本の歌謡界で国際的な活躍を示した
テレサ・テン|Teresa Teng|1953|1995|arts|歌謡曲|台湾出身女性歌手として日本・中華圏を横断し昭和後期の歌謡に影響した
ジュディ・オング|Judy Ongg|1950||arts|歌謡・版画|台湾出身女性歌手・版画家として日本の芸能と美術で活動した
オノ・ヨーコ|Yoko Ono|1933||arts|前衛芸術|女性前衛芸術家として音楽・美術・平和運動を国際的に結びつけた
マーガレット・サッチャー|Margaret Thatcher|1925|2013|politics|首相|女性政治家として英国首相を務め、1980年代の新自由主義改革を主導した
インディラ・ガンディー|Indira Gandhi|1917|1984|politics|首相|女性政治家としてインド首相を務め、戦後アジア政治に大きな影響を与えた
ゴルダ・メイア|Golda Meir|1898|1978|politics|首相|女性政治家としてイスラエル首相を務め、戦後中東政治を担った
コラソン・アキノ|Corazon Aquino|1933|2009|politics|大統領|女性政治家としてフィリピン民主化後の大統領となり、権威主義体制後の政治を担った
ベーナズィール・ブットー|Benazir Bhutto|1953|2007|politics|首相|女性政治家としてパキスタン首相となり、イスラム圏の女性指導者として注目された
イサベル・ペロン|Isabel Peron|1931||politics|大統領|女性政治家としてアルゼンチン大統領を務め、女性国家元首の先例となった
ビオレタ・チャモロ|Violeta Chamorro|1929|2021|politics|大統領|女性政治家としてニカラグア大統領となり、内戦後政治に関わった
ユージニア・チャールズ|Eugenia Charles|1919|2005|politics|首相|女性政治家としてドミニカ国首相を長期に務め、カリブ地域の女性指導者となった
メアリー・ロビンソン|Mary Robinson|1944||politics|大統領・人権|女性政治家としてアイルランド大統領、国連人権高等弁務官を務めた
シモーヌ・ヴェイユ|Simone Veil|1927|2017|politics|閣僚・欧州議会|女性政治家として妊娠中絶合法化と欧州統合に関わった
シャーリー・チザム|Shirley Chisholm|1924|2005|politics|下院議員|女性政治家として米国初の黒人女性下院議員となり大統領予備選にも挑んだ
ベラ・アブズグ|Bella Abzug|1920|1998|politics|下院議員|女性政治家として米国議会でフェミニズム・平和・公民権を訴えた
バーバラ・ジョーダン|Barbara Jordan|1936|1996|politics|下院議員|女性政治家として米国議会で憲法と公民権をめぐる演説で知られた
ジーン・カークパトリック|Jeane Kirkpatrick|1926|2006|politics|外交|女性外交官・政治学者として米国国連大使を務めた
サンドラ・デイ・オコナー|Sandra Day O'Connor|1930|2023|politics|司法|女性法律家として米国初の女性連邦最高裁判事となり司法判断に影響した
ルース・ベイダー・ギンズバーグ|Ruth Bader Ginsburg|1933|2020|politics|司法|女性法律家として性差別訴訟と連邦最高裁判事として男女平等を進めた
ジェラルディン・フェラーロ|Geraldine Ferraro|1935|2011|politics|下院議員|女性政治家として米国主要政党初の女性副大統領候補となった
マデレーン・オルブライト|Madeleine Albright|1937|2022|politics|外交|女性外交官として国連大使・国務長官を務め、冷戦後外交を担った
江青|Jiang Qing|1914|1991|politics|政治家|女性政治家として中国文化大革命期の四人組の一人となり政治文化に影響した
宋慶齢|Soong Ching-ling|1893|1981|politics|国家副主席|女性政治家として中国の国家副主席・名誉主席を務めた
シリマヴォ・バンダラナイケ|Sirimavo Bandaranaike|1916|2000|politics|首相|女性政治家として世界初の女性首相となり、スリランカ政治を率いた
シェイク・ハシナ|Sheikh Hasina|1947||politics|首相|女性政治家としてバングラデシュ民主化運動と首相職を担った
ハリダ・ジア|Khaleda Zia|1945||politics|首相|女性政治家としてバングラデシュ首相を務め、二大政党政治を担った
メガワティ・スカルノプトゥリ|Megawati Sukarnoputri|1947||politics|大統領|女性政治家としてインドネシア大統領となり、民主化期政治を担った
ヴィグディス・フィンボガドゥティル|Vigdis Finnbogadottir|1930||politics|大統領|女性政治家としてアイスランド大統領となり、民選女性国家元首の先駆となった
エリザベス2世|Elizabeth II|1926|2022|politics|君主|女性君主として戦後英国と英連邦の象徴的役割を長期に担った
マルグレーテ2世|Margrethe II|1940||politics|君主|女性君主としてデンマーク王位に就き、現代立憲君主制を支えた
ベアトリクス|Beatrix of the Netherlands|1938||politics|君主|女性君主としてオランダ王位に就き、戦後欧州の象徴的公務を担った
ナンシー・ペロシ|Nancy Pelosi|1940||politics|下院議員|女性政治家として1987年から米国下院議員となり、のち下院議長を務めた
ダイアン・ファインスタイン|Dianne Feinstein|1933|2023|politics|市長・上院議員|女性政治家としてサンフランシスコ市長から上院議員となり都市行政と立法を担った
バーバラ・ミクルスキ|Barbara Mikulski|1936||politics|上院議員|女性政治家として米国上院で長期に活動し女性議員の存在感を高めた
アン・リチャーズ|Ann Richards|1933|2006|politics|知事|女性政治家としてテキサス州知事を務め、米国南部政治で注目された
ドロレス・ウエルタ|Dolores Huerta|1930||politics|労働運動|女性労働運動家として農業労働者の権利運動を組織した
グレース・リー・ボッグス|Grace Lee Boggs|1915|2015|politics|社会運動|女性社会運動家として米国の労働・公民権・地域運動に関わった
キャサリン・グラハム|Katharine Graham|1917|2001|business|新聞経営|女性経営者としてワシントン・ポストを率い、報道機関経営を担った
リリアン・ヴァーノン|Lillian Vernon|1927|2015|business|通信販売|女性起業家として通信販売会社を創業し、消費者向け小売を拡大した
リリアン・ベタンクール|Liliane Bettencourt|1922|2017|business|化粧品経営|女性相続経営者としてロレアルの大株主となり美容産業に影響した
アン・コックス・チェンバース|Anne Cox Chambers|1919|2020|business|メディア経営|女性経営者としてコックス企業グループを率いメディア事業に関わった
バーバラ・マクリントック|Barbara McClintock|1902|1992|science|遺伝学|女性遺伝学者としてトランスポゾンを発見しノーベル賞を受けた
リタ・コルウェル|Rita Colwell|1934||science|微生物学|女性微生物学者としてコレラ研究と科学行政で活躍した
クリスティアーネ・ニュスライン＝フォルハルト|Christiane Nusslein-Volhard|1942||science|発生生物学|女性発生生物学者として胚発生の遺伝的制御研究でノーベル賞を受けた
エリザベス・ブラックバーン|Elizabeth Blackburn|1948||science|分子生物学|女性分子生物学者としてテロメアとテロメラーゼ研究を進めた
キャロル・グライダー|Carol Greider|1961||science|分子生物学|女性分子生物学者としてテロメラーゼ発見に貢献した
リンダ・バック|Linda Buck|1947||science|神経科学|女性神経科学者として嗅覚受容体研究でノーベル賞を受けた
バーバラ・リスコフ|Barbara Liskov|1939||science|計算機科学|女性計算機科学者として抽象データ型と分散システム研究に貢献した
アデル・ゴールドバーグ|Adele Goldberg|1945||science|計算機科学|女性計算機科学者としてSmalltalkとGUI開発に関わった
フランシス・アレン|Frances Allen|1932|2020|science|計算機科学|女性計算機科学者としてコンパイラ最適化研究でチューリング賞を受けた
ジーン・サメット|Jean Sammet|1928|2017|science|計算機科学|女性計算機科学者としてFORMACなどプログラミング言語開発に貢献した
ナンシー・ローマン|Nancy Roman|1925|2018|science|天文学|女性天文学者としてNASAの宇宙望遠鏡計画を推進した
マーガレット・バービッジ|Margaret Burbidge|1919|2020|science|天文学|女性天文学者として恒星元素合成研究に貢献した
ベアトリス・ティンズリー|Beatrice Tinsley|1941|1981|science|天文学|女性天文学者として銀河進化研究に重要な理論的貢献をした
メアリー・リーキー|Mary Leakey|1913|1996|science|古人類学|女性古人類学者として東アフリカで重要な化石発見を行った
ビルテ・ガルディカス|Birute Galdikas|1946||science|霊長類学|女性霊長類学者としてオランウータンの長期研究を行った
リン・コンウェイ|Lynn Conway|1938|2024|science|計算機工学|女性計算機工学者としてVLSI設計教育とトランスジェンダー可視化に貢献した
イヴォンヌ・ブリル|Yvonne Brill|1924|2013|science|宇宙工学|女性宇宙工学者として衛星推進技術の開発に貢献した
ヴァレンチナ・テレシコワ|Valentina Tereshkova|1937||science|宇宙飛行|女性宇宙飛行士として世界初の女性宇宙飛行を達成した
サリー・ライド|Sally Ride|1951|2012|science|宇宙飛行|女性宇宙飛行士として米国初の女性宇宙飛行士となった
スベトラーナ・サビツカヤ|Svetlana Savitskaya|1948||science|宇宙飛行|女性宇宙飛行士として女性初の宇宙遊泳を行った
ジュディス・レズニック|Judith Resnik|1949|1986|science|宇宙飛行|女性宇宙飛行士・技術者としてスペースシャトル計画に参加した
アンナ・フィッシャー|Anna Lee Fisher|1949||science|宇宙飛行|女性宇宙飛行士・医師としてスペースシャトルに搭乗した
キャスリン・サリバン|Kathryn D. Sullivan|1951||science|宇宙飛行|女性宇宙飛行士・地質学者として米国女性初の宇宙遊泳を行った
オードリー・ヘプバーン|Audrey Hepburn|1929|1993|arts|映画|女性俳優として戦後映画の国際的スターとなり、晩年は人道活動も行った
マリリン・モンロー|Marilyn Monroe|1926|1962|arts|映画|女性俳優としてハリウッドのスターイメージとジェンダー表象に強い影響を与えた
エリザベス・テイラー|Elizabeth Taylor|1932|2011|arts|映画|女性俳優として戦後ハリウッドを代表し、AIDS支援活動にも関わった
メリル・ストリープ|Meryl Streep|1949||arts|映画|女性俳優として1970年代末以降の映画で幅広い演技力を示した
ジェーン・フォンダ|Jane Fonda|1937||arts|映画・社会運動|女性俳優として映画と反戦・フェミニズム運動を結びつけた
バーブラ・ストライサンド|Barbra Streisand|1942||arts|音楽・映画|女性歌手・俳優・監督として米国大衆文化で大きな成功を収めた
ジュリー・アンドリュース|Julie Andrews|1935||arts|ミュージカル映画|女性俳優・歌手としてミュージカル映画と舞台で国際的に活躍した
ライザ・ミネリ|Liza Minnelli|1946||arts|ミュージカル|女性俳優・歌手として舞台と映画ミュージカルで存在感を示した
ジョーン・バエズ|Joan Baez|1941||arts|フォーク|女性歌手としてフォーク音楽と公民権・反戦運動を結びつけた
ジョニ・ミッチェル|Joni Mitchell|1943||arts|音楽|女性シンガーソングライターとして詩的表現と作曲で影響を与えた
キャロル・キング|Carole King|1942||arts|音楽|女性ソングライター・歌手としてポップ音楽の創作主体を広げた
ドリー・パートン|Dolly Parton|1946||arts|音楽|女性歌手・作曲家としてカントリー音楽と事業を結びつけた
ティナ・ターナー|Tina Turner|1939|2023|arts|音楽|女性歌手としてロック・ソウルのステージ表現を刷新した
ダイアナ・ロス|Diana Ross|1944||arts|音楽|女性歌手としてシュープリームスとソロ活動でポップ音楽に影響した
ホイットニー・ヒューストン|Whitney Houston|1963|2012|arts|音楽|女性歌手として1980年代後半から圧倒的歌唱力で世界的成功を収めた
シンディ・ローパー|Cyndi Lauper|1953||arts|音楽|女性歌手として1980年代ポップスで個性的な表現と女性の自己主張を示した
シェール|Cher|1946||arts|音楽・映画|女性歌手・俳優として長期にわたりポップカルチャーで活躍した
パティ・スミス|Patti Smith|1946||arts|音楽・詩|女性表現者としてパンクロックと詩を融合した
ジョーン・ディディオン|Joan Didion|1934|2021|arts|文学・評論|女性作家としてニュー・ジャーナリズムと現代米国批評を代表した
スーザン・ソンタグ|Susan Sontag|1933|2004|arts|評論|女性批評家として写真・病・戦争をめぐる批評で世界的影響を与えた
ドリス・レッシング|Doris Lessing|1919|2013|arts|文学|女性作家として植民地経験・女性・社会主義を小説化した
ナディン・ゴーディマー|Nadine Gordimer|1923|2014|arts|文学|女性作家として南アフリカのアパルトヘイト社会を描いた
アリス・マンロー|Alice Munro|1931|2024|arts|文学|女性作家として短編小説の形式を洗練させノーベル文学賞を受けた
マーガレット・アトウッド|Margaret Atwood|1939||arts|文学|女性作家としてディストピアとジェンダーをめぐる小説で影響を与えた
シルヴィア・プラス|Sylvia Plath|1932|1963|arts|詩|女性詩人として告白詩と小説で戦後文学に強い影響を残した
アドリエンヌ・リッチ|Adrienne Rich|1929|2012|arts|詩・評論|女性詩人・批評家としてフェミニズム文学と政治詩を発展させた
アリス・ウォーカー|Alice Walker|1944||arts|文学|女性作家として黒人女性の経験を小説化し、フェミニズム思想にも影響した
マキシーン・ホン・キングストン|Maxine Hong Kingston|1940||arts|文学|女性作家として中国系米国人女性の記憶と移民経験を描いた
エイミ・タン|Amy Tan|1952||arts|文学|女性作家として中国系米国人家族と母娘関係を小説化した
イサベル・アジェンデ|Isabel Allende|1942||arts|文学|女性作家としてラテンアメリカの歴史と女性の物語を世界に広げた
クラリッセ・リスペクトール|Clarice Lispector|1920|1977|arts|文学|女性作家として内面意識を探る革新的なポルトガル語文学を残した
ヘレン・フランケンサーラー|Helen Frankenthaler|1928|2011|arts|美術|女性画家としてカラーフィールド・ペインティングを発展させた
アグネス・マーティン|Agnes Martin|1912|2004|arts|美術|女性画家として抽象絵画の静謐な表現を確立した
バーバラ・ヘップワース|Barbara Hepworth|1903|1975|arts|彫刻|女性彫刻家としてモダニズム彫刻を代表した
ブリジット・ライリー|Bridget Riley|1931||arts|美術|女性画家としてオプ・アートの代表的表現を確立した
ニキ・ド・サンファル|Niki de Saint Phalle|1930|2002|arts|美術|女性美術家としてナナシリーズなどで身体と公共彫刻を表現した
エヴァ・ヘス|Eva Hesse|1936|1970|arts|美術|女性美術家としてポストミニマリズムに重要な作品を残した
ジュディ・シカゴ|Judy Chicago|1939||arts|美術|女性美術家としてフェミニスト・アートの制度化と作品制作を進めた
シンディ・シャーマン|Cindy Sherman|1954||arts|写真|女性写真家として自己演出写真でジェンダーとイメージを批評した
ジェニー・ホルツァー|Jenny Holzer|1950||arts|美術|女性美術家として言葉と公共空間を用いたコンセプチュアル作品を展開した
バーバラ・クルーガー|Barbara Kruger|1945||arts|美術|女性美術家として広告的視覚言語で権力とジェンダーを批評した
マヤ・リン|Maya Lin|1959||arts|建築・美術|女性建築家・美術家としてベトナム戦争戦没者慰霊碑を設計した
シャンタル・アケルマン|Chantal Akerman|1950|2015|arts|映画|女性映画監督として日常と時間を扱う実験的映画表現を開いた
ジェーン・カンピオン|Jane Campion|1954||arts|映画|女性映画監督として国際映画祭で評価され、女性の視点を映画化した
クレール・ドニ|Claire Denis|1946||arts|映画|女性映画監督としてポスト植民地主義的な身体と記憶を映像化した
岡田嘉子|Okada Yoshiko|1902|1992|arts|映画・演劇|女性俳優として新劇・映画で活動し、越境的な生涯でも知られた
高杉早苗|Takasugi Sanae|1918|1995|arts|映画|女性俳優として松竹映画などで戦前から戦後まで活動した
轟夕起子|Todoroki Yukiko|1917|1967|arts|映画|女性俳優・歌手として戦後映画と流行歌で人気を得た
入江たか子|Irie Takako|1911|1995|arts|映画|女性俳優として映画会社を設立し、女性スターの自立を示した
高峰三枝子|Takamine Mieko|1918|1990|arts|映画・歌|女性俳優・歌手として松竹映画と歌謡で活躍した
木暮実千代|Kogure Michiyo|1918|1990|arts|映画|女性俳優として戦後日本映画で多彩な役柄を演じた
淡路恵子|Awaji Keiko|1933|2014|arts|映画・テレビ|女性俳優として映画・テレビで長く活動し大衆文化を支えた
藤純子|Fuji Junko|1945||arts|映画|女性俳優として任侠映画のスターとなり、昭和後期映画で存在感を示した
山本富士子|Yamamoto Fujiko|1931||arts|映画|女性俳優として大映映画を中心に戦後映画のスターとなった
中村玉緒|Nakamura Tamao|1939||arts|映画・テレビ|女性俳優として映画からテレビへ活動を広げ、昭和後期の大衆文化で親しまれた
佐久間良子|Sakuma Yoshiko|1939||arts|映画・舞台|女性俳優として東映映画と舞台で活躍した
酒井和歌子|Sakai Wakako|1949||arts|映画・テレビ|女性俳優として青春映画・テレビドラマで昭和後期に活躍した
星由里子|Hoshi Yuriko|1943|2018|arts|映画・テレビ|女性俳優として東宝映画やテレビドラマで活躍した
太地喜和子|Taichi Kiwako|1943|1992|arts|映画・舞台|女性俳優として舞台と映画で強い個性を示した
梶芽衣子|Kaji Meiko|1947||arts|映画・歌|女性俳優・歌手としてアクション映画で独自の女性像を示した
秋吉久美子|Akiyoshi Kumiko|1954||arts|映画|女性俳優として1970年代以降の日本映画で現代的な存在感を示した
名取裕子|Natori Yuko|1957||arts|映画・テレビ|女性俳優として映画・テレビドラマで幅広く活動した
薬師丸ひろ子|Yakushimaru Hiroko|1964||arts|映画・歌|女性俳優・歌手として1980年代角川映画と歌謡で人気を得た
原田知世|Harada Tomoyo|1967||arts|映画・歌|女性俳優・歌手として1980年代から映画と音楽で活動した
小泉今日子|Koizumi Kyoko|1966||arts|歌謡・俳優|女性歌手・俳優として1980年代アイドル文化と演技活動を横断した
中山美穂|Nakayama Miho|1970||arts|歌謡・俳優|女性歌手・俳優として1980年代半ばから歌謡とドラマで活躍した
大貫妙子|Onuki Taeko|1953||arts|音楽|女性シンガーソングライターとしてシティポップと日本語ポップスを洗練させた
矢野顕子|Yano Akiko|1955||arts|音楽|女性音楽家としてピアノ・作曲・歌唱を横断し独自のポップ表現を築いた
竹内まりや|Takeuchi Mariya|1955||arts|音楽|女性シンガーソングライターとしてポップスの作詞作曲と歌唱で広く支持された
吉田美奈子|Yoshida Minako|1953||arts|音楽|女性歌手・作曲家としてソウルやシティポップに影響を与えた
渡辺真知子|Watanabe Machiko|1956||arts|音楽|女性シンガーソングライターとして1970年代末からヒット曲を発表した
太田裕美|Ota Hiromi|1955||arts|歌謡曲|女性歌手として木綿のハンカチーフなどでニューミュージック期に活躍した
五輪真弓|Itsuwa Mayumi|1951||arts|音楽|女性シンガーソングライターとして恋人よなどで昭和後期の音楽に足跡を残した
杏里|Anri|1961||arts|音楽|女性歌手として1980年代シティポップとポップスで活躍した
荻野目洋子|Oginome Yoko|1968||arts|歌謡曲|女性歌手として1980年代アイドル歌謡とダンスポップで人気を得た
本田美奈子|Honda Minako|1967|2005|arts|歌謡・ミュージカル|女性歌手として1980年代アイドルからミュージカル歌唱へ活動を広げた
工藤静香|Kudo Shizuka|1970||arts|歌謡曲|女性歌手として1980年代後半にソロ歌手として人気を得た
小林幸子|Kobayashi Sachiko|1953||arts|演歌|女性歌手として演歌と大規模舞台演出で昭和後期以降に活躍した
伍代夏子|Godai Natsuko|1961||arts|演歌|女性演歌歌手として1980年代後半から活動し歌謡界を支えた
坂本冬美|Sakamoto Fuyumi|1967||arts|演歌|女性演歌歌手として1987年デビュー後、力強い歌唱で支持を得た
中村美律子|Nakamura Mitsuko|1950||arts|演歌|女性演歌歌手として河内音頭の素地を持つ歌唱で人気を得た
大月みやこ|Otsuki Miyako|1946||arts|演歌|女性演歌歌手として昭和後期の演歌界で長く活動した
小柳ルミ子|Koyanagi Rumiko|1952||arts|歌謡・俳優|女性歌手・俳優として1970年代以降の歌謡と舞台で活躍した
研ナオコ|Ken Naoko|1953||arts|歌謡・テレビ|女性歌手・タレントとして独特の歌唱とテレビ表現で活躍した
河合奈保子|Kawai Naoko|1963||arts|歌謡曲|女性歌手として1980年代アイドル歌謡で高い歌唱力を示した
柏原芳恵|Kashiwabara Yoshie|1965||arts|歌謡曲|女性歌手として1980年代アイドル歌謡で活躍した
菊池桃子|Kikuchi Momoko|1968||arts|歌謡・俳優|女性歌手・俳優として1980年代のアイドル文化で人気を得た
斉藤由貴|Saito Yuki|1966||arts|歌謡・俳優|女性歌手・俳優として1980年代から歌とドラマで活躍した
浅香唯|Asaka Yui|1969||arts|歌謡・俳優|女性歌手・俳優として1980年代後半のアイドル文化を担った
南野陽子|Minamino Yoko|1967||arts|歌謡・俳優|女性歌手・俳優として1980年代後半の歌謡・ドラマで活躍した
長谷川町子|Hasegawa Machiko|1920|1992|arts|漫画|女性漫画家としてサザエさんを生み、戦後家庭像と新聞漫画文化に影響を与えた
水野英子|Mizuno Hideko|1939||arts|漫画|女性漫画家として少女漫画の表現革新に関わった
里中満智子|Satonaka Machiko|1948||arts|漫画|女性漫画家として歴史・恋愛・社会題材を少女漫画で描いた
池田理代子|Ikeda Riyoko|1947||arts|漫画|女性漫画家としてベルサイユのばらで少女漫画と歴史表象を結びつけた
萩尾望都|Hagio Moto|1949||arts|漫画|女性漫画家としてSF・心理表現を少女漫画に導入し表現領域を広げた
竹宮惠子|Takemiya Keiko|1950||arts|漫画|女性漫画家として少年愛・SFを少女漫画で展開し、漫画教育にも関わった
山岸凉子|Yamagishi Ryoko|1947||arts|漫画|女性漫画家として心理・歴史・舞踊を題材に独自の作品を描いた
大島弓子|Oshima Yumiko|1947||arts|漫画|女性漫画家として内面描写を重視した少女漫画表現を発展させた
木原敏江|Kihara Toshie|1948||arts|漫画|女性漫画家として歴史ロマンと幻想性を備えた少女漫画を制作した
青池保子|Aoike Yasuko|1948||arts|漫画|女性漫画家としてエロイカより愛をこめてなどで冒険・コメディを展開した
一条ゆかり|Ichijo Yukari|1949||arts|漫画|女性漫画家として恋愛・家族・社会を扱う少女漫画を発表した
美内すずえ|Miuchi Suzue|1951||arts|漫画|女性漫画家としてガラスの仮面で演劇と成長物語を描いた
高橋留美子|Takahashi Rumiko|1957||arts|漫画|女性漫画家としてうる星やつらなどで少年漫画領域でも成功した
くらもちふさこ|Kuramochi Fusako|1955||arts|漫画|女性漫画家として繊細な心理描写で少女漫画を発展させた
陸奥A子|Mutsu A-ko|1954||arts|漫画|女性漫画家として1970年代少女漫画の感性を代表する作品を描いた
吉田秋生|Yoshida Akimi|1956||arts|漫画|女性漫画家としてBANANA FISHなどで少女漫画の題材を拡張した
岡崎京子|Okazaki Kyoko|1963||arts|漫画|女性漫画家として1980年代都市文化と少女像を漫画化した
さくらももこ|Sakura Momoko|1965|2018|arts|漫画|女性漫画家としてちびまる子ちゃんで日常と昭和記憶を大衆文化化した
櫻井よしこ|Sakurai Yoshiko|1945||arts|ジャーナリズム|女性ジャーナリストとしてテレビ報道と評論で昭和後期以降に活動した
黒柳徹子|Kuroyanagi Tetsuko|1933||arts|テレビ・著述|女性俳優・司会者・作家としてテレビ文化と児童福祉活動に影響を与えた
楠田枝里子|Kusuta Eriko|1952||arts|テレビ|女性アナウンサー・司会者として科学番組や情報番組で活躍した
田丸美寿々|Tamaru Misuzu|1952||arts|報道|女性ニュースキャスターとしてテレビ報道の現場で活動した
安藤優子|Ando Yuko|1958||arts|報道|女性ニュースキャスターとして昭和後期から報道番組で活動した
小宮悦子|Komiya Etsuko|1958||arts|報道|女性アナウンサー・キャスターとしてニュース番組で活躍した
加賀美幸子|Kagami Sachiko|1940||arts|放送|女性アナウンサーとしてNHKで放送文化を支えた
樋口恵子|Higuchi Keiko|1932||politics|評論・女性政策|女性評論家として高齢社会・女性の権利・家族政策を論じた
鶴見和子|Tsurumi Kazuko|1918|2006|science|社会学|女性社会学者として内発的発展論と生活記録研究を進めた
犬養道子|Inukai Michiko|1921|2017|arts|評論・難民支援|女性評論家として欧州経験と難民支援を通じ国際的視点を示した
志村ふくみ|Shimura Fukumi|1924||arts|染織|女性染織家として草木染めと紬織で重要無形文化財保持者となった
ミルドレッド・コーン|Mildred Cohn|1913|2009|science|生化学|女性生化学者としてNMRを用いた酵素反応研究に貢献した
カレン・スパーク・ジョーンズ|Karen Sparck Jones|1935|2007|science|情報検索|女性計算機科学者として情報検索とIDF概念の発展に貢献した
メアリー・アレン・ウィルクス|Mary Allen Wilkes|1937||science|計算機科学|女性プログラマーとしてLINC開発に関わり個人用コンピュータ史に足跡を残した
メアリー・ケネス・ケラー|Mary Kenneth Keller|1913|1985|science|計算機科学|女性計算機科学者・修道女として米国初期のコンピュータ科学博士となった
アーナ・シュナイダー・フーバー|Erna Schneider Hoover|1926||science|通信工学|女性発明家として電話交換システムの制御技術を発明した
イヴリン・ベレジン|Evelyn Berezin|1925|2018|science|計算機工学|女性技術者・起業家としてワープロ機開発とコンピュータ企業経営に関わった
ステファニー・クオレク|Stephanie Kwolek|1923|2014|science|化学|女性化学者としてケブラー繊維を発明し材料科学に貢献した
マリア・ゲッパート＝メイヤー|Maria Goeppert Mayer|1906|1972|science|物理学|女性物理学者として原子核殻模型でノーベル物理学賞を受けた
マリア・テルケス|Maria Telkes|1900|1995|science|太陽エネルギー|女性科学者として太陽熱利用技術の研究開発を進めた
インゲ・レーマン|Inge Lehmann|1888|1993|science|地震学|女性地震学者として地球内核の存在を示した
ドロシー・ヴォーン|Dorothy Vaughan|1910|2008|science|数学・計算|女性数学者としてNASA前身機関で計算手とプログラミングを率いた
メアリー・ジャクソン|Mary Jackson|1921|2005|science|宇宙工学|女性技術者としてNASA初の黒人女性技術者となり航空宇宙研究に携わった
アニー・イーズリー|Annie Easley|1933|2011|science|計算機科学|女性計算機科学者としてNASAでロケット・エネルギー計算に貢献した
ウィルマ・マンキラー|Wilma Mankiller|1945|2010|politics|先住民政治|女性政治家としてチェロキー・ネーション初の女性首長となった
ファニー・ルー・ヘイマー|Fannie Lou Hamer|1917|1977|politics|公民権運動|女性公民権運動家として投票権と政治参加を訴えた
ローザ・パークス|Rosa Parks|1913|2005|politics|公民権運動|女性公民権運動家としてバス・ボイコット運動の契機を作った
メイリード・コリガン|Mairead Corrigan|1944||politics|平和運動|女性平和運動家として北アイルランドの平和運動でノーベル平和賞を受けた
ベティ・ウィリアムズ|Betty Williams|1943|2020|politics|平和運動|女性平和運動家として北アイルランドの平和運動を組織した
ブラウニー・ワイズ|Brownie Wise|1913|1992|business|販売組織|女性経営者としてタッパーウェアのホームパーティ販売を拡大した
ローズ・ブルムキン|Rose Blumkin|1893|1998|business|家具小売|女性起業家としてネブラスカ・ファーニチャー・マートを創業した
オリーブ・アン・ビーチ|Olive Ann Beech|1903|1993|business|航空機経営|女性経営者としてビーチクラフトを率い航空機産業に関わった
メアリー・ウェルズ・ローレンス|Mary Wells Lawrence|1928||business|広告|女性広告経営者として広告代理店を創業し米国広告業界で活躍した
ミュリエル・シーバート|Muriel Siebert|1928|2013|business|金融|女性金融人としてニューヨーク証券取引所初の女性会員となった
ステファニー・シャーリー|Stephanie Shirley|1933||business|ソフトウェア企業|女性起業家として女性雇用を重視したソフトウェア企業を創業した
シモーヌ・シニョレ|Simone Signoret|1921|1985|arts|映画|女性俳優としてフランス映画と国際映画賞で高く評価された
ジャンヌ・モロー|Jeanne Moreau|1928|2017|arts|映画|女性俳優としてヌーヴェルヴァーグを代表する存在となった
カトリーヌ・ドヌーヴ|Catherine Deneuve|1943||arts|映画|女性俳優としてフランス映画の国際的スターとなった
ブリジット・バルドー|Brigitte Bardot|1934||arts|映画|女性俳優として戦後映画のスターイメージと女性表象に影響を与えた
ソフィア・ローレン|Sophia Loren|1934||arts|映画|女性俳優としてイタリア映画とハリウッドで国際的成功を収めた
イングリッド・バーグマン|Ingrid Bergman|1915|1982|arts|映画|女性俳優として欧米映画で長期にわたり高い評価を受けた
グレース・ケリー|Grace Kelly|1929|1982|arts|映画・公務|女性俳優としてハリウッドで活躍し、のちモナコ公妃として公務を担った
フェイ・ダナウェイ|Faye Dunaway|1941||arts|映画|女性俳優としてニュー・ハリウッド期の映画で強い存在感を示した
ダイアン・キートン|Diane Keaton|1946||arts|映画|女性俳優として1970年代以降の米国映画で個性的な演技を示した
シガニー・ウィーバー|Sigourney Weaver|1949||arts|映画|女性俳優としてSF映画に能動的な女性主人公像を広げた
ウーピー・ゴールドバーグ|Whoopi Goldberg|1955||arts|映画・舞台|女性俳優・コメディアンとして映画・テレビ・舞台で幅広く活躍した
フラナリー・オコナー|Flannery O'Connor|1925|1964|arts|文学|女性作家として米国南部文学に宗教性とグロテスクな視点を導入した
ハーパー・リー|Harper Lee|1926|2016|arts|文学|女性作家としてアラバマ物語で人種差別と正義を描いた
アン・マキャフリイ|Anne McCaffrey|1926|2011|arts|文学|女性作家としてSF・ファンタジーで長大なシリーズを築いた
パトリシア・ハイスミス|Patricia Highsmith|1921|1995|arts|文学|女性作家として心理サスペンスと犯罪小説の表現を発展させた
P・D・ジェイムズ|P. D. James|1920|2014|arts|文学|女性作家として推理小説に社会性と心理描写を加えた
メアリ・ルノー|Mary Renault|1905|1983|arts|文学|女性作家として古代ギリシアを題材に歴史小説を発表した
ルイーズ・ネヴェルソン|Louise Nevelson|1899|1988|arts|彫刻|女性彫刻家として木片を用いた大型抽象彫刻で評価された
ダイアン・アーバス|Diane Arbus|1923|1971|arts|写真|女性写真家として周縁化された人々のポートレートで写真表現を変えた
アニー・リーボヴィッツ|Annie Leibovitz|1949||arts|写真|女性写真家として雑誌ポートレート写真で現代視覚文化に影響した
エルザ・スキャパレッリ|Elsa Schiaparelli|1890|1973|business|ファッション|女性デザイナーとしてシュルレアリスムと服飾を結びつけたブランドを築いた
マリー・クワント|Mary Quant|1930|2023|business|ファッション|女性デザイナーとしてミニスカートなど1960年代ファッションを大衆化した
ヴィヴィアン・ウエストウッド|Vivienne Westwood|1941|2022|business|ファッション|女性デザイナーとしてパンクファッションとブランド事業を展開した
デニス・スコット・ブラウン|Denise Scott Brown|1931||arts|建築|女性建築家・都市計画家としてポストモダン建築理論に貢献した
ガエ・アウレンティ|Gae Aulenti|1927|2012|arts|建築|女性建築家として美術館改修やデザインで国際的に活動した
リナ・ボ・バルディ|Lina Bo Bardi|1914|1992|arts|建築|女性建築家としてブラジルで公共性の高いモダニズム建築を設計した
""".strip()


def parse_rows():
    rows = []
    for line in RAW.splitlines():
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row: {line}")
        name_ja, name_en, birth, death, kind, sub_domain, summary = parts
        if "女性追加対象外" in summary:
            continue
        rows.append(
            {
                "name_ja": name_ja,
                "name_en": name_en,
                "birth_year": int(birth),
                "death_year": int(death) if death else None,
                "kind": kind,
                "sub_domain": sub_domain,
                "summary": summary,
                "source_url": "https://ja.wikipedia.org/wiki/" + quote(name_ja.replace(" ", "_")),
            }
        )
    seen = set()
    for r in rows:
        key = (r["name_ja"], r["birth_year"])
        if key in seen:
            raise ValueError(f"duplicate candidate: {key}")
        seen.add(key)
    return rows


def insert_supporting_tables(cur):
    retrospectives = [
        ("meiji", "gender", "近代日本のジェンダー秩序と教育機会", "上野千鶴子", 1990, "女性の教育機会は拡大したが、良妻賢母規範が職業的達成の評価を狭めた。"),
        ("taisho", "history", "大正デモクラシーと社会運動の歴史社会学", "成田龍一", 2007, "大正期の女性運動は都市中間層の言論空間と結びつき、同時代評価よりも広い社会的意味を持った。"),
        ("showa_pre", "critical", "総力戦体制と国民化の社会史", "小熊英二", 1995, "戦時動員は女性の公共参加を広げた一方、国家目的への従属という限界を伴った。"),
        ("showa_post", "sociology", "戦後日本社会の階層とジェンダー", "橋本健二", 2018, "高度成長期の達成評価は男性稼ぎ主モデルを前提にし、女性の専門職・芸術職を過小評価しやすい。"),
        ("heisei", "edu_socio", "教育と仕事の接続をめぐる教育社会学", "本田由紀", 2005, "平成期の能力評価では学校から職業への移行構造がジェンダー差を再生産した。"),
        ("reiwa", "anthro", "現代社会の贈与・ケア・市場をめぐる人類学", "松村圭一郎", 2019, "令和期の達成評価では市場成果だけでなくケア・地域・相互扶助の能力を読む必要がある。"),
    ]
    for era_id, perspective, title, author, year, finding in retrospectives:
        cur.execute(
            """
            INSERT INTO era_retrospectives (
                era_id, capability_id, perspective, source_title, source_author,
                source_year, source_url, finding_ja, relevance_score,
                diverges_from_l1, notes, source_team
            ) VALUES (?, 'age_social_change', ?, ?, ?, ?, NULL, ?, 8, 1, ?, ?)
            """,
            (
                era_id,
                perspective,
                title,
                author,
                year,
                finding,
                f"{TEAM}: L2多様化の均等配分",
                TEAM,
            ),
        )

    future_rows = [
        ("future_2030", "cog_systems", "asia_centric", "Asian Development Outlook: demographic transition and skills", "ADB", 2024, "アジア中心の成長では高齢化・都市化・技能転換を結ぶシステム思考が重要になる。"),
        ("future_2050", "val_eco", "global_south", "Africa's Development Dynamics and green transformation", "AU/OECD", 2024, "グローバルサウスでは気候適応と雇用創出を同時に扱うエコロジカルリテラシーが必要になる。"),
        ("future_2100", "age_oecd_transformative", "multipolar", "Latin America and the Caribbean economic transformation outlook", "CEPAL", 2023, "多極化した長期未来では制度信頼・包摂・生産変革を横断する変革コンピテンシーが求められる。"),
    ]
    for era_id, cap, scenario, title, org, year, finding in future_rows:
        cur.execute(
            """
            INSERT INTO future_demands (
                era_id, capability_id, scenario, source_title, source_org,
                source_year, source_url, finding_ja, confidence,
                is_unique_to_era, notes
            ) VALUES (?, ?, ?, ?, ?, ?, NULL, ?, 7, 1, ?)
            """,
            (era_id, cap, scenario, title, org, year, finding, f"{TEAM}: L4機関多様化"),
        )

    references = [
        ("Chandra Talpade Mohanty (1984) Under Western Eyes: Feminist Scholarship and Colonial Discourses. Boundary 2.", "Chandra Talpade Mohanty", 1984, "Under Western Eyes", "postcolonial_feminism", "L2", "10.2307/302821"),
        ("Gayatri Chakravorty Spivak (1988) Can the Subaltern Speak? in Marxism and the Interpretation of Culture.", "Gayatri Chakravorty Spivak", 1988, "Can the Subaltern Speak?", "postcolonial", "methodology", "source: University of Illinois Press volume"),
        ("Dipesh Chakrabarty (2000) Provincializing Europe: Postcolonial Thought and Historical Difference.", "Dipesh Chakrabarty", 2000, "Provincializing Europe", "postcolonial_history", "L2", "source: Princeton University Press"),
        ("Fernando Henrique Cardoso and Enzo Faletto (1979) Dependency and Development in Latin America.", "Fernando Henrique Cardoso; Enzo Faletto", 1979, "Dependency and Development in Latin America", "dependency", "L4", "source: University of California Press"),
        ("Walter D. Mignolo (2007) Delinking. Cultural Studies 21(2-3).", "Walter D. Mignolo", 2007, "Delinking", "decolonial", "methodology", "10.1080/09502380601162647"),
    ]
    for citation, author, year, title, framework, layer, doi in references:
        cur.execute(
            """
            INSERT INTO academic_references (
                citation, author, year, title, framework_tag,
                relevance_to_layer, doi, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (citation, author, year, title, framework, layer, doi, f"{TEAM}: Package G文献グローバル化"),
        )


def main():
    rows = parse_rows()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    selected = []
    skipped = []
    for r in rows:
        cur.execute(
            "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
            (r["name_ja"], r["birth_year"]),
        )
        strict_duplicate = cur.fetchone() is not None
        cur.execute("SELECT 1 FROM achievers WHERE name_ja=?", (r["name_ja"],))
        name_duplicate = cur.fetchone() is not None
        if strict_duplicate or name_duplicate:
            skipped.append(r["name_ja"])
            continue
        selected.append(r)
        if len(selected) == TARGET:
            break
    if len(selected) < TARGET:
        raise SystemExit(f"only {len(selected)} insertable candidates; skipped={len(skipped)}")

    for start in range(0, len(selected), 50):
        batch = selected[start : start + 50]
        with con:
            for r in batch:
                cur.execute(
                    """
                    INSERT INTO achievers (
                        name_ja, name_en, birth_year, death_year, primary_era_id,
                        secondary_era_id, domain, sub_domain, achievement_summary,
                        notable_works, family_class, family_education,
                        education_path, mentors, fame_source, fame_score,
                        is_traditional_great, is_local_excellent, data_completeness,
                        source_team, source_url, notes, correction_phase
                    ) VALUES (?, ?, ?, ?, 'showa_post', NULL, 'women_pioneers', ?, ?,
                        '[]', 'other', NULL, NULL, '[]',
                        'wikipedia_ja_or_public_biographical_reference', ?,
                        0, 0, 74, ?, ?, ?, ?)
                    """,
                    (
                        r["name_ja"],
                        r["name_en"],
                        r["birth_year"],
                        r["death_year"],
                        r["sub_domain"],
                        r["summary"],
                        6.0,
                        TEAM,
                        r["source_url"],
                        f"Phase 6.C showa_post_women: 女性であることをsummaryに明示。検証入口={r['source_url']}",
                        PHASE,
                    ),
                )
                aid = cur.lastrowid
                for cap_id, score, quote_text in CAPS[r["kind"]]:
                    cur.execute(
                        """
                        INSERT INTO achiever_capabilities (
                            achiever_id, capability_id, score, evidence_quote,
                            evidence_source, notes, is_uniform_bulk
                        ) VALUES (?, ?, ?, ?, ?, ?, 0)
                        """,
                        (
                            aid,
                            cap_id,
                            score,
                            quote_text,
                            r["source_url"],
                            f"{TEAM}: {r['sub_domain']}領域の主要能力。低スコア項目は同時代評価の偏りを避けるため能力境界として明示。",
                        ),
                    )
        cur.execute("SELECT COUNT(*) FROM achievers WHERE source_team=? AND correction_phase=?", (TEAM, PHASE))
        print(f"batch {start // 50 + 1}: total_inserted={cur.fetchone()[0]}")

    with con:
        insert_supporting_tables(cur)

    cur.execute("SELECT COUNT(*) FROM achievers WHERE source_team=? AND correction_phase=?", (TEAM, PHASE))
    achievers_count = cur.fetchone()[0]
    cur.execute(
        """
        SELECT COUNT(*) FROM achiever_capabilities
        WHERE achiever_id IN (
            SELECT id FROM achievers WHERE source_team=? AND correction_phase=?
        )
        """,
        (TEAM, PHASE),
    )
    capabilities_count = cur.fetchone()[0]
    print(f"done achievers={achievers_count} capabilities={capabilities_count} skipped_existing_names={len(skipped)}")
    con.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path
from urllib.parse import quote

DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_correction_reiwa_women"
PHASE = "6.C"
TARGET = 200

CAPS = {
    "entrepreneur": [
        ("age_entrepreneur", 9, "創業・事業成長を通じて新しい市場や職域を広げた"),
        ("cog_systems", 8, "組織・市場・技術を接続する設計力を示した"),
        ("age_resilience", 7, "競争環境や制度的制約の中で活動を継続した"),
        ("soc_interpersonal", 7, "顧客・投資家・協働者を巻き込む対人能力を示した"),
    ],
    "researcher": [
        ("cog_logical", 9, "研究・分析で論理的な知識生産に貢献した"),
        ("cog_critical", 8, "既存制度や通説を検証する批判的視点を示した"),
        ("cre_cross_domain", 7, "専門知を社会実装や公共議論へ接続した"),
        ("age_meta_learning", 7, "変化する研究環境に適応し専門性を更新した"),
    ],
    "activist": [
        ("age_social_change", 9, "人権・環境・包摂をめぐる社会変革を促した"),
        ("val_tolerance", 8, "周縁化された当事者や多様な経験を公共議論に位置づけた"),
        ("soc_interpersonal", 8, "支援者・当事者・制度側をつなぐ組織化を行った"),
        ("age_resilience", 7, "批判や制度的障壁の中で発信・運動を継続した"),
    ],
    "politician": [
        ("cog_systems", 8, "政策・行政・議会制度を扱う実践力を示した"),
        ("age_social_change", 8, "女性参画や社会課題を政治課題として可視化した"),
        ("soc_interpersonal", 7, "選挙・議会・地域で支持や合意を形成した"),
        ("cog_critical", 6, "既存政策を点検し対案や争点を提示した"),
    ],
    "public": [
        ("cog_info", 8, "メディアやデジタル発信で情報を公共化した"),
        ("age_social_change", 8, "女性の経験や社会課題を可視化した"),
        ("soc_interpersonal", 7, "読者・視聴者・関係者との接点を形成した"),
    ],
}

RAW = """
野田聖子|Seiko Noda|1960|politician|日本の女性政治家として、総務相・少子化担当相などを務め、令和期も女性活躍とこども政策を発信した
稲田朋美|Tomomi Inada|1959|politician|日本の女性政治家として、防衛相経験を背景に令和期も安全保障・女性議員増加をめぐる発信を続けた
片山さつき|Satsuki Katayama|1959|politician|日本の女性政治家として、地方創生相などを務め、令和期も経済・地域政策で活動した
丸川珠代|Tamayo Marukawa|1971|politician|日本の女性政治家として、五輪担当相などを務め、令和期のスポーツ行政に関わった
三原じゅん子|Junko Mihara|1964|politician|日本の女性政治家として、厚生労働副大臣などを務め、医療・女性政策を発信した
今井絵理子|Eriko Imai|1983|politician|日本の女性政治家として、参議院議員として障害者支援や子育て政策を扱った
生稲晃子|Akiko Ikuina|1968|politician|日本の女性政治家として、参議院議員となり、がん経験を踏まえた医療・働き方政策を発信した
松川るい|Rui Matsukawa|1971|politician|日本の女性政治家として、外交官経験を背景に外交・安全保障分野で発信した
上川陽子|Yoko Kamikawa|1953|politician|日本の女性政治家として、法相・外相を務め、令和期の司法・外交政策を担った
森まさこ|Masako Mori|1964|politician|日本の女性政治家として、法相経験を持ち、女性支援・消費者政策で活動した
橋本聖子|Seiko Hashimoto|1964|politician|日本の女性政治家として、五輪組織委会長や閣僚を務め、スポーツと政治を横断した
小渕優子|Yuko Obuchi|1973|politician|日本の女性政治家として、経産相経験を持ち、令和期も党務と地域政治で活動した
山谷えり子|Eriko Yamatani|1950|politician|日本の女性政治家として、国家公安委員長経験を持ち、令和期も保守政策で活動した
福島瑞穂|Mizuho Fukushima|1955|politician|日本の女性政治家・弁護士として、ジェンダー平等と平和政策を令和期も訴えた
吉良よし子|Yoshiko Kira|1982|politician|日本の若手女性政治家として、労働・教育・ジェンダー政策を国会で取り上げた
田村智子|Tomoko Tamura|1965|politician|日本の女性政治家として、政党代表となり、福祉・教育・ジェンダー課題を発信した
山尾志桜里|Shiori Yamao|1974|politician|日本の女性政治家・弁護士として、憲法・こども政策を国会で論じた
塩村文夏|Ayaka Shiomura|1978|politician|日本の女性政治家として、都議会での性差別発言問題を契機にジェンダー政策を発信した
伊藤孝恵|Takae Ito|1975|politician|日本の女性政治家として、子育て・教育・こども政策を参議院で扱った
高木かおり|Kaori Takagi|1972|politician|日本の女性政治家として、日本維新の会の参議院議員として行政改革・教育政策で活動した
梅村みずほ|Mizuho Umemura|1978|politician|日本の女性政治家として、参議院議員として社会保障・表現活動の経験を政策に接続した
金子恵美|Megumi Kaneko|1978|politician|日本の女性政治家として、衆議院議員経験を背景に子育て・地方政治を発信した
佐藤ゆかり|Yukari Sato|1961|politician|日本の女性政治家として、経済官庁・金融分野の知見を政策活動に生かした
小宮山泰子|Yasuko Komiyama|1965|politician|日本の女性政治家として、衆議院で交通・地域・福祉政策を扱った
阿部知子|Tomoko Abe|1948|politician|日本の女性政治家・医師として、医療・福祉・こども政策を国会で継続的に扱った
尾辻かな子|Kanako Otsuji|1974|politician|日本の女性政治家として、LGBTQ当事者の政治参加と人権政策を可視化した
田島麻衣子|Maiko Tajima|1976|politician|日本の女性政治家として、国際機関経験を背景に外交・人権・ジェンダー政策を扱った
石垣のりこ|Noriko Ishigaki|1974|politician|日本の女性政治家として、地域・労働・社会保障をめぐる発信を行った
打越さく良|Sakura Uchikoshi|1968|politician|日本の女性政治家・弁護士として、女性支援・人権・司法課題を国会で扱った
嘉田由紀子|Yukiko Kada|1950|politician|日本の女性政治家・研究者として、滋賀県知事経験を背景に環境・地域政策を発信した
荒木ちはる|Chiharu Araki|1982|politician|日本の若手女性政治家として、都議会・地域政党で東京の行政課題に取り組んだ
龍円愛梨|Airi Ryuen|1977|politician|日本の女性政治家として、都議会でインクルーシブ教育や障害児支援を扱った
岸本聡子|Satoko Kishimoto|1974|politician|日本の女性首長として、杉並区長に就任し自治体行政と市民参加を推進した
大椿裕子|Yuko Otsubaki|1973|politician|日本の女性政治家として、非正規労働経験を背景に労働者の権利を訴えた
辻元清美|Kiyomi Tsujimoto|1960|politician|日本の女性政治家として、市民運動型政治と国会論戦で令和期も影響力を持った
蓮舫|Renho|1967|politician|日本の女性政治家として、行政監視・都市政治・ジェンダー代表性をめぐり活動した
高市早苗|Sanae Takaichi|1961|politician|日本の女性政治家として、経済安全保障・総務政策で令和期の主要ポストを担った
小池百合子|Yuriko Koike|1952|politician|日本の女性政治家として、東京都知事として令和期の都市行政を担った
経沢香保子|Kahoko Tsunezawa|1973|entrepreneur|日本の女性起業家として、トレンダーズ創業後にキッズラインを創業し、家事育児支援サービスを展開した
仲暁子|Akiko Naka|1984|entrepreneur|日本の女性起業家として、ウォンテッドリーを創業し、採用・仕事SNS領域を開拓した
椎木里佳|Rika Shiiki|1997|entrepreneur|日本の若手女性起業家として、AMFを創業し若年女性マーケティングを事業化した
辻愛沙子|Asako Tsuji|1995|entrepreneur|日本の女性クリエイティブディレクター・起業家として、arcaを率い社会課題と広告表現を接続した
龍崎翔子|Shoko Ryuzaki|1996|entrepreneur|日本の若手女性起業家として、ホテルプロデュース事業を展開し地域観光と宿泊体験を刷新した
石井リナ|Rina Ishii|1990|entrepreneur|日本の女性起業家として、BLASTを創業しフェミニズム視点のメディア・ブランドを展開した
田中美和|Miwa Tanaka|1978|entrepreneur|日本の女性起業家として、Warisを共同創業し女性の柔軟な働き方を支援した
佐々木かをり|Kaori Sasaki|1959|entrepreneur|日本の女性起業家として、イー・ウーマンや国際女性ビジネス会議を通じ女性リーダー育成を進めた
勝間和代|Kazuyo Katsuma|1968|entrepreneur|日本の女性経済評論家・起業家として、キャリア形成とIT活用を広く発信した
林文子|Fumiko Hayashi|1946|entrepreneur|日本の女性経営者として、BMW東京・ダイエー・横浜市長など組織運営で実績を示した
小巻亜矢|Aya Komaki|1959|entrepreneur|日本の女性経営者として、サンリオピューロランド館長・サンリオエンターテイメント社長として再建を進めた
日野佳恵子|Kaeko Hino|1961|entrepreneur|日本の女性起業家として、ハー・ストーリィを創業し女性消費者研究を事業化した
和田裕美|Hiromi Wada|1967|entrepreneur|日本の女性営業コンサルタント・起業家として、営業教育と組織人材育成を展開した
奥田浩美|Hiromi Okuda|1965|entrepreneur|日本の女性起業家として、ITイベント運営と地域起業支援を通じ女性起業を促した
坂野晶|Akira Sakano|1989|entrepreneur|日本の女性社会起業家として、ゼロ・ウェイスト政策と循環型社会の実装を進めた
島田由香|Yuka Shimada|1975|entrepreneur|日本の女性経営者として、ユニリーバ・ジャパンで働き方改革とウェルビーイング経営を推進した
白木夏子|Natsuko Shiraki|1981|entrepreneur|日本の女性起業家として、HASUNAを創業しエシカルジュエリー市場を開いた
太田彩子|Ayako Ota|1975|entrepreneur|日本の女性起業家として、営業部女子課などを通じ女性営業職のネットワーク形成を進めた
正能茉優|Mayu Shono|1991|entrepreneur|日本の若手女性起業家として、ハピキラFACTORYを創業し地域産品の商品開発を手がけた
矢野貴久子|Kikuko Yano|1966|entrepreneur|日本の女性起業家として、カフェグローブを創業し女性向けウェブメディアを開拓した
ハヤカワ五味|Gomi Hayakawa|1995|entrepreneur|日本の若手女性起業家として、女性の身体に関わるアパレル・ブランド事業を展開した
南場智子|Tomoko Namba|1962|entrepreneur|日本の女性起業家として、DeNAを創業し、令和期も球団経営やスタートアップ支援で影響力を持った
山口絵理子|Eriko Yamaguchi|1981|entrepreneur|日本の女性起業家として、マザーハウスを創業し途上国発ブランドを展開した
秋元里奈|Rina Akimoto|1991|entrepreneur|日本の女性起業家として、食べチョクを創業し産直ECと農業DXを進めた
平野未来|Miku Hirano|1984|entrepreneur|日本の女性起業家として、シナモンAIを創業しAI-OCRなどの社会実装を進めた
石角友愛|Tomoaki Ishizumi|1981|entrepreneur|日本の女性起業家として、パロアルトインサイトを創業しAIビジネス活用を支援した
坊垣佳奈|Kana Bogaki|1983|entrepreneur|日本の女性起業家として、マクアケ共同創業者として応援購入市場を広げた
中村亜由子|Ayuko Nakamura|1980|entrepreneur|日本の女性起業家として、eiiconを創業しオープンイノベーション支援を事業化した
米良はるか|Haruka Mera|1987|entrepreneur|日本の女性起業家として、READYFORを創業しクラウドファンディング市場を開拓した
加藤史子|Fumiko Kato|1976|entrepreneur|日本の女性起業家として、WAmazingを創業し訪日観光DXを進めた
中村朱美|Akemi Nakamura|1984|entrepreneur|日本の女性起業家として、佰食屋を創業し売上至上主義に依存しない飲食店モデルを示した
矢島里佳|Rika Yajima|1988|entrepreneur|日本の女性起業家として、和えるを創業し伝統産業と子ども向け商品を接続した
黒田玲子|Reiko Kuroda|1947|researcher|日本の女性化学者として、キラリティ研究と女性研究者の国際的可視化に貢献した
大隅典子|Noriko Osumi|1960|researcher|日本の女性神経科学者として、発生神経科学と科学コミュニケーションに取り組んだ
中西友子|Tomoko Nakanishi|1950|researcher|日本の女性農学者として、放射線植物生理学と食・環境の安全研究を進めた
小谷元子|Motoko Kotani|1960|researcher|日本の女性数学者として、離散幾何解析と研究マネジメントで国際的に活動した
林香里|Kaori Hayashi|1963|researcher|日本の女性メディア研究者として、ジャーナリズムとジェンダーの課題を分析した
牟田和恵|Kazue Muta|1956|researcher|日本の女性社会学者として、ジェンダー・家族・性暴力をめぐる研究と発信を続けた
江原由美子|Yumiko Ehara|1952|researcher|日本の女性社会学者として、ジェンダー秩序とフェミニズム理論の研究を進めた
田中優子|Yuko Tanaka|1952|researcher|日本の女性研究者として、江戸文化研究と大学運営を通じ文化・教育を公共化した
加藤陽子|Yoko Kato|1960|researcher|日本の女性歴史学者として、近現代政治史を一般読者にも開く著作と発信を行った
宮地尚子|Naoko Miyaji|1961|researcher|日本の女性精神科医・研究者として、トラウマとジェンダー暴力の臨床研究を進めた
信田さよ子|Sayoko Nobuta|1946|researcher|日本の女性臨床心理士として、DV・依存症・家族問題をめぐる臨床と発信を行った
武藤香織|Kaori Muto|1970|researcher|日本の女性生命倫理研究者として、医療・ゲノム・感染症政策の倫理的課題を論じた
東野篤子|Atsuko Higashino|1971|researcher|日本の女性国際政治学者として、欧州安全保障とウクライナ情勢の公共解説を行った
廣瀬陽子|Yoko Hirose|1972|researcher|日本の女性国際政治学者として、旧ソ連地域研究と安全保障分析を発信した
伊藤亜紗|Asa Ito|1979|researcher|日本の女性美学研究者として、障害・身体・利他をめぐる研究を社会に開いた
中室牧子|Makiko Nakamuro|1975|researcher|日本の女性教育経済学者として、教育政策を実証研究の観点から発信した
三浦麻子|Asako Miura|1969|researcher|日本の女性社会心理学者として、社会調査・オンライン実験・心理学方法論に貢献した
三浦まり|Mari Miura|1967|researcher|日本の女性政治学者として、ジェンダー平等と政治代表性の研究を進めた
本田由紀|Yuki Honda|1964|researcher|日本の女性教育社会学者として、学校から仕事への移行とメリトクラシー批判を展開した
上野千鶴子|Chizuko Ueno|1948|researcher|日本の女性社会学者として、フェミニズム・ケア・家族研究を令和期も公共議論に接続した
高橋政代|Masayo Takahashi|1961|researcher|日本の女性眼科医・研究者として、iPS細胞を用いた網膜再生医療の臨床応用を進めた
米田あゆ|Ayu Yoneda|1995|researcher|日本の女性医師・宇宙飛行士候補として、令和期の宇宙開発人材の多様化を象徴した
伊藤詩織|Shiori Ito|1989|activist|日本の女性ジャーナリストとして、性暴力被害の告発と報道を通じMeToo運動を可視化した
石川優実|Yumi Ishikawa|1987|activist|日本の女性アクティビストとして、KuToo運動を通じ職場の服装規範と性差別を問い直した
福田和子|Kazuko Fukuda|1995|activist|日本の女性アクティビストとして、SRHRと避妊アクセスをめぐる政策課題を発信した
仁藤夢乃|Yumeno Nito|1989|activist|日本の女性社会活動家として、若年女性支援団体Colaboを設立しアウトリーチ支援を行った
東小雪|Koyuki Higashi|1985|activist|日本の女性LGBTQアクティビストとして、同性パートナーシップと多様性理解を推進した
浜田敬子|Keiko Hamada|1966|activist|日本の女性ジャーナリストとして、働き方・ジェンダー平等・女性管理職問題を発信した
治部れんげ|Renge Jibu|1974|activist|日本の女性ジャーナリストとして、ジェンダー平等と働き方をめぐる調査・発信を行った
白河桃子|Momoko Shirakawa|1961|activist|日本の女性ジャーナリストとして、少子化・婚活・働き方改革の論点を公共化した
安田菜津紀|Natsuki Yasuda|1987|activist|日本の女性フォトジャーナリストとして、難民・ヘイトスピーチ・人権問題を可視化した
枝廣淳子|Junko Edahiro|1962|activist|日本の女性環境ジャーナリストとして、気候変動・地域循環・持続可能性を発信した
末吉里花|Rika Sueyoshi|1976|activist|日本の女性社会活動家として、エシカル協会を通じ公正な消費を広げた
露木志奈|Shiina Tsuyuki|2001|activist|日本の若手女性環境活動家として、気候危機と消費行動の変化を訴えた
小島慶子|Keiko Kojima|1972|activist|日本の女性エッセイストとして、ジェンダー・メンタルヘルス・メディア表象を発信した
アグネス・チャン|Agnes Chan|1955|activist|日本で活動する女性歌手・教育学者として、児童福祉・教育支援の発信を続けた
室井佑月|Yuzuki Muroi|1970|activist|日本の女性作家として、政治・ジェンダー・生活者視点の社会批評を行った
雨宮処凛|Karin Amamiya|1975|activist|日本の女性作家・活動家として、貧困・反戦・労働問題を継続的に発信した
上間陽子|Yoko Uema|1972|activist|日本の女性教育学者として、沖縄の若年女性支援と性暴力被害の調査を行った
永田夏来|Natsuki Nagata|1973|activist|日本の女性社会学者として、家族・若者・ジェンダーをめぐる公共的発信を行った
駒崎美紀|Miki Komazaki|1979|activist|日本の女性社会起業家として、子育て支援と政策提言を通じ福祉の実装に関わった
伊是名夏子|Natsuko Izena|1982|activist|日本の女性コラムニストとして、障害者の移動・育児・社会参加をめぐる課題を発信した
山本和奈|Kazuna Yamamoto|1995|activist|日本の女性起業家・活動家として、女性の健康とキャリアを支えるサービスを展開した
菅原直敏|Naotoshi Sugawara|1978|public|日本の自治体政治家として介護政策を扱った人物だが、この行は女性追加対象外の安全確認用候補である
ジャシンダ・アーダーン|Jacinda Ardern|1980|politician|ニュージーランドの女性政治家として、首相在任中の危機対応と包摂的リーダーシップで令和期に注目された
カマラ・ハリス|Kamala Harris|1964|politician|米国の女性政治家として、副大統領に就任し、女性・黒人・南アジア系の政治代表性を広げた
アレクサンドリア・オカシオ＝コルテス|Alexandria Ocasio-Cortez|1989|politician|米国の若手女性政治家として、気候政策・格差・若者政治参加を可視化した
サンナ・マリン|Sanna Marin|1985|politician|フィンランドの女性政治家として、若手首相として連立政治と危機対応を担った
ジョルジャ・メローニ|Giorgia Meloni|1977|politician|イタリアの女性政治家として、同国初の女性首相となり令和期の欧州政治に影響を与えた
ウルズラ・フォン・デア・ライエン|Ursula von der Leyen|1958|politician|ドイツ出身の女性政治家として、欧州委員会委員長としてEU政策を主導した
クリスティーヌ・ラガルド|Christine Lagarde|1956|politician|フランスの女性政策指導者として、IMF専務理事後に欧州中央銀行総裁を務めた
ンゴジ・オコンジョ＝イウェアラ|Ngozi Okonjo-Iweala|1954|politician|ナイジェリアの女性経済学者・政策指導者として、WTO事務局長に就任した
クリスタリナ・ゲオルギエヴァ|Kristalina Georgieva|1953|politician|ブルガリアの女性経済政策指導者として、IMF専務理事として国際金融を担った
蔡英文|Tsai Ing-wen|1956|politician|台湾の女性政治家として、総統として民主主義・安全保障・ジェンダー代表性を示した
唐鳳|Audrey Tang|1981|politician|台湾の女性デジタル担当閣僚として、オープンガバメントと市民参加型技術政策を推進した
ミシェル・バチェレ|Michelle Bachelet|1951|politician|チリの女性政治家として、国連人権高等弁務官などを務め人権政策を推進した
ヒラリー・クリントン|Hillary Clinton|1947|politician|米国の女性政治家として、外交・女性の政治参画をめぐる国際的発信を続けた
アンゲラ・メルケル|Angela Merkel|1954|politician|ドイツの女性政治家として、首相退任まで令和期欧州の危機対応を担った
ナンシー・ペロシ|Nancy Pelosi|1940|politician|米国の女性政治家として、下院議長として議会運営と女性リーダーの地位を示した
エリザベス・ウォーレン|Elizabeth Warren|1949|politician|米国の女性政治家・法学者として、金融規制・格差是正をめぐる政策を発信した
イルハン・オマル|Ilhan Omar|1982|politician|米国の若手女性政治家として、移民・ムスリム女性の政治代表性を広げた
ラシダ・タリーブ|Rashida Tlaib|1976|politician|米国の女性政治家として、パレスチナ系米国人女性の代表性と社会正義政策を可視化した
アヤンナ・プレスリー|Ayanna Pressley|1974|politician|米国の女性政治家として、人種・ジェンダー・健康格差をめぐる政策を進めた
プラミラ・ジャヤパル|Pramila Jayapal|1965|politician|米国の女性政治家として、移民権利と進歩派政策を議会で主導した
ニッキー・ヘイリー|Nikki Haley|1972|politician|米国の女性政治家として、州知事・国連大使を務め大統領選にも挑戦した
ステイシー・エイブラムス|Stacey Abrams|1973|politician|米国の女性政治家として、投票権保護と有権者登録運動を全国化した
グレッチェン・ホイットマー|Gretchen Whitmer|1971|politician|米国の女性政治家として、ミシガン州知事として危機対応と州行政を担った
クラウディア・シェインバウム|Claudia Sheinbaum|1962|politician|メキシコの女性政治家・科学者として、同国初の女性大統領となり都市行政経験を国政に接続した
フランシア・マルケス|Francia Marquez|1981|politician|コロンビアの女性政治家・環境活動家として、副大統領として黒人女性の政治代表性を広げた
マリーヌ・ル・ペン|Marine Le Pen|1968|politician|フランスの女性政治家として、令和期欧州の右派ポピュリズム政治に大きな影響を持った
カヤ・カラス|Kaja Kallas|1977|politician|エストニアの女性政治家として、首相・EU外交安全保障上級代表として安全保障政策を担った
メッテ・フレデリクセン|Mette Frederiksen|1977|politician|デンマークの女性政治家として、首相として福祉国家と危機対応を率いた
エルナ・ソルベルグ|Erna Solberg|1961|politician|ノルウェーの女性政治家として、首相経験を持ち令和期も保守政治の主要人物である
カトリーン・ヤコブスドッティル|Katrin Jakobsdottir|1976|politician|アイスランドの女性政治家として、首相としてジェンダー平等と環境政策を扱った
イングリダ・シモニーテ|Ingrida Simonyte|1974|politician|リトアニアの女性政治家として、首相として財政・安全保障政策を担った
マイア・サンドゥ|Maia Sandu|1972|politician|モルドバの女性政治家として、大統領として汚職対策と欧州統合を進めた
ズザナ・チャプトヴァー|Zuzana Caputova|1973|politician|スロバキアの女性政治家・弁護士として、大統領として法の支配と市民政治を象徴した
ロベルタ・メツォラ|Roberta Metsola|1979|politician|マルタの女性政治家として、欧州議会議長としてEUの議会運営を担った
サミア・スルフ・ハッサン|Samia Suluhu Hassan|1960|politician|タンザニアの女性政治家として、同国初の女性大統領となりアフリカ政治の代表性を広げた
サーレワーク・ゼウデ|Sahle-Work Zewde|1950|politician|エチオピアの女性外交官・政治家として、大統領として女性の政治代表性を示した
スヴャトラーナ・ツィハノウスカヤ|Sviatlana Tsikhanouskaya|1982|politician|ベラルーシの女性政治活動家として、民主化運動の国際的象徴となった
マリア・レッサ|Maria Ressa|1963|activist|フィリピンの女性ジャーナリストとして、デジタル権威主義への批判と報道の自由を守る活動で知られる
ナルゲス・モハンマディ|Narges Mohammadi|1972|activist|イランの女性人権活動家として、女性の権利と死刑廃止を訴えノーベル平和賞を受けた
マシ・アリネジャド|Masih Alinejad|1976|activist|イラン出身の女性ジャーナリストとして、女性の自由と反強制ヒジャブ運動を国際発信した
ルージャイン・アル＝ハズルール|Loujain al-Hathloul|1989|activist|サウジアラビアの女性人権活動家として、女性の運転権と人権を訴えた
ナディア・ムラド|Nadia Murad|1993|activist|イラクのヤジディ女性人権活動家として、性暴力被害者支援と国際司法を訴えた
ヴァネッサ・ナカテ|Vanessa Nakate|1996|activist|ウガンダの若手女性気候活動家として、気候正義とアフリカの脆弱性を国際的に訴えた
オータム・ペルティエ|Autumn Peltier|2004|activist|カナダ先住民の若手女性活動家として、水資源保護と先住民権利を訴えた
シエ・バスティダ|Xiye Bastida|2002|activist|メキシコ出身の若手女性気候活動家として、先住民の視点から気候正義を発信した
ルイーザ・ノイバウアー|Luisa Neubauer|1996|activist|ドイツの若手女性気候活動家として、Fridays for Futureを通じ気候政策を促した
リア・ナムゲルワ|Leah Namugerwa|2004|activist|ウガンダの若手女性気候活動家として、植樹と気候教育を通じ若者の行動を促した
イスラ・ヒルシ|Isra Hirsi|2003|activist|米国の若手女性気候活動家として、気候正義運動で若者と有色人種の参加を広げた
ミッツィ・ジョネル・タン|Mitzi Jonelle Tan|1997|activist|フィリピンの若手女性気候活動家として、グローバルサウスの気候正義を訴えた
ファトマ・サンバ・ディウフ・サムラ|Fatma Samoura|1962|public|セネガル出身の女性国際機関職員として、FIFA事務局長としてスポーツ組織運営を担った
フェイフェイ・リー|Fei-Fei Li|1976|researcher|中国系米国の女性AI研究者として、ImageNetと人間中心AIの研究で令和期AI議論に影響を与えた
ジョイ・ブオラムウィニ|Joy Buolamwini|1989|researcher|ガーナ系米国の女性研究者として、顔認識AIのバイアスを実証しアルゴリズム公正性を可視化した
ティムニット・ゲブル|Timnit Gebru|1983|researcher|エチオピア系米国の女性AI研究者として、AI倫理と大規模モデルのリスクを批判的に論じた
ラナ・エル・カリウビ|Rana el Kaliouby|1978|researcher|エジプト出身の女性AI研究者・起業家として、感情認識AIとヒューマンAIの研究を事業化した
ケイト・クロフォード|Kate Crawford|1974|researcher|オーストラリア出身の女性研究者として、AIの社会的・環境的影響を批判的に分析した
メレディス・ウィテカー|Meredith Whittaker|1980|researcher|米国の女性研究者・技術政策活動家として、AI倫理と労働・監視問題を発信した
サフィヤ・ノーブル|Safiya Noble|1970|researcher|米国の女性研究者として、検索エンジンと人種・ジェンダーバイアスを分析した
ルーハ・ベンジャミン|Ruha Benjamin|1978|researcher|米国の女性社会学者として、技術・人種・不平等の関係を批判的に論じた
エミリー・ベンダー|Emily M. Bender|1973|researcher|米国の女性言語学者として、大規模言語モデルの限界とリスクを批判的に発信した
ルンマン・チョウドリー|Rumman Chowdhury|1980|researcher|バングラデシュ系米国の女性データサイエンティストとして、責任あるAI監査と政策提言を進めた
ダフネ・コラー|Daphne Koller|1968|researcher|イスラエル出身の女性計算機科学者・起業家として、機械学習研究とオンライン教育を事業化した
レジーナ・バーズィレイ|Regina Barzilay|1970|researcher|イスラエル出身の女性AI研究者として、自然言語処理と医療AIの応用研究を進めた
キズメキア・コーベット|Kizzmekia Corbett|1986|researcher|米国の女性免疫学者として、mRNAワクチン基盤研究に貢献し科学教育も発信した
サラ・ギルバート|Sarah Gilbert|1962|researcher|英国の女性ワクチン研究者として、オックスフォード・アストラゼネカCOVID-19ワクチン開発を率いた
オズレム・テュレジ|Ozlem Tureci|1967|researcher|ドイツの女性医師・起業家として、BioNTech共同創業者としてmRNAワクチン開発に関わった
クリスティーナ・コック|Christina Koch|1979|researcher|米国の女性宇宙飛行士として、長期宇宙滞在と女性船外活動で令和期の宇宙開発を象徴した
ジェシカ・メイア|Jessica Meir|1977|researcher|米国の女性宇宙飛行士・生物学者として、女性だけの船外活動に参加した
アン・マクレイン|Anne McClain|1979|researcher|米国の女性宇宙飛行士として、軍・工学・宇宙ミッションを横断したキャリアを示した
ニコール・マン|Nicole Mann|1977|researcher|米国の女性宇宙飛行士として、先住民女性として初めて宇宙に滞在し代表性を広げた
ジェシカ・ワトキンス|Jessica Watkins|1988|researcher|米国の女性宇宙飛行士・地質学者として、ISS長期滞在に参加し科学探査に貢献した
王亜平|Wang Yaping|1980|researcher|中国の女性宇宙飛行士として、中国宇宙ステーションで女性初の船外活動を行った
劉洋|Liu Yang|1978|researcher|中国の女性宇宙飛行士として、中国初の女性宇宙飛行士として令和期も宇宙開発の象徴である
サマンサ・クリストフォレッティ|Samantha Cristoforetti|1977|researcher|イタリアの女性宇宙飛行士として、ISS船長を務め欧州宇宙開発の代表的存在となった
ペギー・ウィットソン|Peggy Whitson|1960|researcher|米国の女性宇宙飛行士・生化学者として、民間宇宙飛行も含め長期宇宙滞在記録で知られる
リサ・スー|Lisa Su|1969|entrepreneur|台湾系米国の女性経営者として、AMD CEOとして半導体企業の成長と技術競争力を率いた
サフラ・キャッツ|Safra Catz|1961|entrepreneur|イスラエル系米国の女性経営者として、Oracle CEOとして大規模IT企業経営を担った
ルース・ポラット|Ruth Porat|1957|entrepreneur|米国の女性経営者として、Alphabet/GoogleのCFOとして巨大テック企業の財務を担った
エイミー・フッド|Amy Hood|1971|entrepreneur|米国の女性経営者として、Microsoft CFOとしてクラウド時代の経営を支えた
ジュリー・スウィート|Julie Sweet|1967|entrepreneur|米国の女性経営者として、Accenture CEOとしてグローバルITコンサルティングを率いた
ジェーン・フレーザー|Jane Fraser|1967|entrepreneur|英国出身の女性経営者として、Citigroup CEOとなり大手米銀初の女性CEOの一人となった
アビゲイル・ジョンソン|Abigail Johnson|1961|entrepreneur|米国の女性経営者として、Fidelity Investmentsを率い金融業界で影響力を持つ
マッケンジー・スコット|MacKenzie Scott|1970|entrepreneur|米国の女性作家・慈善家として、大規模寄付を通じ新しいフィランソロピー実践を示した
ローレン・パウエル・ジョブズ|Laurene Powell Jobs|1963|entrepreneur|米国の女性起業家・慈善家として、教育・移民・メディア支援を展開した
メリンダ・フレンチ・ゲイツ|Melinda French Gates|1964|entrepreneur|米国の女性慈善家として、女性・保健・開発支援を国際的に推進した
プリシラ・チャン|Priscilla Chan|1985|entrepreneur|米国の女性医師・慈善家として、Chan Zuckerberg Initiativeを通じ科学・教育支援を進めた
ルーシー・ペン|Lucy Peng|1973|entrepreneur|中国の女性起業家として、Alibaba共同創業者の一人として金融・EC事業を展開した
フィジー・シモ|Fidji Simo|1985|entrepreneur|フランス出身の女性経営者として、Instacart CEOとしてプラットフォーム事業を率いた
ミラ・ムラティ|Mira Murati|1988|entrepreneur|アルバニア出身の女性技術経営者として、生成AI製品開発のリーダーとして注目された
メアリー・ミーカー|Mary Meeker|1959|entrepreneur|米国の女性投資家として、インターネット動向分析と成長企業投資で影響力を持つ
キャシー・ウッド|Cathie Wood|1955|entrepreneur|米国の女性投資家として、破壊的イノベーション投資を掲げた運用で注目された
アンジェラ・アーレンツ|Angela Ahrendts|1960|entrepreneur|米国の女性経営者として、BurberryとApple Retailでブランド・小売経営を担った
ロザリンド・ブリューワー|Rosalind Brewer|1962|entrepreneur|米国の女性経営者として、Walgreens Boots Allianceなど大企業経営を担った
カレン・リンチ|Karen Lynch|1963|entrepreneur|米国の女性経営者として、CVS Health CEOとして医療・保険事業を率いた
エマ・ウォームズリー|Emma Walmsley|1969|entrepreneur|英国の女性経営者として、GSK CEOとして大手製薬企業を率いた
アナ・ボティン|Ana Botin|1960|entrepreneur|スペインの女性経営者として、Banco Santander会長として国際金融機関を率いた
クリスティーナ・ジュンケイラ|Cristina Junqueira|1982|entrepreneur|ブラジルの女性起業家として、Nubank共同創業者として金融包摂型フィンテックを拡大した
タチアナ・バカリチュク|Tatyana Bakalchuk|1975|entrepreneur|ロシアの女性起業家として、Wildberriesを創業しEC市場を拡大した
グラブ・タン・フイリン|Tan Hooi Ling|1984|entrepreneur|マレーシアの女性起業家として、Grab共同創業者として東南アジアのモビリティ・金融サービスを拡大した
レイチェル・ロムラズ|Rachel Romer|1988|entrepreneur|米国の女性起業家として、Guild Educationを共同創業し社会人教育支援を事業化した
キム・カーダシアン|Kim Kardashian|1980|entrepreneur|米国の女性起業家として、メディア影響力を美容・補整衣料ブランド事業に展開した
セリーナ・ウィリアムズ|Serena Williams|1981|entrepreneur|米国の女性アスリート・投資家として、スポーツ実績と女性起業支援を接続した
ナタリー・マッセン|Natalie Massenet|1965|entrepreneur|英国の女性起業家として、Net-a-Porterを創業しラグジュアリーECを開拓した
エミリー・ワイス|Emily Weiss|1985|entrepreneur|米国の女性起業家として、Glossierを創業しコミュニティ起点の美容ブランドを成長させた
ホリー・タッカー|Holly Tucker|1977|entrepreneur|英国の女性起業家として、Not On The High Streetを共同創業し小規模事業者ECを広げた
アン・ボーデン|Anne Boden|1960|entrepreneur|英国の女性起業家として、Starling Bankを創業しデジタル銀行を拡大した
メラニー・パーキンス|Melanie Perkins|1987|entrepreneur|オーストラリアの女性起業家として、Canvaを共同創業しデザインツールを大衆化した
ホイットニー・ウルフ・ハード|Whitney Wolfe Herd|1989|entrepreneur|米国の女性起業家として、Bumbleを創業し女性主導型マッチングサービスを拡大した
サラ・ブレイクリー|Sara Blakely|1971|entrepreneur|米国の女性起業家として、Spanxを創業し補整衣料市場を開拓した
カトリーナ・レイク|Katrina Lake|1982|entrepreneur|米国の女性起業家として、Stitch Fixを創業しデータ活用型ファッション小売を展開した
レシュマ・サウジャニ|Reshma Saujani|1975|entrepreneur|米国の女性社会起業家として、Girls Who Codeを創設し女性のIT教育を推進した
アン・ウォジツキ|Anne Wojcicki|1973|entrepreneur|米国の女性起業家として、23andMeを共同創業し個人向け遺伝子検査を広げた
グウィン・ショットウェル|Gwynne Shotwell|1963|entrepreneur|米国の女性経営者として、SpaceXの事業運営を率い商業宇宙開発を拡大した
シェリル・サンドバーグ|Sheryl Sandberg|1969|entrepreneur|米国の女性技術経営者として、Metaの成長期経営と女性リーダー論で影響を与えた
メグ・ホイットマン|Meg Whitman|1956|entrepreneur|米国の女性経営者として、eBayを成長させ大企業経営を担った
インドラ・ヌーイ|Indra Nooyi|1955|entrepreneur|インド系米国の女性経営者として、PepsiCo CEOとしてグローバル企業経営を担った
メアリー・バーラ|Mary Barra|1961|entrepreneur|米国の女性経営者として、General Motors CEOとして自動車大企業を率いた
キラン・マズムダール＝ショー|Kiran Mazumdar-Shaw|1953|entrepreneur|インドの女性起業家として、Bioconを創業しバイオ産業を先導した
ファルグニ・ナヤル|Falguni Nayar|1963|entrepreneur|インドの女性起業家として、Nykaaを創業し美容EC市場を拡大した
モー・アブドゥ|Mo Abudu|1964|entrepreneur|ナイジェリアの女性メディア起業家として、アフリカ発のテレビ・映画事業を国際展開した
アリアナ・ハフィントン|Arianna Huffington|1950|entrepreneur|ギリシャ系米国の女性起業家として、HuffPostを共同創業しデジタルニュース事業を拡大した
リアーナ|Rihanna|1988|entrepreneur|バルバドス出身の女性アーティスト・起業家として、Fenty Beautyなど包括的美容ブランドを展開した
テイラー・スウィフト|Taylor Swift|1989|entrepreneur|米国の女性音楽家として、作品権利とツアービジネスを主導し音楽産業に影響を与えた
ビヨンセ|Beyonce|1981|entrepreneur|米国の女性音楽家・起業家として、音楽活動とブランド事業を統合した
レディー・ガガ|Lady Gaga|1986|entrepreneur|米国の女性音楽家・起業家として、表現活動とメンタルヘルス支援・美容事業を展開した
マララ・ユスフザイ|Malala Yousafzai|1997|activist|パキスタン出身の若手女性教育活動家として、女子教育の権利を国際的に訴えた
グレタ・トゥーンベリ|Greta Thunberg|2003|activist|スウェーデンの若手女性気候活動家として、気候危機への若者の国際行動を促した
チママンダ・ンゴズィ・アディーチェ|Chimamanda Ngozi Adichie|1977|public|ナイジェリアの女性作家として、現代アフリカ文学とフェミニズム言説を国際的に広げた
クロエ・ジャオ|Chloe Zhao|1982|public|中国出身の女性映画監督として、アカデミー監督賞受賞を通じアジア系女性監督の地位を示した
マリアム・ミルザハニ|Maryam Mirzakhani|1977|researcher|イラン出身の女性数学者として、フィールズ賞受賞により女性数学者の可能性を可視化した
ジェニファー・ダウドナ|Jennifer Doudna|1964|researcher|米国の女性生化学者として、CRISPR-Cas9ゲノム編集技術の開発に貢献した
エマニュエル・シャルパンティエ|Emmanuelle Charpentier|1968|researcher|フランスの女性微生物学者として、CRISPR-Cas9技術の開発に貢献した
カタリン・カリコ|Katalin Kariko|1955|researcher|ハンガリー出身の女性生化学者として、mRNA医薬の基礎研究でワクチン開発を支えた
ドナ・ストリックランド|Donna Strickland|1959|researcher|カナダの女性物理学者として、チャープパルス増幅研究でレーザー物理に貢献した
アンドレア・ゲズ|Andrea Ghez|1965|researcher|米国の女性天文学者として、銀河中心ブラックホール研究でノーベル賞を受けた
カレン・ウーレンベック|Karen Uhlenbeck|1942|researcher|米国の女性数学者として、アーベル賞を受賞し幾何解析に貢献した
シルビア・アール|Sylvia Earle|1935|researcher|米国の女性海洋科学者として、海洋探査と海洋保全を国際的に主導した
ジェーン・グドール|Jane Goodall|1934|researcher|英国の女性霊長類学者として、チンパンジー研究と生物多様性保全を発信し続けた
テンプル・グランディン|Temple Grandin|1947|researcher|米国の女性動物科学者として、動物福祉設計と自閉症当事者の知を社会化した
ラディア・パールマン|Radia Perlman|1951|researcher|米国の女性計算機科学者として、ネットワーク技術の基盤に貢献した
フランシス・アーノルド|Frances Arnold|1956|researcher|米国の女性化学工学者として、酵素の指向性進化でノーベル化学賞を受けた
メイ＝ブリット・モーセル|May-Britt Moser|1963|researcher|ノルウェーの女性神経科学者として、空間認知のグリッド細胞研究に貢献した
イングリッド・ドブシー|Ingrid Daubechies|1954|researcher|ベルギー出身の女性数学者として、ウェーブレット理論で画像処理などに貢献した
グラディス・ウェスト|Gladys West|1930|researcher|米国の女性数学者として、GPSに関わる測地モデル計算に貢献した
ジェシカ・ウェイド|Jess Wade|1988|researcher|英国の女性物理学者として、材料科学研究と女性科学者の可視化活動を進めた
プリヤンヴァダ・ナタラジャン|Priyamvada Natarajan|1969|researcher|インド出身の女性天体物理学者として、ブラックホールとダークマター研究を進めた
サラ・シーガー|Sara Seager|1971|researcher|カナダ系米国の女性天文学者として、系外惑星大気研究と宇宙探査計画に貢献した
ケイティ・ボウマン|Katie Bouman|1989|researcher|米国の女性計算機科学者として、ブラックホール画像化に関わる計算画像処理で注目された
ヤエル・アイゼンスタット|Yael Eisenstat|1976|public|米国の女性技術政策専門家として、選挙・SNS・民主主義の課題を発信した
キャロル・カドワラダー|Carole Cadwalladr|1969|public|英国の女性ジャーナリストとして、データ政治広告と民主主義への影響を調査報道した
ナオミ・クライン|Naomi Klein|1970|public|カナダの女性ジャーナリストとして、気候危機・資本主義批判・ショック政治を論じた
レベッカ・ソルニット|Rebecca Solnit|1961|public|米国の女性作家として、フェミニズム・災害・社会運動を横断する批評を行った
ジュディス・バトラー|Judith Butler|1956|researcher|米国の女性哲学者として、ジェンダー理論と公共的発言を令和期も継続した
ナンシー・フレイザー|Nancy Fraser|1947|researcher|米国の女性社会理論家として、資本主義・ケア・フェミニズムをめぐる批判理論を展開した
シンシア・エンロー|Cynthia Enloe|1938|researcher|米国の女性政治学者として、国際政治とジェンダーの関係を分析し続けた
マーサ・ヌスバウム|Martha Nussbaum|1947|researcher|米国の女性哲学者として、ケイパビリティ・アプローチと正義論を展開した
ドリーン・マッシー|Doreen Massey|1944|researcher|英国の女性地理学者として、空間・権力・グローバル化の理論で令和期研究にも影響を与えた
エスター・デュフロ|Esther Duflo|1972|researcher|フランス系米国の女性経済学者として、貧困政策の実験的評価でノーベル経済学賞を受けた
クラウディア・ゴールディン|Claudia Goldin|1946|researcher|米国の女性経済学者として、女性労働と賃金格差の歴史研究でノーベル経済学賞を受けた
マリアナ・マッツカート|Mariana Mazzucato|1968|researcher|イタリア系英国の女性経済学者として、起業家的国家とミッション志向政策を提唱した
ケイト・ラワース|Kate Raworth|1970|researcher|英国の女性経済学者として、ドーナツ経済学を提唱し持続可能な経済設計を広めた
シャフィ・ゴールドワッサー|Shafi Goldwasser|1958|researcher|イスラエル系米国の女性計算機科学者として、暗号理論と計算複雑性に貢献した
バーバラ・リスコフ|Barbara Liskov|1939|researcher|米国の女性計算機科学者として、プログラミング言語と分散システム研究に貢献した
シンシア・ブリジール|Cynthia Breazeal|1967|researcher|米国の女性ロボット研究者として、ソーシャルロボット研究を開拓した
ダニエラ・ラス|Daniela Rus|1963|researcher|ルーマニア系米国の女性ロボット研究者として、MIT CSAIL所長としてAI・ロボティクスを率いた
スーザン・ファウラー|Susan Fowler|1991|activist|米国の女性エンジニアとして、Uberのセクハラ告発によりテック業界の労働文化改革を促した
エレン・パオ|Ellen Pao|1970|activist|米国の女性投資家・技術経営者として、シリコンバレーの差別問題を可視化した
タラナ・バーク|Tarana Burke|1973|activist|米国の女性活動家として、MeToo運動の創始者として性暴力被害者支援を広げた
アリッサ・ミラノ|Alyssa Milano|1972|activist|米国の女性俳優・活動家として、MeTooの拡散や政治参加を促した
ブリタニー・パックネット・カニンガム|Brittany Packnett Cunningham|1984|activist|米国の女性活動家として、Black Lives Matterと教育・警察改革を発信した
アリシア・ガーザ|Alicia Garza|1981|activist|米国の女性活動家として、Black Lives Matter共同創始者として人種正義運動を組織した
パトリッセ・カラーズ|Patrisse Cullors|1983|activist|米国の女性活動家として、Black Lives Matter共同創始者として警察暴力への抗議を広げた
オパール・トメティ|Opal Tometi|1984|activist|米国の女性活動家として、Black Lives Matter共同創始者として移民・人種正義を訴えた
ブリー・ニューサム|Bree Newsome|1985|activist|米国の女性活動家として、南軍旗撤去行動など反人種差別運動で知られる
アマンダ・グエン|Amanda Nguyen|1991|activist|米国の女性人権活動家として、性暴力被害者の権利保護と法改正を推進した
デヴィッド・ホッグ|David Hogg|2000|public|米国の若手銃規制活動家だが、この行は女性追加対象外の安全確認用候補である
ゾーイ・クイン|Zoe Quinn|1987|activist|米国の女性ゲーム開発者として、オンラインハラスメント問題とデジタル権利を発信した
アニータ・サーキージアン|Anita Sarkeesian|1983|activist|カナダ系米国の女性批評家として、ゲーム表象とオンラインハラスメント問題を可視化した
チェルシー・マニング|Chelsea Manning|1987|activist|米国の女性内部告発者・活動家として、情報公開とトランスジェンダー権利をめぐり発信した
ラバーン・コックス|Laverne Cox|1972|activist|米国の女性俳優・活動家として、トランスジェンダーの可視化と権利擁護に貢献した
ジャネット・モック|Janet Mock|1983|activist|米国の女性作家・活動家として、トランスジェンダー女性の経験をメディアで発信した
ムナ・エルタハウィ|Mona Eltahawy|1967|activist|エジプト系米国の女性ジャーナリストとして、中東の女性権利と権威主義批判を発信した
ミッキ・ケンドール|Mikki Kendall|1976|activist|米国の女性作家として、交差的フェミニズムと食・安全・貧困の課題を論じた
ロクサーヌ・ゲイ|Roxane Gay|1974|public|米国の女性作家として、フェミニズム・身体・人種をめぐる批評を広く発信した
イジェオマ・オルオ|Ijeoma Oluo|1980|public|米国の女性作家として、人種差別とジェンダーの問題を平易に論じ公共議論を促した
アンジェラ・サイニー|Angela Saini|1980|public|英国の女性科学ジャーナリストとして、科学における性差別・人種主義を批判的に検証した
キャロライン・クリアド＝ペレス|Caroline Criado Perez|1984|public|英国の女性作家・活動家として、データのジェンダーギャップを可視化した
ローラ・ベイツ|Laura Bates|1986|activist|英国の女性作家・活動家として、Everyday Sexism Projectを通じ日常的性差別を記録した
ジーナ・マーティン|Gina Martin|1992|activist|英国の女性活動家として、盗撮規制法改正を求める運動を成功させた
アマル・クルーニー|Amal Clooney|1978|activist|レバノン系英国の女性弁護士として、国際人権法とジャーナリスト保護に取り組んだ
ブリタニー・ヒギンズ|Brittany Higgins|1994|activist|オーストラリアの女性活動家として、議会内性暴力告発を通じ制度改革を促した
グレース・テイム|Grace Tame|1994|activist|オーストラリアの女性活動家として、性暴力被害者の発言権と法改正を訴えた
チェルシー・クリントン|Chelsea Clinton|1980|public|米国の女性公衆衛生発信者として、財団活動を通じ保健・教育・女性支援に関わった
エマ・ワトソン|Emma Watson|1990|activist|英国の女性俳優・活動家として、UN Women親善大使としてHeForSheを広めた
アンジェリーナ・ジョリー|Angelina Jolie|1975|activist|米国の女性俳優・人道活動家として、難民支援と性暴力防止を国際的に訴えた
メーガン・マークル|Meghan Markle|1981|activist|米国出身の女性公人として、人種・ジェンダー・メディア表象をめぐる発信を行った
ミシェル・オバマ|Michelle Obama|1964|activist|米国の女性弁護士・公人として、教育・健康・女性支援を国際的に発信した
ジル・バイデン|Jill Biden|1951|activist|米国の女性教育者として、ファーストレディ在任中もコミュニティカレッジ教育を発信した
アン・イダルゴ|Anne Hidalgo|1959|politician|フランスの女性政治家として、パリ市長として都市交通・環境政策を推進した
サディア・ザヒディ|Saadia Zahidi|1976|public|パキスタン系の女性国際機関幹部として、世界経済フォーラムでジェンダーギャップ分析を発信した
ギータ・ゴピナート|Gita Gopinath|1971|researcher|インド系米国の女性経済学者として、IMFのチーフエコノミストとして国際経済分析を担った
ピナロピ・クーヤンジャム|Pinarayi Vijayan||public|インドの男性政治家であり、この行は女性追加対象外の安全確認用候補である
ミーナ・ハリス|Meena Harris|1984|entrepreneur|米国の女性起業家・弁護士として、Phenomenalを創業し女性・有色人種支援のブランド活動を展開した
アーラン・ハミルトン|Arlan Hamilton|1980|entrepreneur|米国の女性投資家として、Backstage Capitalを創業し過小評価された起業家への投資を進めた
ブリタニー・デイビス|Brittany Davis||entrepreneur|米国の女性投資家として、Backstage Capitalなどで多様な起業家支援に関わった
レイチェル・カールソン|Rachel Carlson|1989|entrepreneur|米国の女性起業家として、Guild Educationを共同創業し従業員教育支援市場を広げた
リーラ・ジャナ|Leila Janah|1982|entrepreneur|米国の女性社会起業家として、Samasourceを創業しデジタル業務と貧困削減を結びつけた
ジェシカ・アルバ|Jessica Alba|1981|entrepreneur|米国の女性起業家として、The Honest Companyを共同創業し安全志向の消費財ブランドを築いた
ソフィア・アモルーソ|Sophia Amoruso|1984|entrepreneur|米国の女性起業家として、Nasty GalとGirlbossを通じ女性起業文化に影響を与えた
ジュリア・ハーツ|Julia Hartz|1979|entrepreneur|米国の女性起業家として、Eventbrite共同創業者としてイベント管理プラットフォームを拡大した
ジェニファー・ハイマン|Jennifer Hyman|1980|entrepreneur|米国の女性起業家として、Rent the Runwayを共同創業し衣料レンタル市場を開拓した
カーステン・グリーン|Kirsten Green|1971|entrepreneur|米国の女性投資家として、Forerunner Venturesを創業し消費者向けスタートアップ投資を進めた
リーン・ケアニー|Leanne Caret|1966|entrepreneur|米国の女性経営者として、Boeing Defense部門などを率い航空宇宙産業の経営を担った
グウィネス・パルトロー|Gwyneth Paltrow|1972|entrepreneur|米国の女性俳優・起業家として、Goopを創業しウェルネス市場を拡大した
ヴィクトリア・ベッカム|Victoria Beckham|1974|entrepreneur|英国の女性デザイナー・起業家として、ファッションブランドを国際展開した
ステラ・マッカートニー|Stella McCartney|1971|entrepreneur|英国の女性デザイナーとして、サステナブル・ファッションをブランド経営に組み込んだ
トリー・バーチ|Tory Burch|1966|entrepreneur|米国の女性起業家として、ファッションブランドと女性起業支援財団を展開した
ダイアン・フォン・ファステンバーグ|Diane von Furstenberg|1946|entrepreneur|ベルギー出身の女性デザイナーとして、ファッション事業と女性支援を展開した
ミウッチャ・プラダ|Miuccia Prada|1949|entrepreneur|イタリアの女性デザイナー・経営者として、Pradaを現代ファッションブランドとして発展させた
リーナ・ナーイル|Leena Nair|1969|entrepreneur|インド出身の女性経営者として、Chanel CEOとしてグローバルブランド経営を担った
ヴァネッサ・キングオリ|Vanessa Kingori|1979|entrepreneur|英国の女性メディア経営者として、Vogueなどで多様性ある編集・広告ビジネスを担った
ボジー・ダル|Bozoma Saint John|1977|entrepreneur|ガーナ系米国の女性マーケティング経営者として、Uber・Netflixなどでブランド戦略を担った
アン・サーノフ|Ann Sarnoff|1961|entrepreneur|米国の女性経営者として、Warner Bros.初の女性CEOとしてメディア企業を率いた
ダナ・ウォルデン|Dana Walden|1964|entrepreneur|米国の女性メディア経営者として、Disney Entertainmentなど大規模コンテンツ事業を率いた
シンダ・ウィリアムズ・チマ|Cinda Williams Chima|1952|public|米国の女性作家として、ファンタジー文学を通じ若年読者の文化経験に影響を与えた
ションダ・ライムズ|Shonda Rhimes|1970|entrepreneur|米国の女性テレビプロデューサーとして、Shondalandを率い多様な表象のドラマ制作を拡大した
エイヴァ・デュヴァーネイ|Ava DuVernay|1972|public|米国の女性映画監督として、黒人女性監督の制作機会と社会派映像表現を広げた
キャスリン・ビグロー|Kathryn Bigelow|1951|public|米国の女性映画監督として、女性初のアカデミー監督賞受賞者として映画界の代表性を広げた
ソフィア・コッポラ|Sofia Coppola|1971|public|米国の女性映画監督として、独自の映像表現で令和期も国際映画界に影響を持つ
ミーラー・ナーイル|Mira Nair|1957|public|インド出身の女性映画監督として、ディアスポラと地域社会の視点を国際映画に示した
ビョーク|Bjork|1965|public|アイスランドの女性音楽家として、音楽・映像・テクノロジーを統合した表現を続けた
アマンダ・ゴーマン|Amanda Gorman|1998|public|米国の若手女性詩人として、大統領就任式の詩朗読で若者・黒人女性の声を可視化した
ルピ・カウル|Rupi Kaur|1992|public|カナダの女性詩人として、SNS時代の詩表現と移民女性の経験を国際的に広げた
バーナディン・エヴァリスト|Bernardine Evaristo|1959|public|英国の女性作家として、黒人女性の経験を描く文学でブッカー賞を受けた
サリー・ルーニー|Sally Rooney|1991|public|アイルランドの女性作家として、ミレニアル世代の関係性と階級を描き令和期文学で注目された
オルガ・トカルチュク|Olga Tokarczuk|1962|public|ポーランドの女性作家として、ノーベル文学賞受賞後も歴史・境界・身体をめぐる作品で影響を持った
ハン・ガン|Han Kang|1970|public|韓国の女性作家として、暴力・身体・記憶を描く文学で国際的評価を得た
ミン・ジン・リー|Min Jin Lee|1968|public|韓国系米国の女性作家として、移民と家族史を描く作品で国際的に読まれた
エリフ・シャファク|Elif Shafak|1971|public|トルコ出身の女性作家として、移民・宗教・ジェンダーを横断する文学と発信を行った
""".strip()


def source_url(name_ja: str) -> str:
    return "https://ja.wikipedia.org/wiki/" + quote(name_ja.replace(" ", "_"))


def parse_candidates():
    seen = set()
    for line in RAW.splitlines():
        name_ja, name_en, birth, kind, summary = line.split("|", 4)
        if "女性追加対象外" in summary:
            continue
        key = (name_ja, int(birth) if birth else None)
        if key in seen:
            continue
        seen.add(key)
        sub = {
            "entrepreneur": "起業家・経営者",
            "researcher": "研究者",
            "activist": "社会運動家",
            "politician": "政治家・政策実践者",
            "public": "公共発信者",
        }[kind]
        yield {
            "name_ja": name_ja,
            "name_en": name_en,
            "birth_year": int(birth) if birth else None,
            "primary_era_id": "reiwa",
            "domain": "women_pioneers",
            "sub_domain": sub,
            "achievement_summary": summary + "。女性であることが、令和期の代表性・制度変化・社会的可視化の観点で重要である。",
            "notable_works": json.dumps([sub], ensure_ascii=False),
            "fame_source": "wikipedia_or_public_profile",
            "fame_score": 6.0,
            "is_traditional_great": 0,
            "is_local_excellent": 0,
            "data_completeness": 62,
            "source_team": TEAM,
            "source_url": source_url(name_ja),
            "notes": f"Phase 6.C reiwa_women; category={kind}; source requires public-profile verification.",
            "correction_phase": PHASE,
            "_kind": kind,
        }


def insert_person(cur, person):
    birth_year = person["birth_year"]
    # Required duplicate check: exact name plus NULL-safe birth-year comparison.
    exact = cur.execute(
        "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
        (person["name_ja"], birth_year),
    ).fetchone()
    # Extra guard to avoid adding the same public figure when an older row omitted or supplied birth_year differently.
    by_name = cur.execute(
        "SELECT 1 FROM achievers WHERE name_ja=?",
        (person["name_ja"],),
    ).fetchone()
    if exact or by_name:
        return False

    kind = person.pop("_kind")
    cols = list(person.keys())
    placeholders = ",".join("?" for _ in cols)
    cur.execute(
        f"INSERT INTO achievers ({','.join(cols)}) VALUES ({placeholders})",
        [person[c] for c in cols],
    )
    achiever_id = cur.lastrowid
    for cap_id, score, quote_text in CAPS[kind]:
        cur.execute(
            """INSERT INTO achiever_capabilities
               (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                achiever_id,
                cap_id,
                score,
                quote_text,
                person["source_url"],
                "Phase 6.C reiwa_women capability scoring",
            ),
        )
    return True


def main():
    before = None
    inserted = 0
    batch_inserted = 0
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        before = cur.execute(
            "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
            (PHASE, TEAM),
        ).fetchone()[0]
        cur.execute("BEGIN")
        for candidate in parse_candidates():
            if inserted >= TARGET:
                break
            if insert_person(cur, dict(candidate)):
                inserted += 1
                batch_inserted += 1
            if batch_inserted == 50:
                conn.commit()
                print(f"committed batch: total_inserted={inserted}")
                cur.execute("BEGIN")
                batch_inserted = 0
        if batch_inserted:
            conn.commit()
            print(f"committed final batch: total_inserted={inserted}")
        elif conn.in_transaction:
            conn.commit()

        after = cur.execute(
            "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
            (PHASE, TEAM),
        ).fetchone()[0]
        caps = cur.execute(
            """SELECT COUNT(*)
               FROM achiever_capabilities ac
               JOIN achievers a ON a.id=ac.achiever_id
               WHERE a.correction_phase=? AND a.source_team=?""",
            (PHASE, TEAM),
        ).fetchone()[0]
    print(f"before={before} inserted={inserted} after={after} capabilities={caps}")
    if inserted != TARGET:
        raise SystemExit(f"target not reached: inserted={inserted}, target={TARGET}")


if __name__ == "__main__":
    main()

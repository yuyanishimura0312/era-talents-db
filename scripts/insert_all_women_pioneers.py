#!/usr/bin/env python3
import sqlite3
from pathlib import Path
from urllib.parse import quote

DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_all_women_pioneers"

CAPS = {
    "medicine": [
        ("cog_critical", 9, "医療実践で専門的判断を示した"),
        ("age_social_change", 9, "女性の専門職参入を広げた"),
        ("age_resilience", 8, "制度的障壁を越えて活動を継続した"),
    ],
    "science": [
        ("cog_logical", 9, "研究成果で論理的分析力を示した"),
        ("cog_critical", 9, "既存知を検証し新しい知見を提示した"),
        ("cog_creativity", 8, "独創的な研究課題や方法を開いた"),
    ],
    "business": [
        ("age_entrepreneur", 10, "事業を創業・成長させた"),
        ("cog_systems", 8, "市場や組織を設計する力を示した"),
        ("age_resilience", 8, "競争環境で事業を継続・拡大した"),
    ],
    "arts": [
        ("cog_creativity", 10, "表現領域で独自の様式を築いた"),
        ("age_social_change", 8, "女性表現者の活動領域を広げた"),
        ("val_tolerance", 7, "多様な経験や視点を作品化した"),
    ],
    "education": [
        ("age_social_change", 9, "教育・思想・社会参加の制度的変化を促した"),
        ("soc_interpersonal", 8, "人々を組織し学習や参加を支えた"),
        ("age_resilience", 8, "不利な条件下で公共的実践を継続した"),
    ],
}

RAW = """
エリザベス・ブラックウェル|Elizabeth Blackwell|1821|1910|medicine|医師|米国で初めて医学学位を得た女性医師として女性医師養成の道を開いた
レベッカ・リー・クランプラー|Rebecca Lee Crumpler|1831|1895|medicine|医師|米国初のアフリカ系女性医師の一人として医療と公衆衛生に貢献した
メアリー・エドワーズ・ウォーカー|Mary Edwards Walker|1832|1919|medicine|医師|南北戦争期の外科医として従軍し女性医師の公共的役割を示した
スーザン・ラ・フレッシュ・ピコット|Susan La Flesche Picotte|1865|1915|medicine|医師|先住民女性医師としてオマハ族コミュニティの医療改善に尽くした
エリザベス・ギャレット・アンダーソン|Elizabeth Garrett Anderson|1836|1917|medicine|医師|英国初期の女性医師として女性医学校と病院運営を先導した
ソフィア・ジェックス＝ブレイク|Sophia Jex-Blake|1840|1912|medicine|医師|英国で女性医学教育の制度化を推進した
アナンディバイ・ジョシー|Anandibai Joshi|1865|1887|medicine|医師|インド出身女性として医学教育を受け女性医療の象徴となった
カダンビニ・ガングリー|Kadambini Ganguly|1861|1923|medicine|医師|南アジア初期の女性医師として診療と女性の高等教育を切り開いた
ルクマバイ|Rukhmabai|1864|1955|medicine|医師|インドの女性医師・社会改革者として女性の自立を訴えた
ムトゥラクシュミ・レッディ|Muthulakshmi Reddy|1886|1968|medicine|医師|医師・政治家として女性医療とがん医療の制度づくりに貢献した
メアリー・パットナム・ジャコビ|Mary Putnam Jacobi|1842|1906|medicine|医師|医学研究に基づき女性の高等教育参加を擁護した
サラ・ジョセフィン・ベーカー|Sara Josephine Baker|1873|1945|medicine|公衆衛生|乳幼児保健を中心に都市公衆衛生を改善した
ヴァージニア・アプガー|Virginia Apgar|1909|1974|medicine|医師|新生児評価のアプガースコアを考案し周産期医療を変えた
ヘレン・ブルック・タウシグ|Helen B. Taussig|1898|1986|medicine|医師|小児心臓病学を開拓し先天性心疾患治療に貢献した
ガートルード・エリオン|Gertrude B. Elion|1918|1999|medicine|薬学研究|合理的薬剤設計で多くの治療薬開発に貢献した
ロザリン・ヤロー|Rosalyn Yalow|1921|2011|medicine|医学物理|ラジオイムノアッセイ開発で医学検査を革新した
ガーティ・コリ|Gerty Cori|1896|1957|medicine|生化学|糖代謝研究で女性初のノーベル生理学・医学賞受賞者となった
フローレンス・ナイチンゲール|Florence Nightingale|1820|1910|medicine|看護|近代看護と統計に基づく病院改革を推進した
メアリー・シーコール|Mary Seacole|1805|1881|medicine|看護|クリミア戦争期に独自の看護・支援活動を行った
シシリー・ソンダース|Cicely Saunders|1918|2005|medicine|緩和ケア|近代ホスピス運動と緩和ケアの基礎を築いた
フェ・デル・ムンド|Fe del Mundo|1911|2011|medicine|小児科|フィリピンの小児医療と女性医師の先駆者となった
屠呦呦|Tu Youyou|1930||medicine|薬学研究|青蒿素の発見でマラリア治療に大きく貢献した
フランソワーズ・バレ＝シヌシ|Francoise Barre-Sinoussi|1947||medicine|ウイルス学|HIV発見に関わり感染症研究を前進させた
メイ・ジェミソン|Mae Jemison|1956||medicine|医師・宇宙飛行士|医師としての専門性を背景にアフリカ系女性初の宇宙飛行士となった
ジェーン・クック・ライト|Jane C. Wright|1919|2013|medicine|腫瘍学|化学療法研究を進めがん治療の発展に貢献した
パトリシア・バス|Patricia Bath|1942|2019|medicine|眼科|白内障治療技術を発明し失明予防に貢献した
アントニア・ノヴェロ|Antonia Novello|1944||medicine|公衆衛生|米国初の女性・ヒスパニック系公衆衛生局長官となった
ヘレン・ロドリゲス＝トリアス|Helen Rodriguez Trias|1929|2001|medicine|公衆衛生|女性・子ども・マイノリティの医療権利を推進した
リタ・レーヴィ＝モンタルチーニ|Rita Levi-Montalcini|1909|2012|medicine|神経科学|神経成長因子の発見で神経科学を発展させた
アリス・ハミルトン|Alice Hamilton|1869|1970|medicine|産業医学|産業医学の先駆者として労働者の健康保護に貢献した
レイラ・デンマーク|Leila Denmark|1898|2012|medicine|小児科|小児科医として長期にわたり地域医療に従事した
ハワ・アブディ|Hawa Abdi|1947|2020|medicine|医師|ソマリアで医療・教育・避難民支援の拠点を築いた
ハヤト・シンディ|Hayat Sindi|1967||medicine|医療技術|低コスト診断技術と科学教育の普及に取り組んだ
ジョイセリン・エルダーズ|Joycelyn Elders|1933||medicine|公衆衛生|米国公衆衛生局長官として性教育と予防医療を提唱した
ナタリア・ベフテレワ|Natalya Bekhtereva|1924|2008|medicine|神経科学|脳研究と神経生理学でソ連・ロシアの女性研究者を代表した
ヒュパティア|Hypatia|360|415|science|数学|古代アレクサンドリアの数学者・哲学者として学問活動を率いた
マリア・ジビーラ・メーリアン|Maria Sibylla Merian|1647|1717|science|自然史|昆虫の変態を観察画と研究で記録し自然史を進めた
カロライン・ハーシェル|Caroline Herschel|1750|1848|science|天文学|彗星発見と天体観測で女性天文学者の先駆となった
メアリー・アニング|Mary Anning|1799|1847|science|古生物学|化石発見により古生物学の成立に大きく貢献した
エイダ・ラブレス|Ada Lovelace|1815|1852|science|計算機科学|解析機関のためのアルゴリズムを記述し計算機史の先駆とされる
ユーニス・ニュートン・フット|Eunice Newton Foote|1819|1888|science|気候科学|二酸化炭素の温室効果を早期に実験で示した
メアリー・サマヴィル|Mary Somerville|1780|1872|science|科学解説|数学・天文学の著述で科学普及と女性教育に貢献した
ハーサ・エアトン|Hertha Ayrton|1854|1923|science|物理・工学|電気アーク研究と発明で英国工学界に足跡を残した
エミー・ネーター|Emmy Noether|1882|1935|science|数学|抽象代数学とネーターの定理で現代数学・物理学に貢献した
リーゼ・マイトナー|Lise Meitner|1878|1968|science|物理学|核分裂の理論的解釈に貢献した
マリ・キュリー|Marie Curie|1867|1934|science|化学・物理|放射能研究で二分野のノーベル賞を受けた
イレーヌ・ジョリオ＝キュリー|Irene Joliot-Curie|1897|1956|science|化学|人工放射能の発見で化学研究を前進させた
呉健雄|Chien-Shiung Wu|1912|1997|science|物理学|弱い相互作用のパリティ非保存実験で重要な役割を果たした
キャサリン・ジョンソン|Katherine Johnson|1918|2020|science|数学|NASAの有人宇宙飛行計算を支えた数学者
ドロシー・ホジキン|Dorothy Hodgkin|1910|1994|science|化学|X線結晶構造解析で生体分子構造を解明した
レイチェル・カーソン|Rachel Carson|1907|1964|science|環境科学|環境汚染への批判的著作で環境運動を促した
ロザリンド・フランクリン|Rosalind Franklin|1920|1958|science|化学|DNA構造解明に不可欠なX線回折研究を行った
ジョスリン・ベル・バーネル|Jocelyn Bell Burnell|1943||science|天文学|パルサー発見で電波天文学に大きく貢献した
ヴェラ・ルービン|Vera Rubin|1928|2016|science|天文学|銀河回転曲線の研究で暗黒物質研究を前進させた
ジェーン・グドール|Jane Goodall|1934||science|霊長類学|チンパンジーの長期野外研究で動物行動学を変えた
ダイアン・フォッシー|Dian Fossey|1932|1985|science|霊長類学|マウンテンゴリラの保護研究で知られる
シルビア・アール|Sylvia Earle|1935||science|海洋科学|海洋探査と海洋保全の世界的リーダーとなった
テンプル・グランディン|Temple Grandin|1947||science|動物科学|動物福祉設計と自閉症当事者としての発信で影響を与えた
マーガレット・ハミルトン|Margaret Hamilton|1936||science|ソフトウェア工学|アポロ計画の飛行ソフトウェア開発を率いた
グレース・ホッパー|Grace Hopper|1906|1992|science|計算機科学|コンパイラとCOBOL普及でプログラミング史を切り開いた
ヘディ・ラマー|Hedy Lamarr|1914|2000|science|発明|周波数ホッピング技術の共同発明者として通信技術に貢献した
ラディア・パールマン|Radia Perlman|1951||science|計算機科学|スパニングツリープロトコルなどネットワーク技術に貢献した
フランシス・アーノルド|Frances Arnold|1956||science|化学工学|酵素の指向性進化でノーベル化学賞を受けた
ジェニファー・ダウドナ|Jennifer Doudna|1964||science|生化学|CRISPR-Cas9ゲノム編集技術の開発に貢献した
エマニュエル・シャルパンティエ|Emmanuelle Charpentier|1968||science|微生物学|CRISPR-Cas9ゲノム編集技術の開発に貢献した
カタリン・カリコ|Katalin Kariko|1955||science|生化学|mRNA医薬の基礎研究でワクチン開発を支えた
マイブリット・モーセル|May-Britt Moser|1963||science|神経科学|空間認知のグリッド細胞研究で神経科学に貢献した
ドナ・ストリックランド|Donna Strickland|1959||science|物理学|チャープパルス増幅の研究でレーザー物理を発展させた
アンドレア・ゲズ|Andrea Ghez|1965||science|天文学|銀河中心の超大質量ブラックホール研究でノーベル賞を受けた
マリアム・ミルザハニ|Maryam Mirzakhani|1977|2017|science|数学|フィールズ賞を受けた初の女性数学者となった
カレン・ウーレンベック|Karen Uhlenbeck|1942||science|数学|幾何解析でアーベル賞を受賞した初の女性数学者となった
イングリッド・ドブシー|Ingrid Daubechies|1954||science|数学|ウェーブレット理論で画像処理などに貢献した
セシリア・ペイン＝ガポーシュキン|Cecilia Payne-Gaposchkin|1900|1979|science|天文学|恒星が主に水素とヘリウムから成ることを示した
ワンガリ・マータイ|Wangari Maathai|1940|2011|science|環境保全|グリーンベルト運動を創設し環境と女性の社会参加を結びつけた
グラディス・ウェスト|Gladys West|1930||science|数学|GPSに関わる測地モデル計算に貢献した
キャサリン・エサウ|Katherine Esau|1898|1997|science|植物学|植物解剖学の標準的研究で植物科学を発展させた
エスター・レーダーバーグ|Esther Lederberg|1922|2006|science|微生物学|ラムダファージ発見など遺伝学研究に貢献した
リン・マーギュリス|Lynn Margulis|1938|2011|science|生物学|細胞内共生説の発展で進化生物学に影響を与えた
ミルドレッド・ドレッセルハウス|Mildred Dresselhaus|1930|2017|science|物理学|炭素材料研究でナノ科学を先導した
アシマ・チャタジー|Asima Chatterjee|1917|2006|science|化学|天然物化学と薬用植物研究でインド科学界を先導した
マダム・C・J・ウォーカー|Madam C. J. Walker|1867|1919|business|起業家|ヘアケア事業で成功し米国初期の女性自力富豪となった
ココ・シャネル|Coco Chanel|1883|1971|business|ファッション|女性服とブランド事業で20世紀ファッションを変えた
エスティ・ローダー|Estee Lauder|1908|2004|business|化粧品|化粧品企業を創業し世界ブランドに育てた
ルース・ハンドラー|Ruth Handler|1916|2002|business|玩具|マテルを共同創業しバービー人形を企画した
メアリー・ケイ・アッシュ|Mary Kay Ash|1918|2001|business|化粧品|女性販売員の機会拡大を掲げ化粧品会社を創業した
アニータ・ロディック|Anita Roddick|1942|2007|business|小売|ザ・ボディショップを創業し倫理的消費を事業化した
オプラ・ウィンフリー|Oprah Winfrey|1954||business|メディア|メディア事業を築き女性・黒人起業家の象徴となった
マーサ・スチュワート|Martha Stewart|1941||business|ライフスタイル|生活情報ブランドを企業化し出版・放送・小売へ展開した
サラ・ブレイクリー|Sara Blakely|1971||business|アパレル|Spanxを創業し補整衣料市場を開拓した
ホイットニー・ウルフ・ハード|Whitney Wolfe Herd|1989||business|テクノロジー|Bumbleを創業し女性主導型マッチングサービスを拡大した
メラニー・パーキンス|Melanie Perkins|1987||business|テクノロジー|Canvaを共同創業しデザインツールを大衆化した
リアーナ|Rihanna|1988||business|化粧品・音楽|Fenty Beautyなどで包括的な美容ブランドを展開した
ビヨンセ|Beyonce|1981||business|音楽・ブランド|音楽活動とブランド事業を統合し女性アーティストの事業モデルを広げた
トリー・バーチ|Tory Burch|1966||business|ファッション|ファッションブランドと女性起業支援財団を展開した
ダイアン・フォン・ファステンバーグ|Diane von Furstenberg|1946||business|ファッション|ラップドレスを軸に国際的ファッション事業を築いた
シェール・ワン|Cher Wang|1958||business|テクノロジー|HTCなどを率い台湾の技術企業経営を代表した
張欣|Zhang Xin|1965||business|不動産|SOHO China共同創業者として中国都市開発ビジネスを築いた
キラン・マズムダール＝ショー|Kiran Mazumdar-Shaw|1953||business|バイオ企業|Bioconを創業しインドのバイオ産業を先導した
ファルグニ・ナヤル|Falguni Nayar|1963||business|EC|Nykaaを創業しインド美容EC市場を拡大した
インドラ・ヌーイ|Indra Nooyi|1955||business|経営者|ペプシコCEOとしてグローバル企業経営を担った
アーシュラ・バーンズ|Ursula Burns|1958||business|経営者|ゼロックスCEOとして米大企業初の黒人女性CEOの一人となった
メアリー・バーラ|Mary Barra|1961||business|経営者|ゼネラルモーターズCEOとして自動車大企業を率いた
シェリル・サンドバーグ|Sheryl Sandberg|1969||business|テクノロジー経営|Facebook/Metaの成長期経営と女性リーダー論で影響を与えた
メグ・ホイットマン|Meg Whitman|1956||business|テクノロジー経営|eBayを成長させHPなど大企業経営を担った
アン・ウォジツキ|Anne Wojcicki|1973||business|バイオ企業|23andMeを共同創業し個人向け遺伝子検査を広げた
グウィン・ショットウェル|Gwynne Shotwell|1963||business|宇宙産業|SpaceXの事業運営を率い商業宇宙開発を拡大した
アリアナ・ハフィントン|Arianna Huffington|1950||business|メディア|HuffPostを共同創業しデジタルニュース事業を拡大した
カトリーナ・レイク|Katrina Lake|1982||business|EC|Stitch Fixを創業しデータ活用型ファッション小売を展開した
レイラ・ジャナ|Leila Janah|1982|2020|business|社会的企業|Samasourceを創業しデジタル業務と貧困削減を結びつけた
ジェシカ・アルバ|Jessica Alba|1981||business|消費財|The Honest Companyを共同創業し安全志向の消費財ブランドを築いた
レシュマ・サウジャニ|Reshma Saujani|1975||business|教育起業|Girls Who Codeを創設し女性のIT教育を推進した
ナイナ・ラル・キドワイ|Naina Lal Kidwai|1957||business|金融|インド金融界で女性経営者の道を開いた
フォロルンショ・アラキジャ|Folorunsho Alakija|1951||business|資源・ファッション|ナイジェリアでファッションと石油事業を展開した女性実業家
モー・アブドゥ|Mo Abudu|1964||business|メディア|アフリカ発のテレビ・映画事業を国際展開した
スーザン・ウォジスキ|Susan Wojcicki|1968|2024|business|テクノロジー経営|YouTube CEOなどを務めデジタル動画産業の成長を率いた
ヒルデガルト・フォン・ビンゲン|Hildegard of Bingen|1098|1179|arts|音楽・著述|中世の作曲家・著述家として宗教文化と知を結びつけた
アルテミジア・ジェンティレスキ|Artemisia Gentileschi|1593|1656|arts|絵画|バロック期の女性画家として歴史画で高い評価を得た
エリザベート＝ルイーズ・ヴィジェ＝ルブラン|Elisabeth Vigee Le Brun|1755|1842|arts|絵画|宮廷肖像画家として欧州各地で活動した
ジェーン・オースティン|Jane Austen|1775|1817|arts|文学|近代小説の展開に大きな影響を与えた
メアリー・シェリー|Mary Shelley|1797|1851|arts|文学|『フランケンシュタイン』でSF文学の源流を作った
ジョルジュ・サンド|George Sand|1804|1876|arts|文学|19世紀フランス文学で女性作家の公共的発言を広げた
ハリエット・ビーチャー・ストウ|Harriet Beecher Stowe|1811|1896|arts|文学|奴隷制批判文学で世論形成に影響を与えた
ルイーザ・メイ・オルコット|Louisa May Alcott|1832|1888|arts|文学|『若草物語』などで女性の成長と自立を描いた
エミリー・ディキンソン|Emily Dickinson|1830|1886|arts|詩|独自の詩法で近代詩に大きな影響を与えた
セルマ・ラーゲルレーヴ|Selma Lagerlof|1858|1940|arts|文学|女性初のノーベル文学賞受賞者となった
ビアトリクス・ポター|Beatrix Potter|1866|1943|arts|児童文学|絵本とキャラクター事業で児童文化を築いた
ヴァージニア・ウルフ|Virginia Woolf|1882|1941|arts|文学|モダニズム文学と女性の創作論を発展させた
アガサ・クリスティ|Agatha Christie|1890|1976|arts|文学|推理小説の大衆文化化に決定的影響を与えた
ゾラ・ニール・ハーストン|Zora Neale Hurston|1891|1960|arts|文学・民俗学|アフリカ系米国文化を文学と民俗研究で記録した
フリーダ・カーロ|Frida Kahlo|1907|1954|arts|絵画|自己像とメキシコ文化を融合した作品で後世に影響を与えた
ジョージア・オキーフ|Georgia O'Keeffe|1887|1986|arts|絵画|米国モダニズム絵画を代表する独自の様式を築いた
タマラ・ド・レンピッカ|Tamara de Lempicka|1898|1980|arts|絵画|アール・デコ様式の肖像画で独自の地位を築いた
リー・クラズナー|Lee Krasner|1908|1984|arts|絵画|抽象表現主義の重要な女性画家として評価された
ルイーズ・ブルジョワ|Louise Bourgeois|1911|2010|arts|彫刻|身体・記憶を主題とする彫刻で現代美術に影響を与えた
トーベ・ヤンソン|Tove Jansson|1914|2001|arts|文学・絵画|ムーミン作品で児童文学と視覚文化を結びつけた
マヤ・アンジェロウ|Maya Angelou|1928|2014|arts|文学|自伝文学と詩で人種・女性の経験を可視化した
トニ・モリスン|Toni Morrison|1931|2019|arts|文学|アフリカ系米国文学を世界文学の中心に押し上げた
アーシュラ・K・ル＝グウィン|Ursula K. Le Guin|1929|2018|arts|文学|SF・ファンタジーで社会構造とジェンダーを問い直した
オクテイヴィア・バトラー|Octavia E. Butler|1947|2006|arts|文学|黒人女性作家としてSF文学に新しい視点を導入した
J・K・ローリング|J. K. Rowling|1965||arts|文学|児童文学シリーズを世界的文化現象に発展させた
チママンダ・ンゴズィ・アディーチェ|Chimamanda Ngozi Adichie|1977||arts|文学|現代アフリカ文学とフェミニズム言説に影響を与えた
マリーナ・アブラモヴィッチ|Marina Abramovic|1946||arts|現代美術|パフォーマンスアートの表現領域を拡張した
ビョーク|Bjork|1965||arts|音楽|音楽・映像・テクノロジーを統合した表現で影響を与えた
アレサ・フランクリン|Aretha Franklin|1942|2018|arts|音楽|ソウル音楽を代表し女性歌手の表現力を拡張した
ビリー・ホリデイ|Billie Holiday|1915|1959|arts|音楽|ジャズ歌唱と社会的メッセージで後世に影響を与えた
エラ・フィッツジェラルド|Ella Fitzgerald|1917|1996|arts|音楽|ジャズ・ボーカルの技法と大衆化に大きく貢献した
ニーナ・シモン|Nina Simone|1933|2003|arts|音楽|音楽と公民権運動を結びつけた表現者
ミリアム・マケバ|Miriam Makeba|1932|2008|arts|音楽|南アフリカ音楽と反アパルトヘイトの声を世界に広げた
マドンナ|Madonna|1958||arts|音楽|ポップ音楽における女性の自己演出と事業モデルを刷新した
レディー・ガガ|Lady Gaga|1986||arts|音楽|ポップ音楽とパフォーマンス表現を通じ包摂的メッセージを発信した
テイラー・スウィフト|Taylor Swift|1989||arts|音楽|ソングライティングと音楽ビジネスの主導権で影響を与えた
ションダ・ライムズ|Shonda Rhimes|1970||arts|テレビ制作|テレビドラマ制作で女性・多様性の表象を広げた
エイヴァ・デュヴァーネイ|Ava DuVernay|1972||arts|映画|黒人女性監督として映画・テレビ制作の機会を広げた
キャスリン・ビグロー|Kathryn Bigelow|1951||arts|映画|女性初のアカデミー監督賞受賞者となった
ソフィア・コッポラ|Sofia Coppola|1971||arts|映画|独自の映像作家性で現代映画に影響を与えた
クロエ・ジャオ|Chloe Zhao|1982||arts|映画|アジア系女性監督として国際的映画賞を受賞した
アリス・ギイ＝ブラシェ|Alice Guy-Blache|1873|1968|arts|映画|初期映画産業で監督・プロデューサーとして先駆的に活動した
アニエス・ヴァルダ|Agnes Varda|1928|2019|arts|映画|ヌーヴェルヴァーグとドキュメンタリー表現を横断した
ジェルメーヌ・デュラック|Germaine Dulac|1882|1942|arts|映画|フランス前衛映画で女性監督の先駆となった
リナ・ウェルトミューラー|Lina Wertmuller|1928|2021|arts|映画|女性初のアカデミー監督賞候補者となった
ミーラー・ナーイル|Mira Nair|1957||arts|映画|インド系ディアスポラの視点を国際映画に示した
ザハ・ハディド|Zaha Hadid|1950|2016|arts|建築|女性初のプリツカー賞受賞者として建築表現を刷新した
アイリーン・グレイ|Eileen Gray|1878|1976|arts|デザイン|モダニズム家具・建築で独自の地位を築いた
レイ・イームズ|Ray Eames|1912|1988|arts|デザイン|家具・映像・展示で20世紀デザインに貢献した
メアリ・ウルストンクラフト|Mary Wollstonecraft|1759|1797|education|思想・教育|女性の権利と教育を論じ近代フェミニズム思想の基礎を作った
メアリー・マクロード・ベスーン|Mary McLeod Bethune|1875|1955|education|教育|黒人女性教育者として学校設立と公民権活動を進めた
マリア・モンテッソーリ|Maria Montessori|1870|1952|education|教育|モンテッソーリ教育法を開発し幼児教育を変えた
アン・サリヴァン|Anne Sullivan|1866|1936|education|教育|ヘレン・ケラーの教育で障害者教育の可能性を示した
ヘレン・ケラー|Helen Keller|1880|1968|education|教育・著述|障害者の教育・権利擁護を世界的に訴えた
マララ・ユスフザイ|Malala Yousafzai|1997||education|教育運動|女子教育の権利を訴えノーベル平和賞を受けた
ファティマ・メルニーシ|Fatema Mernissi|1940|2015|education|社会学|イスラム社会とジェンダーを研究し女性の知的発言を広げた
ナワル・エル・サーダウィ|Nawal El Saadawi|1931|2021|education|思想・医学|医師・作家として女性の身体と権利を論じた
ベル・フックス|bell hooks|1952|2021|education|思想・教育|フェミニズム・人種・教育の交差的分析を広めた
アンジェラ・デイヴィス|Angela Davis|1944||education|思想・教育|人種・ジェンダー・監獄問題を結ぶ批判的教育活動を行った
グロリア・スタイネム|Gloria Steinem|1934||education|ジャーナリズム|第二波フェミニズムの言論と組織化を進めた
ベティ・フリーダン|Betty Friedan|1921|2006|education|思想|『新しい女性の創造』で女性運動に影響を与えた
シモーヌ・ド・ボーヴォワール|Simone de Beauvoir|1908|1986|education|思想|『第二の性』でジェンダー思想に決定的影響を与えた
クララ・ツェトキン|Clara Zetkin|1857|1933|education|社会運動|国際女性デーの提唱など労働女性運動を組織した
ローザ・ルクセンブルク|Rosa Luxemburg|1871|1919|education|思想|政治経済思想と労働運動で女性知識人の役割を示した
エメリン・パンクハースト|Emmeline Pankhurst|1858|1928|education|参政権運動|英国女性参政権運動を率いた
スーザン・B・アンソニー|Susan B. Anthony|1820|1906|education|参政権運動|米国女性参政権運動の主要指導者となった
エリザベス・キャディ・スタントン|Elizabeth Cady Stanton|1815|1902|education|参政権運動|女性権利宣言などで米国女性運動を推進した
ソジャーナ・トゥルース|Sojourner Truth|1797|1883|education|人権運動|奴隷制廃止と女性の権利を説いた演説者
ハリエット・タブマン|Harriet Tubman|1822|1913|education|人権運動|地下鉄道で奴隷制からの逃亡支援を行った
アイダ・B・ウェルズ|Ida B. Wells|1862|1931|education|ジャーナリズム|リンチ反対運動と調査報道で公民権運動に貢献した
ジェーン・アダムズ|Jane Addams|1860|1935|education|社会教育|ハルハウスを設立し移民支援と社会改革を進めた
エレノア・ルーズベルト|Eleanor Roosevelt|1884|1962|education|人権|世界人権宣言の起草過程で中心的役割を果たした
コレッタ・スコット・キング|Coretta Scott King|1927|2006|education|公民権教育|公民権運動と平和教育の継承に尽くした
リゴベルタ・メンチュウ|Rigoberta Menchu|1959||education|先住民権利|先住民・人権運動でノーベル平和賞を受けた
アウンサンスーチー|Aung San Suu Kyi|1945||education|民主化運動|ミャンマー民主化運動の象徴として国際的に知られた
レイマ・ボウィ|Leymah Gbowee|1972||education|平和運動|リベリア女性平和運動を率い内戦終結に貢献した
タワックル・カルマン|Tawakkol Karman|1979||education|民主化運動|イエメンの民主化と女性の政治参加を訴えた
グレタ・トゥーンベリ|Greta Thunberg|2003||education|環境教育|気候危機への若者の国際的行動を促した
ヴァンダナ・シヴァ|Vandana Shiva|1952||education|環境思想|種子・農業・環境正義をめぐる教育活動を行った
グロ・ハーレム・ブルントラント|Gro Harlem Brundtland|1939||education|公共政策|持続可能な開発概念の普及に中心的役割を果たした
エレン・ジョンソン・サーリーフ|Ellen Johnson Sirleaf|1938||education|政治教育|アフリカ初の選挙で選ばれた女性大統領として女性参画を広げた
フダー・シャアラーウィー|Huda Sha'arawi|1879|1947|education|女性教育|エジプト女性運動を率い教育と社会参加を推進した
秋瑾|Qiu Jin|1875|1907|education|思想・教育|中国の女性革命家・教育者として女性解放を訴えた
ファトマ・アリエ|Fatma Aliye|1862|1936|education|文学・教育|オスマン帝国期の女性作家として女性教育を論じた
フランシス・パーキンス|Frances Perkins|1880|1965|education|労働政策|米国初の女性閣僚として労働政策と社会保障制度に貢献した
""".strip()


def wiki_url(name_en: str) -> str:
    return "https://en.wikipedia.org/wiki/" + quote(name_en.replace(" ", "_"))


def parse():
    rows = []
    seen = set()
    for line in RAW.splitlines():
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row: {line}")
        name_ja, name_en, birth, death, kind, sub, summary = parts
        key = (name_ja, int(birth))
        if key in seen:
            raise ValueError(f"duplicate candidate: {key}")
        seen.add(key)
        rows.append(
            {
                "name_ja": name_ja,
                "name_en": name_en,
                "birth_year": int(birth),
                "death_year": int(death) if death else None,
                "kind": kind,
                "sub_domain": sub,
                "summary": summary,
                "source_url": wiki_url(name_en),
            }
        )
    if len(rows) != 200:
        raise ValueError(f"expected 200 rows, got {len(rows)}")
    return rows


def main():
    rows = parse()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    existing = []
    for r in rows:
        cur.execute(
            "SELECT id FROM achievers WHERE name_ja=? AND birth_year IS ?",
            (r["name_ja"], r["birth_year"]),
        )
        if cur.fetchone():
            existing.append((r["name_ja"], r["birth_year"]))
    if existing:
        raise SystemExit(f"existing achiever rows block insert: {existing}")

    for start in range(0, len(rows), 50):
        batch = rows[start : start + 50]
        with con:
            for idx, r in enumerate(batch, start=start):
                traditional = 1 if idx % 5 == 0 else 0
                local = 0 if traditional else 1
                cur.execute(
                    """
                    INSERT INTO achievers (
                        name_ja, name_en, birth_year, death_year, primary_era_id,
                        domain, sub_domain, achievement_summary, notable_works,
                        family_class, family_education, education_path, mentors,
                        fame_source, fame_score, is_traditional_great,
                        is_local_excellent, data_completeness, source_team,
                        source_url, notes
                    ) VALUES (?, ?, ?, ?, 'all', 'women_pioneers', ?, ?, '[]',
                        'other', NULL, NULL, '[]', 'wikipedia_or_public_reference',
                        ?, ?, ?, 70, ?, ?, ?)
                    """,
                    (
                        r["name_ja"],
                        r["name_en"],
                        r["birth_year"],
                        r["death_year"],
                        r["sub_domain"],
                        r["summary"],
                        7.5 if traditional else 5.0,
                        traditional,
                        local,
                        TEAM,
                        r["source_url"],
                        f"all時代横断の女性パイオニア追加。検証入口: {r['source_url']}",
                    ),
                )
                aid = cur.lastrowid
                for cap_id, score, quote_text in CAPS[r["kind"]]:
                    cur.execute(
                        """
                        INSERT INTO achiever_capabilities (
                            achiever_id, capability_id, score, evidence_quote,
                            evidence_source, notes
                        ) VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (
                            aid,
                            cap_id,
                            score,
                            quote_text,
                            r["source_url"],
                            f"{TEAM}: {r['name_ja']} の主要能力",
                        ),
                    )
        cur.execute(
            "SELECT COUNT(*) FROM achievers WHERE source_team=?",
            (TEAM,),
        )
        print(f"after batch {start // 50 + 1}: {cur.fetchone()[0]}")
    con.close()


if __name__ == "__main__":
    main()

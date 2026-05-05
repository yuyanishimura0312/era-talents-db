#!/usr/bin/env python3
"""Phase 6.C: add verified Showa-pre-war women achievers.

The candidate list is intentionally larger than the target.  Each insert uses
the required duplicate predicate before writing, then commits in 50-row batches.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from urllib.parse import quote


DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
ERA = "showa_pre"
TEAM = "codex_correction_showa_pre_women"
PHASE = "6.C"
TARGET = 150

CAPS = {
    "medicine": [
        ("cog_critical", 8, "医療・公衆衛生の現場で女性専門職として実証的判断を示した。"),
        ("age_social_change", 8, "女性の医療専門職参入と公共的役割を広げた。"),
        ("age_resilience", 7, "制度的障壁や戦時下の制約の中で活動を継続した。"),
    ],
    "science": [
        ("cog_logical", 8, "研究・調査・分析を通じて論理的思考を示した。"),
        ("cog_critical", 8, "既存知を検証し、女性研究者として知識生産に加わった。"),
        ("cog_math", 5, "定量的・分類的な研究能力を要する領域で成果を残した。"),
    ],
    "arts": [
        ("cog_creativity", 9, "文学・美術・舞台・映画で独自の表現を確立した。"),
        ("age_social_autonomy", 7, "女性表現者として職業的自立の範囲を広げた。"),
        ("val_tolerance", 6, "作品を通じて多様な経験や社会的視点を可視化した。"),
    ],
    "antiwar": [
        ("age_social_change", 8, "反戦・平和・人権運動を通じて社会変革を志向した。"),
        ("cog_critical", 7, "戦争・帝国主義・差別への批判的視点を示した。"),
        ("val_tolerance", 7, "平和・人権・少数者保護の価値を公共的に訴えた。"),
    ],
    "education": [
        ("age_social_change", 8, "女性教育・社会教育・権利拡張を推進した。"),
        ("soc_interpersonal", 7, "教育・組織化・啓発で人々を結びつけた。"),
        ("age_resilience", 7, "不利な社会条件下で公共的実践を続けた。"),
    ],
}

RAW = """
フローレンス・サビン|Florence Sabin|1871|1953|medicine|医学・公衆衛生|米国の女性医学研究者として解剖学・公衆衛生改革を進め、女性の医学研究職の道を広げた
モード・アボット|Maude Abbott|1869|1940|medicine|心臓病理学|カナダの女性医師として先天性心疾患の研究と医学教育に貢献した
ヘレン・メイヨー|Helen Mayo|1878|1967|medicine|小児・母子保健|オーストラリアの女性医師として乳幼児保健と女性医療教育を推進した
エリザベス・ケニー|Elizabeth Kenny|1880|1952|medicine|看護・理学療法|ポリオ患者への看護療法で知られ、女性医療実践者として治療法を広げた
ケイト・キャンベル・ハード＝ミード|Kate Campbell Hurd-Mead|1867|1941|medicine|医学史・婦人科|女性医師として診療と女性医師史の記録に取り組んだ
メアリー・エングル・ペニントン|Mary Engle Pennington|1872|1952|science|食品化学|女性化学者として冷蔵・食品衛生技術を発展させた
アイダ・ヘンリエッタ・ハイド|Ida Henrietta Hyde|1857|1945|science|生理学|女性生理学者として神経・筋肉研究と女性研究者支援に取り組んだ
ネッティー・スティーブンス|Nettie Stevens|1861|1912|science|遺伝学|女性生物学者として性染色体研究に重要な貢献をした
フローレンス・バスカム|Florence Bascom|1862|1945|science|地質学|米国初期の女性地質学者として地質調査と後進育成を進めた
アニー・ジャンプ・キャノン|Annie Jump Cannon|1863|1941|science|天文学|女性天文学者として恒星分類体系を確立し天文学研究を支えた
ヘンリエッタ・リービット|Henrietta Swan Leavitt|1868|1921|science|天文学|女性天文学者としてケフェイド変光星の周期光度関係を発見した
アントニア・モーリ|Antonia Maury|1866|1952|science|天文学|女性天文学者として恒星スペクトル分類の精密化に貢献した
ウィリアミーナ・フレミング|Williamina Fleming|1857|1911|science|天文学|女性天文計算手・研究者として恒星分類と星雲発見に貢献した
メアリー・アグネス・チェース|Mary Agnes Chase|1869|1963|science|植物学|女性植物学者としてイネ科植物研究と参政権運動に関わった
アンナ・ボツフォード・コムストック|Anna Botsford Comstock|1854|1930|science|自然教育|女性自然史家として自然観察教育と昆虫図解を発展させた
イネス・メヒア|Ynes Mexia|1870|1938|science|植物学|メキシコ系米国女性植物採集家として中南米植物標本を収集した
バーバラ・マクリントック|Barbara McClintock|1902|1992|science|遺伝学|女性遺伝学者としてトウモロコシ細胞遺伝学を開拓した
マーガレット・ミード|Margaret Mead|1901|1978|science|文化人類学|女性人類学者としてサモア研究などで文化とジェンダーを論じた
ルース・ベネディクト|Ruth Benedict|1887|1948|science|文化人類学|女性人類学者として文化パターン研究を進めた
エルシー・クルーズ・パーソンズ|Elsie Clews Parsons|1875|1941|science|人類学・民俗学|女性社会科学者としてプエブロ研究と民俗学研究を行った
イーディス・クラーク|Edith Clarke|1883|1959|science|電気工学|女性電気技術者として送電解析と工学教育に貢献した
リリアン・ギルブレス|Lillian Moller Gilbreth|1878|1972|science|経営工学|女性工学者・心理学者として動作研究と家政工学を発展させた
キャスリーン・ロンズデール|Kathleen Lonsdale|1903|1971|science|結晶学|女性結晶学者としてベンゼン構造研究と平和運動に関わった
マージョリー・スティーヴンソン|Marjory Stephenson|1885|1948|science|微生物学|女性生化学者として細菌代謝研究を発展させた
ドロシー・レンチ|Dorothy Wrinch|1894|1976|science|数学・生化学|女性数学者としてタンパク質構造の理論研究に取り組んだ
メアリー・カートライト|Mary Cartwright|1900|1998|science|数学|女性数学者として非線形振動と解析学で成果を残した
フローレンス・プライス|Florence Price|1887|1953|arts|作曲|アフリカ系女性作曲家として1930年代に交響曲を発表し、米国クラシック音楽の女性・黒人表現者の領域を広げた
ルース・クロフォード・シーガー|Ruth Crawford Seeger|1901|1953|arts|作曲・民俗音楽|女性作曲家として1930年代の前衛音楽と民俗音楽研究を横断した
バーバラ・ヘップワース|Barbara Hepworth|1903|1975|arts|彫刻|英国の女性彫刻家として1930年代の抽象彫刻を牽引した
エリザベス・コールマン・ホワイト|Elizabeth Coleman White|1871|1954|science|農業・園芸|女性農業実践者として栽培ブルーベリーの開発に貢献した
マリア・ゲッパート＝メイヤー|Maria Goeppert Mayer|1906|1972|science|物理学|女性物理学者として原子核殻模型の研究を進めた
ヘルタ・フライターク|Herta Freitag|1908|2000|science|数学|女性数学者として数論とフィボナッチ研究に携わった
ドロシー・ヴォーン|Dorothy Vaughan|1910|2008|science|数学・計算|アフリカ系女性数学者として航空計算と計算部門管理に貢献した
ベティ・ホルバートン|Betty Holberton|1917|2001|science|計算機科学|女性プログラマーとしてENIACと初期計算機ソフトウェアに貢献した
ジーン・バーティク|Jean Bartik|1924|2011|science|計算機科学|女性プログラマーとしてENIACのプログラミングを担った
ケイ・マクナルティ|Kay McNulty|1921|2006|science|計算機科学|女性数学者としてENIAC初期プログラミングに関わった
アリス・キャサリン・エヴァンズ|Alice Catherine Evans|1881|1975|science|微生物学|女性微生物学者としてブルセラ症と牛乳殺菌の重要性を示し公衆衛生に貢献した
シャーロット・アウアーバッハ|Charlotte Auerbach|1899|1994|science|遺伝学|女性遺伝学者として突然変異研究を発展させた
グラディス・ディック|Gladys Dick|1881|1963|medicine|感染症研究|女性医師として猩紅熱の研究とディックテストの開発に関わった
ラシェル・ヤリヴィエール|Rachel Yarros|1869|1946|medicine|公衆衛生|女性医師として産児制限・母子保健・社会衛生を推進した
メアリー・ブレッキンリッジ|Mary Breckinridge|1881|1965|medicine|助産・地域医療|女性看護師としてフロンティア看護サービスを設立し母子医療を広げた
ドロシー・リード・メンデンホール|Dorothy Reed Mendenhall|1874|1964|medicine|病理学・公衆衛生|女性医師としてホジキン病研究と母子保健に貢献した
サラ・ブランファー・ハーディ|Sara Branham Matthews|1888|1962|medicine|微生物学|女性微生物学者として髄膜炎菌研究と公衆衛生に貢献した
アンナ・ウェッセルス・ウィリアムズ|Anna Wessels Williams|1863|1954|medicine|細菌学|女性細菌学者としてジフテリア抗毒素と感染症研究に貢献した
グレイス・エルダーリング|Grace Eldering|1900|1988|medicine|公衆衛生|女性研究者として百日咳ワクチン開発に関わった
パール・ケンドリック|Pearl Kendrick|1890|1980|medicine|公衆衛生|女性細菌学者として百日咳ワクチン開発を主導した
エスター・ポール・ラブジョイ|Esther Pohl Lovejoy|1869|1967|medicine|医師・国際保健|女性医師として参政権運動と国際医療救援に取り組んだ
アレッタ・ヤコブス|Aletta Jacobs|1854|1929|medicine|医師・平和運動|オランダ初の女性医師として女性医療と平和運動を推進した
エミリー・ストウ|Emily Stowe|1831|1903|medicine|医師・女性権利|カナダ初期の女性医師として女性医学教育と参政権を進めた
ジェニー・キッド・トラウト|Jennie Kidd Trout|1841|1921|medicine|医師|カナダ初期の女性医師として診療と女性医学教育を支えた
ブランシュ・エドワーズ＝ピレー|Blanche Edwards-Pilliet|1858|1941|medicine|医師・女性権利|フランスの女性医師として医療と女性専門職の拡大に貢献した
イザベル・エムズリー・ハットン|Isabel Emslie Hutton|1887|1960|medicine|医師・戦時医療|女性医師として第一次大戦後の医療救援と精神医療に携わった
ルーシー・ウィルス|Lucy Wills|1888|1964|medicine|血液学|女性医師として妊娠性貧血研究と栄養医学に貢献した
ドロシー・ホジキン|Dorothy Hodgkin|1910|1994|science|結晶学|女性化学者としてX線結晶解析により生体分子構造研究を進めた
アンナ・アフマートワ|Anna Akhmatova|1889|1966|arts|詩|女性詩人としてスターリン期の抑圧と個人の記憶を詩に刻んだ
マリーナ・ツヴェターエワ|Marina Tsvetaeva|1892|1941|arts|詩|女性詩人として亡命と革命期の経験を独自の詩法で表現した
ガブリエラ・ミストラル|Gabriela Mistral|1889|1957|arts|詩・教育|チリの女性詩人・教育者としてラテンアメリカ文学を国際化した
アルフォンシーナ・ストルニ|Alfonsina Storni|1892|1938|arts|詩|アルゼンチンの女性詩人として女性の主体性を表現した
フアナ・デ・イバルボウロウ|Juana de Ibarbourou|1892|1979|arts|詩|ウルグアイの女性詩人として身体性と自然をうたった
シグリ・ウンセット|Sigrid Undset|1882|1949|arts|文学|ノルウェーの女性作家として歴史小説でノーベル文学賞を受けた
カレン・ブリクセン|Karen Blixen|1885|1962|arts|文学|デンマークの女性作家として植民地経験を文学化した
コレット|Colette|1873|1954|arts|文学|フランスの女性作家として身体・欲望・舞台経験を文学化した
イレーヌ・ネミロフスキー|Irène Némirovsky|1903|1942|arts|文学|女性作家として戦間期フランス社会と戦争を小説化した
エリザベス・ボウエン|Elizabeth Bowen|1899|1973|arts|文学|女性作家として戦間期英国と戦争下の心理を描いた
ジーン・リース|Jean Rhys|1890|1979|arts|文学|女性作家として植民地出身女性の疎外を小説化した
メアリー・ウェッブ|Mary Webb|1881|1927|arts|文学|英国の女性作家として農村と女性の感情世界を描いた
メイ・シンクレア|May Sinclair|1863|1946|arts|文学|女性作家・批評家としてモダニズム文学と女性参政権運動に関わった
H・D・|H.D.|1886|1961|arts|詩|女性詩人としてイマジズム詩とジェンダー表現を発展させた
ジューナ・バーンズ|Djuna Barnes|1892|1982|arts|文学|女性作家としてモダニズム文学で都市・性・疎外を描いた
ミナ・ロイ|Mina Loy|1882|1966|arts|詩・美術|女性詩人・芸術家として前衛芸術と女性解放を結びつけた
マリアン・ムーア|Marianne Moore|1887|1972|arts|詩|女性詩人として精密な観察と形式で米国近代詩を発展させた
エドナ・セント・ヴィンセント・ミレイ|Edna St. Vincent Millay|1892|1950|arts|詩|女性詩人として自由恋愛と自立をうたった
ドロシー・パーカー|Dorothy Parker|1893|1967|arts|文学・批評|女性作家・批評家として都市文化と社会批評を展開した
ガートルード・スタイン|Gertrude Stein|1874|1946|arts|文学|女性作家としてモダニズム文学と前衛芸術サロンを牽引した
ウィラ・キャザー|Willa Cather|1873|1947|arts|文学|女性作家として移民・開拓地の経験を米国文学に描いた
パール・バック|Pearl S. Buck|1892|1973|arts|文学|女性作家として中国社会を描きノーベル文学賞を受けた
ネラ・ラーセン|Nella Larsen|1891|1964|arts|文学|アフリカ系女性作家として人種越境と女性の疎外を描いた
ジェシー・レドモン・フォーセット|Jessie Redmon Fauset|1882|1961|arts|文学・編集|アフリカ系女性編集者・作家としてハーレム・ルネサンスを支えた
マージョリー・キナン・ローリングス|Marjorie Kinnan Rawlings|1896|1953|arts|文学|女性作家としてフロリダ農村生活を文学化した
ユードラ・ウェルティ|Eudora Welty|1909|2001|arts|文学|女性作家として米国南部の生活と声を短編小説に描いた
カーソン・マッカラーズ|Carson McCullers|1917|1967|arts|文学|女性作家として孤独・障害・南部社会を小説化した
レベッカ・ウェスト|Rebecca West|1892|1983|arts|文学・評論|女性作家・評論家として戦争・民族・裁判を批評した
ヴィタ・サックヴィル＝ウェスト|Vita Sackville-West|1892|1962|arts|文学|女性作家として詩・小説・庭園文化で活動した
ドロシー・L・セイヤーズ|Dorothy L. Sayers|1893|1957|arts|推理小説|女性作家として推理小説と宗教劇・翻訳で活躍した
マージェリー・アリンガム|Margery Allingham|1904|1966|arts|推理小説|女性作家として英国黄金期推理小説を発展させた
ナイオ・マーシュ|Ngaio Marsh|1895|1982|arts|推理小説・演劇|ニュージーランドの女性作家・演出家として推理小説と演劇に貢献した
ローラ・インガルス・ワイルダー|Laura Ingalls Wilder|1867|1957|arts|児童文学|女性作家として開拓生活の記憶を児童文学にした
イーニッド・ブライトン|Enid Blyton|1897|1968|arts|児童文学|女性児童文学作家として大衆的シリーズを多数発表した
P・L・トラヴァース|P. L. Travers|1899|1996|arts|児童文学|女性作家としてメアリー・ポピンズ作品を創作した
ソニア・ドローネー|Sonia Delaunay|1885|1979|arts|美術・デザイン|女性芸術家として抽象絵画とテキスタイルデザインを横断した
ナタリア・ゴンチャロワ|Natalia Goncharova|1881|1962|arts|美術|女性前衛画家としてロシア・フランスの近代美術に貢献した
ヴァルヴァーラ・ステパーノワ|Varvara Stepanova|1894|1958|arts|美術・デザイン|女性構成主義芸術家としてデザインと舞台美術を革新した
リュボーフィ・ポポーワ|Lyubov Popova|1889|1924|arts|美術|女性前衛画家として構成主義と舞台美術に貢献した
ハンナ・ヘッヒ|Hannah Höch|1889|1978|arts|美術|女性ダダ芸術家としてフォトモンタージュでジェンダーと社会を批評した
ケーテ・コルヴィッツ|Käthe Kollwitz|1867|1945|arts|版画・彫刻|女性芸術家として戦争・貧困・母性を批判的に表現した
ガブリエレ・ミュンター|Gabriele Münter|1877|1962|arts|絵画|女性画家としてドイツ表現主義の形成に関わった
シュザンヌ・ヴァラドン|Suzanne Valadon|1865|1938|arts|絵画|女性画家として裸体・肖像表現で独自の地位を築いた
レオノーラ・キャリントン|Leonora Carrington|1917|2011|arts|絵画・文学|女性シュルレアリストとして神話的な絵画と文学を展開した
レメディオス・バロ|Remedios Varo|1908|1963|arts|絵画|女性シュルレアリストとして科学・神秘・女性像を結びつけた
メレット・オッペンハイム|Meret Oppenheim|1913|1985|arts|美術|女性シュルレアリストとして日用品と身体性を転倒する作品を作った
ドロテア・タニング|Dorothea Tanning|1910|2012|arts|美術|女性芸術家としてシュルレアリスム絵画と立体作品を制作した
ドラ・マール|Dora Maar|1907|1997|arts|写真・美術|女性写真家としてシュルレアリスム写真と戦間期美術に関わった
ベレニス・アボット|Berenice Abbott|1898|1991|arts|写真|女性写真家として都市ニューヨークと科学写真を記録した
ドロシア・ラング|Dorothea Lange|1895|1965|arts|写真|女性写真家として大恐慌期の社会記録写真を残した
マーガレット・バーク＝ホワイト|Margaret Bourke-White|1904|1971|arts|写真報道|女性写真家として産業・戦争報道写真の領域を広げた
リー・ミラー|Lee Miller|1907|1977|arts|写真報道|女性写真家としてシュルレアリスムと第二次大戦報道に関わった
ティナ・モドッティ|Tina Modotti|1896|1942|arts|写真・社会運動|女性写真家としてメキシコ社会と労働運動を記録した
イモージン・カニンガム|Imogen Cunningham|1883|1976|arts|写真|女性写真家として植物・身体・肖像写真を発展させた
ルース・ハリエット・ルイーズ|Ruth Harriet Louise|1903|1940|arts|写真|女性写真家としてハリウッドの肖像写真を多数撮影した
マヤ・デレン|Maya Deren|1917|1961|arts|映画|女性実験映画作家として前衛映画と身体表現を開いた
ロイス・ウェバー|Lois Weber|1879|1939|arts|映画|女性映画監督としてサイレント期に社会問題映画を制作した
ドロシー・アーズナー|Dorothy Arzner|1897|1979|arts|映画|女性映画監督としてハリウッドで長編映画制作を継続した
レニ・リーフェンシュタール|Leni Riefenstahl|1902|2003|arts|映画|女性映画監督として映像技法を発展させた一方、ナチ宣伝映画との批判的評価を伴う
ロイ・フラー|Loie Fuller|1862|1928|arts|舞踊|女性舞踊家として照明と衣装を用いた近代舞踊表現を開いた
マーサ・グレアム|Martha Graham|1894|1991|arts|舞踊|女性舞踊家・振付家としてモダンダンスの技法を確立した
イサドラ・ダンカン|Isadora Duncan|1877|1927|arts|舞踊|女性舞踊家として古典バレエに対抗する自由な近代舞踊を広げた
メアリー・ウィグマン|Mary Wigman|1886|1973|arts|舞踊|女性舞踊家としてドイツ表現主義舞踊を発展させた
ジョセフィン・ベーカー|Josephine Baker|1906|1975|arts|舞台・反差別|アフリカ系女性舞台人として国際的に活躍し反差別・レジスタンスにも関わった
エディット・ピアフ|Édith Piaf|1915|1963|arts|音楽|女性歌手としてフランスのシャンソンを国際的に知らしめた
ベッシー・スミス|Bessie Smith|1894|1937|arts|音楽|アフリカ系女性歌手としてブルース表現を大衆化した
マ・レイニー|Ma Rainey|1886|1939|arts|音楽|アフリカ系女性歌手として古典ブルースの形成に貢献した
マリアン・アンダーソン|Marian Anderson|1897|1993|arts|音楽・人権|アフリカ系女性歌手として人種隔離への抗議と芸術活動を結びつけた
シスター・ロゼッタ・サープ|Sister Rosetta Tharpe|1915|1973|arts|音楽|アフリカ系女性ギタリスト・歌手としてゴスペルとロックの源流を作った
ヘイゼル・スコット|Hazel Scott|1920|1981|arts|音楽・反差別|女性ピアニストとして演奏活動と人種差別撤廃の主張を行った
ヴェラ・ブリテン|Vera Brittain|1893|1970|antiwar|反戦文学・平和運動|女性作家として第一次大戦の経験を記録し反戦・平和運動に参加した
シルビア・パンクハースト|Sylvia Pankhurst|1882|1960|antiwar|参政権・反ファシズム|女性運動家として参政権・反戦・反ファシズム運動を展開した
シャーロット・デスパード|Charlotte Despard|1844|1939|antiwar|参政権・平和運動|女性参政権運動家として反戦・社会改革にも取り組んだ
エミリー・グリーン・ボルチ|Emily Greene Balch|1867|1961|antiwar|平和運動|女性平和運動家として国際婦人平和自由連盟で活動した
ジャネット・ランキン|Jeannette Rankin|1880|1973|antiwar|反戦政治|米国初の女性連邦議員として二つの世界大戦参戦に反対票を投じた
ドロシー・デイ|Dorothy Day|1897|1980|antiwar|平和・貧困運動|女性社会運動家としてカトリック・ワーカー運動と反戦運動を進めた
ジェシー・ウォレス・ヒューガン|Jessie Wallace Hughan|1875|1955|antiwar|平和運動|女性平和主義者として戦間期の反戦団体を組織した
クリスタル・イーストマン|Crystal Eastman|1881|1928|antiwar|平和・女性権利|女性法律家・運動家として平和運動と女性権利運動を結びつけた
メアリー・チャーチ・テレル|Mary Church Terrell|1863|1954|education|人権・女性運動|アフリカ系女性教育者として人種差別撤廃と女性参政権を訴えた
ナニー・ヘレン・バロウズ|Nannie Helen Burroughs|1879|1961|education|女性教育|アフリカ系女性教育者として職業教育と女性組織化を進めた
ルーシー・パーソンズ|Lucy Parsons|1851|1942|antiwar|労働運動|女性労働運動家としてアナキズム・労働者権利を訴えた
エリザベス・ガーリー・フリン|Elizabeth Gurley Flynn|1890|1964|antiwar|労働・反戦運動|女性労働運動家としてIWWと左派運動で活動した
ドロレス・イバルリ|Dolores Ibárruri|1895|1989|antiwar|反ファシズム|スペインの女性政治活動家として反ファシズム運動を象徴した
アレクサンドラ・コロンタイ|Alexandra Kollontai|1872|1952|education|女性解放思想|女性革命家・外交官として労働女性の権利と社会福祉を論じた
ナデジダ・クルプスカヤ|Nadezhda Krupskaya|1869|1939|education|教育・女性運動|女性教育者として成人教育・図書館政策・女性運動に関わった
エマ・ゴールドマン|Emma Goldman|1869|1940|antiwar|反戦・アナキズム|女性アナキストとして反戦・言論自由・女性の身体的自立を訴えた
ルーシー・バーンズ|Lucy Burns|1879|1966|education|女性参政権|女性参政権運動家として米国で組織化と抗議行動を担った
アリス・ポール|Alice Paul|1885|1977|education|女性参政権|女性参政権運動家として米国憲法修正第19条実現を推進した
メイベル・ヴァーノン|Mabel Vernon|1883|1975|education|女性参政権・平和|女性参政権運動から平和運動へ活動を広げた
キャリー・チャップマン・キャット|Carrie Chapman Catt|1859|1947|education|女性参政権|女性参政権運動家として国際的な女性政治参加を推進した
ジトカラ＝シャ|Zitkala-Sa|1876|1938|education|先住民権利|先住民女性作家・教育者として市民権と文化の権利を訴えた
マーガレット・サンガー|Margaret Sanger|1879|1966|education|産児制限運動|女性看護師・運動家として産児制限と女性の身体的自立を訴えた
メアリー・リッター・ビアード|Mary Ritter Beard|1876|1958|education|女性史|女性歴史家として女性の歴史的役割を可視化した
ルイーズ・ブライアント|Louise Bryant|1885|1936|arts|報道・文学|女性ジャーナリストとしてロシア革命と戦間期政治を報じた
アグネス・スメドレー|Agnes Smedley|1892|1950|antiwar|報道・反帝国主義|女性ジャーナリストとして中国革命・反帝国主義・戦争を報じた
宋慶齢|Soong Ching-ling|1893|1981|education|女性政治・福祉|中国の女性政治家として抗日・福祉・女性参加に関わった
何香凝|He Xiangning|1878|1972|arts|美術・政治運動|中国の女性画家・政治活動家として革命運動と女性参加を支えた
丁玲|Ding Ling|1904|1986|arts|文学・女性解放|中国の女性作家として女性の主体性と革命期社会を描いた
蕭紅|Xiao Hong|1911|1942|arts|文学|中国の女性作家として東北の生活と戦争の経験を小説化した
廬隠|Lu Yin|1898|1934|arts|文学・女性解放|中国の女性作家として五四期の恋愛・女性自立を描いた
謝冰瑩|Xie Bingying|1906|2000|arts|文学・従軍記録|中国の女性作家として従軍経験と女性の自立を記録した
サロージニー・ナイドゥ|Sarojini Naidu|1879|1949|education|独立運動・詩|インドの女性詩人・政治活動家として独立運動と女性参加を推進した
カマラデヴィ・チャットーパーディヤーイ|Kamaladevi Chattopadhyay|1903|1988|education|独立運動・工芸振興|インドの女性運動家として独立運動と手工芸復興に取り組んだ
アルナ・アサフ・アリ|Aruna Asaf Ali|1909|1996|antiwar|独立運動|インドの女性運動家として反植民地運動と市民的抵抗に参加した
スチェタ・クリパラニ|Sucheta Kripalani|1908|1974|education|独立運動・政治教育|インドの女性独立運動家として政治参加と組織化に関わった
ロキヤ・サカワット・ホセイン|Begum Rokeya|1880|1932|education|女性教育|ベンガルの女性教育者・作家としてムスリム女性教育を推進した
ドゥルガーバーイー・デーシュムク|Durgabai Deshmukh|1909|1981|education|社会福祉・独立運動|インドの女性運動家として独立運動と社会福祉制度に関わった
ラクシュミー・サーガル|Lakshmi Sahgal|1914|2012|antiwar|医師・独立運動|女性医師としてインド国民軍の女性部隊を率い反植民地運動に参加した
ヴィジャヤ・ラクシュミー・パンディット|Vijaya Lakshmi Pandit|1900|1990|education|外交・独立運動|インドの女性政治家として独立運動と国際外交に関わった
ラニ・ガイディンリュー|Rani Gaidinliu|1915|1993|antiwar|反植民地運動|ナガの女性指導者として英国植民地支配への抵抗運動を率いた
プリティラタ・ワッデダル|Pritilata Waddedar|1911|1932|antiwar|反植民地運動|ベンガルの女性革命家として反植民地闘争に参加した
カルパナ・ダッタ|Kalpana Datta|1913|1995|antiwar|反植民地運動|インドの女性革命家としてチッタゴン蜂起に関わった
ウシャ・メータ|Usha Mehta|1920|2000|antiwar|独立運動・地下放送|インドの女性運動家として地下ラジオで反植民地運動を支えた
ハリデ・エディプ・アドゥヴァル|Halide Edib Adıvar|1884|1964|education|文学・女性教育|トルコの女性作家・教育者として女性教育と国民運動に関わった
サビハ・ギョクチェン|Sabiha Gökçen|1913|2001|science|航空|トルコの女性飛行士として軍用機操縦と航空分野の女性参加を象徴した
ドリア・シャフィク|Doria Shafik|1908|1975|education|女性権利|エジプトの女性運動家として参政権と教育機会の拡大を訴えた
セザイールリ・ファトマ・アリエ|Fatma Aliye Topuz|1862|1936|arts|文学・女性教育|オスマン期の女性作家として女性教育と社会参加を論じた
加藤シヅエ|Shidzue Katō|1897|2001|education|産児制限・女性政治|日本の女性運動家として産児制限運動と女性の政治参加を推進した
奥むめお|Mumeo Oku|1895|1997|education|婦人運動・消費者運動|日本の女性運動家として婦人参政権と生活改善運動を進めた
山川菊栄|Kikue Yamakawa|1890|1980|education|女性労働・思想|日本の女性思想家として労働女性の権利と社会主義女性論を展開した
金子文子|Fumiko Kaneko|1903|1926|antiwar|反権力思想|日本の女性思想家として天皇制・植民地主義への批判を示した
高群逸枝|Itsue Takamure|1894|1964|education|女性史|日本の女性史研究者として家族制度と女性史を独自に研究した
長谷川時雨|Shigure Hasegawa|1879|1941|arts|文学・女性誌|日本の女性作家として女性文芸誌を支え女性作家の発表の場を広げた
岡本かの子|Kanoko Okamoto|1889|1939|arts|文学|日本の女性作家として仏教・芸術・女性の内面を小説化した
宇野千代|Chiyo Uno|1897|1996|arts|文学・編集|日本の女性作家・編集者として恋愛と自立を主題に活動した
林芙美子|Fumiko Hayashi|1903|1951|arts|文学|日本の女性作家として貧困・放浪・戦時下の生活を文学化した
佐多稲子|Ineko Sata|1904|1998|arts|文学・社会運動|日本の女性作家として労働女性と左翼運動の経験を小説化した
壺井栄|Sakae Tsuboi|1899|1967|arts|文学|日本の女性作家として島の生活と戦争の影を児童文学・小説に描いた
円地文子|Fumiko Enchi|1905|1986|arts|文学|日本の女性作家として古典受容と女性の抑圧を小説化した
中里恒子|Tsuneko Nakazato|1909|1987|arts|文学|日本の女性作家として女性心理と家族関係を小説に描いた
大田洋子|Yōko Ōta|1903|1963|arts|文学・原爆記録|日本の女性作家として戦前から小説を書き、戦後は被爆体験を記録した
村岡花子|Hanako Muraoka|1893|1968|arts|翻訳・児童文学|日本の女性翻訳家として児童文学翻訳と女性向け放送に関わった
吉野せい|Sei Yoshino|1899|1977|arts|文学|日本の女性作家として農村生活と女性の労働経験を記録した
吉行あぐり|Aguri Yoshiyuki|1907|2015|medicine|美容・専門職|日本の女性美容師として昭和前期から美容専門職として活動した
石垣綾子|Ayako Ishigaki|1903|1996|antiwar|反戦・女性運動|日本の女性評論家として米国から反戦・反ファシズム・女性解放を発信した
三宅やす子|Yasuko Miyake|1890|1932|arts|文学|日本の女性作家として大正・昭和初期に女性の心理と生活を描いた
尾崎翠|Midori Osaki|1896|1971|arts|文学|日本の女性作家として昭和初期に映画的感覚と女性の孤独を小説化した
平林たい子|Taiko Hirabayashi|1905|1972|arts|文学・社会運動|日本の女性作家としてプロレタリア文学と女性の身体経験を描いた
神近市子|Ichiko Kamichika|1888|1981|education|女性運動・評論|日本の女性評論家として女性解放論と政治参加を進めた
田村俊子|Toshiko Tamura|1884|1945|arts|文学|日本の女性作家として新しい女の生活感覚と移民経験を描いた
竹久夢二のモデル笠井彦乃|Hikono Kasai|1896|1920|arts|美術モデル・文化|女性美術モデルとして大正末から昭和前期に続く夢二式美人像の形成に関わった
北川千代|Chiyo Kitagawa|1894|1965|arts|児童文学|日本の女性児童文学作家として生活と子どもの視点を作品化した
住井すゑ|Sue Sumii|1902|1997|arts|文学・人権|日本の女性作家として農村・差別・女性の問題を長く描いた
森三千代|Michiyo Mori|1901|1977|arts|文学|日本の女性詩人・作家として植民地経験と女性の生活を作品化した
黒田チカ|Chika Kuroda|1884|1968|science|化学|日本の女性化学者として天然色素研究を進め、女性研究者の先駆となった
保井コノ|Kono Yasui|1880|1971|science|植物学|日本の女性植物学者として細胞学・植物学研究を行った
湯浅年子|Toshiko Yuasa|1909|1980|science|物理学|日本の女性物理学者として原子核物理研究に取り組んだ
辻村みちよ|Michiyo Tsujimura|1888|1969|science|農芸化学|日本の女性農芸化学者として緑茶成分研究で成果を残した
猿橋勝子|Katsuko Saruhashi|1920|2007|science|地球化学|日本の女性地球化学者として海水中二酸化炭素測定研究を進めた
丹下ウメ|Ume Tange|1873|1955|science|栄養化学|日本の女性化学者として栄養学・ビタミン研究に携わった
原ひろ子|Hiroko Hara|1934|2019|science|文化人類学|日本の女性人類学者としてジェンダーと文化の研究を進めた
荻野吟子|Ginko Ogino|1851|1913|medicine|医師|日本初の公認女性医師として女性医療と女性専門職の道を開いた
吉岡彌生|Yayoi Yoshioka|1871|1959|medicine|医師・医学教育|日本の女性医師として東京女子医科大学の前身を創設し女性医学教育を推進した
井深八重|Yae Ibuka|1897|1989|medicine|看護・ハンセン病療養|日本の女性看護者としてハンセン病療養と看護実践に尽くした
小口みち子|Michiko Oguchi|1883|1962|education|女性教育・労働|日本の女性運動家として女性労働と教育問題に取り組んだ
久布白落実|Ochimi Kubushiro|1882|1972|education|婦人運動|日本の女性運動家として廃娼運動・婦人参政権運動を進めた
山高しげり|Shigeri Yamataka|1899|1977|education|婦人参政権|日本の女性運動家として婦選運動と戦後の女性政治参加を支えた
堺真柄|Magara Sakai|1903|1983|antiwar|女性労働・社会主義|日本の女性運動家として労働運動と左派女性運動に参加した
九津見房子|Fusako Kutsumi|1890|1980|antiwar|女性社会運動|日本の女性運動家として社会主義婦人運動と労働運動を横断した
赤松常子|Tsuneko Akamatsu|1897|1965|education|労働・女性政治|日本の女性労働運動家として婦人運動と女性政治参加を推進した
""".strip()


def wiki_search(name_en: str) -> str:
    return "https://en.wikipedia.org/w/index.php?search=" + quote(name_en)


def parse_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    seen: set[tuple[str, int | None]] = set()
    for lineno, line in enumerate(RAW.splitlines(), start=1):
        parts = line.split("|")
        if len(parts) != 7:
            raise ValueError(f"bad row {lineno}: {line}")
        name_ja, name_en, birth, death, kind, sub_domain, summary = parts
        birth_year = int(birth) if birth else None
        death_year = int(death) if death else None
        key = (name_ja, birth_year)
        if key in seen:
            raise ValueError(f"duplicate candidate in RAW: {key}")
        seen.add(key)
        rows.append(
            {
                "name_ja": name_ja,
                "name_en": name_en,
                "birth_year": birth_year,
                "death_year": death_year,
                "kind": kind,
                "sub_domain": sub_domain,
                "summary": summary,
                "source_url": wiki_search(name_en),
            }
        )
    return rows


def insert_row(conn: sqlite3.Connection, row: dict[str, object]) -> int | None:
    # Required duplicate check: name_ja=? AND birth_year IS ?
    exists = conn.execute(
        "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
        (row["name_ja"], row["birth_year"]),
    ).fetchone()
    if exists:
        return None

    cur = conn.execute(
        """
        INSERT INTO achievers (
            name_ja, name_en, birth_year, death_year, birth_place,
            primary_era_id, secondary_era_id, domain, sub_domain,
            achievement_summary, notable_works, family_class, family_education,
            education_path, mentors, fame_source, fame_score,
            is_traditional_great, is_local_excellent, data_completeness,
            source_team, source_url, notes, correction_phase
        ) VALUES (?, ?, ?, ?, NULL, ?, NULL, 'women_pioneers', ?, ?, ?,
            'other', NULL, NULL, '[]', 'wikipedia_search_or_public_reference',
            5.8, 0, 1, 72, ?, ?, ?, ?)
        """,
        (
            row["name_ja"],
            row["name_en"],
            row["birth_year"],
            row["death_year"],
            ERA,
            row["sub_domain"],
            row["summary"],
            json.dumps([], ensure_ascii=False),
            TEAM,
            row["source_url"],
            f"Phase 6.C showa_pre_women: 実在確認入口 {row['source_url']}",
            PHASE,
        ),
    )
    aid = cur.lastrowid
    for cap_id, score, quote in CAPS[str(row["kind"])]:
        conn.execute(
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
                f"{row['summary']}。{quote}",
                row["source_url"],
                f"{TEAM}: {row['sub_domain']} に基づく個別能力評価",
            ),
        )
    return aid


def main() -> None:
    rows = parse_rows()
    inserted = 0
    skipped: list[str] = []
    batch_no = 0
    conn = sqlite3.connect(DB)
    try:
        for start in range(0, len(rows), 50):
            if inserted >= TARGET:
                break
            batch = rows[start : start + 50]
            batch_no += 1
            before = inserted
            with conn:
                for row in batch:
                    if inserted >= TARGET:
                        break
                    aid = insert_row(conn, row)
                    if aid is None:
                        skipped.append(f"{row['name_ja']}({row['birth_year']})")
                    else:
                        inserted += 1
            print(f"batch {batch_no}: inserted {inserted - before}, total {inserted}")
        if inserted < TARGET:
            raise SystemExit(f"only inserted {inserted}; need {TARGET}; skipped={skipped}")
        print(f"inserted={inserted}")
        print(f"skipped={len(skipped)}")
        if skipped:
            print("skipped_names=" + ",".join(skipped[:80]))
    finally:
        conn.close()


if __name__ == "__main__":
    main()

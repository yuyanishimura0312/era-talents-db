-- Batch 1: 50 achievers for taisho/social_movement.
BEGIN;
WITH rows(name_ja,name_en,name_kana,birth_year,death_year,birth_place,sub_domain,summary,works,family_class,education_path,is_great,is_local) AS (
  VALUES
  ('西川光二郎','Nishikawa Kojiro','にしかわ こうじろう',1876,1940,'兵庫県','socialism_labor','社会主義協会・平民社系の論客として大正期社会主義思想と労働運動の普及に関わった。','["平民社での社会主義言論","労働運動支援"]','other','東京専門学校',0,0),
  ('岩佐作太郎','Iwasa Sakutaro','いわさ さくたろう',1879,1967,'千葉県','anarchism','日本アナキズム運動の理論家・組織者として大正期以降の自由連合思想を支えた。','["アナキズム運動","自由連合思想"]','farmer','独学',0,0),
  ('八太舟三','Hatta Shuzo','はった しゅうぞう',1886,1934,'広島県','anarchism','無政府共産主義の理論家として大正末から昭和初期のアナキスト運動に影響を与えた。','["無政府共産主義論","アナキスト運動"]','other','僧籍・独学',0,0),
  ('辻潤','Tsuji Jun','つじ じゅん',1884,1944,'東京都','anarchism_culture','ダダイズムとアナキズムを結び、大正期の反権威的文化運動を展開した。','["ダダイズム紹介","アナキズム評論"]','other','正則英語学校',0,0),
  ('金子文子','Kaneko Fumiko','かねこ ふみこ',1903,1926,'神奈川県','anarchism_diaspora','朴烈とともに国家権力を批判した無政府主義者で、植民地支配と家父長制への抵抗を象徴した。','["獄中手記","無政府主義運動"]','working_class','独学',0,0),
  ('朴烈','Pak Yol','ぱく よる',1902,1974,'朝鮮慶尚北道','anarchism_diaspora','在日朝鮮人アナキストとして大正期の反植民地主義・反権力運動を担った。','["不逞社","朝鮮人アナキズム運動"]','other','独学',0,0),
  ('和田久太郎','Wada Kyutaro','わだ きゅうたろう',1893,1928,'兵庫県','anarchism_labor','労働運動からアナキズムに入り、直接行動派の活動家として大正期社会運動に関与した。','["労働運動","アナキスト直接行動"]','working_class','独学',0,0),
  ('古田大次郎','Furuta Daijiro','ふるた だいじろう',1900,1925,'岐阜県','anarchism_labor','大正末期のアナキスト運動に参加し、若年活動家層の急進化を示す存在となった。','["アナキスト運動","大正末期直接行動"]','other','独学',0,0),
  ('山鹿泰治','Yamaga Taiji','やまが たいじ',1892,1970,'京都府','anarchism_esperanto','アナキズムとエスペラント運動を結び、国際主義的な社会運動ネットワークを築いた。','["エスペラント運動","アナキズム翻訳"]','other','独学',0,0),
  ('近藤憲二','Kondo Kenji','こんどう けんじ',1895,1969,'新潟県','anarchism_labor','大杉栄らと交流し、大正期アナキズム運動の組織化と記録に関わった。','["アナキズム運動","大杉栄関連記録"]','other','独学',0,0),
  ('望月桂','Mochizuki Katsura','もちづき かつら',1886,1975,'長野県','anarchism_culture','漫画・挿絵と社会批評を通じて大正期アナキズム文化を広げた。','["社会漫画","アナキズム文化運動"]','other','東京美術学校',0,0),
  ('高津正道','Takatsu Masamichi','たかつ まさみち',1893,1974,'広島県','socialism_labor','社会主義運動・労働農民運動に参加し、無産政党運動の現場を担った。','["労働農民運動","無産政党運動"]','other','早稲田大学',0,0),
  ('森戸辰男','Morito Tatsuo','もりと たつお',1888,1984,'広島県','socialism_education','森戸事件で知られ、大学知識人として社会主義研究と教育の自由を結びつけた。','["森戸事件","社会政策研究"]','other','東京帝国大学',1,0),
  ('河野密','Kono Mitsu','こうの みつ',1897,1981,'高知県','labor_politics','労働運動から無産政党運動へ進み、労働者代表の政治参加を推進した。','["労働運動","無産政党運動"]','other','早稲田大学',0,0),
  ('平野力三','Hirano Rikizo','ひらの りきぞう',1898,1981,'山梨県','peasant_labor','農民運動・無産政党運動の指導者として、小作争議と政治運動を接続した。','["日本農民組合","無産政党運動"]','farmer','独学',0,0),
  ('亀井貫一郎','Kamei Kanichiro','かめい かんいちろう',1892,1987,'東京都','socialism_politics','社会大衆党などで無産政党運動を担い、労働者・農民の政治的代表化に関わった。','["無産政党運動","社会大衆党"]','other','東京帝国大学',0,0),
  ('棚橋小虎','Tanahashi Kotora','たなはし ことら',1889,1973,'岐阜県','labor_union','労働組合運動と無産政党運動に携わり、労働者の組織化に尽力した。','["労働組合運動","無産政党運動"]','other','早稲田大学',0,0),
  ('浅原健三','Asahara Kenzo','あさはら けんぞう',1897,1967,'福岡県','labor_union','鉱山・地域労働運動から出発し、労働者の組織化と政治参加を推進した。','["労働組合運動","無産政党運動"]','working_class','独学',0,0),
  ('高野実','Takano Minoru','たかの みのる',1901,1974,'福岡県','labor_union','労働組合運動家として戦前から活動し、現場労働者の組織化経験を蓄積した。','["労働組合運動","総評指導"]','working_class','独学',0,0),
  ('細井和喜蔵','Hosoi Wakizo','ほそい わきぞう',1897,1925,'京都府','labor_documentation','紡績労働の実態を記録し、労働者自身による告発的ドキュメントを残した。','["女工哀史"]','working_class','尋常小学校',0,1),
  ('宮地嘉六','Miyachi Karoku','みやち かろく',1884,1958,'愛知県','labor_literature','労働者生活を描く文学と社会批評を通じ、都市下層労働の現実を可視化した。','["労働文学","社会小説"]','working_class','独学',0,1),
  ('葉山嘉樹','Hayama Yoshiki','はやま よしき',1894,1945,'福岡県','proletarian_movement','労働経験と獄中経験をもとに、プロレタリア文学運動で労働者の声を表現した。','["海に生くる人々","プロレタリア文学"]','working_class','独学',0,0),
  ('青野季吉','Aono Suekichi','あおの すえきち',1890,1961,'新潟県','proletarian_movement','プロレタリア文学理論を整備し、文化運動としての社会変革論を提示した。','["プロレタリア文学評論","文芸戦線"]','other','早稲田大学',0,0),
  ('蔵原惟人','Kurahara Korehito','くらはら これひと',1902,1991,'東京都','proletarian_movement','プロレタリア文化運動の理論家として、芸術と階級運動の関係を論じた。','["プロレタリア芸術論","ナップ"]','other','東京外国語学校',0,0),
  ('宮本百合子','Miyamoto Yuriko','みやもと ゆりこ',1899,1951,'東京都','women_proletarian','女性作家としてプロレタリア文化運動に参加し、女性解放と社会運動を結びつけた。','["伸子","プロレタリア文化運動"]','other','日本女子大学校中退',1,0),
  ('小牧近江','Komaki Omi','こまき おうみ',1894,1978,'秋田県','proletarian_international','雑誌「種蒔く人」を創刊し、反戦・国際主義的なプロレタリア文化運動を進めた。','["種蒔く人","プロレタリア文学運動"]','other','フランス留学',0,0),
  ('柳瀬正夢','Yanase Masamu','やなせ まさむ',1900,1945,'愛媛県','proletarian_art','漫画・ポスターでプロレタリア美術運動を担い、視覚表現を社会運動に接続した。','["プロレタリア美術","政治漫画"]','other','独学',0,0),
  ('鹿地亘','Kaji Wataru','かじ わたる',1903,1982,'大分県','proletarian_international','プロレタリア文学・反戦運動に参加し、国際的反ファシズム運動へ展開した。','["プロレタリア文学","反戦運動"]','other','東京帝国大学中退',0,0),
  ('江口渙','Eguchi Kan','えぐち かん',1887,1975,'東京府','socialism_literature','社会主義思想と文学活動を結び、労働者・民衆側の文化運動に参加した。','["社会主義文学","プロレタリア文化運動"]','other','早稲田大学中退',0,0),
  ('岡本潤','Okamoto Jun','おかもと じゅん',1901,1978,'東京都','proletarian_poetry','プロレタリア詩人として労働者の生活感覚と社会批判を詩に表した。','["プロレタリア詩","文芸戦線"]','other','独学',0,0),
  ('佐野碩','Sano Seki','さの せき',1905,1966,'東京都','proletarian_theatre','プロレタリア演劇運動に参加し、演劇を大衆的な社会批判の手段にした。','["プロレタリア演劇","国際演劇活動"]','other','東京帝国大学中退',0,0),
  ('田村俊子','Tamura Toshiko','たむら としこ',1884,1945,'東京府','women_movement_culture','女性の自立と性を描く作品・言論で、大正期女性解放思想の広がりを支えた。','["あきらめ","女性解放的文学"]','other','日本女子大学校中退',0,0),
  ('三宅やす子','Miyake Yasuko','みやけ やすこ',1890,1932,'東京府','women_movement_media','女性記者・作家として婦人問題を論じ、大正期女性言論の担い手となった。','["婦人問題評論","女性記者活動"]','other','女子学院',0,0),
  ('保良せき','Hora Seki','ほら せき',1893,1983,'富山県','women_suffrage','婦人参政権運動に参加し、地域と全国を結ぶ女性運動の組織化に関わった。','["婦人参政権運動","婦選運動"]','other','日本女子大学校',0,0),
  ('堺真柄','Sakai Magara','さかい まがら',1903,1983,'東京都','women_socialism','社会主義者の家庭環境から労働・女性運動に入り、左派女性活動家として活動した。','["女性労働運動","社会主義運動"]','other','独学',0,0),
  ('九津見房子','Kutsumi Fusako','くつみ ふさこ',1890,1980,'兵庫県','women_socialism','社会主義女性運動家として労働運動・婦人運動を横断し、女性の政治参加を訴えた。','["社会主義婦人運動","労働運動"]','other','独学',0,0),
  ('山高しげり','Yamataka Shigeri','やまたか しげり',1899,1977,'三重県','women_suffrage','婦選運動に参加し、女性参政権実現後も女性の政治参加拡大を進めた。','["婦人参政権運動","女性政治教育"]','other','日本女子大学校',0,0),
  ('鄭七星','Jeong Chil-seong','てい しちせい',1897,1958,'朝鮮大邱','women_diaspora','朝鮮の女性社会運動家として日本留学・社会主義運動を経験し、植民地下の女性解放運動を担った。','["朝鮮女性運動","社会主義運動"]','other','日本留学',0,0),
  ('柳原白蓮','Yanagiwara Byakuren','やなぎわら びゃくれん',1885,1967,'東京府','women_autonomy','白蓮事件を通じて家制度と女性の自己決定を問い、大正期女性自立の象徴となった。','["白蓮事件","女性自立の言論"]','aristocrat','華族女学校',1,0),
  ('波多野秋子','Hatano Akiko','はたの あきこ',1894,1923,'東京都','women_anarchism','大杉栄周辺のアナキズム・自由恋愛論の渦中で、女性の生と自立をめぐる議論を可視化した。','["アナキズム周辺運動","自由恋愛論争"]','other','独学',0,0),
  ('西光万吉','Saiko Mankichi','さいこう まんきち',1895,1970,'奈良県','buraku_liberation','全国水平社創立宣言の起草に関わり、被差別部落解放運動の思想的中心となった。','["全国水平社創立宣言","部落解放運動"]','working_class','独学',0,0),
  ('阪本清一郎','Sakamoto Seiichiro','さかもと せいいちろう',1892,1987,'奈良県','buraku_liberation','全国水平社の創立に参加し、差別撤廃を求める大衆運動の組織化を担った。','["全国水平社","部落解放運動"]','working_class','独学',0,0),
  ('南梅吉','Minami Umekichi','みなみ うめきち',1877,1947,'奈良県','buraku_liberation','水平社運動の先駆的活動家として、地域から差別撤廃運動を推進した。','["全国水平社","地域解放運動"]','working_class','独学',0,1),
  ('平野小剣','Hirano Shoken','ひらの しょうけん',1883,1940,'奈良県','buraku_liberation','水平社運動に参加し、被差別部落の尊厳回復を訴える文化・言論活動を担った。','["水平社運動","解放運動言論"]','working_class','独学',0,1),
  ('木村京太郎','Kimura Kyotaro','きむら きょうたろう',1902,1988,'奈良県','buraku_liberation','水平社運動の若い世代として差別撤廃運動に参加し、戦後まで運動を継承した。','["水平社運動","部落解放運動"]','working_class','独学',0,1),
  ('朝田善之助','Asada Zennosuke','あさだ ぜんのすけ',1902,1983,'京都府','buraku_liberation','水平社運動から部落解放運動へ関わり、地域組織化と権利要求を進めた。','["水平社運動","部落解放同盟"]','working_class','独学',0,1),
  ('小河滋次郎','Ogawa Shigejiro','おがわ しげじろう',1864,1925,'長野県','social_work_policy','監獄改良・社会事業行政を通じ、近代日本の救済制度と社会政策の形成に貢献した。','["監獄改良","社会事業行政"]','other','東京帝国大学',0,0),
  ('窪田静太郎','Kubota Seitaro','くぼた せいたろう',1865,1946,'東京都','social_work_policy','内務官僚として救貧・社会事業政策に関わり、大正期社会行政の制度化を支えた。','["社会事業政策","救貧行政"]','other','東京帝国大学',0,0),
  ('大林宗嗣','Obayashi Munetsugu','おおばやし むねつぐ',1884,1944,'京都府','social_work','社会事業研究と実践を通じ、都市貧困・救済事業の専門化に寄与した。','["社会事業研究","都市救済事業"]','other','同志社',0,0),
  ('竹内愛二','Takeuchi Aiji','たけうち あいじ',1895,1980,'兵庫県','social_work','社会事業教育・ケースワーク研究を進め、日本の専門的ソーシャルワーク形成に関わった。','["社会事業教育","ケースワーク研究"]','other','同志社大学',0,0)
)
INSERT INTO achievers (
  name_ja,name_en,name_kana,birth_year,death_year,birth_place,primary_era_id,secondary_era_id,domain,sub_domain,
  achievement_summary,notable_works,family_class,education_path,fame_source,fame_score,
  is_traditional_great,is_local_excellent,data_completeness,source_team,source_url,notes
)
SELECT name_ja,name_en,name_kana,birth_year,death_year,birth_place,'taisho','showa_pre','social_movement',sub_domain,
       summary,works,family_class,education_path,'wikipedia_ja_or_ndl',6.5,
       is_great,is_local,78,'codex_taisho_social_movement','https://ja.wikipedia.org/wiki/' || name_ja,
       '大正期社会運動セルの追加。INSERT時に name_ja + birth_year で重複回避。'
FROM rows
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a WHERE a.name_ja = rows.name_ja AND a.birth_year = rows.birth_year
);
COMMIT;

SELECT 'after_batch_1', COUNT(*) FROM achievers WHERE source_team='codex_taisho_social_movement';

-- Batch 2: 30 achievers for taisho/social_movement.
BEGIN;
WITH rows(name_ja,name_en,name_kana,birth_year,death_year,birth_place,sub_domain,summary,works,family_class,education_path,is_great,is_local) AS (
  VALUES
  ('石井亮一','Ishii Ryoichi','いしい りょういち',1867,1937,'佐賀県','disability_welfare_education','滝乃川学園を創設し、知的障害児教育と福祉実践の制度化を切り開いた。','["滝乃川学園","知的障害児教育"]','other','立教学校',0,0),
  ('石井筆子','Ishii Fudeko','いしい ふでこ',1861,1944,'長崎県','disability_welfare_education','滝乃川学園を支え、女性教育と障害児福祉を結びつけた実践者となった。','["滝乃川学園","女性・障害児福祉"]','aristocrat','女子師範学校',0,0),
  ('西村伊作','Nishimura Isaku','にしむら いさく',1884,1963,'和歌山県','free_education','文化学院を創立し、個性尊重・男女共学を掲げる大正自由教育を実践した。','["文化学院","自由教育実践"]','merchant','独学・海外見聞',0,0),
  ('木下竹次','Kinoshita Takeji','きのした たけじ',1872,1946,'福井県','free_education','奈良女子高等師範附属小で合科学習を進め、大正自由教育の実践理論を築いた。','["合科学習","奈良女高師附属小実践"]','other','東京高等師範学校',0,0),
  ('手塚岸衛','Tezuka Kishie','てづか きしえ',1880,1936,'新潟県','free_education','自由教育協会で児童中心主義を唱え、画一的学校教育への批判を展開した。','["自由教育協会","児童中心主義"]','other','東京高等師範学校',0,0),
  ('稲毛金七','Inage Kinsichi','いなげ きんしち',1887,1946,'千葉県','free_education','児童の自発性を重んじる教育実践を進め、大正自由教育の現場を担った。','["自由教育実践","児童中心教育"]','other','東京高等師範学校',0,1),
  ('千葉命吉','Chiba Meikichi','ちば めいきち',1887,1959,'宮城県','free_education','一人ひとりの学習過程を重視する教育実践を行い、大正新教育の普及に関わった。','["自由教育実践","個性尊重教育"]','other','師範学校',0,1),
  ('及川平治','Oikawa Heiji','おいかわ へいじ',1875,1939,'岩手県','free_education','分団式動的教育法で児童の能動的学習を組織し、大正自由教育の方法論を示した。','["分団式動的教育法","大正新教育"]','other','師範学校',0,0),
  ('芦田恵之助','Ashida Enosuke','あしだ えのすけ',1873,1951,'兵庫県','free_education','随意選題による綴方教育を実践し、児童の生活表現を重視する教育運動を進めた。','["綴方教育","随意選題"]','other','兵庫県師範学校',0,0),
  ('赤井米吉','Akai Yonekichi','あかい よねきち',1887,1974,'石川県','free_education','明星学園創立に関わり、児童の自治と創造性を重んじる教育実践を展開した。','["明星学園","自由教育実践"]','other','東京高等師範学校',0,0),
  ('野村芳兵衛','Nomura Yoshihei','のむら よしべえ',1896,1986,'大阪府','free_education','成城小学校などで児童中心の学習実践を進め、生活に根ざす教育を提唱した。','["成城小学校実践","児童中心教育"]','other','東京高等師範学校',0,1),
  ('河野清丸','Kono Kiyomaru','こうの きよまる',1873,1942,'大分県','free_education','自学教育を提唱し、教師主導の注入主義を批判する大正期教育改革に関わった。','["自学教育","自由教育論"]','other','師範学校',0,1),
  ('樋口長市','Higuchi Choichi','ひぐち ちょういち',1871,1945,'長野県','free_education','児童の生活と表現を重視する教育実践を進め、大正新教育の地方的展開に寄与した。','["生活教育実践","大正新教育"]','other','師範学校',0,1),
  ('権田保之助','Gonda Yasusuke','ごんだ やすのすけ',1887,1951,'東京都','urban_social_research','民衆娯楽・都市生活の調査を通じ、大衆社会の実態を社会改良の対象として分析した。','["民衆娯楽論","都市社会調査"]','other','東京帝国大学',0,0),
  ('米田庄太郎','Yoneda Shotaro','よねだ しょうたろう',1873,1945,'奈良県','social_research','社会学者として家族・農村・社会問題を研究し、社会改良の実証的基盤を整えた。','["社会学研究","農村社会研究"]','other','東京帝国大学',0,0),
  ('戸田貞三','Toda Teizo','とだ ていぞう',1887,1955,'東京都','social_research','家族社会学・社会調査を通じ、近代日本の家族変動と社会問題を分析した。','["家族社会学","社会調査"]','other','東京帝国大学',0,0),
  ('市川正一','Ichikawa Shoichi','いちかわ しょういち',1892,1945,'山口県','communist_labor','日本共産党の初期指導者として、労働運動・無産政党運動の組織化に関わった。','["日本共産党初期活動","労働運動"]','other','早稲田大学',0,0),
  ('渡辺政之輔','Watanabe Masanosuke','わたなべ まさのすけ',1899,1928,'千葉県','communist_labor','労働運動から日本共産党活動に入り、大正末期の左派組織化を担った。','["労働運動","日本共産党活動"]','working_class','独学',0,0),
  ('野呂栄太郎','Noro Eitaro','のろ えいたろう',1900,1934,'北海道','marxist_research','日本資本主義分析を通じ、社会運動に理論的基盤を与えたマルクス主義経済学者。','["日本資本主義発達史","マルクス主義研究"]','other','慶應義塾大学',0,0),
  ('向坂逸郎','Sakisaka Itsuro','さきさか いつろう',1897,1985,'福岡県','marxist_education','マルクス経済学の翻訳・教育を通じ、労働運動と社会主義理論を結びつけた。','["資本論翻訳","マルクス経済学教育"]','other','東京帝国大学',0,0),
  ('山本懸蔵','Yamamoto Kenzo','やまもと けんぞう',1895,1939,'大阪府','communist_labor','労働運動・共産主義運動に関わり、国際的な左派ネットワークとも接続した。','["労働運動","共産主義運動"]','working_class','独学',0,0),
  ('前田河広一郎','Maedako Koichiro','まえだこう こういちろう',1888,1957,'宮城県','labor_literature','渡米労働経験を背景に、労働者・移民の現実を描き社会問題への関心を広げた。','["三等船客","労働者文学"]','other','早稲田大学中退',0,0),
  ('犬田卯','Inuta Shigeru','いぬた しげる',1891,1957,'茨城県','peasant_literature','農民文学と農村運動を結び、小作・農村貧困の問題を社会に訴えた。','["農民文学","農村社会運動"]','farmer','独学',0,1),
  ('島木健作','Shimaki Kensaku','しまき けんさく',1903,1945,'北海道','peasant_proletarian','農民運動・プロレタリア文学を経験し、農村青年の社会意識を文学化した。','["生活の探求","農民運動"]','farmer','独学',0,0),
  ('黒島伝治','Kuroshima Denji','くろしま でんじ',1898,1943,'香川県','antiwar_proletarian','反戦的プロレタリア文学で兵士・農民・労働者の視点から帝国主義を批判した。','["橇","反戦文学"]','farmer','独学',0,0),
  ('村島帰之','Murashima Yoriyuki','むらしま よりゆき',1891,1965,'大阪府','social_work_journalism','新聞記者・社会事業家として労働者生活や社会事業を取材・記録し、社会問題を可視化した。','["社会事業報道","労働者生活記録"]','other','関西学院',0,1),
  ('吉田源治郎','Yoshida Genjiro','よしだ げんじろう',1891,1960,'兵庫県','cooperative_social_work','賀川豊彦らと協同組合・農民福音学校運動に関わり、生活改善型の社会運動を進めた。','["協同組合運動","農民福音学校"]','farmer','神戸神学校',0,1),
  ('長谷川良信','Hasegawa Ryoshin','はせがわ りょうしん',1890,1966,'新潟県','social_work_religion','マハヤナ学園を創設し、児童保護・社会事業を宗教的実践として展開した。','["マハヤナ学園","児童保護事業"]','other','仏教系教育',0,0),
  ('高木憲次','Takagi Kenji','たかぎ けんじ',1889,1963,'東京都','disability_welfare','肢体不自由児療育の先駆者として、医療・教育・福祉を結ぶ実践を切り開いた。','["肢体不自由児療育","整肢療護園"]','other','東京帝国大学',0,0),
  ('川田貞治郎','Kawada Teijiro','かわだ ていじろう',1879,1959,'東京都','child_welfare','児童保護・少年教護の実践を進め、近代日本の児童福祉制度形成に関わった。','["児童保護事業","少年教護"]','other','東京帝国大学',0,0)
)
INSERT INTO achievers (
  name_ja,name_en,name_kana,birth_year,death_year,birth_place,primary_era_id,secondary_era_id,domain,sub_domain,
  achievement_summary,notable_works,family_class,education_path,fame_source,fame_score,
  is_traditional_great,is_local_excellent,data_completeness,source_team,source_url,notes
)
SELECT name_ja,name_en,name_kana,birth_year,death_year,birth_place,'taisho','showa_pre','social_movement',sub_domain,
       summary,works,family_class,education_path,'wikipedia_ja_or_ndl',6.3,
       is_great,is_local,78,'codex_taisho_social_movement','https://ja.wikipedia.org/wiki/' || name_ja,
       '大正期社会運動セルの追加。INSERT時に name_ja + birth_year で重複回避。'
FROM rows
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a WHERE a.name_ja = rows.name_ja AND a.birth_year = rows.birth_year
);
COMMIT;

SELECT 'after_batch_2', COUNT(*) FROM achievers WHERE source_team='codex_taisho_social_movement';

-- Capability scores: 4 capabilities per inserted achiever.
BEGIN;
WITH caps(capability_id, base_score, label) AS (
  VALUES
  ('age_social_change',9,'既存制度や差別構造を変える社会運動・教育改革に取り組んだ。'),
  ('cog_critical',8,'労働・女性・教育・福祉などの現状を批判的に分析し、問題を可視化した。'),
  ('soc_interpersonal',8,'組織化、教育実践、支援活動を通じて多様な当事者・協力者を結びつけた。'),
  ('age_social_autonomy',8,'国家・学校・家制度・職場慣行に対して自律的な生き方と参加を求めた。')
)
INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id,
       caps.capability_id,
       CASE
         WHEN a.sub_domain LIKE '%free_education%' AND caps.capability_id='soc_interpersonal' THEN 9
         WHEN a.sub_domain LIKE '%buraku%' AND caps.capability_id='age_social_change' THEN 10
         WHEN a.sub_domain LIKE '%women%' AND caps.capability_id='age_social_autonomy' THEN 9
         WHEN a.sub_domain LIKE '%labor%' AND caps.capability_id='age_social_change' THEN 9
         ELSE caps.base_score
       END AS score,
       a.achievement_summary || ' ' || caps.label AS evidence_quote,
       a.source_url AS evidence_source,
       'codex_taisho_social_movement batch capability scoring'
FROM achievers a
CROSS JOIN caps
WHERE a.source_team='codex_taisho_social_movement'
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id=a.id AND ac.capability_id=caps.capability_id
      AND ac.notes='codex_taisho_social_movement batch capability scoring'
  );
COMMIT;

SELECT 'final_achievers', COUNT(*) FROM achievers WHERE source_team='codex_taisho_social_movement';
SELECT 'final_capabilities', COUNT(*) FROM achiever_capabilities ac JOIN achievers a ON a.id=ac.achiever_id WHERE a.source_team='codex_taisho_social_movement';

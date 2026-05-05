BEGIN;

CREATE TEMP TABLE pending_showa_pre_social_movement (
  name_ja TEXT PRIMARY KEY,
  name_en TEXT,
  name_kana TEXT,
  birth_year INTEGER,
  death_year INTEGER,
  birth_place TEXT,
  sub_domain TEXT,
  achievement_summary TEXT,
  notable_works TEXT,
  family_class TEXT,
  education_path TEXT,
  fame_score REAL,
  is_traditional_great INTEGER,
  is_local_excellent INTEGER,
  data_completeness INTEGER,
  source_url TEXT,
  notes TEXT
);

INSERT INTO pending_showa_pre_social_movement VALUES
('向坂逸郎','Itsuro Sakisaka','さきさか いつろう',1897,1985,'福岡県','労働運動・社会主義研究','マルクス経済学の教育と社会主義運動を通じて、戦前の労働者教育と理論形成を支えた。','["マルクス経済学講義","社会主義協会"]','other','東京帝国大学経済学部',7.0,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=向坂逸郎','昭和前期の社会主義理論・労働者教育。'),
('野呂栄太郎','Eitaro Noro','のろ えいたろう',1900,1934,'北海道','社会主義研究・抵抗運動','日本資本主義論争で講座派の中核を担い、治安維持法下の弾圧で獄死した。','["日本資本主義発達史"]','other','慶應義塾大学',8.0,0,0,85,'https://ja.wikipedia.org/wiki/Special:Search?search=野呂栄太郎','思想弾圧への抵抗を含む。'),
('瀧川幸辰','Yukitoki Takigawa','たきがわ ゆきとき',1891,1962,'岡山県','学問の自由・自由主義抵抗','滝川事件で大学自治と学問の自由を象徴する存在となり、思想統制への抵抗の焦点となった。','["刑法講義","滝川事件"]','other','京都帝国大学法科大学',8.0,1,0,90,'https://ja.wikipedia.org/wiki/Special:Search?search=瀧川幸辰','自由主義的抵抗運動として採録。'),
('河合栄治郎','Eijiro Kawai','かわい えいじろう',1891,1944,'東京府','自由主義・社会思想','自由主義と社会政策を結び、著作発禁・休職処分に抗して戦時下の知的抵抗を示した。','["学生に与う","ファッシズム批判"]','other','東京帝国大学',8.0,1,0,90,'https://ja.wikipedia.org/wiki/Special:Search?search=河合栄治郎','自由主義者として反ファシズム言説を形成。'),
('岩佐作太郎','Sakutaro Iwasa','いわさ さくたろう',1879,1967,'千葉県','アナキズム・労働運動','無政府主義運動の古参として労働者組織と反権力思想の継承に関わった。','["労働運動社","アナキズム運動"]','working_class','尋常小学校',6.5,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=岩佐作太郎','地域・職工層を含む運動史要員。'),
('新居格','Itaru Nii','にい いたる',1888,1951,'徳島県','社会評論・都市自治','アナキズム・協同自治の思想を背景に、戦前の都市自治論と社会批評を展開した。','["一隅より","都市自治論"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=新居格','評論を通じた社会運動。'),
('松谷天光光','Tenko Matsutani','まつたに てんこうこう',1919,2012,'東京府','女性政治参加・労働運動','戦前期から女性の社会参加を志向し、戦後初の女性代議士世代として政治参画の道を開いた。','["女性代議士活動"]','other','日本女子大学校',7.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=松谷天光光','主活動は戦後だが昭和前期世代の女性参政枠。'),
('竹中勝男','Katsuo Takenaka','たけなか かつお',1898,1959,'長崎県','社会福祉・社会政策','同志社で厚生理論を研究し、戦時下から社会福祉学の制度化と社会保障論の基礎を築いた。','["社会福祉研究","社会保障"]','other','同志社大学',6.0,0,1,80,'https://kotobank.jp/word/竹中勝男-1088738','コトバンクで生没・経歴確認。'),
('北浦千太郎','Sentaro Kitaura','きたうら せんたろう',1901,1961,'長野県','労働運動・印刷工組合','印刷工として労働組合運動に入り、共産党再建と三・一五事件での検挙を経験した現場活動家。','["東京印刷工組合連合会","三・一五事件"]','working_class','難波小学校',6.5,0,1,85,'https://kotobank.jp/word/北浦千太郎-1069233','コトバンクで生没・経歴確認。'),
('木村京太郎','Kyotaro Kimura','きむら きょうたろう',1902,1988,'奈良県','部落解放運動','全国水平社から部落解放運動に関わり、差別撤廃の組織化と啓発を進めた。','["全国水平社","部落解放運動"]','working_class','小学校卒',6.5,0,1,80,'https://ja.wikipedia.org/wiki/Special:Search?search=木村京太郎','水平社系活動家。'),
('朝田善之助','Zennosuke Asada','あさだ ぜんのすけ',1902,1983,'京都府','部落解放運動','水平社運動から戦後の部落解放運動へ連続する組織活動を担った。','["全国水平社","部落解放同盟"]','working_class','小学校卒',7.0,0,1,85,'https://ja.wikipedia.org/wiki/Special:Search?search=朝田善之助','差別撤廃の現場リーダー。'),
('江口渙','Kan Eguchi','えぐち かん',1887,1975,'東京府','プロレタリア文化運動','作家同盟などを通じ、プロレタリア文学運動を社会運動の表現基盤として組織した。','["日本プロレタリア作家同盟"]','other','早稲田大学中退',6.5,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=江口渙','文化運動枠。'),
('中野鈴子','Suzuko Nakano','なかの すずこ',1906,1958,'福井県','女性・プロレタリア文学運動','プロレタリア詩と反戦的表現を通じ、女性労働者の視点を社会運動に接続した。','["プロレタリア詩"]','other','福井県立福井高等女学校',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=中野鈴子','女性表現者として採録。'),
('岡邦雄','Kunio Oka','おか くにお',1890,1971,'東京府','科学運動・唯物論研究','唯物論研究会などで科学的世界観を普及し、思想統制下の知識人運動を担った。','["唯物論研究会","科学論"]','other','東京帝国大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=岡邦雄','科学運動・抵抗思想。'),
('鹿地亘','Wataru Kaji','かじ わたる',1903,1982,'大分県','反戦・国際連帯','中国での反戦宣伝活動などを通じ、日本軍国主義への国際的抵抗運動に関わった。','["反戦同盟","中国での反戦活動"]','other','東京帝国大学中退',7.0,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=鹿地亘','国際反戦運動。'),
('高倉テル','Teru Takakura','たかくら てる',1891,1986,'高知県','社会主義・農民文学','農民・労働者の生活を描く文学と社会主義運動を結び、戦前左翼文化を支えた。','["農民文学","社会主義運動"]','other','早稲田大学',6.0,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=高倉テル','文化運動枠。'),
('宮地嘉六','Karoku Miyachi','みやち かろく',1884,1958,'岐阜県','労働文学・社会運動','労働者生活の経験を文学化し、プロレタリア文化運動の初期基盤を形成した。','["坑夫","労働文学"]','working_class','独学',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=宮地嘉六','労働者出身の表現運動。'),
('羽仁説子','Setsuko Hani','はに せつこ',1903,1987,'東京府','女性教育・生活運動','自由学園・婦人之友系の教育実践を基盤に、女性の生活改善と教育活動を進めた。','["婦人之友","自由学園"]','other','自由学園',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=羽仁説子','女性生活運動。'),
('住井すゑ','Sue Sumii','すみい すえ',1902,1997,'奈良県','差別撤廃・女性表現','被差別部落への関心と女性の生活経験を文学・社会批評に結び、差別問題を可視化した。','["橋のない川"]','farmer','奈良県立郡山高等女学校',7.0,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=住井すゑ','主著は戦後だが戦前から活動。'),
('長谷川テル','Teru Hasegawa','はせがわ てる',1912,1947,'山梨県','反戦・エスペラント運動','中国から日本軍向け反戦放送を行い、エスペラントを国際連帯の手段として用いた。','["反戦放送","エスペラント運動"]','other','奈良女子高等師範学校中退',7.5,0,0,85,'https://ja.wikipedia.org/wiki/Special:Search?search=長谷川テル','女性反戦活動家。'),
('佐々木孝丸','Takamaru Sasaki','ささき たかまる',1898,1986,'北海道','プロレタリア演劇運動','左翼劇場・新劇を通じて労働者文化と反体制表現の場を組織した。','["左翼劇場","新劇運動"]','other','早稲田大学中退',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=佐々木孝丸','演劇運動枠。'),
('佐多忠隆','Tadataka Sata','さた ただたか',1904,1968,'長崎県','労働運動・社会主義政治','戦前の労働運動・社会主義運動に関わり、弾圧下での組織活動を経験した。','["労働運動","社会主義運動"]','other','東京帝国大学',6.0,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=佐多忠隆','左派政治運動。'),
('青野季吉','Sueyoshi Aono','あおの すえきち',1890,1961,'新潟県','プロレタリア文学運動','プロレタリア文学理論を形成し、文学を労働者運動の批評装置として位置づけた。','["プロレタリア文学評論"]','other','早稲田大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=青野季吉','文化運動理論。'),
('前田河広一郎','Koichiro Maedako','まえだこう こういちろう',1888,1957,'宮城県','労働文学・移民労働','労働者・移民の経験を描き、プロレタリア文学運動の国際的視野を広げた。','["三等船客","労働文学"]','other','早稲田大学中退',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=前田河広一郎','労働者表象。'),
('橋浦泰雄','Yasuo Hashiura','はしうら やすお',1888,1979,'鳥取県','農民美術・生活改善','農村生活と民衆芸術を結び、農民の自己表現と地域文化運動を支援した。','["農民美術運動","民俗調査"]','farmer','東京美術学校',5.5,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=橋浦泰雄','農村文化運動。'),
('青柳盛雄','Morio Aoyagi','あおやぎ もりお',1903,1976,'群馬県','労働弁護・救援運動','治安維持法事件などの弁護・救援を通じ、弾圧下の社会運動を法的に支えた。','["治安維持法事件弁護","救援運動"]','other','中央大学',6.5,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=青柳盛雄','法曹による運動支援。'),
('中村高一','Koichi Nakamura','なかむら こういち',1897,1980,'山梨県','人権派弁護士・労働運動','労働事件・思想事件の弁護を担い、社会運動の防衛線を法廷で支えた。','["労働事件弁護","思想事件弁護"]','other','東京帝国大学',6.5,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=中村高一','法曹支援。'),
('山本懸蔵','Kenzo Yamamoto','やまもと けんぞう',1895,1939,'茨城県','共産主義運動・国際連帯','労働運動から共産主義運動に入り、国際組織との連携を担ったがスターリン期に粛清された。','["日本共産党","コミンテルン"]','working_class','小学校卒',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=山本懸蔵','国際共産主義運動。'),
('宮本百合子','Yuriko Miyamoto','みやもと ゆりこ',1899,1951,'東京府','女性・プロレタリア文化運動','女性の自立と反戦・民主主義の課題を文学と評論で結び、戦前左翼文化運動に参加した。','["伸子","播州平野"]','other','日本女子大学校中退',7.5,0,0,85,'https://ja.wikipedia.org/wiki/Special:Search?search=宮本百合子','女性文化運動。'),
('平野力三','Rikizo Hirano','ひらの りきぞう',1898,1981,'福岡県','農民運動・無産政党','日本農民組合などで農民運動を進め、無産政党運動と農村問題を結びつけた。','["日本農民組合","無産政党運動"]','farmer','早稲田大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=平野力三','農民運動。'),
('太田典礼','Tenrei Ota','おおた てんれい',1900,1985,'京都府','産児調節・社会改革','産児調節・優生保護をめぐる議論に関わり、女性の身体と社会政策の改革を唱えた。','["産児調節運動","社会医学"]','other','京都帝国大学',6.0,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=太田典礼','現代的評価に留意が必要な社会改革論。'),
('金子文子','Fumiko Kaneko','かねこ ふみこ',1903,1926,'神奈川県','アナキズム・植民地抵抗','朴烈とともに天皇制国家への抵抗を示し、大逆事件後のアナキズム弾圧を象徴した。','["何が私をこうさせたか","朴烈事件"]','working_class','尋常小学校',8.0,1,0,90,'https://ja.wikipedia.org/wiki/Special:Search?search=金子文子','1926年没で昭和初年に接続。'),
('朴烈','Pak Yol','ぱく よる',1902,1974,'慶尚北道','植民地抵抗・アナキズム','朝鮮独立運動とアナキズムを結び、日本帝国下の植民地支配に抵抗した。','["朴烈事件","不逞社"]','working_class','京城高等普通学校中退',8.0,1,0,90,'https://ja.wikipedia.org/wiki/Special:Search?search=朴烈','在日朝鮮人抵抗運動。'),
('金天海','Kim Chon-hae','きん てんかい',1898,NULL,'慶尚南道','在日朝鮮人労働運動','在日朝鮮人労働者の組織化と民族運動に関わり、植民地支配下の権利要求を担った。','["在日本朝鮮労働総同盟","在日朝鮮人運動"]','working_class','不詳',7.0,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=金天海','没年は資料により未確定。'),
('違星北斗','Hokuto Iboshi','いぼし ほくと',1901,1929,'北海道','アイヌ権利・文化抵抗','短歌と評論でアイヌへの差別を告発し、同化圧力下の民族的尊厳を表現した。','["違星北斗遺稿"]','working_class','小学校卒',7.0,0,1,85,'https://ja.wikipedia.org/wiki/Special:Search?search=違星北斗','アイヌ民族運動・表現。'),
('森竹竹市','Takeichi Moritake','もりたけ たけいち',1902,1976,'北海道','アイヌ文化運動','アイヌの権利と文化継承を訴え、同化政策下で民族文化の記録と発信を続けた。','["原始林","アイヌ文化活動"]','working_class','不詳',6.0,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=森竹竹市','アイヌ文化指導者。'),
('西光万吉','Mankichi Saiko','さいこう まんきち',1895,1970,'奈良県','部落解放運動','全国水平社創立に関わり、水平社宣言の思想を通じて差別撤廃運動を方向づけた。','["水平社宣言","全国水平社"]','working_class','中学校中退',8.0,1,0,90,'https://ja.wikipedia.org/wiki/Special:Search?search=西光万吉','水平社創立者。'),
('阪本清一郎','Seiichiro Sakamoto','さかもと せいいちろう',1892,1987,'奈良県','部落解放運動','全国水平社創立に参加し、地域から差別撤廃の組織化を進めた。','["全国水平社","水平社運動"]','working_class','不詳',7.0,0,1,85,'https://ja.wikipedia.org/wiki/Special:Search?search=阪本清一郎','水平社創立メンバー。'),
('北原泰作','Taisaku Kitahara','きたはら たいさく',1906,1981,'長野県','部落解放・軍隊内差別告発','軍隊内差別への抵抗で知られ、部落差別を国家組織内の人権問題として可視化した。','["軍隊内差別告発","水平社運動"]','working_class','不詳',6.5,0,1,80,'https://ja.wikipedia.org/wiki/Special:Search?search=北原泰作','現場からの差別告発。'),
('河野密','Mitsuru Kono','こうの みつる',1897,1981,'高知県','労働運動・無産政党','労働運動と無産政党活動を通じ、戦前社会民主主義の組織形成に関わった。','["無産政党運動","労働運動"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=河野密','社会民主主義系。'),
('鈴木茂三郎','Mosaburo Suzuki','すずき もさぶろう',1893,1970,'愛知県','社会主義・反軍国主義','無産政党運動と反軍国主義的言論に関わり、戦前・戦後の社会党系運動をつないだ。','["無産政党運動","日本社会党"]','other','早稲田大学',7.0,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=鈴木茂三郎','左派政治運動。'),
('川俣清音','Kiyoto Kawamata','かわまた きよと',1899,1972,'山形県','農民運動・社会党運動','農民運動を基盤に無産政党活動へ参加し、農村の権利要求を政治化した。','["農民運動","日本社会党"]','farmer','明治大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=川俣清音','農民運動。'),
('伊藤律','Ritsu Ito','いとう りつ',1913,1989,'岐阜県','共産主義運動','治安維持法下の共産主義運動に関わり、戦前から戦後地下活動へ連続した組織経験を持った。','["日本共産党","治安維持法"]','other','一高中退',6.0,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=伊藤律','評価の分かれる運動家。'),
('春日庄次郎','Shojiro Kasuga','かすが しょうじろう',1903,1976,'大阪府','労働運動・共産主義','労働者組織と共産主義運動に関わり、戦前弾圧下の組織維持を担った。','["労働運動","日本共産党"]','working_class','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=春日庄次郎','現場組織者。'),
('蔵原惟人','Korehito Kurahara','くらはら これひと',1902,1991,'東京府','プロレタリア文化運動','プロレタリア芸術理論を体系化し、文学・芸術運動の組織方針に影響を与えた。','["プロレタリア芸術論","ナップ"]','other','東京帝国大学',7.0,0,0,85,'https://ja.wikipedia.org/wiki/Special:Search?search=蔵原惟人','文化運動理論。'),
('勝間田清一','Seiichi Katsumata','かつまた せいいち',1908,1989,'静岡県','社会主義・無産政党','青年期から社会主義運動に関わり、戦前の弾圧経験を戦後社会党活動へ接続した。','["社会主義運動","日本社会党"]','other','早稲田大学',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=勝間田清一','戦前経験を持つ社会党系。'),
('稲村順三','Junzo Inamura','いなむら じゅんぞう',1900,1955,'新潟県','農民運動','日本農民組合などで小作農の権利擁護と農村組織化に取り組んだ。','["日本農民組合","農民運動"]','farmer','早稲田大学',5.5,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=稲村順三','農村現場リーダー。'),
('山花秀雄','Hideo Yamanaka','やまはな ひでお',1904,1987,'兵庫県','労働運動・社会党運動','戦前の労働運動経験を持ち、労働組合と社会党政治の接続を担った。','["労働運動","日本社会党"]','working_class','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=山花秀雄','労働組合系。'),
('櫛田民蔵','Tamizo Kushida','くしだ たみぞう',1885,1934,'福島県','社会主義経済論','マルクス経済学の研究と普及を通じ、戦前社会主義運動の理論的基盤を支えた。','["マルクス経済学研究"]','other','東京帝国大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=櫛田民蔵','理論運動。'),
('猪俣津南雄','Tsunanobu Inomata','いのまた つなお',1889,1942,'新潟県','社会主義経済論・労農派','労農派マルクス主義の理論家として、日本資本主義論争と社会主義運動に関わった。','["日本資本主義論争","労農派"]','other','早稲田大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=猪俣津南雄','労農派理論。'),
('丸岡秀子','Hideko Maruoka','まるおか ひでこ',1903,1990,'長野県','農村女性・生活改善','農村女性の生活・労働問題を取り上げ、女性の社会参加と生活改善運動を支えた。','["農村女性論","生活改善運動"]','farmer','日本女子大学校',6.0,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=丸岡秀子','女性・農村現場。'),
('山高しげり','Shigeri Yamataka','やまたか しげり',1899,1977,'三重県','女性運動・母性保護','婦人運動に参加し、母性保護・女性の地位向上を社会政策課題として訴えた。','["婦人運動","母性保護運動"]','other','日本女子大学校',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=山高しげり','女性活動家。'),
('山根キク','Kiku Yamane','やまね きく',1893,1965,'鳥取県','女性ジャーナリズム・社会批評','女性記者・評論家として婦人問題を報じ、女性の社会的発言の場を広げた。','["婦人問題評論","女性ジャーナリズム"]','other','日本女子大学校',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=山根キク','女性メディア活動。'),
('関鑑子','Akiko Seki','せき あきこ',1899,1973,'東京府','労働歌・文化運動','労働歌・合唱運動を通じ、労働者文化と平和運動の表現基盤を作った。','["うたごえ運動","労働歌"]','other','東京音楽学校',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=関鑑子','文化運動。'),
('石垣栄太郎','Eitaro Ishigaki','いしがき えいたろう',1893,1958,'和歌山県','反戦美術・在外社会運動','米国で労働者・反ファシズムを描き、在外日本人の反戦美術運動に関わった。','["反戦美術","在米日本人社会運動"]','other','独学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=石垣栄太郎','在外反戦文化運動。'),
('古在由重','Yoshishige Kozai','こざい よししげ',1901,1990,'東京府','唯物論研究・反戦思想','唯物論研究会などで思想統制に抗する哲学研究を進め、戦前知識人運動に関わった。','["唯物論研究会","哲学研究"]','other','東京帝国大学',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=古在由重','思想運動。'),
('佐野碩','Seki Sano','さの せき',1905,1966,'天津','プロレタリア演劇・国際文化運動','プロレタリア演劇運動を担い、国外亡命後も反ファシズム演劇の国際的展開に関わった。','["プロレタリア演劇","メキシコ演劇活動"]','other','東京帝国大学中退',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=佐野碩','国際文化運動。'),
('秋田雨雀','Ujaku Akita','あきた うじゃく',1883,1962,'青森県','社会主義文化運動・児童文化','社会主義思想と児童文化運動を結び、民衆教育・文化運動に関与した。','["児童文化運動","社会主義文化運動"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=秋田雨雀','民衆文化運動。'),
('山代巴','Tomo Yamashiro','やましろ ともえ',1912,2004,'広島県','女性・反戦生活記録','農村女性・被爆者の生活記録を通じ、戦争と女性の経験を社会的記憶へ変えた。','["荷車の歌","生活記録運動"]','farmer','広島県立高等女学校',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=山代巴','主活動は戦後だが戦前体験に基づく女性記録。'),
('土岐善麿','Zenmaro Toki','とき ぜんまろ',1885,1980,'東京府','社会批評・生活短歌','生活者の言葉による短歌革新と社会批評を通じ、民衆的表現の拡張に寄与した。','["生活短歌","社会批評"]','other','早稲田大学',5.5,0,0,65,'https://ja.wikipedia.org/wiki/Special:Search?search=土岐善麿','社会運動周辺の表現者。');

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, secondary_era_id, domain, sub_domain, achievement_summary,
  notable_works, family_class, education_path, fame_source, fame_score,
  is_traditional_great, is_local_excellent, data_completeness, source_team,
  source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  'showa_pre', NULL, 'social_movement', sub_domain, achievement_summary,
  notable_works, family_class, education_path, 'wikipedia_or_kotobank', fame_score,
  is_traditional_great, is_local_excellent, data_completeness,
  'codex_showa_pre_social_movement', source_url, notes
FROM pending_showa_pre_social_movement
WHERE rowid <= 50
  AND NOT EXISTS (
    SELECT 1 FROM achievers a
    WHERE a.name_ja = pending_showa_pre_social_movement.name_ja
      AND a.birth_year = pending_showa_pre_social_movement.birth_year
  );

SELECT 'after_batch_50', COUNT(*) FROM achievers
WHERE primary_era_id='showa_pre'
  AND domain='social_movement'
  AND source_team='codex_showa_pre_social_movement';

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, secondary_era_id, domain, sub_domain, achievement_summary,
  notable_works, family_class, education_path, fame_source, fame_score,
  is_traditional_great, is_local_excellent, data_completeness, source_team,
  source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  'showa_pre', NULL, 'social_movement', sub_domain, achievement_summary,
  notable_works, family_class, education_path, 'wikipedia_or_kotobank', fame_score,
  is_traditional_great, is_local_excellent, data_completeness,
  'codex_showa_pre_social_movement', source_url, notes
FROM pending_showa_pre_social_movement
WHERE rowid > 50
  AND NOT EXISTS (
    SELECT 1 FROM achievers a
    WHERE a.name_ja = pending_showa_pre_social_movement.name_ja
      AND a.birth_year = pending_showa_pre_social_movement.birth_year
  );

SELECT 'after_batch_60', COUNT(*) FROM achievers
WHERE primary_era_id='showa_pre'
  AND domain='social_movement'
  AND source_team='codex_showa_pre_social_movement';

CREATE TEMP TABLE pending_capabilities (
  name_ja TEXT,
  capability_id TEXT,
  score INTEGER,
  evidence_quote TEXT
);

INSERT INTO pending_capabilities VALUES
('向坂逸郎','cog_logical',8,'マルクス経済学の教育で社会主義理論を体系化した。'),('向坂逸郎','age_social_change',8,'労働者教育を通じて社会主義運動を支えた。'),('向坂逸郎','age_resilience',7,'戦前から戦後まで弾圧環境を越えて理論活動を継続した。'),
('野呂栄太郎','cog_critical',9,'日本資本主義論争で構造批判を担った。'),('野呂栄太郎','cog_systems',8,'資本主義発達を歴史構造として分析した。'),('野呂栄太郎','age_social_change',9,'治安維持法下で社会主義運動に関与した。'),
('瀧川幸辰','age_social_autonomy',9,'滝川事件で学問の自由をめぐる抵抗の象徴となった。'),('瀧川幸辰','cog_critical',8,'刑法学の立場から国家権力と法の関係を問うた。'),('瀧川幸辰','age_resilience',8,'休職処分後も法学教育と大学自治の課題に関わった。'),
('河合栄治郎','cog_critical',9,'ファシズム批判と自由主義擁護を展開した。'),('河合栄治郎','val_tolerance',8,'個人の自由と社会政策を結ぶ思想を示した。'),('河合栄治郎','age_resilience',8,'著作発禁・休職処分下でも言論活動を続けた。'),
('岩佐作太郎','age_social_change',8,'アナキズムと労働運動の組織化に関わった。'),('岩佐作太郎','age_social_autonomy',8,'反権力的な自律思想を実践した。'),('岩佐作太郎','soc_interpersonal',7,'運動内部の連絡・継承役を担った。'),
('新居格','cog_creativity',7,'自治と協同をめぐる社会評論を展開した。'),('新居格','age_social_autonomy',8,'都市自治論で生活者主体の社会を構想した。'),('新居格','cog_critical',7,'国家中心の統治観を批判的に論じた。'),
('松谷天光光','age_social_change',7,'女性の政治参加を切り開く世代となった。'),('松谷天光光','soc_interpersonal',7,'政治参加と組織活動を通じて支持を広げた。'),('松谷天光光','age_resilience',7,'戦前・戦後の制度転換を越えて活動した。'),
('竹中勝男','cog_systems',7,'社会福祉を制度・政策の体系として研究した。'),('竹中勝男','age_social_change',7,'社会保障論を通じて福祉政策の形成に寄与した。'),('竹中勝男','val_collective',7,'厚生・福祉を共同的支援の課題として扱った。'),
('北浦千太郎','age_social_change',8,'印刷工組合と共産主義運動の現場で活動した。'),('北浦千太郎','soc_interpersonal',8,'労働組合の青年幹部として組織化を担った。'),('北浦千太郎','age_resilience',8,'検挙・除名を経験しつつ労働運動を継続した。'),
('木村京太郎','age_social_change',8,'部落解放運動の組織化に取り組んだ。'),('木村京太郎','val_tolerance',8,'差別撤廃を社会的課題として訴えた。'),('木村京太郎','soc_interpersonal',7,'地域と全国組織を結ぶ運動を担った。'),
('朝田善之助','age_social_change',8,'水平社から部落解放運動への継続的活動を担った。'),('朝田善之助','age_resilience',8,'弾圧と戦時体制を越えて運動経験を継承した。'),('朝田善之助','val_tolerance',8,'差別撤廃の理念を組織活動にした。'),
('江口渙','cog_creativity',8,'プロレタリア文学を運動の表現基盤にした。'),('江口渙','age_social_change',7,'作家同盟を通じて文化運動を組織した。'),('江口渙','soc_interpersonal',7,'文学者の結集と運動組織に関わった。'),
('中野鈴子','cog_creativity',8,'詩によって女性労働者の視点を表現した。'),('中野鈴子','age_social_change',7,'プロレタリア文学運動に女性の経験を接続した。'),('中野鈴子','age_resilience',7,'困難な生活条件の中で表現活動を続けた。'),
('岡邦雄','cog_critical',8,'唯物論研究を通じて観念論的統制に対抗した。'),('岡邦雄','cog_systems',8,'科学と社会思想を接続して論じた。'),('岡邦雄','age_social_change',7,'知識人運動として科学的世界観を普及した。'),
('鹿地亘','age_social_change',8,'中国で日本軍国主義への反戦活動に関わった。'),('鹿地亘','cre_cross_domain',8,'文学・宣伝・国際政治を結びつけた。'),('鹿地亘','val_tolerance',8,'国境を越えた反戦連帯を実践した。'),
('高倉テル','cog_creativity',7,'農民・労働者の生活を文学で表現した。'),('高倉テル','age_social_change',7,'社会主義文化運動に参加した。'),('高倉テル','val_collective',7,'農村・労働者の共同的課題を描いた。'),
('宮地嘉六','cog_creativity',7,'労働経験を文学表現へ転換した。'),('宮地嘉六','age_social_autonomy',7,'労働者自身の視点から社会を語った。'),('宮地嘉六','age_social_change',6,'労働文学を通じて社会問題を可視化した。'),
('羽仁説子','soc_interpersonal',8,'教育と生活運動で女性同士の学びを組織した。'),('羽仁説子','age_meta_learning',8,'生活に根ざす教育実践を広げた。'),('羽仁説子','age_social_change',7,'女性の生活改善と社会参加を支えた。'),
('住井すゑ','cog_creativity',8,'差別問題を物語として社会に伝えた。'),('住井すゑ','val_tolerance',9,'被差別部落への差別撤廃を作品の中心課題にした。'),('住井すゑ','age_social_change',7,'文学を通じて人権意識を広げた。'),
('長谷川テル','age_social_change',9,'日本軍向け反戦放送で戦争遂行に抵抗した。'),('長谷川テル','cre_cross_domain',8,'エスペラントと放送を国際連帯に用いた。'),('長谷川テル','age_resilience',8,'国外での困難な条件下で反戦活動を続けた。'),
('佐々木孝丸','cog_creativity',7,'演劇を社会運動の表現手段にした。'),('佐々木孝丸','soc_interpersonal',7,'左翼劇場で集団制作を組織した。'),('佐々木孝丸','age_social_change',7,'プロレタリア演劇運動に参加した。'),
('佐多忠隆','age_social_change',7,'労働運動と社会主義政治に関与した。'),('佐多忠隆','cog_logical',7,'政策・組織論で左派運動を支えた。'),('佐多忠隆','age_resilience',7,'弾圧期を経て社会主義活動を継続した。'),
('青野季吉','cog_critical',8,'プロレタリア文学を理論的に批評した。'),('青野季吉','cog_creativity',7,'文学批評を運動方針の形成に結びつけた。'),('青野季吉','age_social_change',7,'文化運動の理論的支柱となった。'),
('前田河広一郎','cog_creativity',7,'移民・労働者の経験を文学化した。'),('前田河広一郎','val_tolerance',7,'周縁化された労働者の視点を提示した。'),('前田河広一郎','age_social_change',6,'労働文学を通じて社会問題を伝えた。'),
('橋浦泰雄','cre_cross_domain',8,'民俗調査・美術・農村生活を結びつけた。'),('橋浦泰雄','val_traditional',7,'地域の民衆芸術を尊重し再評価した。'),('橋浦泰雄','age_social_change',6,'農民の自己表現を支援した。'),
('青柳盛雄','cog_logical',8,'思想事件・労働事件を法的に防衛した。'),('青柳盛雄','age_social_change',7,'弾圧された運動の救援に関わった。'),('青柳盛雄','val_tolerance',8,'人権と思想の自由を法廷で守った。'),
('中村高一','cog_logical',8,'労働・思想事件の弁護で法理を用いた。'),('中村高一','val_tolerance',8,'思想信条の自由を守る弁護活動を行った。'),('中村高一','age_social_change',7,'社会運動の法的支援を担った。'),
('山本懸蔵','age_social_change',8,'労働運動から国際共産主義運動へ参加した。'),('山本懸蔵','soc_interpersonal',7,'党組織と国際組織の連絡に関わった。'),('山本懸蔵','age_resilience',7,'国外活動と弾圧下で運動を継続した。'),
('宮本百合子','cog_creativity',9,'女性の自立と社会矛盾を文学化した。'),('宮本百合子','age_social_change',8,'プロレタリア文化運動と民主主義運動に参加した。'),('宮本百合子','age_resilience',8,'検挙・病気を経ながら執筆を継続した。'),
('平野力三','age_social_change',8,'農民組合を通じて小作農の権利要求を政治化した。'),('平野力三','soc_interpersonal',8,'農村組織と無産政党を結びつけた。'),('平野力三','val_collective',7,'農民の共同的利益を政策課題にした。'),
('太田典礼','cog_critical',7,'人口・性・社会政策を批判的に論じた。'),('太田典礼','age_social_change',7,'産児調節を社会改革の論点にした。'),('太田典礼','cre_cross_domain',7,'医学と社会運動を接続した。'),
('金子文子','age_social_autonomy',10,'国家と家制度に従属しない自己決定を貫いた。'),('金子文子','age_social_change',9,'天皇制国家への抵抗を示した。'),('金子文子','age_resilience',9,'貧困と拘禁の中で思想を保持した。'),
('朴烈','age_social_change',9,'植民地支配と天皇制国家への抵抗を行った。'),('朴烈','val_tolerance',8,'朝鮮独立と反帝国主義の立場を示した。'),('朴烈','age_resilience',8,'長期拘禁を経ても政治的立場を保った。'),
('金天海','soc_interpersonal',8,'在日朝鮮人労働者の組織化を担った。'),('金天海','age_social_change',8,'民族運動と労働運動を結びつけた。'),('金天海','val_tolerance',8,'植民地下の民族的権利要求を掲げた。'),
('違星北斗','cog_creativity',8,'短歌でアイヌ差別を告発した。'),('違星北斗','val_tolerance',9,'民族的尊厳と差別撤廃を訴えた。'),('違星北斗','age_social_autonomy',8,'同化圧力下でアイヌとしての自己表現を貫いた。'),
('森竹竹市','val_traditional',8,'アイヌ文化の記録と継承に取り組んだ。'),('森竹竹市','val_tolerance',8,'民族差別への問題意識を発信した。'),('森竹竹市','age_social_change',7,'文化活動を通じて権利意識を広げた。'),
('西光万吉','age_social_change',10,'水平社宣言を通じて差別撤廃運動を方向づけた。'),('西光万吉','val_tolerance',10,'人間尊重を部落解放運動の中心理念にした。'),('西光万吉','cog_creativity',8,'解放思想を宣言文として表現した。'),
('阪本清一郎','age_social_change',8,'全国水平社の創立と地域組織化に参加した。'),('阪本清一郎','soc_interpersonal',8,'地域の被差別部落住民を運動へ結集した。'),('阪本清一郎','val_tolerance',9,'差別撤廃の運動を実践した。'),
('北原泰作','age_social_autonomy',8,'軍隊内差別に対して自ら告発行動を起こした。'),('北原泰作','val_tolerance',9,'国家組織内の部落差別を可視化した。'),('北原泰作','age_social_change',8,'個人の抵抗を差別撤廃運動へ接続した。'),
('河野密','soc_interpersonal',7,'労働運動と無産政党をつなぐ組織活動を行った。'),('河野密','age_social_change',7,'社会民主主義の政治運動に関与した。'),('河野密','cog_logical',7,'政策論を通じて運動を制度政治へ接続した。'),
('鈴木茂三郎','cog_critical',8,'軍国主義と社会不平等への批判を展開した。'),('鈴木茂三郎','age_social_change',8,'無産政党から社会党運動へ連続して活動した。'),('鈴木茂三郎','soc_interpersonal',7,'左派政治勢力の組織形成に関わった。'),
('川俣清音','age_social_change',7,'農民運動を通じて農村の権利要求を政治化した。'),('川俣清音','val_collective',7,'農民の共同利益を代表した。'),('川俣清音','soc_interpersonal',7,'地域農民と政党運動を結びつけた。'),
('伊藤律','age_resilience',7,'弾圧下の非合法運動に関わった。'),('伊藤律','soc_interpersonal',6,'地下組織で連絡・活動を担った。'),('伊藤律','age_social_change',6,'共産主義運動に参加した。'),
('春日庄次郎','age_social_change',7,'労働運動と共産主義運動に参加した。'),('春日庄次郎','soc_interpersonal',7,'労働者組織の現場活動を担った。'),('春日庄次郎','age_resilience',7,'戦前弾圧下で活動した。'),
('蔵原惟人','cog_critical',8,'プロレタリア芸術理論を体系化した。'),('蔵原惟人','cre_cross_domain',8,'政治理論と芸術運動を結びつけた。'),('蔵原惟人','age_social_change',8,'文化運動の方針形成に影響した。'),
('勝間田清一','age_social_change',7,'社会主義運動に参加し戦後社会党へ接続した。'),('勝間田清一','age_resilience',7,'弾圧期の経験を政治活動に生かした。'),('勝間田清一','soc_interpersonal',6,'党派内の組織活動を担った。'),
('稲村順三','age_social_change',7,'小作農の権利をめぐる農民運動に関わった。'),('稲村順三','soc_interpersonal',7,'農村の組織化に取り組んだ。'),('稲村順三','val_collective',7,'農民の共同的利益を代表した。'),
('山花秀雄','soc_interpersonal',7,'労働組合の組織活動を担った。'),('山花秀雄','age_social_change',7,'労働者の政治参加を支えた。'),('山花秀雄','age_resilience',6,'戦前から戦後へ運動を継続した。'),
('櫛田民蔵','cog_logical',8,'マルクス経済学を理論的に研究した。'),('櫛田民蔵','cog_critical',8,'資本主義社会を批判的に分析した。'),('櫛田民蔵','age_social_change',7,'社会主義理論の普及で運動を支えた。'),
('猪俣津南雄','cog_systems',8,'日本資本主義を歴史構造として論じた。'),('猪俣津南雄','cog_critical',8,'労農派の立場から社会分析を行った。'),('猪俣津南雄','age_social_change',7,'社会主義運動の理論形成に関与した。'),
('丸岡秀子','val_collective',8,'農村女性の生活課題を共同的に捉えた。'),('丸岡秀子','age_social_change',7,'女性の社会参加と生活改善を進めた。'),('丸岡秀子','soc_interpersonal',7,'農村女性の声を結びつけた。'),
('山高しげり','age_social_change',7,'婦人運動で女性の地位向上を訴えた。'),('山高しげり','val_tolerance',8,'母性保護と女性の権利を社会課題化した。'),('山高しげり','soc_interpersonal',7,'女性団体での組織活動を担った。'),
('山根キク','cog_info',7,'女性記者として婦人問題を報道した。'),('山根キク','age_social_change',6,'女性の社会的発言の場を広げた。'),('山根キク','cog_critical',7,'婦人問題を社会批評として論じた。'),
('関鑑子','cog_creativity',7,'労働歌と合唱を運動表現にした。'),('関鑑子','soc_interpersonal',8,'合唱運動で集団的表現を組織した。'),('関鑑子','age_social_change',7,'音楽を労働・平和運動に接続した。'),
('石垣栄太郎','cog_creativity',8,'反戦・労働者主題を絵画で表現した。'),('石垣栄太郎','val_tolerance',7,'移民・労働者への共感を作品に込めた。'),('石垣栄太郎','cre_cross_domain',7,'美術と国際社会運動を接続した。'),
('古在由重','cog_critical',8,'唯物論哲学で思想統制に抗した。'),('古在由重','cog_logical',8,'哲学的論証で社会認識を鍛えた。'),('古在由重','age_social_change',7,'知識人運動に参加した。'),
('佐野碩','cog_creativity',8,'演劇を反ファシズム表現へ転換した。'),('佐野碩','cre_cross_domain',8,'日本・欧米・メキシコの演劇運動を結んだ。'),('佐野碩','age_resilience',7,'亡命後も演劇活動を継続した。'),
('秋田雨雀','cog_creativity',7,'児童文化と社会主義的表現を結びつけた。'),('秋田雨雀','age_social_change',7,'民衆教育・文化運動に関わった。'),('秋田雨雀','val_tolerance',7,'子どもと民衆の視点を尊重した。'),
('山代巴','cog_creativity',7,'生活記録で女性と戦争の経験を伝えた。'),('山代巴','val_tolerance',8,'被爆者・農村女性の声を社会化した。'),('山代巴','age_social_change',7,'記録運動を通じて社会的記憶を形成した。'),
('土岐善麿','cog_creativity',7,'生活短歌で民衆的表現を広げた。'),('土岐善麿','cog_info',6,'新聞・出版を通じて社会的表現を流通させた。'),('土岐善麿','age_social_autonomy',6,'定型に拘束されない生活者表現を追求した。');

INSERT INTO achiever_capabilities (
  achiever_id, capability_id, score, evidence_quote, evidence_source, notes
)
SELECT
  a.id, pc.capability_id, pc.score, pc.evidence_quote, a.source_url,
  'codex_showa_pre_social_movement capability scoring'
FROM pending_capabilities pc
JOIN achievers a ON a.name_ja = pc.name_ja
WHERE a.source_team = 'codex_showa_pre_social_movement'
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id = a.id
      AND ac.capability_id = pc.capability_id
      AND ac.evidence_quote = pc.evidence_quote
  );

SELECT 'capabilities_inserted', COUNT(*)
FROM achiever_capabilities ac
JOIN achievers a ON a.id = ac.achiever_id
WHERE a.source_team = 'codex_showa_pre_social_movement';

SELECT 'traditional_count', SUM(is_traditional_great), COUNT(*)
FROM achievers
WHERE source_team='codex_showa_pre_social_movement';

COMMIT;

BEGIN;

CREATE TEMP TABLE diaspora_candidates (
  rn INTEGER PRIMARY KEY,
  name_ja TEXT NOT NULL,
  name_en TEXT,
  name_kana TEXT,
  birth_year INTEGER,
  death_year INTEGER,
  birth_place TEXT,
  sub_domain TEXT NOT NULL,
  achievement_summary TEXT NOT NULL,
  notable_works TEXT NOT NULL,
  is_traditional_great INTEGER NOT NULL,
  is_local_excellent INTEGER NOT NULL,
  fame_source TEXT NOT NULL,
  fame_score REAL NOT NULL
);

INSERT INTO diaspora_candidates VALUES
(1,'知里幸恵','Chiri Yukie','チリ ユキエ',1903,1922,'北海道登別市','ainu_language','アイヌ口承文芸を日本語で記録した『アイヌ神謡集』により、アイヌ語・口承文化の近代的保存に決定的な役割を果たした。','["アイヌ神謡集"]',1,0,'wikipedia_ja',8.7),
(2,'萱野茂','Kayano Shigeru','カヤノ シゲル',1926,2006,'北海道二風谷','ainu_rights','二風谷アイヌ資料館の設立、アイヌ語教育、参議院議員としての活動を通じ、アイヌ文化復興と権利回復を全国課題にした。','["アイヌの碑","二風谷アイヌ資料館"]',1,0,'wikipedia_ja',8.8),
(3,'貝澤藤蔵','Kaizawa Tōzō','カイザワ トウゾウ',1888,1966,'北海道平取町','ainu_rights','二風谷地域で土地・生活・文化を守る運動を担い、戦後アイヌ運動の地域基盤形成に寄与した。','[]',0,1,'wikipedia_ja',6.8),
(4,'砂澤ビッキ','Sunazawa Bikky','スナザワ ビッキ',1931,1989,'北海道旭川市','ainu_arts','木彫を現代彫刻へ展開し、アイヌの造形感覚を戦後日本美術の文脈へ接続した。','["風","午前3時の玩具"]',1,0,'wikipedia_ja',8.1),
(5,'宇梶静江','Ukaji Shizue','ウカジ シズエ',1933,NULL,'北海道浦河町','ainu_arts','古布絵作家・詩人として、アイヌ女性の経験、差別、記憶を作品と語りで可視化した。','["大地よ！"]',0,1,'wikipedia_ja',7.1),
(6,'宇梶剛士','Ukaji Takashi','ウカジ タカシ',1962,NULL,'東京都新宿区','ainu_media','俳優活動と母・宇梶静江との発信を通じ、都市生活者としてのアイヌ・ルーツを大衆的認知へつないだ。','[]',0,1,'wikipedia_ja',7.2),
(7,'アシリ・レラ','Asiri Rera','アシリ レラ',1946,NULL,'北海道','ainu_rights','アイヌ文化継承と先住民族の権利回復を訴え、国内外の先住民族ネットワークとも連携した活動を行った。','[]',0,1,'wikipedia_ja',6.9),
(8,'山本多助','Yamamoto Tasuke','ヤマモト タスケ',1904,1993,'北海道阿寒町','ainu_language','阿寒地方のアイヌ文化伝承者として、ユーカラ、生活文化、語彙の記録保存に尽力した。','["アイヌ・モシリ"]',0,1,'wikipedia_ja',6.9),
(9,'違星北斗','Iboshi Hokuto','イボシ ホクト',1901,1929,'北海道余市町','ainu_literature','短歌と評論により、近代日本社会におけるアイヌ青年の自己表現と差別批判を先鋭化した。','["違星北斗遺稿 コタン"]',0,1,'wikipedia_ja',7.2),
(10,'バチェラー八重子','Batchelor Yaeko','バチェラー ヤエコ',1884,1962,'北海道','ainu_literature','アイヌ出身の歌人として短歌と教育活動に携わり、近代アイヌ女性の表現史に足跡を残した。','["若きウタリに"]',0,1,'wikipedia_ja',7.0),
(11,'森竹竹市','Moritake Takeichi','モリタケ タケイチ',1902,1976,'北海道白老町','ainu_literature','詩歌・民俗記録を通じてアイヌの生活と思想を表現し、戦後のアイヌ文芸運動を支えた。','["原始林"]',0,1,'wikipedia_ja',6.7),
(12,'結城庄司','Yūki Shōji','ユウキ ショウジ',1938,1983,'北海道','ainu_rights','アイヌ解放同盟などで先住民族としての権利を主張し、同化政策批判を社会運動へ押し広げた。','[]',0,1,'wikipedia_ja',6.8),
(13,'秋辺日出男','Akibe Hideo','アキベ ヒデオ',1943,NULL,'北海道阿寒町','ainu_performing_arts','阿寒アイヌ工芸協同組合やアイヌ古式舞踊の継承に携わり、観光と文化継承の接点を作った。','[]',0,1,'wikipedia_ja',6.6),
(14,'チカップ美恵子','Chikappu Mieko','チカップ ミエコ',1948,2010,'北海道','ainu_arts','刺繍家・文筆家として、アイヌ文様と女性の経験を結びつけ、文化表象と権利意識を発信した。','["カムイの言霊"]',0,1,'wikipedia_ja',6.9),
(15,'萱野志朗','Kayano Shirō','カヤノ シロウ',1958,NULL,'北海道平取町','ainu_language','萱野茂の後継世代としてアイヌ語教育、文化施設運営、民族共生象徴空間をめぐる議論に関わった。','[]',0,1,'wikipedia_ja',6.5),
(16,'多原香里','Taharah Kaori','タハラ カオリ',1972,NULL,'北海道札幌市','ainu_politics','アイヌ政策推進会議などに関わり、現代のアイヌ女性リーダーとして制度・教育・国際発信を担った。','[]',0,1,'wikipedia_ja',6.4),
(17,'鳩沢佐美夫','Hatozawa Samio','ハトザワ サミオ',1935,1971,'北海道','ainu_literature','アイヌ民族を主題とする文学作品を発表し、戦後アイヌ文学の層を広げた。','["コタンに死す"]',0,1,'wikipedia_ja',6.4),
(18,'川村カ子ト','Kawamura Kaneto','カワムラ カネト',1893,1977,'北海道旭川市','ainu_craft_museum','測量技師として近代インフラに関わり、川村カ子トアイヌ記念館の基礎を築いて文化継承に貢献した。','["川村カ子トアイヌ記念館"]',0,1,'wikipedia_ja',6.9),
(19,'尚真王','Shō Shin','ショウ シン',1465,1527,'琉球王国','okinawa_politics','琉球王国第二尚氏の王として中央集権化、地方統治、対外交易体制を整え、琉球の国家制度を成熟させた。','[]',1,0,'wikipedia_ja',8.1),
(20,'蔡温','Sai On','サイ オン',1682,1762,'琉球王国久米村','okinawa_policy','三司官として農政・林政・治水を重視し、琉球王国の行政実務と社会経済政策を体系化した。','["独物語"]',1,0,'wikipedia_ja',8.0),
(21,'程順則','Tei Junsoku','テイ ジュンソク',1663,1734,'琉球王国久米村','okinawa_education','琉球の儒学者・教育者として中国古典を導入し、琉球士族教育と東アジア外交知の形成に寄与した。','["六諭衍義"]',1,0,'wikipedia_ja',7.8),
(22,'羽地朝秀','Haneji Chōshū','ハネジ チョウシュウ',1617,1676,'琉球王国','okinawa_policy','摂政として王府改革を進め、『中山世鑑』編纂により琉球の歴史叙述と統治理念を整えた。','["中山世鑑"]',1,0,'wikipedia_ja',7.8),
(23,'儀間真常','Gima Shinjō','ギマ シンジョウ',1557,1644,'琉球王国','okinawa_agriculture','サツマイモや木綿、製糖技術の普及に関わったとされ、琉球の農業・産業基盤を拡大した。','[]',1,0,'wikipedia_ja',7.5),
(24,'玉城朝薫','Tamagusuku Chōkun','タマグスク チョウクン',1684,1734,'琉球王国','okinawa_performing_arts','組踊を創始し、琉球王府の儀礼芸能を高度な舞台芸術として制度化した。','["執心鐘入","二童敵討"]',1,0,'wikipedia_ja',7.9),
(25,'恩納なべ','Onna Nabe','オンナ ナベ',1660,NULL,'琉球王国恩納村','okinawa_literature','琉歌の名手として知られ、女性の声による琉球文学の古典的系譜を形成した。','[]',0,1,'wikipedia_ja',6.4),
(26,'仲宗根政善','Nakasone Seizen','ナカソネ セイゼン',1907,1995,'沖縄県今帰仁村','okinawa_language','沖縄語研究と沖縄戦記録に取り組み、言語・記憶・教育を結びつけた沖縄学の重要人物となった。','["沖縄今帰仁方言辞典"]',0,1,'wikipedia_ja',7.0),
(27,'外間守善','Hokama Shuzen','ホカマ シュゼン',1924,2012,'沖縄県','okinawa_studies','沖縄文学・民俗・歴史研究を横断し、沖縄学を戦後日本の学術領域として発展させた。','["沖縄の歴史と文化"]',0,1,'wikipedia_ja',7.0),
(28,'大城立裕','Ōshiro Tatsuhiro','オオシロ タツヒロ',1925,2020,'沖縄県中城村','okinawa_literature','小説『カクテル・パーティー』で芥川賞を受け、占領下沖縄の経験を日本文学に刻んだ。','["カクテル・パーティー"]',1,0,'wikipedia_ja',7.6),
(29,'山之口貘','Yamanokuchi Baku','ヤマノクチ バク',1903,1963,'沖縄県那覇市','okinawa_literature','貧困、漂泊、沖縄出身者の視点を詩に結晶させ、近代詩に独自のユーモアと批評性をもたらした。','["思辨の苑"]',0,1,'wikipedia_ja',7.1),
(30,'比嘉春潮','Higa Shunchō','ヒガ シュンチョウ',1883,1977,'沖縄県','okinawa_studies','沖縄史研究と社会運動を結びつけ、沖縄近現代史の基礎的叙述に貢献した。','["沖縄の歳月"]',0,1,'wikipedia_ja',6.8),
(31,'平良とみ','Taira Tomi','タイラ トミ',1928,2015,'沖縄県那覇市','okinawa_media','沖縄芝居とテレビドラマで沖縄の言葉・生活感を全国に届け、地域文化の大衆的認知を高めた。','["ナビィの恋","ちゅらさん"]',0,1,'wikipedia_ja',7.1),
(32,'照屋林助','Teruya Rinsuke','テルヤ リンスケ',1929,2005,'沖縄県','okinawa_performing_arts','沖縄音楽・漫談・芸能の革新者として、戦後沖縄の大衆文化と反骨精神を体現した。','[]',0,1,'wikipedia_ja',7.0),
(33,'喜納昌吉','Kina Shōkichi','キナ ショウキチ',1948,NULL,'沖縄県コザ市','okinawa_music_politics','音楽『花』などで沖縄発の平和メッセージを国際化し、参議院議員としても発信した。','["花〜すべての人の心に花を〜"]',1,0,'wikipedia_ja',7.7),
(34,'稲嶺恵一','Inamine Keiichi','イナミネ ケイイチ',1933,NULL,'沖縄県','okinawa_politics','沖縄県知事として基地問題、地域振興、経済政策の調整に取り組んだ。','[]',0,1,'wikipedia_ja',6.7),
(35,'知花昌一','Chibana Shōichi','チバナ ショウイチ',1948,NULL,'沖縄県読谷村','okinawa_peace_movement','反戦地主・平和運動家として、米軍基地と土地問題を地域から問い続けた。','[]',0,1,'wikipedia_ja',6.6),
(36,'島袋文子','Shimabukuro Fumiko','シマブクロ フミコ',1929,NULL,'沖縄県','okinawa_peace_movement','沖縄戦体験者として辺野古などの基地反対運動に参加し、戦争記憶を現場の言葉で継承した。','[]',0,1,'wikipedia_ja',6.5),
(37,'高里鈴代','Takazato Suzuyo','タカザト スズヨ',1940,NULL,'台湾','okinawa_women_peace','那覇市議や女性団体で米軍基地と性暴力の問題に取り組み、沖縄のフェミニズム平和運動を牽引した。','[]',0,1,'wikipedia_ja',6.8),
(38,'山城博治','Yamashiro Hiroji','ヤマシロ ヒロジ',1952,NULL,'沖縄県','okinawa_peace_movement','基地建設反対運動の現場リーダーとして、辺野古・高江をめぐる市民運動を全国へ可視化した。','[]',0,1,'wikipedia_ja',6.6),
(39,'大城美佐子','Ōshiro Misako','オオシロ ミサコ',1936,2021,'大阪府','okinawa_music','沖縄民謡歌手として島唄の表現を磨き、戦後沖縄音楽の女性継承者として後進を育てた。','["片思い"]',0,1,'wikipedia_ja',6.9),
(40,'古謝美佐子','Koja Misako','コジャ ミサコ',1954,NULL,'沖縄県嘉手納町','okinawa_music','ネーネーズやソロ活動を通じ、沖縄民謡を現代音楽として国内外へ伝えた。','["童神"]',0,1,'wikipedia_ja',7.0),
(41,'夏川りみ','Natsukawa Rimi','ナツカワ リミ',1973,NULL,'沖縄県石垣市','okinawa_music','『涙そうそう』の歌唱で沖縄発の楽曲を全国的ヒットにし、島唄系ポップスの受容を広げた。','["涙そうそう"]',0,1,'wikipedia_ja',7.2),
(42,'宮良長包','Miyara Chōhō','ミヤラ チョウホウ',1883,1939,'沖縄県石垣市','okinawa_music_education','作曲家・教育者として八重山・沖縄の音楽素材を近代学校教育と歌曲へ接続した。','["安里屋ユンタ"]',0,1,'wikipedia_ja',6.7),
(43,'普久原恒勇','Fukuhara Tsuneo','フクハラ ツネオ',1932,2022,'大阪府','okinawa_music','作曲家として沖縄音楽の旋律を戦後歌謡と結び、沖縄ポップスの基盤を作った。','["芭蕉布"]',0,1,'wikipedia_ja',6.9),
(44,'目取真俊','Medoruma Shun','メドルマ シュン',1960,NULL,'沖縄県今帰仁村','okinawa_literature','沖縄戦と基地問題を小説で描き、現代日本文学に沖縄の記憶政治を突きつけた。','["水滴"]',1,0,'wikipedia_ja',7.3),
(45,'又吉栄喜','Matayoshi Eiki','マタヨシ エイキ',1947,NULL,'沖縄県浦添市','okinawa_literature','小説『豚の報い』で芥川賞を受け、沖縄社会の矛盾と生の感覚を文学化した。','["豚の報い"]',0,1,'wikipedia_ja',6.9),
(46,'李恢成','Lee Hoesung','リ カイセイ',1935,NULL,'樺太真岡町','zainichi_korean_literature','在日朝鮮人二世の経験を小説化し、『砧をうつ女』で芥川賞を受賞した。','["砧をうつ女"]',1,0,'wikipedia_ja',7.5),
(47,'金石範','Kim Sok-pom','キム ソクポム',1925,NULL,'大阪府大阪市','zainichi_korean_literature','済州四・三事件と在日朝鮮人の歴史を大河小説として描き、記憶の継承に貢献した。','["火山島"]',1,0,'wikipedia_ja',7.4),
(48,'金時鐘','Kim Sijong','キム シジョン',1929,NULL,'釜山','zainichi_korean_poetry','朝鮮語と日本語のあいだで詩作し、戦後日本語文学に植民地経験と分断の視点を刻んだ。','["猪飼野詩集"]',1,0,'wikipedia_ja',7.3),
(49,'梁石日','Yan Sogil','ヤン ソギル',1936,2024,'大阪府大阪市','zainichi_korean_literature','在日朝鮮人コミュニティと都市下層の経験を描き、『血と骨』などで大衆文学にも影響を与えた。','["血と骨"]',1,0,'wikipedia_ja',7.4),
(50,'李良枝','Lee Yang-ji','イ ヤンジ',1955,1992,'山梨県南都留郡','zainichi_korean_literature','在日韓国人女性の身体感覚・言語・帰属を小説化し、『由熙』で芥川賞を受賞した。','["由熙"]',1,0,'wikipedia_ja',7.3),
(51,'金達寿','Kim Talsu','キム タルス',1919,1997,'慶尚南道','zainichi_korean_literature','在日朝鮮人文学の先駆者として創作と古代朝鮮・日本交流史の紹介を行った。','["朴達の裁判"]',0,1,'wikipedia_ja',7.0),
(52,'鄭義信','Chong Wishing','チョン ウィシン',1957,NULL,'兵庫県姫路市','zainichi_korean_theater','劇作・脚本で在日コリアンの家族、笑い、痛みを舞台化し、日本演劇・映画に独自の語りをもたらした。','["焼肉ドラゴン"]',0,1,'wikipedia_ja',7.1),
(53,'崔洋一','Sai Yōichi','サイ ヨウイチ',1949,2022,'長野県佐久市','zainichi_korean_film','映画監督として暴力、差別、家族を描き、日本映画界で在日コリアンの視点を可視化した。','["月はどっちに出ている","血と骨"]',1,0,'wikipedia_ja',7.3),
(54,'梁英姫','Yang Yong-hi','ヤン ヨンヒ',1964,NULL,'大阪府大阪市','zainichi_korean_documentary','家族と北朝鮮帰国事業をめぐるドキュメンタリー・劇映画で、在日コリアンの分断経験を国際的に伝えた。','["ディア・ピョンヤン","かぞくのくに"]',0,1,'wikipedia_ja',7.0),
(55,'辛格浩','Shin Kyuk-ho','シン ギョクホ',1921,2020,'慶尚南道蔚山郡','zainichi_korean_business','日本でロッテを創業し、菓子・流通・観光をまたぐ日韓企業グループを築いた。','["ロッテ"]',1,0,'wikipedia_ja',7.8),
(56,'韓昌祐','Han Chang-woo','ハン チャンウ',1931,NULL,'慶尚南道三千浦','zainichi_korean_business','マルハンを創業し、在日コリアン起業家として娯楽産業から社会貢献活動まで展開した。','["マルハン"]',1,0,'wikipedia_ja',7.4),
(57,'朴慶南','Park Kyongnam','パク キョンナム',1950,NULL,'鳥取県','zainichi_korean_nonfiction','在日コリアン女性の視点から差別、家族、国籍、共生をノンフィクションで発信した。','["ポッカリ月が出ましたら"]',0,1,'wikipedia_ja',6.5),
(58,'玄月','Gengetsu','ゲンゲツ',1965,NULL,'大阪府大阪市','zainichi_korean_literature','在日コリアンの日常と周縁性を小説化し、『蔭の棲みか』で芥川賞を受賞した。','["蔭の棲みか"]',0,1,'wikipedia_ja',6.9),
(59,'深沢潮','Fukazawa Ushio','フカザワ ウシオ',1966,NULL,'東京都','zainichi_korean_literature','在日コリアン女性の家族・労働・ジェンダーを現代小説として描き、複合的なマイノリティ経験を可視化した。','["ハンサラン 愛する人びと"]',0,1,'wikipedia_ja',6.4),
(60,'金守珍','Kim Sujin','キム スジン',1954,NULL,'東京都','zainichi_korean_theater','新宿梁山泊を率い、アングラ演劇と在日コリアンの身体性を結びつけた舞台表現を展開した。','["新宿梁山泊"]',0,1,'wikipedia_ja',6.6),
(61,'李鳳宇','Lee Bong-ou','リ ボンウ',1960,NULL,'京都府京都市','zainichi_korean_film_business','映画プロデューサー・配給者としてアジア映画と日本映画をつなぎ、多文化的な映画流通を切り開いた。','["パッチギ!"]',0,1,'wikipedia_ja',6.8),
(62,'白眞勲','Haku Shinkun','ハク シンクン',1958,NULL,'東京都新宿区','zainichi_korean_politics','朝鮮日報日本支社長を経て参議院議員となり、在日コリアン出身政治家として外交・人権課題に関わった。','[]',0,1,'wikipedia_ja',6.6),
(63,'新井英一','Arai Eiichi','アライ エイイチ',1950,NULL,'福岡県','zainichi_korean_music','在日コリアンの生活史とブルースを結びつけ、歌でマイノリティの記憶を表現した。','["清河への道"]',0,1,'wikipedia_ja',6.5),
(64,'康珍化','Kan Chinfa','カン チンファ',1953,NULL,'静岡県浜松市','zainichi_korean_lyrics','作詞家として多数のヒット曲を生み、日本語ポップスの表現を広げた在日コリアンのクリエイター。','["悲しみがとまらない","ギザギザハートの子守唄"]',0,1,'wikipedia_ja',6.8),
(65,'金満里','Kim Manri','キム マンリ',1953,NULL,'大阪府','zainichi_korean_dance','劇団態変を主宰し、障害者の身体表現と在日コリアン女性の経験を舞台芸術に結びつけた。','["劇団態変"]',0,1,'wikipedia_ja',6.4),
(66,'邱永漢','Kyu Eikan','キュウ エイカン',1924,2012,'台湾台南市','zainichi_chinese_business_literature','直木賞作家であり投資・経営評論家として、華人ネットワークと日本のビジネス読者を結びつけた。','["香港","食は広州に在り"]',1,0,'wikipedia_ja',7.4),
(67,'陳舜臣','Chen Shunchen','チン シュンシン',1924,2015,'兵庫県神戸市','zainichi_chinese_literature','中国史小説・推理小説を通じ、華僑二世の視点から東アジア史を日本語読者へ開いた。','["枯草の根","阿片戦争"]',1,0,'wikipedia_ja',7.6),
(68,'金美齢','Kin Birei','キン ビレイ',1934,NULL,'台湾台北州','zainichi_taiwan_commentary','台湾出身の評論家として、日本社会に台湾政治、教育、女性の視点を発信した。','[]',0,1,'wikipedia_ja',6.9),
(69,'黄文雄','Kō Bun’yū','コウ ブンユウ',1938,NULL,'台湾高雄州','zainichi_taiwan_commentary','台湾出身の評論家として、日台関係、東アジア近現代史、華人社会をめぐる言論活動を行った。','[]',0,1,'wikipedia_ja',6.8),
(70,'王立誠','Ō Rissei','オウ リッセイ',1958,NULL,'台湾','zainichi_chinese_go','台湾出身の囲碁棋士として日本棋院で活躍し、棋戦優勝を重ねて囲碁界の国際化を体現した。','[]',0,1,'wikipedia_ja',6.8),
(71,'王銘琬','Ō Meien','オウ メイエン',1961,NULL,'台湾台北市','zainichi_chinese_go','台湾出身の囲碁棋士として先進的な棋風と普及活動で日本囲碁界に影響を与えた。','[]',0,1,'wikipedia_ja',6.8),
(72,'林海峰','Rin Kaihō','リン カイホウ',1942,NULL,'上海市','zainichi_chinese_go','上海出身の囲碁棋士として名人・本因坊などで活躍し、戦後囲碁界のトップ層を形成した。','[]',1,0,'wikipedia_ja',7.3),
(73,'周富徳','Shū Tomitoku','シュウ トミトク',1943,2014,'神奈川県横浜市','zainichi_chinese_food_business','広東料理人としてテレビ出演と店舗経営を通じ、日本の大衆的な中華料理文化を広げた。','[]',0,1,'wikipedia_ja',6.9),
(74,'周富輝','Shū Tomiteru','シュウ トミテル',1950,NULL,'神奈川県横浜市','zainichi_chinese_food_business','料理人・実業家として広東料理店を運営し、横浜中華街系の食文化を継承・発信した。','[]',0,1,'wikipedia_ja',6.4),
(75,'楊逸','Yang Yi','ヤン イー',1964,NULL,'中国ハルビン市','zainichi_chinese_literature','中国語母語話者として日本語小説を書き、『時が滲む朝』で芥川賞を受賞した。','["時が滲む朝"]',1,0,'wikipedia_ja',7.2),
(76,'莫邦富','Mo Bangfu','モー バンフ','1953',NULL,'中国上海市','zainichi_chinese_media','中国出身の作家・ジャーナリストとして、日中ビジネス、留学生、華人社会を継続的に論じた。','[]',0,1,'wikipedia_ja',6.5),
(77,'劉セイラ','Liu Seira','リュウ セイラ',1985,NULL,'中国北京市','zainichi_chinese_media','中国出身の声優・漫画家として日本のアニメ文化に参加し、日中のポップカルチャー交流を体現した。','[]',0,1,'wikipedia_ja',6.2),
(78,'鳳蘭','Ran Ōtori','オオトリ ラン',1946,NULL,'兵庫県神戸市','zainichi_chinese_performing_arts','宝塚歌劇団星組トップスターを経て俳優として活躍し、華人ルーツを持つ舞台人の代表例となった。','[]',1,0,'wikipedia_ja',7.2),
(79,'ジュディ・オング','Judy Ongg','ジュディ オング',1950,NULL,'台湾台北市','zainichi_taiwan_music_arts','台湾出身の歌手・木版画家として、日本の歌謡・美術の双方で長く活動した。','["魅せられて"]',1,0,'wikipedia_ja',7.5),
(80,'陳美齢','Agnes Chan','アグネス チャン',1955,NULL,'香港','zainichi_chinese_music_education','香港出身の歌手・教育学者として、日本の芸能、子育て、ユニセフ活動を横断して発信した。','["ひなげしの花"]',1,0,'wikipedia_ja',7.4);

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, secondary_era_id, domain, sub_domain, achievement_summary,
  notable_works, family_class, family_education, education_path, mentors,
  fame_source, fame_score, is_traditional_great, is_local_excellent,
  data_completeness, source_team, source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  'all', NULL, 'diaspora_ainu_okinawa', sub_domain, achievement_summary,
  notable_works, 'other', NULL, NULL, '[]',
  fame_source, fame_score, is_traditional_great, is_local_excellent,
  80, 'codex_all_diaspora_ainu_okinawa',
  'https://ja.wikipedia.org/wiki/' || replace(name_ja, ' ', '_'),
  '全時代横断のdiaspora_ainu_okinawa追加。Wikipedia等で実在確認可能な人物を選定。'
FROM diaspora_candidates c
WHERE rn BETWEEN 1 AND 50
  AND NOT EXISTS (
    SELECT 1 FROM achievers a
    WHERE a.name_ja = c.name_ja AND a.birth_year = c.birth_year
  );

SELECT 'after_batch_1', COUNT(*)
FROM achievers
WHERE primary_era_id='all'
  AND domain='diaspora_ainu_okinawa'
  AND source_team='codex_all_diaspora_ainu_okinawa';

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, secondary_era_id, domain, sub_domain, achievement_summary,
  notable_works, family_class, family_education, education_path, mentors,
  fame_source, fame_score, is_traditional_great, is_local_excellent,
  data_completeness, source_team, source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  'all', NULL, 'diaspora_ainu_okinawa', sub_domain, achievement_summary,
  notable_works, 'other', NULL, NULL, '[]',
  fame_source, fame_score, is_traditional_great, is_local_excellent,
  80, 'codex_all_diaspora_ainu_okinawa',
  'https://ja.wikipedia.org/wiki/' || replace(name_ja, ' ', '_'),
  '全時代横断のdiaspora_ainu_okinawa追加。Wikipedia等で実在確認可能な人物を選定。'
FROM diaspora_candidates c
WHERE rn BETWEEN 51 AND 80
  AND NOT EXISTS (
    SELECT 1 FROM achievers a
    WHERE a.name_ja = c.name_ja AND a.birth_year = c.birth_year
  );

SELECT 'after_batch_2', COUNT(*)
FROM achievers
WHERE primary_era_id='all'
  AND domain='diaspora_ainu_okinawa'
  AND source_team='codex_all_diaspora_ainu_okinawa';

INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id, 'val_traditional', 9,
       '民族文化・地域文化の継承と再解釈に顕著な貢献がある。',
       a.source_url, 'codex_all_diaspora_ainu_okinawa batch capability'
FROM achievers a
WHERE a.source_team='codex_all_diaspora_ainu_okinawa';

INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id,
       CASE
         WHEN a.sub_domain LIKE '%business%' OR a.sub_domain LIKE '%food_business%' THEN 'age_entrepreneur'
         WHEN a.sub_domain LIKE '%politics%' OR a.sub_domain LIKE '%policy%' OR a.sub_domain LIKE '%rights%' OR a.sub_domain LIKE '%movement%' THEN 'age_social_change'
         WHEN a.sub_domain LIKE '%literature%' OR a.sub_domain LIKE '%poetry%' OR a.sub_domain LIKE '%arts%' OR a.sub_domain LIKE '%music%' OR a.sub_domain LIKE '%film%' OR a.sub_domain LIKE '%theater%' OR a.sub_domain LIKE '%media%' THEN 'cog_creativity'
         ELSE 'age_oecd_transformative'
       END,
       CASE
         WHEN a.sub_domain LIKE '%business%' OR a.sub_domain LIKE '%food_business%' THEN 8
         WHEN a.sub_domain LIKE '%politics%' OR a.sub_domain LIKE '%policy%' OR a.sub_domain LIKE '%rights%' OR a.sub_domain LIKE '%movement%' THEN 9
         ELSE 8
       END,
       a.achievement_summary,
       a.source_url, 'codex_all_diaspora_ainu_okinawa batch capability'
FROM achievers a
WHERE a.source_team='codex_all_diaspora_ainu_okinawa';

INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id,
       CASE
         WHEN a.sub_domain LIKE '%language%' OR a.sub_domain LIKE '%education%' OR a.sub_domain LIKE '%studies%' THEN 'age_meta_learning'
         WHEN a.sub_domain LIKE '%peace%' OR a.sub_domain LIKE '%rights%' OR a.sub_domain LIKE '%politics%' THEN 'val_tolerance'
         WHEN a.sub_domain LIKE '%business%' OR a.sub_domain LIKE '%food_business%' THEN 'cog_systems'
         ELSE 'cre_cross_domain'
       END,
       8,
       '複数文化・複数制度のあいだで活動し、知識・表現・組織を橋渡しした。',
       a.source_url, 'codex_all_diaspora_ainu_okinawa batch capability'
FROM achievers a
WHERE a.source_team='codex_all_diaspora_ainu_okinawa';

COMMIT;

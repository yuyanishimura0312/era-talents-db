BEGIN TRANSACTION;

DROP TABLE IF EXISTS temp_reiwa_social_movement_candidates;
CREATE TEMP TABLE temp_reiwa_social_movement_candidates (
  name_ja TEXT NOT NULL,
  name_en TEXT,
  birth_year INTEGER,
  death_year INTEGER,
  birth_place TEXT,
  sub_domain TEXT NOT NULL,
  achievement_summary TEXT NOT NULL,
  notable_works TEXT,
  family_class TEXT,
  education_path TEXT,
  fame_source TEXT,
  fame_score REAL,
  is_traditional_great INTEGER,
  is_local_excellent INTEGER,
  source_url TEXT NOT NULL,
  notes TEXT
);

INSERT INTO temp_reiwa_social_movement_candidates VALUES
('平田仁子','Kiko Hirata',1970,NULL,NULL,'環境・気候政策','気候ネットワークを基盤に石炭火力発電抑制と気候政策転換を国際的に訴え、令和期の日本の脱炭素世論形成に影響を与えた。','["気候ネットワーク","Goldman Environmental Prize 2021"]','other','早稲田大学、Climate Action Network等','goldman_prize',8.0,0,0,'https://www.goldmanprize.org/recipient/kiko-hirata/','気候変動政策アドボカシー'),
('小西雅子','Masako Konishi',NULL,NULL,NULL,'環境・気候政策','WWFジャパンで気候変動・エネルギー政策の提言を続け、自治体・企業・国際交渉をつなぐ専門的な市民提言を担った。','["WWFジャパン気候変動政策"]','other','ハーバード大学大学院等','org_profile',5.5,0,1,'https://www.wwf.or.jp/staffblog/profile/konishi/','専門NGO型の政策提言者'),
('桃井貴子','Takako Momoi',NULL,NULL,NULL,'環境・気候政策','気候ネットワークでエネルギー転換、原発・石炭火力問題、自治体気候政策の調査提言を進めた。','["気候ネットワーク"]','other',NULL,'org_profile',5.0,0,1,'https://www.kikonet.org/','環境NGOの政策実務者'),
('吉田明子','Akiko Yoshida',NULL,NULL,NULL,'環境・気候政策','FoE Japanで気候変動、脱石炭、エネルギー民主主義のキャンペーンと政策提言に携わった。','["FoE Japan気候変動・エネルギー"]','other',NULL,'org_profile',5.0,0,1,'https://foejapan.org/','国際環境NGOの現場リーダー'),
('小野寺ゆうり','Yuri Onodera',NULL,NULL,NULL,'環境・気候政策','FoE Japan等で気候正義、国際開発金融、エネルギー転換をめぐる市民側の監視と提言を担った。','["FoE Japan"]','other',NULL,'org_profile',4.8,0,1,'https://foejapan.org/','気候正義・国際金融監視'),
('ランダル・ヘルテン','Randal Helten',NULL,NULL,NULL,'環境・気候政策','FoE Japanで気候変動・開発金融・エネルギー政策の国際連携型アドボカシーを担った。','["FoE Japan"]','other',NULL,'org_profile',4.7,0,1,'https://foejapan.org/','国際NGOネットワーク型実務者'),
('青木陽子','Yoko Aoki',NULL,NULL,NULL,'環境・気候政策','グリーンピース・ジャパンで気候、海洋、持続可能な社会をめぐるキャンペーン型市民運動を牽引した。','["グリーンピース・ジャパン"]','other',NULL,'org_profile',5.2,0,1,'https://www.greenpeace.org/japan/','環境キャンペーン運営'),
('寺中誠','Makoto Teranaka',NULL,NULL,NULL,'人権・環境NGO運営','アムネスティ日本やグリーンピース・ジャパン等で国際人権・環境NGOの組織運営と政策提言を担った。','["アムネスティ・インターナショナル日本","グリーンピース・ジャパン"]','other',NULL,'org_profile',5.3,0,0,'https://www.amnesty.or.jp/','国際NGO組織運営'),
('下村委津子','Itsuko Shimomura',NULL,NULL,NULL,'環境教育・消費者運動','環境市民で持続可能な消費、自治体環境政策、環境教育を市民参加型で推進した。','["環境市民"]','other',NULL,'org_profile',4.7,0,1,'https://www.kankyoshimin.org/','環境教育・消費者市民活動'),
('谷口たかひさ','Takahisa Taniguchi',NULL,NULL,NULL,'気候アクション','気候危機の講演活動と市民啓発を全国で展開し、若年層にも届く環境コミュニケーションを行った。','["地球を守ろう"]','other',NULL,'official_profile',5.0,0,1,'https://chikyuwomamorou.com/','気候危機コミュニケーター'),
('小野りりあん','Lillian Ono',NULL,NULL,NULL,'気候アクション','Fridays For Future Tokyoなど若者の気候アクションに関わり、生活者目線の気候危機発信を行った。','["Fridays For Future Tokyo"]','other',NULL,'public_profile',5.0,0,1,'https://fridaysforfuture.jp/','若者気候運動'),
('櫻田彩子','Ayako Sakurada',1974,NULL,NULL,'環境コミュニケーション','エコアナウンサーとして環境問題、防災、持続可能な暮らしをメディアと地域活動の双方で発信した。','["エコアナウンサー活動"]','other',NULL,'official_profile',4.8,0,1,'https://www.ayakosakurada.com/','環境広報'),
('古沢広祐','Kosuke Furusawa',1950,NULL,NULL,'環境・国際協力','JACSES等で環境、開発、経済の接続を扱い、持続可能な社会に向けた市民政策研究を進めた。','["JACSES","持続可能な社会論"]','other','大阪大学大学院等','researcher_profile',5.0,0,0,'https://researchmap.jp/read0001805','市民政策研究'),
('貝沼美紀子','Mikiko Kainuma',1950,NULL,NULL,'環境政策研究','気候変動対策と持続可能な低炭素社会シナリオ研究を通じて、環境政策と市民的議論の基盤を支えた。','["低炭素社会シナリオ研究"]','other','京都大学等','researcher_profile',5.2,0,0,'https://researchmap.jp/read0009016','環境政策研究者'),
('大林ミカ','Mika Ohbayashi',NULL,NULL,NULL,'再生可能エネルギー','自然エネルギー財団などで再生可能エネルギー拡大と電力システム改革を市民政策として提言した。','["自然エネルギー財団"]','other',NULL,'org_profile',5.3,0,0,'https://www.renewable-ei.org/','再エネ政策提言'),
('村田早耶香','Sayaka Murata',1981,NULL,NULL,'国際協力NPO','かものはしプロジェクトを創設し、児童買春・人身売買問題への国際協力型NPO活動を展開した。','["かものはしプロジェクト"]','other','フェリス女学院大学','org_profile',6.0,0,0,'https://www.kamonohashi-project.net/','児童搾取防止NPO'),
('三輪開人','Kaito Miwa',1986,NULL,NULL,'教育NPO・国際協力','e-Educationを通じて途上国の映像教育支援と教育格差縮小に取り組んだ。','["e-Education"]','other','早稲田大学','org_profile',5.6,0,0,'https://eedu.jp/','教育格差への国際NPO実践'),
('安部敏樹','Toshiki Abe',1987,NULL,NULL,'社会課題学習','リディラバを創業し、社会課題の現場スタディツアーと調査報道型メディアを通じて市民参加を促した。','["リディラバ"]','other','東京大学','org_profile',5.8,0,0,'https://ridilover.jp/','社会課題の可視化'),
('今井紀明','Noriaki Imai',1985,NULL,NULL,'若者支援NPO','D×Pで不登校・中退・困窮など孤立する若者の相談支援と居場所づくりを進めた。','["認定NPO法人D×P"]','other',NULL,'org_profile',5.5,0,1,'https://www.dreampossibility.com/','若者の孤立支援'),
('小河光治','Koji Ogawa',NULL,NULL,NULL,'子ども貧困対策','子どもの貧困対策センター「あすのば」等で制度提言と当事者支援を結びつけた活動を進めた。','["あすのば"]','other',NULL,'org_profile',5.0,0,1,'https://www.usnova.org/','子ども貧困の政策提言'),
('赤石千衣子','Chieko Akaishi',1955,NULL,NULL,'ひとり親支援','しんぐるまざあず・ふぉーらむでひとり親家庭の生活支援、政策提言、コロナ禍の緊急支援を担った。','["しんぐるまざあず・ふぉーらむ"]','other',NULL,'org_profile',5.7,0,1,'https://www.single-mama.com/','ひとり親支援'),
('藤木和子','Kazuko Fujiki',1982,NULL,NULL,'障害児者家族支援','きょうだい児・者支援を専門に、障害や病気のある人の兄弟姉妹への相談、啓発、政策提言を行った。','["きょうだい会SHAMS"]','other',NULL,'official_profile',4.8,0,1,'https://siblingsibling.org/','きょうだい支援'),
('山田壮志郎','Soshiro Yamada',NULL,NULL,NULL,'フードバンク・貧困研究','フードバンク活動と貧困研究を接続し、食品ロス削減と生活困窮者支援の実践知を広げた。','["フードバンク研究"]','other',NULL,'researcher_profile',4.8,0,1,'https://researchmap.jp/s-yamada','フードバンク実践研究'),
('清輔夏輝','Natsuki Kiyosuke',NULL,NULL,NULL,'子ども支援NPO','チャリティーサンタを通じ、子どもの貧困や体験格差に対する寄付・ボランティア参加の仕組みを広げた。','["チャリティーサンタ"]','other',NULL,'org_profile',4.7,0,1,'https://www.charity-santa.com/','体験格差支援'),
('川口加奈','Kana Kawaguchi',NULL,NULL,NULL,'ホームレス支援','Homedoorを創設し、路上生活者・生活困窮者への就労支援、住まい支援、相談支援を大阪で展開した。','["Homedoor"]','other','大阪市立大学','org_profile',5.5,0,1,'https://www.homedoor.org/','地域型ホームレス支援'),
('清水康之','Yasuyuki Shimizu',NULL,NULL,NULL,'自殺対策NPO','ライフリンクを設立し、自殺対策基本法以後の地域連携型自殺対策と相談支援の社会化を推進した。','["ライフリンク"]','other',NULL,'org_profile',5.7,0,0,'https://lifelink.or.jp/','自殺対策の市民政策'),
('石川えり','Eri Ishikawa',1976,NULL,NULL,'難民支援','難民支援協会で難民申請者への法的・生活支援と制度改善のアドボカシーを行った。','["難民支援協会"]','other','上智大学等','org_profile',5.5,0,1,'https://www.refugee.or.jp/','難民支援NGO'),
('渡部カンコロンゴ清花','Sayaka Watanabe Kankolongo',1991,NULL,NULL,'難民・移民支援','WELgeeを創設し、日本に逃れた難民・避難民の伴走支援、就労支援、社会参加を促した。','["WELgee"]','other','東京大学大学院','org_profile',5.5,0,1,'https://www.welgee.jp/','難民人材支援'),
('田中宝紀','Hoki Tanaka',NULL,NULL,NULL,'外国ルーツの子ども支援','YSCグローバル・スクールで外国にルーツを持つ子ども・若者の学習支援と制度提言を続けた。','["YSCグローバル・スクール"]','other',NULL,'org_profile',5.2,0,1,'https://www.kodomo-nihongo.com/','移民第二世代支援'),
('織田朝日','Asahi Oda',NULL,NULL,NULL,'難民・入管問題','在日難民や入管収容の問題を当事者・支援者の視点から発信し、市民的関心を広げた。','["難民問題発信"]','other',NULL,'public_profile',5.0,0,1,'https://twitter.com/freeasahi','難民・入管問題の発信者'),
('駒井知会','Chie Komai',NULL,NULL,NULL,'移民・難民法支援','弁護士として難民認定、入管収容、外国人労働者の権利擁護に取り組み、市民団体と連携した支援を行った。','["入管・難民法務"]','other',NULL,'professional_profile',5.1,0,1,'https://www.call4.jp/','移民難民法の実務支援'),
('児玉晃一','Koichi Kodama',NULL,NULL,NULL,'入管問題・法律支援','入管収容や難民認定をめぐる訴訟・支援活動に携わり、制度改善に向けた市民的議論を支えた。','["入管収容問題"]','other',NULL,'professional_profile',5.0,0,1,'https://www.call4.jp/','入管問題の法的支援'),
('指宿昭一','Shoichi Ibusuki',NULL,NULL,NULL,'外国人労働者支援','技能実習生・外国人労働者の労働相談、訴訟支援、制度批判を通じて労働権の保護を訴えた。','["外国人労働者弁護団"]','other',NULL,'professional_profile',5.3,0,1,'https://www.jlaf.jp/','外国人労働者の権利擁護'),
('鳥井一平','Ippei Torii',NULL,NULL,NULL,'移住労働者支援','移住者と連帯する全国ネットワーク等で移民・難民・外国人労働者の権利擁護と政策提言を行った。','["移住連"]','other',NULL,'org_profile',5.1,0,1,'https://migrants.jp/','移住者権利運動'),
('杉田昌平','Shohei Sugita',NULL,NULL,NULL,'外国人労働・入管法務','外国人雇用・入管・技能実習制度に関わる法実務と制度提言を通じ、多文化共生の実装を支えた。','["外国人雇用法務"]','other',NULL,'professional_profile',4.8,0,1,'https://www.jil.go.jp/','外国人労働制度の専門実務'),
('薬師実芳','Mika Yakushi',NULL,NULL,NULL,'LGBTQ若者支援','ReBitを設立し、LGBTQの子ども・若者の教育、就労、居場所づくりを全国に広げた。','["ReBit"]','other','早稲田大学','org_profile',5.7,0,1,'https://rebitlgbt.org/','LGBTQ若者支援'),
('松岡宗嗣','Soshi Matsuoka',1994,NULL,NULL,'LGBTQ報道・政策提言','一般社団法人fairでLGBTQに関する報道、調査、法制度提言を行い、同性婚・差別禁止の世論形成に寄与した。','["fair","LGBTQ報道"]','other',NULL,'org_profile',5.6,0,1,'https://fair-fair.org/','LGBTQメディア・政策提言'),
('村木真紀','Maki Muraki',NULL,NULL,NULL,'LGBTQ職場包摂','虹色ダイバーシティを設立し、職場・自治体におけるLGBTQ包摂と調査研究を推進した。','["虹色ダイバーシティ"]','other',NULL,'org_profile',5.6,0,1,'https://nijiirodiversity.jp/','LGBTQ職場包摂'),
('星賢人','Kento Hoshi',1993,NULL,NULL,'LGBTQ就労支援','JobRainbowを創業し、LGBTQフレンドリーな就職・転職支援と企業評価の仕組みを広げた。','["JobRainbow"]','other',NULL,'org_profile',5.3,0,1,'https://jobrainbow.jp/','LGBTQ就労支援'),
('太田啓子','Keiko Ota',NULL,NULL,NULL,'ジェンダー平等・法曹','弁護士として性暴力、DV、選択的夫婦別姓、性差別をめぐる発信と法的支援を行った。','["ジェンダー法務","これからの男の子たちへ"]','other',NULL,'public_profile',5.5,0,0,'https://www.ohtakeiko.com/','ジェンダー法務と啓発'),
('北原みのり','Minori Kitahara',1970,NULL,NULL,'フェミニズム・性暴力反対','作家・事業者として性暴力、性の商品化、女性の身体をめぐる社会問題を継続的に発信した。','["性暴力反対運動","フェミニズム言論"]','other',NULL,'wikipedia_ja',6.0,0,0,'https://ja.wikipedia.org/wiki/%E5%8C%97%E5%8E%9F%E3%81%BF%E3%81%AE%E3%82%8A','フェミニズム言論'),
('中野円佳','Madoka Nakano',1984,NULL,NULL,'女性労働・ケア','女性の就労継続、子育てと労働、ケア責任をめぐる調査・発信を行い、政策議論に接続した。','["育休世代のジレンマ"]','other','東京大学','public_profile',5.4,0,0,'https://researchmap.jp/madoka_nakano','女性労働研究と発信'),
('笛美','Fuemi',NULL,NULL,NULL,'ジェンダー平等キャンペーン','SNS発の#検察庁法改正案に抗議しますやジェンダー平等関連の発信で、市民参加型のオンライン運動を可視化した。','["ぜんぶ運命だったんかい"]','other',NULL,'public_profile',5.0,0,1,'https://www.kinokuniya.co.jp/f/dsg-01-9784750517176','オンライン市民運動'),
('山本潤','Jun Yamamoto',NULL,NULL,NULL,'性暴力被害者支援','Spring等で性暴力被害当事者の声を法改正運動に接続し、刑法性犯罪規定の見直し議論に関わった。','["一般社団法人Spring"]','other',NULL,'org_profile',5.5,0,1,'https://spring-voice.org/','性暴力被害者支援'),
('岡田実穂','Miho Okada',NULL,NULL,NULL,'IT教育・ジェンダー','Waffleで女子・ノンバイナリー中高生のIT教育機会拡大とジェンダーギャップ是正を推進した。','["Waffle"]','other',NULL,'org_profile',5.0,0,1,'https://waffle-waffle.org/','ジェンダーとIT教育'),
('徳永桂子','Keiko Tokunaga',NULL,NULL,NULL,'性教育・人権教育','性教育、人権教育、デートDV予防の講演・教材づくりを通じ、若者の自己決定と暴力予防を支援した。','["性教育・デートDV予防"]','other',NULL,'public_profile',4.7,0,1,'https://www.kyoto-womens.org/','性教育実践者'),
('染矢明日香','Asuka Someya',NULL,NULL,NULL,'SRHR・性教育','Pilconを設立し、若者の性の健康、避妊、SRHRに関する教育・啓発と政策提言を行った。','["Pilcon"]','other',NULL,'org_profile',5.2,0,1,'https://pilcon.org/','SRHR教育'),
('勝部元気','Genki Katsube',1983,NULL,NULL,'男性性・ジェンダー平等','男性のジェンダー規範、性暴力、ケア参加をめぐる発信を行い、男性側からのジェンダー平等運動を促した。','["ジェンダー平等言論"]','other','早稲田大学','public_profile',5.0,0,1,'https://gendai.media/list/author/genkikatsube','男性性批判'),
('牟田和恵','Kazue Muta',1956,NULL,NULL,'フェミニズム研究・運動','ジェンダー研究者としてハラスメント、性差別、大学内外のフェミニズム運動に関わり続けた。','["ジェンダー家族研究","ハラスメント問題"]','other','京都大学大学院等','researcher_profile',5.5,0,0,'https://researchmap.jp/read0012736','フェミニズム研究と社会運動'),
('海老原宏美','Hiromi Ebihara',NULL,2021,NULL,'障害者権利','自立生活運動の担い手として、重度障害者の地域生活、介助制度、相模原事件後の優生思想批判を発信した。','["自立生活運動","まあぶる"]','other',NULL,'public_profile',5.3,0,1,'https://www.nhk.or.jp/heart-net/article/537/','障害者権利運動'),
('佐藤聡','Satoshi Sato',NULL,NULL,NULL,'障害者権利','DPI日本会議で障害者差別解消、バリアフリー、地域生活をめぐる政策提言と当事者運動を担った。','["DPI日本会議"]','other',NULL,'org_profile',5.2,0,1,'https://www.dpi-japan.org/','障害者政策アドボカシー'),
('尾上浩二','Koji Onoue',NULL,NULL,NULL,'障害者権利','DPI日本会議などで障害者権利条約、差別解消、交通・街づくりのバリアフリー政策を推進した。','["DPI日本会議"]','other',NULL,'org_profile',5.2,0,1,'https://www.dpi-japan.org/','障害者運動リーダー'),
('崔栄繁','Yongbeon Choi',NULL,NULL,NULL,'障害者権利・国際人権','DPI日本会議で障害者権利条約の国内実施、国際人権基準に基づく制度改善を支えた。','["DPI日本会議"]','other',NULL,'org_profile',5.1,0,1,'https://www.dpi-japan.org/','障害者権利条約の国内実装'),
('熊篠慶彦','Yoshihiko Kumashino',NULL,NULL,NULL,'障害と性・権利擁護','障害者の性と生、介助、自己決定をめぐる社会的タブーを問い、当事者発信と啓発活動を行った。','["障害者の性と自己決定"]','other',NULL,'public_profile',5.0,0,1,'https://www.whitehands.jp/','障害と性の権利擁護'),
('伊藤たてお','Tateo Ito',NULL,NULL,NULL,'難病・障害者運動','日本ALS協会など難病当事者運動に関わり、医療・介助・意思決定支援をめぐる制度改善を訴えた。','["日本ALS協会"]','other',NULL,'org_profile',4.8,0,1,'https://alsjapan.org/','難病当事者運動'),
('恩田聖敬','Satoshi Onda',NULL,NULL,NULL,'ALS当事者発信','ALS当事者として就労、スポーツ、地域生活を発信し、難病とともに生きる社会参加モデルを示した。','["ALS当事者発信"]','other',NULL,'official_profile',4.8,0,1,'https://onda-inc.com/','難病当事者の社会参加'),
('川口有美子','Yumiko Kawaguchi',NULL,NULL,NULL,'ALS介護・意思決定支援','ALSの介護経験と当事者家族支援をもとに、人工呼吸器、在宅介護、尊厳をめぐる発信を行った。','["逝かない身体","ALS/MNDサポートセンターさくら会"]','other',NULL,'wikipedia_ja',5.3,0,0,'https://ja.wikipedia.org/wiki/%E5%B7%9D%E5%8F%A3%E6%9C%89%E7%BE%8E%E5%AD%90','ALS介護と生命倫理'),
('廣川麻子','Asako Hirokawa',NULL,NULL,NULL,'聴覚障害・文化アクセシビリティ','TA-netで舞台芸術・文化施設の情報保障を進め、聴覚障害者の文化参加を広げた。','["TA-net"]','other',NULL,'org_profile',4.8,0,1,'https://ta-net.org/','文化アクセシビリティ'),
('桐原尚之','Naoyuki Kirihara',NULL,NULL,NULL,'精神障害者権利','精神医療ユーザーの立場から精神科医療、隔離拘束、地域生活をめぐる権利擁護と政策提言を行った。','["精神障害者権利主張センター・絆"]','other',NULL,'public_profile',4.8,0,1,'https://www.jngmdp.org/','精神障害者の権利擁護'),
('森山誉恵','Takae Moriyama',NULL,NULL,NULL,'子ども貧困・虐待予防','3keysを設立し、虐待・貧困・孤立に直面する子どもへの学習支援、相談、子どもの権利保障の啓発を進めた。','["認定NPO法人3keys"]','other','慶應義塾大学法学部','org_profile',5.2,0,1,'https://3keys.jp/about/profile/','子どもの権利保障NPO');

INSERT INTO achievers (
  name_ja, name_en, birth_year, death_year, birth_place, primary_era_id,
  domain, sub_domain, achievement_summary, notable_works, family_class,
  education_path, fame_source, fame_score, is_traditional_great,
  is_local_excellent, data_completeness, source_team, source_url, notes
)
SELECT
  c.name_ja, c.name_en, c.birth_year, c.death_year, c.birth_place, 'reiwa',
  'social_movement', c.sub_domain, c.achievement_summary, c.notable_works,
  c.family_class, c.education_path, c.fame_source, c.fame_score,
  c.is_traditional_great, c.is_local_excellent, 60,
  'codex_reiwa_social_movement', c.source_url, c.notes
FROM temp_reiwa_social_movement_candidates c
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a
  WHERE a.name_ja = c.name_ja
    AND ((a.birth_year = c.birth_year) OR (a.birth_year IS NULL AND c.birth_year IS NULL))
);

INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id, v.capability_id, v.score,
       '令和期の' || c.sub_domain || 'で、' || c.achievement_summary,
       c.source_url,
       'codex_reiwa_social_movement capability scoring'
FROM temp_reiwa_social_movement_candidates c
JOIN achievers a
  ON a.name_ja = c.name_ja
 AND a.primary_era_id = 'reiwa'
 AND a.domain = 'social_movement'
JOIN (
  SELECT name_ja, 'age_social_change' AS capability_id, 9 AS score FROM temp_reiwa_social_movement_candidates
  UNION ALL
  SELECT name_ja, 'soc_interpersonal', 8 FROM temp_reiwa_social_movement_candidates
  UNION ALL
  SELECT name_ja,
         CASE
           WHEN sub_domain LIKE '%環境%' OR sub_domain LIKE '%気候%' OR sub_domain LIKE '%エネルギー%' THEN 'val_eco'
           WHEN sub_domain LIKE '%障害%' OR sub_domain LIKE '%難病%' OR sub_domain LIKE '%精神%' OR sub_domain LIKE '%聴覚%' THEN 'val_tolerance'
           WHEN sub_domain LIKE '%LGBTQ%' OR sub_domain LIKE '%ジェンダー%' OR sub_domain LIKE '%性%' OR sub_domain LIKE '%女性%' THEN 'val_tolerance'
           WHEN sub_domain LIKE '%難民%' OR sub_domain LIKE '%移民%' OR sub_domain LIKE '%外国%' THEN 'val_tolerance'
           ELSE 'age_resilience'
         END,
         8
  FROM temp_reiwa_social_movement_candidates
  UNION ALL
  SELECT name_ja,
         CASE
           WHEN sub_domain LIKE '%政策%' OR sub_domain LIKE '%法%' OR sub_domain LIKE '%研究%' THEN 'cog_critical'
           WHEN sub_domain LIKE '%教育%' OR sub_domain LIKE '%学習%' THEN 'age_meta_learning'
           WHEN sub_domain LIKE '%NPO%' OR sub_domain LIKE '%支援%' OR sub_domain LIKE '%就労%' THEN 'age_entrepreneur'
           ELSE 'cog_systems'
         END,
         7
  FROM temp_reiwa_social_movement_candidates
) v ON v.name_ja = c.name_ja
WHERE NOT EXISTS (
  SELECT 1 FROM achiever_capabilities ac
  WHERE ac.achiever_id = a.id
    AND ac.capability_id = v.capability_id
);

COMMIT;

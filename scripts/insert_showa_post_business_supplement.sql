BEGIN;

DROP TABLE IF EXISTS temp_showa_post_business_supplement;
CREATE TEMP TABLE temp_showa_post_business_supplement (
  seq INTEGER PRIMARY KEY,
  name_ja TEXT NOT NULL,
  name_en TEXT,
  name_kana TEXT,
  birth_year INTEGER NOT NULL,
  death_year INTEGER,
  birth_place TEXT,
  sub_domain TEXT,
  achievement_summary TEXT NOT NULL,
  notable_works TEXT,
  family_class TEXT,
  education_path TEXT,
  fame_score REAL,
  is_traditional_great INTEGER,
  is_local_excellent INTEGER,
  source_url TEXT,
  notes TEXT
);

INSERT INTO temp_showa_post_business_supplement VALUES
(1,'関本忠弘','Tadahiro Sekimoto','せきもと ただひろ',1926,2007,'兵庫県','電機・通信','日本電気社長。C&C構想を掲げ、通信とコンピュータを統合する事業展開を進めた。','["日本電気","C&C"]','other','東京大学理学部',7.2,0,1,'https://ja.wikipedia.org/wiki/関本忠弘','情報通信産業の経営'),
(2,'佐波正一','Shoichi Saba','さば しょういち',1919,2012,'東京都','電機','東芝社長。総合電機メーカーの国際化と半導体・重電事業の展開期を担った。','["東芝"]','other','東京帝国大学工学部',6.8,0,1,'https://ja.wikipedia.org/wiki/佐波正一','総合電機経営'),
(3,'西室泰三','Taizo Nishimuro','にしむろ たいぞう',1935,2017,'山梨県','電機','東芝社長。海外事業と情報機器事業に携わり、総合電機の転換期を担った。','["東芝"]','other','慶應義塾大学経済学部',6.7,0,1,'https://ja.wikipedia.org/wiki/西室泰三','電機企業国際化'),
(4,'岩谷直治','Naoji Iwatani','いわたに なおじ',1903,2005,'島根県','エネルギー・商社','岩谷産業創業者。LPガスの家庭普及を進め、戦後生活エネルギー流通を拡大した。','["岩谷産業","LPガス"]','merchant','実務経験を経て創業',7.0,0,1,'https://ja.wikipedia.org/wiki/岩谷直治','生活エネルギー事業'),
(5,'三澤千代治','Chiyoji Misawa','みさわ ちよじ',1938,NULL,'新潟県','住宅','ミサワホーム創業者。工業化住宅とプレハブ住宅販売を広げ、住宅メーカーの多様化に貢献した。','["ミサワホーム"]','working_class','日本大学理工学部',6.9,0,1,'https://ja.wikipedia.org/wiki/三澤千代治','住宅メーカー創業'),
(6,'毒島邦雄','Kunio Busujima','ぶすじま くにお',1925,2016,'群馬県','娯楽機器','三共創業者。パチンコ機メーカーを成長させ、娯楽機器産業の技術・量産を進めた。','["SANKYO"]','working_class','桐生工業専門学校',6.8,0,1,'https://ja.wikipedia.org/wiki/毒島邦雄','娯楽機器メーカー創業'),
(7,'岡崎嘉平太','Kaheita Okazaki','おかざき かへいた',1897,1989,'岡山県','航空・商社','全日本空輸創設に関わり、戦後航空事業と日中経済交流を支えた実業家。','["全日本空輸","日中経済交流"]','other','東京帝国大学法学部',7.0,0,1,'https://ja.wikipedia.org/wiki/岡崎嘉平太','航空事業と経済交流'),
(8,'若狭得治','Tokuji Wakasa','わかさ とくじ',1914,2005,'富山県','航空','全日本空輸社長。国内航空網の拡大と安全運航体制の整備に関わった。','["全日本空輸"]','other','東京帝国大学法学部',6.7,0,1,'https://ja.wikipedia.org/wiki/若狭得治','航空会社経営'),
(9,'利光松男','Matsuo Toshimitsu','としみつ まつお',1923,2009,'大分県','航空','日本航空社長。国際線拡大期の航空会社経営を担った。','["日本航空"]','other','東京帝国大学法学部',6.6,0,1,'https://ja.wikipedia.org/wiki/利光松男','航空会社経営'),
(10,'佐伯勇','Isamu Saeki','さえき いさむ',1903,1989,'愛媛県','鉄道・観光','近畿日本鉄道社長。鉄道、観光、百貨店を連携させ、関西私鉄経営を発展させた。','["近畿日本鉄道"]','other','京都帝国大学法学部',6.8,0,1,'https://ja.wikipedia.org/wiki/佐伯勇','私鉄経営'),
(11,'上山善紀','Yoshinori Ueyama','うえやま よしのり',1914,2004,'大阪府','鉄道・観光','近畿日本鉄道社長。沿線開発と観光事業を進め、私鉄グループ経営を担った。','["近畿日本鉄道"]','other','京都帝国大学法学部',6.6,0,1,'https://ja.wikipedia.org/wiki/上山善紀','私鉄グループ経営'),
(12,'川勝傳','Den Kawakatsu','かわかつ でん',1901,1988,'大阪府','鉄道・流通','南海電気鉄道社長。鉄道と流通・不動産を組み合わせた沿線事業を展開した。','["南海電気鉄道"]','merchant','慶應義塾大学',6.6,0,1,'https://ja.wikipedia.org/wiki/川勝傳','沿線事業経営'),
(13,'石井幸孝','Yoshitaka Ishii','いしい よしたか',1932,NULL,'広島県','鉄道','JR九州初代社長。国鉄分割民営化後の地域鉄道経営と観光化の基盤を作った。','["JR九州"]','other','東京大学法学部',6.7,0,1,'https://ja.wikipedia.org/wiki/石井幸孝','地域鉄道経営'),
(14,'高木文雄','Fumio Takagi','たかぎ ふみお',1919,2006,'東京都','公共企業・鉄道','日本国有鉄道総裁。巨大公共企業の経営再建と労使問題に取り組んだ。','["日本国有鉄道"]','other','東京帝国大学法学部',6.4,0,1,'https://ja.wikipedia.org/wiki/高木文雄','公共企業経営'),
(15,'仁杉巌','Iwao Nisugi','にすぎ いわお',1915,2015,'東京都','鉄道','日本国有鉄道総裁。国鉄末期の経営改革と分割民営化前の調整に関わった。','["日本国有鉄道"]','other','東京帝国大学工学部',6.4,0,1,'https://ja.wikipedia.org/wiki/仁杉巌','鉄道事業改革'),
(16,'住田正二','Shoji Sumita','すみた しょうじ',1922,2017,'東京都','鉄道','JR東日本初代社長。民営化後の鉄道会社経営とサービス改善を主導した。','["JR東日本"]','other','東京帝国大学法学部',6.6,0,1,'https://ja.wikipedia.org/wiki/住田正二','民営化後鉄道経営'),
(17,'松田昌士','Masatake Matsuda','まつだ まさたけ',1936,2020,'北海道','鉄道','JR東日本社長。民営化後の経営安定化と駅ビジネス展開を進めた。','["JR東日本"]','other','北海道大学法学部',6.5,0,1,'https://ja.wikipedia.org/wiki/松田昌士','鉄道事業の経営安定化'),
(18,'根本二郎','Jiro Nemoto','ねもと じろう',1928,2016,'東京都','海運・財界','日本郵船社長、経団連会長。海運業の国際競争と財界調整を担った。','["日本郵船","経団連"]','other','東京大学法学部',6.8,0,1,'https://ja.wikipedia.org/wiki/根本二郎','海運経営と財界'),
(19,'宮原賢次','Kenji Miyahara','みやはら けんじ',1935,NULL,'東京都','総合商社','住友商事社長。総合商社の事業投資と国際取引を拡大した。','["住友商事"]','other','東京大学法学部',6.5,0,1,'https://ja.wikipedia.org/wiki/宮原賢次','総合商社経営'),
(20,'川久保玲','Rei Kawakubo','かわくぼ れい',1942,NULL,'東京都','ファッション・女性起業','コムデギャルソン創業者。前衛的デザインを国際的ブランドビジネスにした女性経営者。','["コムデギャルソン"]','other','慶應義塾大学文学部',7.4,0,1,'https://ja.wikipedia.org/wiki/川久保玲','女性創業者・国際ファッション'),
(21,'山本耀司','Yohji Yamamoto','やまもと ようじ',1943,NULL,'東京都','ファッション','ヨウジヤマモト創業者。日本発のデザイナーブランドを国際市場に展開した。','["ヨウジヤマモト"]','other','慶應義塾大学法学部',7.3,0,1,'https://ja.wikipedia.org/wiki/山本耀司','国際ファッションブランド'),
(22,'菊池武夫','Takeo Kikuchi','きくち たけお',1939,NULL,'東京都','ファッション','メンズブランドを展開し、戦後日本のデザイナーズファッション市場を広げた。','["TAKEO KIKUCHI"]','other','文化服装学院',6.8,0,1,'https://ja.wikipedia.org/wiki/菊池武夫','メンズファッション事業'),
(23,'鳥居ユキ','Yuki Torii','とりい ゆき',1943,NULL,'東京都','ファッション・女性起業','ユキトリヰブランドを展開し、女性デザイナーとして高級既製服市場で活動した。','["ユキトリヰ"]','merchant','文化学院',6.6,0,1,'https://ja.wikipedia.org/wiki/鳥居ユキ','女性ファッション経営'),
(24,'花井幸子','Yukiko Hanai','はない ゆきこ',1937,NULL,'神奈川県','ファッション・女性起業','ハナイユキコブランドを展開し、婦人服事業とデザイン教育に関わった。','["ハナイユキコ"]','other','文化服装学院',6.6,0,1,'https://ja.wikipedia.org/wiki/花井幸子','女性ファッション事業'),
(25,'桂由美','Yumi Katsura','かつら ゆみ',1930,2024,'東京都','ブライダル・女性起業','ブライダルファッションを事業化し、日本の婚礼衣装市場を近代化した。','["ユミカツラ"]','other','共立女子大学',7.1,0,1,'https://ja.wikipedia.org/wiki/桂由美','ブライダル産業の形成'),
(26,'島田順子','Junko Shimada','しまだ じゅんこ',1941,NULL,'千葉県','ファッション・海外展開','パリを拠点にブランドを展開し、日本人デザイナーの海外事業化を進めた。','["JUNKO SHIMADA"]','other','杉野学園ドレスメーカー学院',6.7,0,1,'https://ja.wikipedia.org/wiki/島田順子','海外ファッション事業'),
(27,'コシノヒロコ','Hiroko Koshino','こしの ひろこ',1937,NULL,'大阪府','ファッション・女性起業','ヒロココシノブランドを展開し、戦後女性デザイナーの事業化を進めた。','["ヒロココシノ"]','merchant','文化服装学院',6.8,0,1,'https://ja.wikipedia.org/wiki/コシノヒロコ','女性ファッション経営'),
(28,'高田賢三','Kenzo Takada','たかだ けんぞう',1939,2020,'兵庫県','ファッション・海外展開','KENZO創業者。パリで日本人デザイナーブランドを確立し、国際ファッション市場で成功した。','["KENZO"]','other','文化服装学院',7.3,0,1,'https://ja.wikipedia.org/wiki/高田賢三','海外ブランド創業'),
(29,'堀貞一郎','Teiichiro Hori','ほり ていいちろう',1929,2014,'東京都','レジャー・企画','オリエンタルランドで東京ディズニーランド誘致・企画に関わり、テーマパーク事業を日本に定着させた。','["東京ディズニーランド"]','other','慶應義塾大学',6.9,0,1,'https://ja.wikipedia.org/wiki/堀貞一郎','テーマパーク事業'),
(30,'高橋政知','Masatomo Takahashi','たかはし まさとも',1913,2000,'福島県','レジャー・不動産','オリエンタルランド社長。東京ディズニーランド開業を実現し、湾岸レジャー開発を進めた。','["東京ディズニーランド"]','other','東京帝国大学法学部',7.0,0,1,'https://ja.wikipedia.org/wiki/高橋政知','テーマパーク開発'),
(31,'永田雅一','Masaichi Nagata','ながた まさいち',1906,1985,'京都府','映画・興行','大映社長。映画製作と興行を拡大し、戦後映画産業の競争を担った。','["大映"]','merchant','実務経験を経て映画事業',6.9,0,1,'https://ja.wikipedia.org/wiki/永田雅一','映画会社経営'),
(32,'城戸四郎','Shiro Kido','きど しろう',1894,1977,'東京都','映画・興行','松竹社長。映画製作・興行の近代化を進め、戦後映画会社経営に影響した。','["松竹"]','other','東京帝国大学法学部',6.8,0,1,'https://ja.wikipedia.org/wiki/城戸四郎','映画興行経営'),
(33,'倉田主税','Chikara Kurata','くらた ちから',1921,2011,'東京都','電機','日立製作所社長。総合電機企業の品質・生産体制と国際事業を担った。','["日立製作所"]','other','東京帝国大学工学部',6.7,0,1,'https://ja.wikipedia.org/wiki/倉田主税','総合電機経営'),
(34,'金井務','Tsutomu Kanai','かない つとむ',1929,2020,'東京都','電機','日立製作所社長。重電・情報・電子事業の複合経営を進めた。','["日立製作所"]','other','東京大学工学部',6.6,0,1,'https://ja.wikipedia.org/wiki/金井務','電機企業経営'),
(35,'谷井昭雄','Akio Tanii','たにい あきお',1928,2021,'大阪府','電機','松下電器産業社長。家電の国際展開と事業部制経営を継承発展させた。','["松下電器産業"]','other','神戸大学経営学部',6.6,0,1,'https://ja.wikipedia.org/wiki/谷井昭雄','家電企業経営'),
(36,'森下洋一','Yoichi Morishita','もりした よういち',1934,NULL,'兵庫県','電機','松下電器産業社長。海外事業とデジタル化前夜の家電経営に携わった。','["松下電器産業"]','other','大阪大学経済学部',6.5,0,1,'https://ja.wikipedia.org/wiki/森下洋一','家電企業経営'),
(37,'野田一夫','Kazuo Noda','のだ かずお',1927,2022,'東京都','経営教育','日本総合研究所などで経営教育・ベンチャー支援に携わり、戦後の経営人材育成に影響した。','["経営教育","ベンチャー支援"]','other','東京大学',6.4,0,1,'https://ja.wikipedia.org/wiki/野田一夫','経営教育'),
(38,'中山悠','Hisashi Nakayama','なかやま ひさし',1927,2010,'東京都','医薬品','第一製薬社長。医薬品企業の研究開発と営業体制の近代化に関わった。','["第一製薬"]','other','東京大学薬学部',6.3,0,1,'https://ja.wikipedia.org/wiki/中山悠','製薬企業経営'),
(39,'松尾静磨','Shizuma Matsuo','まつお しずま',1903,1972,'佐賀県','航空','日本航空初代社長。戦後民間航空会社の立ち上げと運航体制整備を担った。','["日本航空"]','other','東京帝国大学法学部',6.7,0,1,'https://ja.wikipedia.org/wiki/松尾静磨','民間航空立ち上げ'),
(40,'朝田静夫','Shizuo Asada','あさだ しずお',1934,NULL,'東京都','航空','全日本空輸社長。国内航空の競争環境と路線展開を担った。','["全日本空輸"]','other','東京大学法学部',6.3,0,1,'https://ja.wikipedia.org/wiki/朝田静夫','航空会社経営'),
(41,'青井忠治','Chuji Aoi','あおい ちゅうじ',1904,1975,'富山県','小売・金融','丸井創業者。月賦販売を広げ、都市小売と消費者信用を結びつけた。','["丸井","月賦販売"]','working_class','実務経験を経て創業',7.0,0,1,'https://ja.wikipedia.org/wiki/青井忠治','月賦小売の創業者'),
(42,'横井英樹','Hideki Yokoi','よこい ひでき',1913,1998,'愛知県','不動産・ホテル','不動産・ホテル事業を展開した実業家。戦後都市不動産投資の象徴的存在となった。','["ホテルニュージャパン"]','working_class','実務経験を経て事業',6.4,0,1,'https://ja.wikipedia.org/wiki/横井英樹','都市不動産事業'),
(43,'木下恭輔','Kyosuke Kinoshita','きのした きょうすけ',1940,NULL,'兵庫県','金融','アコム創業者。個人向け信用供与を店舗網と審査システムで拡大した。','["アコム"]','working_class','実務経験を経て創業',6.4,0,1,'https://ja.wikipedia.org/wiki/木下恭輔','消費者金融創業'),
(44,'福田吉孝','Yoshitaka Fukuda','ふくだ よしたか',1947,NULL,'滋賀県','金融','アイフル創業者。消費者金融会社を全国展開し、個人金融市場の拡大に関わった。','["アイフル"]','working_class','実務経験を経て創業',6.4,0,1,'https://ja.wikipedia.org/wiki/福田吉孝','消費者金融創業'),
(45,'田谷哲哉','Tetsuya Taya','たや てつや',1941,NULL,'東京都','美容サービス','田谷創業者。美容室をチェーン化し、都市型美容サービス業を拡大した。','["TAYA"]','working_class','美容実務',6.3,0,1,'https://ja.wikipedia.org/wiki/田谷哲哉','美容室チェーン'),
(46,'中村長芳','Nagayoshi Nakamura','なかむら ながよし',1924,2007,'福岡県','興行・スポーツビジネス','プロ野球球団経営などに関わり、戦後スポーツ興行ビジネスに影響した。','["ロッテオリオンズ"]','other','実務経験を経て興行事業',6.3,0,1,'https://ja.wikipedia.org/wiki/中村長芳','スポーツ興行経営'),
(47,'小林與三次','Yosaji Kobayashi','こばやし よそじ',1913,1999,'富山県','メディア事業','読売新聞グループ本社社長、日本テレビ会長。新聞・テレビのメディア経営を担った。','["読売新聞","日本テレビ"]','other','東京帝国大学法学部',6.8,0,1,'https://ja.wikipedia.org/wiki/小林與三次','メディア企業経営'),
(48,'氏家齊一郎','Seiichiro Ujiie','うじいえ せいいちろう',1926,2011,'東京都','メディア事業','日本テレビ社長。民放テレビの広告・番組ビジネスを拡大した。','["日本テレビ"]','other','東京大学経済学部',6.7,0,1,'https://ja.wikipedia.org/wiki/氏家齊一郎','テレビ事業経営'),
(49,'渡邉恒雄','Tsuneo Watanabe','わたなべ つねお',1926,NULL,'東京都','メディア事業','読売新聞グループ本社主筆・経営者。新聞・スポーツ・テレビを含むメディア事業に影響した。','["読売新聞グループ本社"]','other','東京大学文学部',6.8,0,1,'https://ja.wikipedia.org/wiki/渡邉恒雄','メディア事業経営'),
(50,'金子宏','Hiroshi Kaneko','かねこ ひろし',1930,NULL,'東京都','税務・専門職','税法学者として企業税務・租税制度に影響し、専門職知識の経済実務への接続を担った。','["租税法"]','other','東京大学法学部',6.1,0,1,'https://ja.wikipedia.org/wiki/金子宏','専門職知識と企業実務');

DROP TABLE IF EXISTS temp_showa_post_business_supplement_valid;
CREATE TEMP TABLE temp_showa_post_business_supplement_valid AS
SELECT row_number() OVER (ORDER BY s.seq) AS rn, s.*
FROM temp_showa_post_business_supplement s
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a
  WHERE a.name_ja=s.name_ja
     OR (a.name_ja=s.name_ja AND a.birth_year=s.birth_year)
)
ORDER BY s.seq
LIMIT (150 - (SELECT COUNT(*) FROM achievers WHERE source_team='codex_showa_post_business'));

SELECT 'supplement_valid', COUNT(*) FROM temp_showa_post_business_supplement_valid;

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, secondary_era_id, domain, sub_domain, achievement_summary,
  notable_works, family_class, family_education, education_path, mentors,
  fame_source, fame_score, is_traditional_great, is_local_excellent,
  data_completeness, source_team, source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  'showa_post', NULL, 'business', sub_domain, achievement_summary,
  notable_works, family_class, NULL, education_path, '[]',
  'wikipedia_ja', fame_score, is_traditional_great, is_local_excellent,
  82, 'codex_showa_post_business', source_url, notes
FROM temp_showa_post_business_supplement_valid;

SELECT 'after_supplement_team_count', COUNT(*) FROM achievers WHERE source_team='codex_showa_post_business';

INSERT INTO achiever_capabilities (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
SELECT a.id, c.capability_id, c.score,
       a.name_ja || '：' || a.achievement_summary,
       a.source_url,
       'codex_showa_post_business capability scoring'
FROM achievers a
JOIN (
  SELECT 'age_entrepreneur' AS capability_id, 9 AS score
  UNION ALL SELECT 'cog_systems', 8
  UNION ALL SELECT 'soc_interpersonal', 8
  UNION ALL SELECT 'age_resilience', 8
) c
WHERE a.source_team='codex_showa_post_business'
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id=a.id AND ac.capability_id=c.capability_id
  );

SELECT 'capability_rows_for_team', COUNT(*)
FROM achiever_capabilities ac
JOIN achievers a ON a.id=ac.achiever_id
WHERE a.source_team='codex_showa_post_business';

COMMIT;

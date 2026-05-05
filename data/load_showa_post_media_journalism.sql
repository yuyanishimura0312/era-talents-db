-- showa_post / media_journalism additions by codex_showa_post_media_journalism
.bail on

BEGIN;

DROP TABLE IF EXISTS temp_showa_post_media_batch1;
CREATE TEMP TABLE temp_showa_post_media_batch1 (
  name_ja TEXT, name_en TEXT, name_kana TEXT, birth_year INTEGER, death_year INTEGER,
  birth_place TEXT, sub_domain TEXT, achievement_summary TEXT, notable_works TEXT,
  family_class TEXT, education_path TEXT, fame_score REAL, is_traditional_great INTEGER,
  is_local_excellent INTEGER, source_url TEXT, notes TEXT
);

INSERT INTO temp_showa_post_media_batch1 VALUES
('草柳大蔵','Daizo Kusayanagi','くさやなぎ だいぞう',1924,2002,'神奈川県','journalism_criticism','戦後日本の社会評論・人物評論で新聞、雑誌、テレビを横断して大衆的な論点形成を担った。','["実力者の条件","現代王国論"]','other','東京帝国大学法学部',7.3,0,0,'https://ja.wikipedia.org/wiki/草柳大蔵','戦後評論・テレビ言論'),
('大森実','Minoru Omori','おおもり みのる',1922,2010,'大阪府','international_reporting','毎日新聞外信記者としてベトナム戦争報道など国際報道を展開し、独立後も現地取材型ジャーナリズムを続けた。','["ベトナムから来たもう一つの手紙","国際事件記者"]','other','大阪外国語学校',7.6,1,0,'https://ja.wikipedia.org/wiki/大森実','外信・戦争報道'),
('立花隆','Takashi Tachibana','たちばな たかし',1940,2021,'長崎県','investigative_journalism','田中角栄研究をはじめ政治・科学・知の現場を取材し、調査報道と長編ノンフィクションの基準を押し上げた。','["田中角栄研究","宇宙からの帰還","脳死"]','other','東京大学文学部',9.2,1,0,'https://ja.wikipedia.org/wiki/立花隆','調査報道・知識人ジャーナリズム'),
('黒田清','Kiyoshi Kuroda','くろだ きよし',1931,2000,'大阪府','newspaper_journalism','読売新聞大阪本社社会部で黒田軍団と呼ばれる取材体制を築き、弱者の視点を重視した社会部報道を実践した。','["新聞記者の現場","黒田ジャーナル"]','other','京都大学文学部',7.2,0,1,'https://ja.wikipedia.org/wiki/黒田清','大阪社会部報道'),
('柳田邦男','Kunio Yanagida','やなぎだ くにお',1936,NULL,'栃木県','nonfiction_reporting','航空事故、医療、災害、生命倫理を長期取材し、事故調査型ノンフィクションを社会に定着させた。','["マッハの恐怖","犠牲","空白の天気図"]','other','東京大学経済学部',8.4,1,0,'https://ja.wikipedia.org/wiki/柳田邦男','事故・科学報道'),
('佐野眞一','Shinichi Sano','さの しんいち',1947,2022,'東京都','nonfiction_reporting','人物評伝と企業・地域取材を重ね、戦後日本の権力、流通、地方社会を追跡するノンフィクションを残した。','["旅する巨人","カリスマ","東電OL殺人事件"]','other','早稲田大学第一文学部',7.8,0,0,'https://ja.wikipedia.org/wiki/佐野眞一','評伝・調査ノンフィクション'),
('櫻井よしこ','Yoshiko Sakurai','さくらい よしこ',1945,NULL,'ベトナム','broadcast_commentary','ニュースキャスターから論説活動へ進み、安全保障、政治、歴史認識をめぐる保守論壇の主要な発信者となった。','["エイズ犯罪 血友病患者の悲劇","日本の危機"]','other','ハワイ大学マノア校',8.0,1,0,'https://ja.wikipedia.org/wiki/櫻井よしこ','キャスター・論説'),
('岸井成格','Shigetada Kishii','きしい しげただ',1944,2018,'東京都','political_journalism','毎日新聞政治部記者、論説委員、テレビ解説者として政治取材と選挙報道の経験を公共的解説へ接続した。','["岸井成格の政治読本"]','other','慶應義塾大学法学部',7.4,0,0,'https://ja.wikipedia.org/wiki/岸井成格','政治報道'),
('木村太郎','Taro Kimura','きむら たろう',1938,NULL,'東京都','broadcast_commentary','NHK記者、キャスターを経て民放ニュース解説で国際情勢と政治を平易に伝えた。','["木村太郎のニュースを読む技術"]','other','慶應義塾大学法学部',7.5,0,0,'https://ja.wikipedia.org/wiki/木村太郎_(ジャーナリスト)','ニュース解説'),
('小中陽太郎','Yotaro Konaka','こなか ようたろう',1934,2024,'兵庫県','civic_journalism','NHK記者を経てベトナム反戦、教育、地域、市民運動を横断する評論とノンフィクションを展開した。','["ベトナムのダーちゃん","市民のためのメディア入門"]','other','東京大学文学部',6.8,0,1,'https://ja.wikipedia.org/wiki/小中陽太郎','市民派ジャーナリズム'),
('石川文洋','Bunyo Ishikawa','いしかわ ぶんよう',1938,NULL,'沖縄県','photojournalism','ベトナム戦争を現地で長期撮影し、沖縄出身の報道写真家として戦争と民衆の記録を伝えた。','["戦場カメラマン","ベトナム戦争と私"]','other','東京写真短期大学',7.8,0,1,'https://ja.wikipedia.org/wiki/石川文洋','沖縄・戦場写真'),
('吉田ルイ子','Ruiko Yoshida','よしだ ルイこ',1934,NULL,'北海道','photojournalism','アメリカ社会、人種差別、女性、子どもを取材し、写真と文章を組み合わせた社会派ドキュメンタリーを開いた。','["ハーレムの熱い日々","南ア・アパルトヘイト共和国"]','other','慶應義塾大学文学部',7.4,0,1,'https://ja.wikipedia.org/wiki/吉田ルイ子','女性フォトジャーナリスト'),
('下村満子','Mitsuko Shimomura','しもむら みつこ',1938,NULL,'東京都','international_reporting','朝日新聞記者として女性初の海外特派員級の仕事を担い、国際報道と女性の働き方の両面で先駆的役割を果たした。','["アメリカの女たち","男たちのらしさ"]','other','慶應義塾大学経済学部',7.1,0,1,'https://ja.wikipedia.org/wiki/下村満子','女性記者・国際報道'),
('兼高かおる','Kaoru Kanetaka','かねたか かおる',1928,2019,'兵庫県','travel_journalism','世界の旅をテレビで長期紹介し、海外情報が限られた時代に国際理解型の紀行ジャーナリズムを普及させた。','["兼高かおる世界の旅"]','other','ロサンゼルス市立大学',8.0,1,0,'https://ja.wikipedia.org/wiki/兼高かおる','紀行番組'),
('田丸美寿々','Misuzu Tamaru','たまる みすず',1952,NULL,'広島県','news_anchor','民放女性ニュースキャスターの先駆として報道番組の司会、インタビュー、選挙報道に取り組んだ。','["FNNニュースレポート6:00","報道特集"]','other','東京外国語大学',7.1,0,0,'https://ja.wikipedia.org/wiki/田丸美寿々','女性キャスター'),
('小宮悦子','Etsuko Komiya','こみや えつこ',1958,NULL,'埼玉県','news_anchor','テレビ朝日系ニュース番組で長くメインキャスターを務め、夕方ニュースの語り口と生活者目線を定着させた。','["ニュースステーション","スーパーJチャンネル"]','other','東京都立大学人文学部',7.0,0,0,'https://ja.wikipedia.org/wiki/小宮悦子','ニュースキャスター'),
('安藤優子','Yuko Ando','あんどう ゆうこ',1958,NULL,'千葉県','news_anchor','報道番組の現場リポートと長時間ニュース司会を担い、女性メインキャスターの職域を広げた。','["FNNスーパータイム","ニュースJAPAN","直撃LIVE グッディ!"]','other','上智大学外国語学部',7.2,0,0,'https://ja.wikipedia.org/wiki/安藤優子','ニュースキャスター'),
('宮崎緑','Midori Miyazaki','みやざき みどり',1958,NULL,'神奈川県','news_anchor','NHKニュース番組で国際報道を伝え、のち政策・教育分野にも関わる報道キャスターとして活動した。','["ニュースセンター9時"]','other','慶應義塾大学法学部',6.8,0,0,'https://ja.wikipedia.org/wiki/宮崎緑','国際ニュースキャスター'),
('高橋圭三','Keizo Takahashi','たかはし けいぞう',1918,2002,'岩手県','broadcast_announcing','NHKアナウンサーから民放司会者へ移り、紅白歌合戦や大型番組でテレビ司会の基礎をつくった。','["NHK紅白歌合戦","私の秘密"]','other','日本大学芸術学部',7.5,1,0,'https://ja.wikipedia.org/wiki/高橋圭三','放送司会'),
('逸見政孝','Masataka Itsumi','いつみ まさたか',1945,1993,'大阪府','broadcast_announcing','フジテレビアナウンサーからフリーへ転じ、ニュース、情報、バラエティを横断するテレビ司会像を示した。','["FNNスーパータイム","クイズ世界はSHOW by ショーバイ!!"]','other','早稲田大学第一文学部',7.5,1,0,'https://ja.wikipedia.org/wiki/逸見政孝','アナウンサー・司会'),
('須田哲夫','Tetsuo Suda','すだ てつお',1948,NULL,'東京都','broadcast_announcing','フジテレビ報道アナウンサーとしてニュース番組、災害報道、選挙特番の安定した進行を担った。','["FNNスーパータイム","FNNスピーク"]','other','慶應義塾大学法学部',6.4,0,0,'https://ja.wikipedia.org/wiki/須田哲夫','報道アナウンサー'),
('山本文郎','Fumio Yamamoto','やまもと ふみお',1934,2014,'東京都','broadcast_announcing','TBSアナウンサーとしてニュース、ワイドショー、ラジオを担当し、民放の生活情報番組を支えた。','["モーニングジャンボ","テレポートTBS6"]','other','早稲田大学第一文学部',6.4,0,0,'https://ja.wikipedia.org/wiki/山本文郎','民放アナウンサー'),
('小川宏','Hiroshi Ogawa','おがわ ひろし',1926,2016,'東京都','broadcast_announcing','NHKからフジテレビへ移り、小川宏ショーで朝のワイドショー形式を定着させた。','["小川宏ショー"]','other','早稲田大学専門部',7.3,1,0,'https://ja.wikipedia.org/wiki/小川宏','ワイドショー司会'),
('露木茂','Shigeru Tsuyuki','つゆき しげる',1940,NULL,'東京都','broadcast_announcing','フジテレビ報道アナウンサーとしてニュース、選挙、事件報道を担当し、民放報道の顔となった。','["FNNスーパータイム","ニュースJAPAN"]','other','早稲田大学政治経済学部',6.8,0,0,'https://ja.wikipedia.org/wiki/露木茂','報道アナウンサー'),
('森本毅郎','Takero Morimoto','もりもと たけろう',1939,NULL,'東京都','news_anchor','NHK記者・アナウンサーから民放キャスターへ転じ、ニュースと生活情報を結ぶ番組進行を担った。','["ニュースワイド","噂の!東京マガジン"]','other','慶應義塾大学文学部',7.0,0,0,'https://ja.wikipedia.org/wiki/森本毅郎','ニュースキャスター'),
('磯村尚徳','Hisanori Isomura','いそむら ひさのり',1929,2023,'東京都','international_broadcasting','NHKヨーロッパ総局長、ニュースキャスターとして国際報道と公共放送の解説文化を築いた。','["ニュースセンター9時"]','other','東京大学文学部',7.5,1,0,'https://ja.wikipedia.org/wiki/磯村尚徳','公共放送・国際報道'),
('大塚範一','Norikazu Otsuka','おおつか のりかず',1948,NULL,'東京都','broadcast_announcing','NHKアナウンサーから民放情報番組へ移り、朝の情報番組で長期にわたりニュース解説と進行を担った。','["めざましテレビ"]','other','早稲田大学政治経済学部',6.9,0,0,'https://ja.wikipedia.org/wiki/大塚範一','情報番組司会'),
('鈴木健二','Kenji Suzuki','すずき けんじ',1929,2024,'東京都','broadcast_announcing','NHKアナウンサーとしてクイズ、教養、インタビュー番組を担当し、公共放送の語りの技術を磨いた。','["クイズ面白ゼミナール","歴史への招待"]','other','東北大学文学部',7.7,1,0,'https://ja.wikipedia.org/wiki/鈴木健二','教養番組司会'),
('宮田輝','Teru Miyata','みやた てる',1921,1990,'東京都','broadcast_announcing','NHKアナウンサーとして紅白歌合戦、のど自慢など国民的番組の司会を務めた。','["NHK紅白歌合戦","のど自慢素人演芸会"]','other','東京帝国大学文学部',7.2,1,0,'https://ja.wikipedia.org/wiki/宮田輝','公共放送司会'),
('芥川隆行','Takayuki Akutagawa','あくたがわ たかゆき',1919,1990,'東京都','broadcast_narration','ラジオ東京、TBS系の語り手としてドラマ、演芸、ナレーションで放送の音声表現を発展させた。','["ナショナル劇場","水戸黄門"]','other','東京高等師範学校',6.7,0,0,'https://ja.wikipedia.org/wiki/芥川隆行','放送ナレーション'),
('糸居五郎','Goro Itoi','いとい ごろう',1921,1984,'東京都','radio_personality','ニッポン放送の深夜放送で若者文化と音楽紹介を結び、ラジオDJの職能を確立した。','["オールナイトニッポン"]','other','早稲田大学',6.9,0,0,'https://ja.wikipedia.org/wiki/糸居五郎','ラジオDJ'),
('吉田照美','Terumi Yoshida','よしだ てるみ',1951,NULL,'東京都','radio_personality','文化放送アナウンサー、ラジオパーソナリティとして深夜放送と情報番組で聴取者参加型の番組を展開した。','["セイ!ヤング","吉田照美のやる気MANMAN!"]','other','早稲田大学政治経済学部',6.8,0,0,'https://ja.wikipedia.org/wiki/吉田照美','ラジオ・情報番組'),
('花森安治','Yasuji Hanamori','はなもり やすじ',1911,1978,'兵庫県','magazine_editing','暮しの手帖を創刊し、広告に依存しない商品テストと生活者視点の編集で消費社会を批評した。','["暮しの手帖","一銭五厘の旗"]','other','東京帝国大学文学部',8.5,1,0,'https://ja.wikipedia.org/wiki/花森安治','生活雑誌編集'),
('大橋鎭子','Shizuko Ohashi','おおはし しずこ',1920,2013,'東京府','magazine_publishing','暮しの手帖社を創業し、戦後の生活改善、商品テスト、女性読者に根ざす出版事業を支えた。','["暮しの手帖"]','other','日本女子大学校',8.0,1,0,'https://ja.wikipedia.org/wiki/大橋鎭子','女性出版人'),
('嶋中鵬二','Hoji Shimanaka','しまなか ほうじ',1923,1997,'東京都','publishing_management','中央公論社社長として総合雑誌と単行本出版を率い、戦後論壇誌の経営と編集基盤を担った。','["中央公論"]','merchant','慶應義塾大学経済学部',6.9,0,0,'https://ja.wikipedia.org/wiki/嶋中鵬二','総合雑誌経営'),
('池島信平','Shinpei Ikejima','いけじま しんぺい',1909,1973,'東京都','magazine_editing','文藝春秋編集者、社長として総合月刊誌と文芸出版を発展させ、戦後論壇の場を作った。','["文藝春秋"]','other','東京帝国大学文学部',7.5,1,0,'https://ja.wikipedia.org/wiki/池島信平','総合誌編集'),
('村上兵衛','Hyoe Murakami','むらかみ ひょうえ',1923,2003,'栃木県','magazine_editing','文藝春秋の編集者・作家として戦後の文芸誌、ノンフィクション、人物記事の編集に関わった。','["文藝春秋","桜と剣"]','other','東京大学文学部',6.3,0,0,'https://ja.wikipedia.org/wiki/村上兵衛','文芸・総合誌編集'),
('粕谷一希','Kazuki Kasuya','かすや かずき',1930,2014,'東京都','magazine_editing','中央公論編集長を経て評論家として戦後知識人と論壇誌の編集文化を記録、分析した。','["中央公論","二十歳にして心朽ちたり"]','other','東京大学文学部',6.7,0,0,'https://ja.wikipedia.org/wiki/粕谷一希','論壇誌編集'),
('山本夏彦','Natsuhiko Yamamoto','やまもと なつひこ',1915,2002,'東京都','magazine_editing','工作社を拠点に室内、暮し、言葉をめぐる随筆と編集を行い、少部数雑誌文化を支えた。','["室内","茶の間の正義"]','merchant','東京帝国大学中退',7.1,0,1,'https://ja.wikipedia.org/wiki/山本夏彦','小出版社・随筆編集'),
('小林勇','Isamu Kobayashi','こばやし いさむ',1903,1981,'長野県','publishing_editing','岩波書店編集者として学術・教養出版を支え、戦後日本の知識流通に寄与した。','["惜櫟荘主人","岩波新書編集"]','other','旧制中学',6.8,0,0,'https://ja.wikipedia.org/wiki/小林勇','岩波編集者'),
('塩澤実信','Minobu Shiozawa','しおざわ みのぶ',1930,2023,'長野県','publishing_history','出版ジャーナリストとして出版社、編集者、雑誌史を記録し、業界史の基礎資料を残した。','["出版界おもしろ豆事典","雑誌記者池島信平"]','other','法政大学文学部',6.2,0,1,'https://ja.wikipedia.org/wiki/塩澤実信','出版史記録'),
('小林信彦','Nobuhiko Kobayashi','こばやし のぶひこ',1932,NULL,'東京府','magazine_editing','ヒッチコック・マガジン編集長を経て、ミステリ、喜劇、テレビ文化批評を横断した。','["ヒッチコック・マガジン","日本の喜劇人"]','other','早稲田大学第一文学部',7.3,0,0,'https://ja.wikipedia.org/wiki/小林信彦','雑誌編集・文化批評'),
('椎名誠','Makoto Shiina','しいな まこと',1944,NULL,'東京都','magazine_editing','本の雑誌創刊に関わり、書評、旅、エッセイを結ぶ読者参加型の出版文化を広げた。','["本の雑誌","さらば国分寺書店のオババ"]','other','東京写真大学中退',7.4,0,0,'https://ja.wikipedia.org/wiki/椎名誠','書評誌・エッセイ'),
('嵐山光三郎','Kozaburo Arashiyama','あらしやま こうざぶろう',1942,NULL,'静岡県','magazine_editing','平凡パンチ、太陽などの編集を経て、昭和の雑誌文化、旅、食、文芸批評を担った。','["素人庖丁記","文人悪食"]','other','國學院大學文学部',6.8,0,0,'https://ja.wikipedia.org/wiki/嵐山光三郎','雑誌編集・随筆');

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place, primary_era_id,
  domain, sub_domain, achievement_summary, notable_works, family_class, education_path,
  fame_source, fame_score, is_traditional_great, is_local_excellent, data_completeness,
  source_team, source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place, 'showa_post',
  'media_journalism', sub_domain, achievement_summary, notable_works, family_class, education_path,
  'wikipedia_ja_or_industry_reference', fame_score, is_traditional_great, is_local_excellent, 88,
  'codex_showa_post_media_journalism', source_url, notes
FROM temp_showa_post_media_batch1 b
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a WHERE a.name_ja=b.name_ja AND a.birth_year=b.birth_year
);

COMMIT;

SELECT 'after_batch1_count', COUNT(*) FROM achievers
WHERE primary_era_id='showa_post' AND domain='media_journalism'
  AND source_team='codex_showa_post_media_journalism';

BEGIN;

DROP TABLE IF EXISTS temp_showa_post_media_batch2;
CREATE TEMP TABLE temp_showa_post_media_batch2 AS SELECT * FROM temp_showa_post_media_batch1 WHERE 0;

INSERT INTO temp_showa_post_media_batch2 VALUES
('長井勝一','Katsuichi Nagai','ながい かついち',1921,1996,'宮城県','manga_editing','青林堂を創業し、月刊漫画ガロを通じて白土三平、水木しげる、つげ義春らの実験的漫画表現を世に出した。','["月刊漫画ガロ"]','other','旧制中学',7.7,1,0,'https://ja.wikipedia.org/wiki/長井勝一','漫画編集'),
('内田勝','Masaru Uchida','うちだ まさる',1935,2008,'東京都','manga_editing','週刊少年マガジン編集長として劇画路線と少年漫画誌の大衆化を推進した。','["週刊少年マガジン"]','other','早稲田大学',7.2,0,0,'https://ja.wikipedia.org/wiki/内田勝_(編集者)','漫画誌編集'),
('鳥嶋和彦','Kazuhiko Torishima','とりしま かずひこ',1952,NULL,'新潟県','manga_editing','週刊少年ジャンプ編集者として鳥山明らを担当し、漫画編集者の作家育成モデルを可視化した。','["Dr.スランプ","ドラゴンボール","週刊少年ジャンプ"]','other','慶應義塾大学法学部',7.9,1,0,'https://ja.wikipedia.org/wiki/鳥嶋和彦','漫画編集・出版経営'),
('堀江信彦','Nobuhiko Horie','ほりえ のぶひこ',1955,NULL,'熊本県','manga_editing','週刊少年ジャンプ編集長として北斗の拳などを担当し、漫画編集と版権ビジネスを結んだ。','["北斗の拳","週刊少年ジャンプ","コミックバンチ"]','other','早稲田大学法学部',7.0,0,0,'https://ja.wikipedia.org/wiki/堀江信彦','漫画編集'),
('角南攻','Osamu Sunami','すなみ おさむ',1944,NULL,'岡山県','manga_editing','週刊少年ジャンプ編集者として少年漫画誌の編集体制と新人発掘に関わった。','["週刊少年ジャンプ"]','other','明治大学',6.2,0,1,'https://ja.wikipedia.org/wiki/角南攻','漫画編集'),
('沢田教一','Kyoichi Sawada','さわだ きょういち',1936,1970,'青森県','photojournalism','ベトナム戦争を撮影し、UPI通信の報道写真家としてピュリツァー賞受賞作を残した。','["安全への逃避"]','other','青森県立青森高等学校',8.4,1,0,'https://ja.wikipedia.org/wiki/沢田教一','戦争写真'),
('秋山亮二','Ryoji Akiyama','あきやま りょうじ',1942,NULL,'東京都','photojournalism','写真家として子ども、都市、家族を記録し、雑誌・広告・報道を横断する視覚文化に貢献した。','["なら","津軽"]','other','早稲田大学文学部',6.5,0,1,'https://ja.wikipedia.org/wiki/秋山亮二','写真記録'),
('濱谷浩','Hiroshi Hamaya','はまや ひろし',1915,1999,'東京都','documentary_photography','雪国、民俗、社会運動を長期撮影し、日本のドキュメンタリー写真を国際的水準へ押し上げた。','["雪国","裏日本"]','other','関東商業学校',7.9,1,0,'https://ja.wikipedia.org/wiki/濱谷浩','ドキュメンタリー写真'),
('土門拳','Ken Domon','どもん けん',1909,1990,'山形県','documentary_photography','リアリズム写真運動を主導し、戦後日本の報道写真、仏像写真、社会記録に大きな影響を与えた。','["筑豊のこどもたち","古寺巡礼"]','working_class','日本工房',9.0,1,0,'https://ja.wikipedia.org/wiki/土門拳','リアリズム写真'),
('長倉洋海','Hiromi Nagakura','ながくら ひろみ',1952,NULL,'北海道','photojournalism','アフガニスタン、中南米、紛争地の民衆を長期取材し、戦争を生活者の視点から伝えた。','["マスード 愛しの大地アフガン","サルバドル 遥かなる日々"]','other','同志社大学法学部',7.0,0,1,'https://ja.wikipedia.org/wiki/長倉洋海','紛争地写真'),
('広河隆一','Ryuichi Hirokawa','ひろかわ りゅういち',1943,NULL,'天津市','photojournalism','中東、チェルノブイリ、原発事故を取材し、写真誌DAYS JAPANを通じて市民型報道写真の場を作った。','["DAYS JAPAN","チェルノブイリ報告"]','other','早稲田大学教育学部',7.0,0,0,'https://ja.wikipedia.org/wiki/広河隆一','フォトジャーナリズム'),
('橋田信介','Shinsuke Hashida','はしだ しんすけ',1942,2004,'山口県','war_reporting','ベトナム、中東、イラクなど紛争地を取材し、テレビと雑誌で現場報道を続けた。','["戦場特派員","イラクの中心で、バカとさけぶ"]','other','法政大学',6.8,0,1,'https://ja.wikipedia.org/wiki/橋田信介','戦争報道'),
('一ノ瀬泰造','Taizo Ichinose','いちのせ たいぞう',1947,1973,'佐賀県','photojournalism','カンボジア内戦を撮影し、若い戦場カメラマン像と取材倫理をめぐる議論を残した。','["地雷を踏んだらサヨウナラ"]','other','日本大学芸術学部',7.2,1,0,'https://ja.wikipedia.org/wiki/一ノ瀬泰造','戦場写真'),
('石井ふく子','Fukuko Ishii','いしい ふくこ',1926,NULL,'東京都','television_production','テレビドラマプロデューサーとしてホームドラマと長寿番組を制作し、民放テレビの制作現場を牽引した。','["渡る世間は鬼ばかり","肝っ玉かあさん"]','other','日本女子経済短期大学',8.1,1,0,'https://ja.wikipedia.org/wiki/石井ふく子','テレビ制作'),
('横澤彪','Takeshi Yokozawa','よこざわ たけし',1937,2011,'群馬県','television_production','フジテレビのプロデューサーとして漫才ブーム、バラエティ番組の制作体制を作り、テレビ娯楽の編成を変えた。','["オレたちひょうきん族","THE MANZAI"]','other','東京大学文学部',7.4,1,0,'https://ja.wikipedia.org/wiki/横澤彪','テレビバラエティ制作'),
('萩元晴彦','Haruhiko Hagiwara','はぎもと はるひこ',1930,2001,'東京都','television_documentary','テレビマンユニオン創設に関わり、ドキュメンタリーと教養番組を独立制作の形で切り開いた。','["遠くへ行きたい","オーケストラがやって来た"]','other','東京大学文学部',7.2,0,0,'https://ja.wikipedia.org/wiki/萩元晴彦','独立テレビ制作'),
('今野勉','Tsutomu Konno','こんの つとむ',1936,NULL,'秋田県','television_documentary','テレビディレクターとしてドキュメンタリー、ドラマ、メディア論を横断し、テレビ表現の批評性を追求した。','["七人の刑事","テレビの嘘を見破る"]','other','東北大学文学部',7.0,0,0,'https://ja.wikipedia.org/wiki/今野勉','テレビ演出・メディア論'),
('村木良彦','Yoshihiko Muraki','むらき よしひこ',1935,2008,'東京都','television_documentary','東京12チャンネル、日本テレビ、テレビマンユニオンで実験的番組と独立制作を推進した。','["テレビマンユニオン","ドキュメンタリー青春"]','other','早稲田大学文学部',6.6,0,1,'https://ja.wikipedia.org/wiki/村木良彦','独立制作'),
('牛山純一','Junichi Ushiyama','うしやま じゅんいち',1930,1997,'東京都','television_documentary','日本テレビのドキュメンタリー制作者として世界各地の記録番組を制作し、映像記録の国際性を高めた。','["ノンフィクション劇場","すばらしい世界旅行"]','other','慶應義塾大学',6.9,0,0,'https://ja.wikipedia.org/wiki/牛山純一','テレビドキュメンタリー'),
('大谷昭宏','Akihiro Otani','おおたに あきひろ',1945,NULL,'東京都','investigative_journalism','読売新聞大阪社会部から独立し、事件報道、警察取材、テレビ解説で現場型ジャーナリズムを続けた。','["事件記者という生き方"]','other','早稲田大学第一文学部',6.8,0,0,'https://ja.wikipedia.org/wiki/大谷昭宏','事件報道'),
('俵孝太郎','Kotaro Tawara','たわら こうたろう',1930,2023,'東京都','broadcast_commentary','産経新聞記者からニュースキャスターへ転じ、政治解説と討論番組でテレビ言論に関わった。','["FNNニュースレポート23:00"]','other','東京大学文学部',6.9,0,0,'https://ja.wikipedia.org/wiki/俵孝太郎','政治解説'),
('料治直矢','Naoya Ryoji','りょうじ なおや',1935,1997,'東京都','news_anchor','TBSの報道記者、ニュースキャスターとしてJNN報道特集などで硬派な報道番組を担った。','["JNN報道特集","筑紫哲也のニュース23"]','other','早稲田大学',6.7,0,0,'https://ja.wikipedia.org/wiki/料治直矢','報道キャスター'),
('小島一慶','Ikkei Kojima','こじま いっけい',1944,2020,'長崎県','broadcast_announcing','TBSアナウンサーとしてラジオ、テレビの情報番組を担当し、民放アナウンサーの話芸を支えた。','["パックインミュージック","どうぶつ奇想天外!"]','other','早稲田大学',6.2,0,1,'https://ja.wikipedia.org/wiki/小島一慶','民放アナウンス'),
('久和ひとみ','Hitomi Kuwa','くわ ひとみ',1960,2001,'東京都','news_anchor','テレビ朝日、TBS系の報道番組でキャスターを務め、1980年代後半以降の女性ニュース司会を担った。','["ニュースステーション","JNNニュースの森"]','other','東京大学文学部',6.5,0,0,'https://ja.wikipedia.org/wiki/久和ひとみ','ニュースキャスター'),
('渡邉恒雄','Tsuneo Watanabe','わたなべ つねお',1926,2024,'東京府','media_management','読売新聞政治記者から主筆、社長へ進み、新聞経営、政治報道、プロ野球メディアを強く動かした。','["読売新聞","読売ジャイアンツ"]','other','東京大学文学部',8.3,1,0,'https://ja.wikipedia.org/wiki/渡邉恒雄','新聞経営・政治報道'),
('氏家齊一郎','Seiichiro Ujiie','うじいえ せいいちろう',1926,2011,'東京都','media_management','日本テレビ社長、会長として民放テレビ経営と放送制度をめぐる業界運営に関わった。','["日本テレビ放送網"]','other','東京大学経済学部',7.2,0,0,'https://ja.wikipedia.org/wiki/氏家齊一郎','民放経営'),
('北村正任','Masato Kitamura','きたむら まさとう',1941,NULL,'東京都','newspaper_management','毎日新聞記者、社長として新聞経営と紙面改革に携わり、日本新聞協会会長も務めた。','["毎日新聞"]','other','東京大学法学部',6.3,0,0,'https://ja.wikipedia.org/wiki/北村正任','新聞経営'),
('箱島信一','Shinichi Hakojima','はこしま しんいち',1937,NULL,'福岡県','newspaper_management','朝日新聞記者、社長として全国紙の経営、編集、ジャーナリズム倫理の課題に対応した。','["朝日新聞"]','other','九州大学法学部',6.4,0,0,'https://ja.wikipedia.org/wiki/箱島信一','新聞経営'),
('中江利忠','Toshitada Nakae','なかえ としただ',1929,2019,'大阪府','newspaper_management','朝日新聞社長として全国紙経営と編集組織を率い、戦後新聞産業の制度運営に関わった。','["朝日新聞"]','other','京都大学法学部',6.3,0,0,'https://ja.wikipedia.org/wiki/中江利忠','新聞経営'),
('若宮啓文','Yoshifumi Wakamiya','わかみや よしぶみ',1948,2016,'東京都','editorial_writing','朝日新聞論説主幹、主筆として外交、歴史認識、東アジア論を中心に社説・論説を担った。','["和解とナショナリズム","朝日新聞社説"]','other','東京大学法学部',6.9,0,0,'https://ja.wikipedia.org/wiki/若宮啓文','論説・外交報道'),
('船橋洋一','Yoichi Funabashi','ふなばし よういち',1944,NULL,'北京市','international_reporting','朝日新聞記者、コラムニストとして日米関係、外交、安全保障を取材し、独立系言論機関の創設にも関わった。','["通貨烈烈","カウントダウン・メルトダウン"]','other','東京大学教養学部',7.5,0,0,'https://ja.wikipedia.org/wiki/船橋洋一','国際報道・外交論'),
('加藤千洋','Chihiro Kato','かとう ちひろ',1947,NULL,'東京都','international_reporting','朝日新聞中国総局長、編集委員として中国、アジア報道とテレビ解説を担った。','["胡同の記憶","中国報道"]','other','東京外国語大学',6.5,0,0,'https://ja.wikipedia.org/wiki/加藤千洋','中国報道'),
('竹村健一','Kenichi Takemura','たけむら けんいち',1930,2019,'大阪府','broadcast_commentary','新聞記者、英文誌編集者を経てテレビ時事評論家として国際政治、経済、情報化を大衆向けに語った。','["世相を斬る","報道2001"]','other','京都大学文学部',7.2,1,0,'https://ja.wikipedia.org/wiki/竹村健一','時事評論'),
('増田れい子','Reiko Masuda','ますだ れいこ',1929,NULL,'東京都','newspaper_column','毎日新聞記者、論説委員として生活者の視点からコラム、書評、社会評論を書き続けた。','["女の眼","毎日新聞コラム"]','other','東京女子大学',6.5,0,1,'https://ja.wikipedia.org/wiki/増田れい子','女性新聞記者・コラム'),
('竹中労','Tsutomu Takenaka','たけなか ろう',1930,1991,'東京都','counterculture_journalism','芸能、沖縄、政治、やくざ、反権力文化を取材し、既成メディア外のルポルタージュを展開した。','["美空ひばり","琉球共和国"]','other','旧制中学',7.0,0,1,'https://ja.wikipedia.org/wiki/竹中労','反権力ルポ'),
('ばばこういち','Koichi Baba','ばば こういち',1933,2010,'東京都','broadcast_commentary','放送作家、ジャーナリスト、政治評論家としてテレビ討論と市民向け政治解説を担った。','["スーパーモーニング","朝まで生テレビ!"]','other','早稲田大学',6.4,0,0,'https://ja.wikipedia.org/wiki/ばばこういち','政治評論・放送');

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place, primary_era_id,
  domain, sub_domain, achievement_summary, notable_works, family_class, education_path,
  fame_source, fame_score, is_traditional_great, is_local_excellent, data_completeness,
  source_team, source_url, notes
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place, 'showa_post',
  'media_journalism', sub_domain, achievement_summary, notable_works, family_class, education_path,
  'wikipedia_ja_or_industry_reference', fame_score, is_traditional_great, is_local_excellent, 88,
  'codex_showa_post_media_journalism', source_url, notes
FROM temp_showa_post_media_batch2 b
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a WHERE a.name_ja=b.name_ja AND a.birth_year=b.birth_year
);

INSERT INTO achiever_capabilities (
  achiever_id, capability_id, score, evidence_quote, evidence_source, notes
)
SELECT a.id, v.capability_id, v.score,
       a.name_ja || '：' || v.evidence,
       a.source_url,
       'codex_showa_post_media_journalism capability scoring'
FROM achievers a
JOIN (
  SELECT 'cog_info' AS capability_id, 9 AS score, '取材・編集・放送を通じて情報を収集、検証、社会に伝達した。' AS evidence
  UNION ALL SELECT 'cog_critical', 8, '権力、制度、事件、社会状況を批判的に読み解く報道・編集を行った。'
  UNION ALL SELECT 'soc_interpersonal', 8, 'インタビュー、現場取材、番組進行、読者・視聴者との接点形成を担った。'
  UNION ALL SELECT 'cre_cross_domain', 7, '新聞、雑誌、写真、テレビ、出版など複数領域を結び表現形式を更新した。'
) v
WHERE a.source_team='codex_showa_post_media_journalism'
  AND a.primary_era_id='showa_post'
  AND a.domain='media_journalism'
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id=a.id AND ac.capability_id=v.capability_id
  );

COMMIT;

SELECT 'after_batch2_count', COUNT(*) FROM achievers
WHERE primary_era_id='showa_post' AND domain='media_journalism'
  AND source_team='codex_showa_post_media_journalism';

SELECT 'capability_rows', COUNT(*) FROM achiever_capabilities ac
JOIN achievers a ON a.id=ac.achiever_id
WHERE a.source_team='codex_showa_post_media_journalism'
  AND a.primary_era_id='showa_post'
  AND a.domain='media_journalism';

SELECT 'traditional_great_count', SUM(is_traditional_great), COUNT(*),
       ROUND(100.0 * SUM(is_traditional_great) / COUNT(*), 1)
FROM achievers
WHERE primary_era_id='showa_post' AND domain='media_journalism'
  AND source_team='codex_showa_post_media_journalism';

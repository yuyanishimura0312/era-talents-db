BEGIN;

DROP TABLE IF EXISTS temp.new_achievers_6e;
CREATE TEMP TABLE new_achievers_6e (
  package TEXT,
  name_ja TEXT,
  name_en TEXT,
  name_kana TEXT,
  birth_year INTEGER,
  death_year INTEGER,
  birth_place TEXT,
  primary_era_id TEXT,
  domain TEXT,
  sub_domain TEXT,
  achievement_summary TEXT,
  notable_works TEXT,
  family_class TEXT,
  education_path TEXT,
  fame_source TEXT,
  fame_score REAL,
  is_traditional_great INTEGER,
  is_local_excellent INTEGER,
  data_completeness INTEGER,
  source_url TEXT,
  notes TEXT
);

INSERT INTO new_achievers_6e VALUES
('B','呉仁宝','Wu Renbao','ご じんぽう',1928,2013,'中国江蘇省','showa_post','local_excellent_business','village_enterprise','江蘇省華西村で集団経済と郷鎮企業を組織し、農村工業化の象徴的事例を作った。','["華西村の郷鎮企業運営"]','farmer','地域党組織・農村実務','official_history',6.8,0,1,72,'China Daily obituary; Xinhua profile; Jiangsu local histories','Package B: China rural industrialization case.'),
('B','魯冠球','Lu Guanqiu','ろ かんきゅう',1945,2017,'中国浙江省','heisei','local_excellent_business','township_enterprise','浙江省の小工場から万向集団を育て、中国民営製造業と自動車部品産業の拡大を牽引した。','["万向集団"]','farmer','職業学校中退後に工場経営','company_history',7.1,0,1,73,'Wanxiang Group history; Xinhua obituary','Package B: Chinese private manufacturing and township enterprise.'),
('B','褚時健','Chu Shijian','ちょ じけん',1928,2019,'中国雲南省','heisei','agriculture_local','citrus_agriculture','たばこ企業経営後、雲南省で高齢期に柑橘ブランド「褚橙」を作り、農産物流通の地域モデルを示した。','["褚橙"]','farmer','雲南地方行政・企業経営','biography',6.5,0,1,70,'Caixin obituary; South China Morning Post profile','Package B: local agriculture and late-career entrepreneurship.'),
('B','袁隆平','Yuan Longping','えん りゅうへい',1930,2021,'中国湖南省','showa_post','agriculture_local','hybrid_rice','中国でハイブリッド米研究を主導し、アジア・アフリカの食料安全保障に大きな影響を与えた。','["ハイブリッド米"]','farmer','西南農学院','prize',8.7,1,1,82,'FAO profile; Xinhua obituary; World Food Prize biography','Package B: agriculture-local knowledge scaled to Global South food security.'),
('B','黄道婆','Huang Daopo','こう どうば',1245,1330,'中国上海松江付近','all','craft','textile_technology','海南で学んだ綿織技術を江南に伝え、紡績・織布工程の改良で地域手工業を発展させた。','["綿紡績技術の改良"]','working_class','海南での織物技術習得','historical_record',6.2,0,1,64,'Shanghai local gazetteers; Chinese textile history references','Package B: premodern craft technology transmission.'),
('B','顧景舟','Gu Jingzhou','こ けいしゅう',1915,1996,'中国江蘇省宜興','showa_post','craft','zisha_teapot','宜興紫砂壺の名工として伝統陶芸を現代工芸へ継承し、地域クラフトの評価を高めた。','["宜興紫砂壺"]','artisan','家業と宜興陶芸実務','museum_profile',6.9,0,1,74,'Yixing Zisha Museum materials; Chinese ceramics references','Package B: craft lineage and local excellence.'),
('B','イワン・ゴリコフ','Ivan Golikov','いわん ごりこふ',1886,1937,'ロシア帝国パレフ','taisho','craft','palekh_miniature','ロシアのパレフ細密画をイコン絵師の技術から世俗的漆器工芸へ転換し、地域工芸の基盤を作った。','["パレフ細密画"]','artisan','イコン工房での徒弟修業','museum_profile',6.0,0,1,67,'State Museum of Palekh Art; Russian Academy art-history references','Package B: Russian local craft modernization.'),
('B','王石','Wang Shi','おう せき',1951,NULL,'中国広西チワン族自治区','heisei','local_excellent_business','real_estate_governance','万科企業を共同創業し、中国都市化期の住宅開発企業にガバナンス改革を導入した。','["万科企業"]','other','蘭州交通大学','company_history',6.8,0,1,70,'Vanke corporate history; Harvard Business School case materials','Package B: Chinese urbanization business institution.'),
('B','張瑞敏','Zhang Ruimin','ちょう ずいびん',1949,NULL,'中国山東省青島','heisei','local_excellent_business','manufacturing_management','青島の冷蔵庫工場を海爾集団へ発展させ、品質管理と組織改革で中国製造業の国際化を進めた。','["海爾集団の経営改革"]','working_class','青島市企業管理実務','case_study',7.4,0,1,76,'Haier corporate history; Harvard Business School cases','Package B: management innovation from China manufacturing.'),
('B','馬化騰','Pony Ma Huateng','ば かとう',1971,NULL,'中国広東省汕頭','heisei','local_excellent_business','digital_platform','深圳でテンセントを共同創業し、QQ・微信を通じて中国語圏のデジタル生活基盤を形成した。','["Tencent QQ","WeChat"]','other','深圳大学計算機科学','company_history',7.8,0,1,77,'Tencent corporate history; Forbes profile','Package B: non-Western digital platform growth.'),
('B','馬明哲','Ma Mingzhe','ば めいてつ',1955,NULL,'中国吉林省','heisei','local_excellent_business','insurance_finance','平安保険を育て、中国の保険・金融サービスに統合型グループ経営を定着させた。','["中国平安保険"]','working_class','金融実務','company_history',6.7,0,1,70,'Ping An corporate history; company annual reports','Package B: Chinese finance institution building.'),
('B','モハメド・ユヌス','Muhammad Yunus','もはめど ゆぬす',1940,NULL,'バングラデシュ・チッタゴン','showa_post','local_excellent_business','microfinance','グラミン銀行を創設し、貧困層向け小口金融を制度化してグローバルサウスの社会的事業モデルを広めた。','["グラミン銀行"]','middle_class','ダッカ大学、ヴァンダービルト大学','nobel_prize',8.1,1,1,82,'Nobel Prize biography; Grameen Bank history','Package B: local finance model with Global South diffusion.'),
('C','ワレンチナ・テレシコワ','Valentina Tereshkova','われんちな てれしこわ',1937,NULL,'ソビエト連邦ヤロスラヴリ州','showa_post','women_pioneers','spaceflight','女性宇宙飛行士として世界で初めて単独宇宙飛行を行い、冷戦期科学技術における女性参加を可視化した。','["ボストーク6号"]','working_class','工場労働、航空クラブ、宇宙飛行士訓練','space_agency',8.0,1,0,78,'Roscosmos biography; Encyclopaedia Britannica','Package C: woman pioneer in Soviet space program.'),
('C','陳薇','Chen Wei','ちん び',1966,NULL,'中国浙江省','heisei','women_pioneers','biomedical_defense','女性軍事医学者としてエボラ・COVID-19ワクチン研究を主導し、中国の感染症対応能力を高めた。','["Ad5-nCoV vaccine research"]','other','浙江大学、清華大学','academy_profile',7.1,0,0,72,'Chinese Academy of Engineering profile; WHO-linked vaccine publications','Package C: woman biomedical researcher in China.'),
('C','王貞儀','Wang Zhenyi','おう ていぎ',1768,1797,'清朝江寧','all','women_pioneers','astronomy_mathematics','清代の女性学者として天文学・数学を学び、月食説明などで女性の科学知を示した。','["月食の説明","数学著述"]','scholar_official','家学による天文・数学学習','historical_record',6.8,0,0,66,'Biographical Dictionary of Chinese Women; Chinese astronomy histories','Package C: woman scientist in Qing China.'),
('C','向警予','Xiang Jingyu','こう けいよ',1895,1928,'中国湖南省','taisho','women_pioneers','labor_feminism','中国共産党初期の女性指導者として女性労働者組織化と女子教育に取り組んだ。','["女性労働運動の組織化"]','other','フランス勤工倹学、女子教育実務','historical_record',6.4,0,0,68,'CPC historical materials; Biographical Dictionary of Chinese Women','Package C: woman labor and feminist organizer.'),
('C','宋慶齢','Soong Ching-ling','そう けいれい',1893,1981,'清朝上海','showa_pre','women_pioneers','social_welfare_politics','女性政治家・社会事業家として児童福祉と対外平和運動を担い、中華人民共和国名誉主席も務めた。','["中国福利会"]','elite','ウェスリアン大学','official_biography',7.5,1,0,78,'Encyclopaedia Britannica; China Welfare Institute history','Package C: woman statesperson and welfare organizer.'),
('C','アレクサンドラ・コロンタイ','Alexandra Kollontai','あれくさんどら ころんたい',1872,1952,'ロシア帝国サンクトペテルブルク','taisho','women_pioneers','socialist_feminism_diplomacy','女性革命家・外交官として女性解放政策と世界初期の女性大使級外交実務を担った。','["女性労働者部","外交官活動"]','aristocrat','チューリヒ大学聴講、社会主義運動','biography',7.2,0,0,74,'Marxists Internet Archive writings; Encyclopaedia Britannica','Package C: woman socialist theorist and diplomat.'),
('C','アンナ・アフマートワ','Anna Akhmatova','あんな あふまとわ',1889,1966,'ロシア帝国オデッサ近郊','showa_pre','women_pioneers','poetry_memory','女性詩人としてスターリン期抑圧と家族の収監経験を詩に刻み、ロシア文学の記憶文化を支えた。','["レクイエム"]','middle_class','ツァールスコエ・セローの教育、文学サークル','literary_history',7.7,1,0,76,'Poetry Foundation biography; Encyclopaedia Britannica','Package C: woman poet under Soviet repression.'),
('C','リュドミラ・パヴリチェンコ','Lyudmila Pavlichenko','りゅどみら ぱゔりちぇんこ',1916,1974,'ロシア帝国ベーラヤ・ツェールコフ','showa_pre','women_pioneers','military_history','女性狙撃兵として第二次世界大戦で従軍し、戦時動員における女性軍務の象徴となった。','["第二次世界大戦での狙撃兵活動"]','working_class','キエフ大学、射撃訓練','military_record',6.9,0,0,69,'Smithsonian profile; Soviet military records references','Package C: woman combatant and public diplomacy figure.'),
('C','ナジェージダ・マンデリシュターム','Nadezhda Mandelstam','なじぇーじだ まんでりしゅたーむ',1899,1980,'ロシア帝国サラトフ','showa_post','women_pioneers','memoir_memory','女性回想録作家として夫オシップ・マンデリシュタームの詩とスターリン期弾圧の記憶を保存した。','["Hope Against Hope"]','middle_class','キエフの美術教育','memoir',6.8,0,0,70,'New York Review Books biography; Russian literary histories','Package C: woman guardian of cultural memory.'),
('C','ファティマ・メルニーシー','Fatema Mernissi','ふぁてぃま めるにーしー',1940,2015,'モロッコ・フェズ','heisei','women_pioneers','gender_sociology','女性社会学者としてイスラーム社会のジェンダー秩序を批判的に分析し、ポストコロニアル・フェミニズムに貢献した。','["Beyond the Veil","The Veil and the Male Elite"]','middle_class','ムハンマド5世大学、ブランダイス大学','academic_citation',7.0,0,0,74,'Encyclopaedia Britannica; academic publisher biographies','Package C: woman sociologist from Morocco.'),
('C','ドロレス・カクアンゴ','Dolores Cacuango','どろれす かくあんご',1881,1971,'エクアドル・カヤンベ','showa_pre','women_pioneers','indigenous_education','先住民女性指導者として土地権利運動とケチュア語教育を推進し、エクアドル先住民運動の基盤を作った。','["先住民学校の設立"]','farmer','農村共同体での実践知','movement_history',6.5,0,0,68,'Ecuador Ministry of Culture materials; Latin American indigenous movement histories','Package C: Indigenous woman organizer.'),
('C','ベルタ・カセレス','Berta Caceres','べるた かせれす',1971,2016,'ホンジュラス・ラ・エスペランサ','heisei','women_pioneers','environmental_justice','レンカ人女性環境運動家として水力発電計画に反対し、先住民権利と環境正義を国際的に訴えた。','["COPINH","Goldman Environmental Prize"]','other','社会運動実務','prize',7.2,0,0,72,'Goldman Environmental Prize biography; COPINH materials','Package C: Indigenous woman environmental defender.'),
('C','アスマ・ジャハンギール','Asma Jahangir','あすま じゃはんぎーる',1952,2018,'パキスタン・ラホール','heisei','women_pioneers','human_rights_law','女性弁護士としてパキスタンの人権訴訟、女性・宗教的少数者の権利擁護、国連特別報告者を担った。','["Human Rights Commission of Pakistan"]','elite','パンジャーブ大学法学部','un_profile',7.3,0,0,75,'UN OHCHR profile; HRCP history','Package C: woman human-rights lawyer.'),
('C','バンダナ・シヴァ','Vandana Shiva','ばんだな しゔぁ',1952,NULL,'インド・デヘラードゥーン','heisei','women_pioneers','eco_feminism','女性環境思想家として種子主権、農業生物多様性、エコフェミニズムをグローバルサウスの視点から論じた。','["Staying Alive","Navdanya"]','middle_class','パンジャーブ大学、ウェスタンオンタリオ大学','academic_citation',7.0,0,0,73,'Navdanya biography; publisher biographies','Package C: woman ecofeminist public intellectual.'),
('C','メドハ・パートカル','Medha Patkar','めどは ぱーとかる',1954,NULL,'インド・ムンバイ','heisei','women_pioneers','social_movement','女性社会運動家としてナルマダー川流域の住民移転問題を訴え、開発と権利の関係を問い直した。','["Narmada Bachao Andolan"]','middle_class','タタ社会科学研究所','movement_history',6.6,0,0,70,'Right Livelihood profile; Narmada movement histories','Package C: woman anti-displacement organizer.'),
('C','林巧稚','Lin Qiaozhi','りん こうち',1901,1983,'清朝福建省厦門','showa_post','women_pioneers','medicine_obstetrics','女性産婦人科医として北京協和医院で多数の出産・婦人科医療を担い、中国近代医学の女性専門職モデルとなった。','["産婦人科臨床と医学教育"]','middle_class','北京協和医学院','academy_profile',7.1,0,0,74,'Peking Union Medical College Hospital history; Chinese Academy biographical materials','Package C: woman physician in modern China.'),
('C','何沢慧','He Zehui','か たくけい',1914,2011,'中国江蘇省蘇州','showa_post','women_pioneers','nuclear_physics','女性核物理学者として原子核分裂・宇宙線研究に携わり、中国科学院で物理学研究を進めた。','["核物理研究"]','scholar_official','清華大学、ベルリン工科大学','academy_profile',6.8,0,0,72,'Chinese Academy of Sciences biography; physics history references','Package C: woman physicist in China.'),
('C','郭建梅','Guo Jianmei','かく けんばい',1961,NULL,'中国河南省','heisei','women_pioneers','public_interest_law','女性弁護士として中国の女性法律扶助と公益訴訟を開拓し、女性権利保護の制度化に取り組んだ。','["北京大学女性法律研究・サービスセンター"]','other','北京大学法学部','award',6.7,0,0,70,'Right Livelihood profile; public interest law reports','Package C: woman public-interest lawyer in China.'),
('C','シリン・エバディ','Shirin Ebadi','しりん えばでぃ',1947,NULL,'イラン・ハマダーン','heisei','women_pioneers','human_rights_law','女性裁判官・弁護士としてイランの人権と子ども・女性の権利を擁護し、ノーベル平和賞を受賞した。','["Defenders of Human Rights Center"]','middle_class','テヘラン大学法学部','nobel_prize',7.8,1,0,78,'Nobel Prize biography; Encyclopaedia Britannica','Package C: woman human-rights lawyer from Iran.'),
('C','アルンダティ・ロイ','Arundhati Roy','あるんだてぃ ろい',1961,NULL,'インド・シロン','heisei','women_pioneers','literature_activism','女性作家として小説と反核・反ダム・少数者権利の論考を通じ、インドの開発政治を批判した。','["The God of Small Things","The Algebra of Infinite Justice"]','middle_class','デリー建築学校','literary_prize',7.0,0,0,73,'Booker Prize biography; publisher biographies','Package C: woman writer and public intellectual.'),
('D','ネルー','Jawaharlal Nehru','ねるー',1889,1964,'英領インド・アラーハーバード','showa_post','politics','postcolonial_state_building','インド初代首相として非同盟と計画経済を主導したが、対中戦争や中央集権的開発への批判も受けた。','["The Discovery of India","非同盟外交"]','elite','ハロウ校、ケンブリッジ大学、インナー・テンプル','historical_biography',7.8,1,0,78,'','Package D critical sources: Sarvepalli Gopal, Jawaharlal Nehru: A Biography; Judith M. Brown, Nehru.'),
('D','スカルノ','Sukarno','すかるの',1901,1970,'オランダ領東インド・スラバヤ','showa_post','politics','anti_colonial_nationalism','インドネシア独立の象徴となったが、指導された民主主義と経済混乱、権威主義化が批判された。','["パンチャシラ","バンドン会議"]','middle_class','バンドン工科大学','historical_biography',7.3,1,0,75,'','Package D critical sources: John D. Legge, Sukarno; George McTurnan Kahin, Nationalism and Revolution in Indonesia.'),
('D','ナーセル','Gamal Abdel Nasser','なーせる',1918,1970,'エジプト・アレクサンドリア','showa_post','politics','arab_socialism','エジプト大統領としてスエズ運河国有化とアラブ民族主義を推進したが、政治的抑圧と1967年敗戦への批判も大きい。','["スエズ運河国有化","アラブ社会主義"]','working_class','エジプト王立陸軍士官学校','historical_biography',7.4,1,0,76,'','Package D critical sources: P. J. Vatikiotis, Nasser and His Generation; Said K. Aburish, Nasser.'),
('D','クワメ・ンクルマ','Kwame Nkrumah','くわめ んくるま',1909,1972,'英領ゴールドコースト','showa_post','politics','pan_africanism','ガーナ独立とパン・アフリカ主義を主導したが、一党化・個人崇拝・財政運営への批判も残した。','["アフリカ統一思想","ガーナ独立"]','working_class','リンカーン大学、ロンドン政治経済学院','historical_biography',7.2,1,0,75,'','Package D critical sources: David Birmingham, Kwame Nkrumah; Ali A. Mazrui, Nkrumah: The Leninist Czar.'),
('D','パトリス・ルムンバ','Patrice Lumumba','ぱとりす るむんば',1925,1961,'ベルギー領コンゴ・カサイ','showa_post','politics','decolonization','コンゴ独立政府の初代首相として反植民地主義の象徴となったが、政権運営の混乱と冷戦下の孤立も研究対象となった。','["コンゴ独立演説"]','working_class','宣教師学校、郵便局勤務','historical_biography',7.0,1,0,72,'','Package D critical sources: Ludo De Witte, The Assassination of Lumumba; Georges Nzongola-Ntalaja, The Congo.'),
('D','フランツ・ファノン','Frantz Fanon','ふらんつ ふぁのん',1925,1961,'マルティニーク・フォール＝ド＝フランス','showa_post','social_movement','postcolonial_psychiatry','精神科医・思想家として植民地主義の心理的暴力を分析したが、暴力論の解釈をめぐる批判的研究も多い。','["Black Skin, White Masks","The Wretched of the Earth"]','middle_class','リヨン大学医学部','academic_citation',7.7,1,0,78,'','Package D critical sources: David Macey, Frantz Fanon: A Biography; Alice Cherki, Frantz Fanon.'),
('D','サルバドール・アジェンデ','Salvador Allende','さるばどーる あじぇんで',1908,1973,'チリ・バルパライソ','showa_post','politics','democratic_socialism','チリ大統領として選挙による社会主義改革を進めたが、経済危機・政治分極化への評価は分かれる。','["人民連合政権"]','middle_class','チリ大学医学部','historical_biography',7.1,1,0,74,'','Package D critical sources: Tanya Harmer, Allende''s Chile and the Inter-American Cold War; Peter Winn, Weavers of Revolution.'),
('D','ホセ・リサール','Jose Rizal','ほせ りさーる',1861,1896,'スペイン領フィリピン・カランバ','meiji','social_movement','anti_colonial_literature','フィリピン独立運動の知識人として小説で植民地支配を批判したが、革命路線との距離をめぐり評価が分かれた。','["Noli Me Tangere","El Filibusterismo"]','middle_class','サント・トマス大学、マドリード中央大学','historical_biography',7.4,1,0,76,'','Package D critical sources: John N. Schumacher, The Propaganda Movement; Benedict Anderson, Under Three Flags.');

-- Required duplicate check before INSERT.
SELECT 'duplicate_before_insert' AS check_name, n.name_ja, n.birth_year
FROM new_achievers_6e n
WHERE EXISTS (
  SELECT 1 FROM achievers a
  WHERE a.name_ja = n.name_ja AND a.birth_year IS n.birth_year
);

INSERT INTO achievers (
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, domain, sub_domain, achievement_summary, notable_works,
  family_class, education_path, fame_source, fame_score,
  is_traditional_great, is_local_excellent, data_completeness,
  source_team, source_url, notes, correction_phase
)
SELECT
  name_ja, name_en, name_kana, birth_year, death_year, birth_place,
  primary_era_id, domain, sub_domain, achievement_summary, notable_works,
  family_class, education_path, fame_source, fame_score,
  is_traditional_great, is_local_excellent, data_completeness,
  'codex_correction_l4_postwest', source_url, notes, '6.E'
FROM new_achievers_6e n
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a
  WHERE a.name_ja = n.name_ja AND a.birth_year IS n.birth_year
);

DROP TABLE IF EXISTS temp.package_caps_6e;
CREATE TEMP TABLE package_caps_6e (
  package TEXT,
  capability_id TEXT,
  score INTEGER,
  notes TEXT
);

INSERT INTO package_caps_6e VALUES
('B','age_entrepreneur',8,'Package B: regional enterprise or craft/agricultural initiative.'),
('B','cog_systems',7,'Package B: local production, finance, or craft systems.'),
('B','val_collective',7,'Package B: community and collective capability.'),
('C','age_social_change',8,'Package C: woman pioneer changing institutional participation.'),
('C','cog_critical',7,'Package C: critical knowledge or advocacy by women.'),
('C','age_resilience',6,'Package C: persistence under gendered institutional constraints.'),
('D','age_social_change',8,'Package D: postcolonial political or intellectual transformation.'),
('D','cog_math',3,'Package D low score: limited evidence that mathematical literacy was a central capability.'),
('D','cog_info',4,'Package D low score: information management was uneven or contested in critical biographies.');

INSERT INTO achiever_capabilities (
  achiever_id, capability_id, score, evidence_quote, evidence_source, notes
)
SELECT
  a.id,
  pc.capability_id,
  pc.score,
  CASE
    WHEN n.package = 'D' THEN '批判的研究を含む根拠: ' || n.achievement_summary
    ELSE '根拠: ' || n.achievement_summary
  END,
  CASE WHEN n.package = 'D' THEN n.notes ELSE n.source_url END,
  pc.notes || ' source_team=codex_correction_l4_postwest; correction_phase=6.E'
FROM new_achievers_6e n
JOIN achievers a
  ON a.name_ja = n.name_ja
 AND a.birth_year IS n.birth_year
 AND a.source_team = 'codex_correction_l4_postwest'
 AND a.correction_phase = '6.E'
JOIN package_caps_6e pc
  ON pc.package = n.package
WHERE NOT EXISTS (
  SELECT 1 FROM achiever_capabilities ac
  WHERE ac.achiever_id = a.id
    AND ac.capability_id = pc.capability_id
    AND ac.evidence_source = CASE WHEN n.package = 'D' THEN n.notes ELSE n.source_url END
);

COMMIT;

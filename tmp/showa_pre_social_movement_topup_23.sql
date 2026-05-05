BEGIN;

CREATE TEMP TABLE topup_showa_pre_social_movement (
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

INSERT INTO topup_showa_pre_social_movement VALUES
('井上良二','Ryoji Inoue','いのうえ りょうじ',1898,1975,'兵庫県','労働運動・社会党運動','戦前の労働運動に参加し、労働者の政治的代表形成に関わった。','["労働運動","社会党運動"]','working_class','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=井上良二','労働運動系の現場政治家。'),
('岡田春夫','Haruo Okada','おかだ はるお',1914,1991,'北海道','学生運動・社会主義政治','学生期から左派運動に関わり、戦前弾圧の経験を戦後社会主義政治へ接続した。','["学生運動","社会党左派"]','other','東京帝国大学',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=岡田春夫','昭和前期世代の左派活動家。'),
('櫛田ふき','Fuki Kushida','くしだ ふき',1899,2001,'山口県','女性運動・平和運動','婦人運動に参加し、女性の政治参加と平和運動の基盤形成に関わった。','["婦人運動","平和運動"]','other','日本女子大学校',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=櫛田ふき','女性活動家。'),
('森三千代','Michiyo Mori','もり みちよ',1901,1977,'東京府','女性・反戦文化運動','鹿地亘らとともに中国での反戦文化活動に関わり、女性表現者として国際連帯を担った。','["反戦文化活動","中国での活動"]','other','不詳',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=森三千代','女性反戦文化運動。'),
('壺井繁治','Shigeji Tsuboi','つぼい しげじ',1897,1975,'香川県','プロレタリア詩・文化運動','詩を通じてプロレタリア文化運動に参加し、労働者・民衆の表現を広げた。','["プロレタリア詩","詩人会議"]','other','不詳',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=壺井繁治','文化運動枠。'),
('窪川鶴次郎','Tsurujirō Kubokawa','くぼかわ つるじろう',1903,1974,'高知県','プロレタリア文学評論','プロレタリア文学評論と組織活動を通じ、左翼文化運動の理論形成に関わった。','["プロレタリア文学評論","ナップ"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=窪川鶴次郎','文化運動理論。'),
('小堀甚二','Jinji Kobori','こぼり じんじ',1901,1959,'東京府','プロレタリア文学運動','文学評論を通じ、プロレタリア文化運動の方針形成と組織化に加わった。','["プロレタリア文学評論","文化運動"]','other','不詳',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=小堀甚二','文化運動枠。'),
('貴司山治','Yamaji Kishi','きし やまじ',1899,1973,'大阪府','プロレタリア文学・労働運動','労働者の生活と運動を描く小説で、戦前の社会問題を可視化した。','["プロレタリア文学","労働小説"]','working_class','不詳',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=貴司山治','労働文学。'),
('藤森成吉','Seikichi Fujimori','ふじもり せいきち',1892,1977,'長野県','社会主義文化運動','戯曲・小説を通じて社会主義文化運動に関わり、民衆教育的表現を展開した。','["社会主義文学","戯曲"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=藤森成吉','文化運動。'),
('本庄陸男','Mutsuo Honjo','ほんじょう むつお',1905,1939,'北海道','プロレタリア文学・農民問題','農民・開拓民の矛盾を描き、農村社会の問題を左翼文化運動に接続した。','["石狩川","プロレタリア文学"]','farmer','不詳',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=本庄陸男','農民問題の表現。'),
('今野大力','Dairiki Konno','こんの だいりき',1904,1935,'北海道','プロレタリア詩・労働運動','労働者の生活感覚を詩にし、北海道のプロレタリア文化運動を担った。','["プロレタリア詩","労働者詩"]','working_class','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=今野大力','地域文化運動。'),
('岩藤雪夫','Yukio Iwafuji','いわふじ ゆきお',1902,1933,'秋田県','プロレタリア文学・農民運動','農民の困窮と小作争議を題材にし、農村社会運動の感覚を文学で伝えた。','["小作争議文学","プロレタリア文学"]','farmer','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=岩藤雪夫','農民運動周辺。'),
('林歌子','Utako Hayashi','はやし うたこ',1864,1946,'京都府','女性運動・矯風運動','日本基督教婦人矯風会で廃娼・禁酒・女性保護の社会改良運動を進めた。','["日本基督教婦人矯風会","廃娼運動"]','other','不詳',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=林歌子','女性社会改良運動。'),
('城ノブ','Nobu Jo','じょう のぶ',1872,1959,'愛媛県','女性運動・社会事業','婦人矯風会などで廃娼・女性保護・社会事業に取り組み、地域の女性運動を支えた。','["婦人矯風会","女性保護運動"]','other','不詳',6.0,0,1,75,'https://ja.wikipedia.org/wiki/Special:Search?search=城ノブ','女性社会事業。'),
('砂沢クラ','Kura Sunazawa','すなざわ くら',1897,1990,'北海道','アイヌ権利・生活記録','アイヌ女性として同化政策下の生活経験を語り、民族差別と生活史を後世に残した。','["クスクップ・オルシペ","アイヌ生活記録"]','working_class','不詳',6.5,0,1,80,'https://ja.wikipedia.org/wiki/Special:Search?search=砂沢クラ','アイヌ女性の生活記録。'),
('石川準十郎','Junzuro Ishikawa','いしかわ じゅんじゅうろう',1899,1977,'東京府','労働運動・社会主義','労働運動と社会主義運動に参加し、戦前の無産運動を現場から支えた。','["労働運動","無産運動"]','working_class','不詳',5.5,0,1,70,'https://ja.wikipedia.org/wiki/Special:Search?search=石川準十郎','労働運動系。'),
('永田広志','Hiroshi Nagata','ながた ひろし',1904,1947,'長野県','唯物論研究・社会思想','唯物論研究と社会科学の普及を通じ、思想統制下の知識人運動に加わった。','["唯物論研究","社会思想"]','other','東京帝国大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=永田広志','思想運動。'),
('千田是也','Koreya Senda','せんだ これや',1904,1994,'東京府','プロレタリア演劇・反戦文化','左翼演劇運動に参加し、演劇を反戦・民主主義の表現手段として発展させた。','["新劇運動","プロレタリア演劇"]','other','早稲田大学中退',6.5,0,0,80,'https://ja.wikipedia.org/wiki/Special:Search?search=千田是也','演劇運動。'),
('原泉','Sen Hara','はら せん',1905,1989,'島根県','プロレタリア演劇・女性表現','左翼演劇運動に参加し、女性俳優として社会派表現の現場を担った。','["左翼劇場","新劇"]','other','不詳',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=原泉','女性文化運動。'),
('滝沢修','Osamu Takizawa','たきざわ おさむ',1906,2000,'東京府','新劇・社会派演劇','新劇・左翼演劇の現場で社会派表現を担い、戦前文化運動の一端を形成した。','["新劇運動","社会派演劇"]','other','築地小劇場',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=滝沢修','演劇運動。'),
('久保栄','Sakae Kubo','くぼ さかえ',1900,1958,'北海道','プロレタリア演劇・戯曲','戯曲と演劇運動を通じ、労働者・農民の社会問題を舞台化した。','["火山灰地","プロレタリア演劇"]','other','東京帝国大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=久保栄','演劇文化運動。'),
('三好十郎','Juro Miyoshi','みよし じゅうろう',1902,1958,'佐賀県','社会派演劇・反戦表現','左翼演劇から出発し、戦争と民衆の矛盾を問う戯曲を発表した。','["斬られの仙太","社会派戯曲"]','other','早稲田大学',6.0,0,0,75,'https://ja.wikipedia.org/wiki/Special:Search?search=三好十郎','反戦的文化運動。'),
('薄田研二','Kenji Susukida','すすきだ けんじ',1898,1972,'福岡県','プロレタリア演劇','左翼劇場・新劇運動で労働者文化を表現し、演劇の社会的役割を広げた。','["左翼劇場","新劇運動"]','other','不詳',5.5,0,0,70,'https://ja.wikipedia.org/wiki/Special:Search?search=薄田研二','演劇運動。');

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
FROM topup_showa_pre_social_movement t
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a
  WHERE a.name_ja = t.name_ja
    AND a.birth_year = t.birth_year
);

CREATE TEMP TABLE topup_capabilities (
  name_ja TEXT,
  capability_id TEXT,
  score INTEGER,
  evidence_quote TEXT
);

INSERT INTO topup_capabilities VALUES
('井上良二','age_social_change',7,'労働者の政治的代表形成に関わった。'),('井上良二','soc_interpersonal',7,'労働運動の組織活動を担った。'),('井上良二','val_collective',7,'労働者の共同利益を代表した。'),
('岡田春夫','age_social_change',6,'学生期から左派運動に関わった。'),('岡田春夫','age_resilience',7,'弾圧経験を経て社会主義政治へ接続した。'),('岡田春夫','soc_interpersonal',6,'左派組織内で活動した。'),
('櫛田ふき','age_social_change',7,'女性の政治参加と平和運動に関わった。'),('櫛田ふき','val_tolerance',8,'女性の権利と平和を社会課題化した。'),('櫛田ふき','soc_interpersonal',7,'婦人運動の組織活動を担った。'),
('森三千代','age_social_change',7,'中国での反戦文化活動に関わった。'),('森三千代','cre_cross_domain',7,'文学・国際連帯・反戦宣伝を結んだ。'),('森三千代','age_resilience',7,'国外活動の困難な条件下で表現を続けた。'),
('壺井繁治','cog_creativity',7,'詩で労働者・民衆の表現を広げた。'),('壺井繁治','age_social_change',7,'プロレタリア文化運動に参加した。'),('壺井繁治','soc_interpersonal',6,'詩人・文化人の運動に関わった。'),
('窪川鶴次郎','cog_critical',7,'プロレタリア文学評論で運動方針を論じた。'),('窪川鶴次郎','age_social_change',7,'左翼文化運動の理論形成に関わった。'),('窪川鶴次郎','cog_logical',7,'文学運動を理論的に整理した。'),
('小堀甚二','cog_critical',7,'文学評論を通じて社会矛盾を論じた。'),('小堀甚二','age_social_change',6,'文化運動の組織化に加わった。'),('小堀甚二','cog_info',6,'評論で運動方針を伝達した。'),
('貴司山治','cog_creativity',7,'労働者の生活と運動を小説で描いた。'),('貴司山治','val_collective',7,'労働者の共同経験を表現した。'),('貴司山治','age_social_change',6,'労働文学で社会問題を可視化した。'),
('藤森成吉','cog_creativity',7,'戯曲・小説で社会主義的課題を表現した。'),('藤森成吉','age_social_change',6,'民衆教育的な文化運動に関与した。'),('藤森成吉','val_tolerance',6,'民衆の視点を重視した表現を行った。'),
('本庄陸男','cog_creativity',7,'農民・開拓民の矛盾を文学化した。'),('本庄陸男','val_collective',7,'農村社会の共同的困難を描いた。'),('本庄陸男','age_social_change',6,'農村問題を文化運動に接続した。'),
('今野大力','cog_creativity',7,'労働者の生活感覚を詩にした。'),('今野大力','age_social_change',6,'北海道のプロレタリア文化運動を担った。'),('今野大力','age_resilience',6,'短い生涯の中で地域文化運動の表現を続けた。'),
('岩藤雪夫','cog_creativity',7,'小作争議と農民の困窮を文学化した。'),('岩藤雪夫','age_social_change',6,'農民運動周辺の問題を伝えた。'),('岩藤雪夫','val_collective',7,'農民の共同的困難を表現した。'),
('林歌子','age_social_change',8,'廃娼・禁酒・女性保護の社会改良運動を進めた。'),('林歌子','val_tolerance',8,'女性保護を社会的権利課題として扱った。'),('林歌子','soc_interpersonal',7,'婦人矯風会で組織活動を行った。'),
('城ノブ','age_social_change',7,'廃娼・女性保護・社会事業に取り組んだ。'),('城ノブ','soc_interpersonal',7,'地域の女性運動を支えた。'),('城ノブ','val_tolerance',8,'困難を抱える女性の保護を訴えた。'),
('砂沢クラ','val_traditional',8,'アイヌの生活経験を記録として残した。'),('砂沢クラ','val_tolerance',8,'民族差別と生活史を語った。'),('砂沢クラ','age_social_autonomy',7,'アイヌ女性として自らの経験を発信した。'),
('石川準十郎','age_social_change',6,'労働運動と無産運動に参加した。'),('石川準十郎','soc_interpersonal',6,'現場の組織活動を支えた。'),('石川準十郎','val_collective',6,'労働者の共同利益を重視した。'),
('永田広志','cog_critical',8,'唯物論研究で思想統制に抗した。'),('永田広志','cog_logical',7,'社会思想を理論的に整理した。'),('永田広志','age_social_change',6,'知識人運動に参加した。'),
('千田是也','cog_creativity',8,'演劇を反戦・民主主義の表現手段にした。'),('千田是也','soc_interpersonal',8,'新劇運動で集団制作を組織した。'),('千田是也','age_social_change',7,'左翼演劇運動に参加した。'),
('原泉','cog_creativity',7,'左翼演劇で社会派表現を担った。'),('原泉','age_social_change',6,'女性俳優として文化運動に参加した。'),('原泉','soc_interpersonal',6,'劇団活動を通じた集団表現を支えた。'),
('滝沢修','cog_creativity',7,'新劇で社会派表現を担った。'),('滝沢修','soc_interpersonal',7,'演劇集団の現場で活動した。'),('滝沢修','age_social_change',6,'文化運動としての新劇に参加した。'),
('久保栄','cog_creativity',8,'労働者・農民の問題を戯曲化した。'),('久保栄','age_social_change',7,'プロレタリア演劇運動に参加した。'),('久保栄','cog_critical',7,'戯曲で社会矛盾を批判的に描いた。'),
('三好十郎','cog_creativity',7,'戦争と民衆の矛盾を戯曲で問うた。'),('三好十郎','cog_critical',7,'社会と戦争への批判を作品化した。'),('三好十郎','age_social_change',6,'左翼演劇から社会派表現へ展開した。'),
('薄田研二','cog_creativity',7,'左翼劇場で労働者文化を表現した。'),('薄田研二','soc_interpersonal',7,'新劇運動の集団制作に関わった。'),('薄田研二','age_social_change',6,'演劇の社会的役割を広げた。');

INSERT INTO achiever_capabilities (
  achiever_id, capability_id, score, evidence_quote, evidence_source, notes
)
SELECT
  a.id, tc.capability_id, tc.score, tc.evidence_quote, a.source_url,
  'codex_showa_pre_social_movement capability scoring topup'
FROM topup_capabilities tc
JOIN achievers a ON a.name_ja = tc.name_ja
WHERE a.source_team = 'codex_showa_pre_social_movement'
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id = a.id
      AND ac.capability_id = tc.capability_id
      AND ac.evidence_quote = tc.evidence_quote
  );

SELECT 'topup_inserted_total', COUNT(*)
FROM achievers
WHERE source_team='codex_showa_pre_social_movement';

SELECT 'topup_capabilities_total', COUNT(*)
FROM achiever_capabilities ac
JOIN achievers a ON a.id = ac.achiever_id
WHERE a.source_team='codex_showa_pre_social_movement';

COMMIT;

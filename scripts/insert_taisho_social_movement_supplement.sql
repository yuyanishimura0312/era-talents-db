BEGIN;
WITH rows(name_ja,name_en,name_kana,birth_year,death_year,birth_place,sub_domain,summary,works,family_class,education_path,is_great,is_local) AS (
  VALUES
  ('丹野セツ','Tanno Setsu','たんの せつ',1902,1987,'福島県','women_labor_communist','紡績労働者から労働運動・女性運動に参加し、女性労働者の組織化を担った。','["女性労働運動","日本共産党女性活動"]','working_class','尋常小学校',0,0),
  ('鍋山歌子','Nabeyama Utako','なべやま うたこ',1904,1988,'東京都','women_labor_communist','労働運動・左派女性運動に参加し、女性労働者と政治運動を結びつけた。','["女性労働運動","左派女性運動"]','working_class','独学',0,0),
  ('伊藤千代子','Ito Chiyoko','いとう ちよこ',1905,1929,'長野県','women_student_communist','学生運動から社会主義運動に参加し、若い女性知識人の政治参加を象徴した。','["学生社会運動","社会主義運動"]','other','諏訪高等女学校',0,0),
  ('中本たか子','Nakamoto Takako','なかもと たかこ',1903,1991,'山口県','women_proletarian','プロレタリア文学・女性運動に関わり、女性労働者と生活者の視点を社会批判に接続した。','["プロレタリア文学","女性運動"]','other','日本女子大学校中退',0,0)
)
INSERT INTO achievers (
  name_ja,name_en,name_kana,birth_year,death_year,birth_place,primary_era_id,secondary_era_id,domain,sub_domain,
  achievement_summary,notable_works,family_class,education_path,fame_source,fame_score,
  is_traditional_great,is_local_excellent,data_completeness,source_team,source_url,notes
)
SELECT name_ja,name_en,name_kana,birth_year,death_year,birth_place,'taisho','showa_pre','social_movement',sub_domain,
       summary,works,family_class,education_path,'wikipedia_ja_or_ndl',6.2,
       is_great,is_local,78,'codex_taisho_social_movement','https://ja.wikipedia.org/wiki/' || name_ja,
       '大正期社会運動セルの補充分。INSERT時に name_ja + birth_year で重複回避。'
FROM rows
WHERE NOT EXISTS (
  SELECT 1 FROM achievers a WHERE a.name_ja = rows.name_ja AND a.birth_year = rows.birth_year
);
COMMIT;

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
  AND a.name_ja IN ('丹野セツ','鍋山歌子','伊藤千代子','中本たか子')
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id=a.id AND ac.capability_id=caps.capability_id
      AND ac.notes='codex_taisho_social_movement batch capability scoring'
  );
COMMIT;

SELECT 'supplement_achievers', COUNT(*) FROM achievers WHERE source_team='codex_taisho_social_movement';
SELECT 'supplement_capabilities', COUNT(*) FROM achiever_capabilities ac JOIN achievers a ON a.id=ac.achiever_id WHERE a.source_team='codex_taisho_social_movement';

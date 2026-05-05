-- Final top-up for showa_post / media_journalism to reach 80 additions.
.bail on

BEGIN;

CREATE TEMP TABLE temp_showa_post_media_batch3 (
  name_ja TEXT, name_en TEXT, name_kana TEXT, birth_year INTEGER, death_year INTEGER,
  birth_place TEXT, sub_domain TEXT, achievement_summary TEXT, notable_works TEXT,
  family_class TEXT, education_path TEXT, fame_score REAL, is_traditional_great INTEGER,
  is_local_excellent INTEGER, source_url TEXT, notes TEXT
);

INSERT INTO temp_showa_post_media_batch3 VALUES
('加賀美幸子','Sachiko Kagami','かがみ さちこ',1940,NULL,'東京都','broadcast_announcing','NHKアナウンサーとしてニュース、朗読、古典番組を担当し、女性アナウンサーの職域拡大と音声表現に貢献した。','["NHKニュース","古典講読"]','other','立教大学文学部',6.8,0,0,'https://ja.wikipedia.org/wiki/加賀美幸子','公共放送・女性アナウンサー'),
('山根基世','Motoyo Yamane','やまね もとよ',1948,NULL,'山口県','broadcast_announcing','NHKアナウンサー、アナウンス室長として報道、ナレーション、朗読を担い、放送言語教育にも取り組んだ。','["NHKニュース","映像の世紀"]','other','早稲田大学第一文学部',7.1,0,0,'https://ja.wikipedia.org/wiki/山根基世','公共放送・放送言語');

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
FROM temp_showa_post_media_batch3 b
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
  AND a.name_ja IN ('加賀美幸子','山根基世')
  AND NOT EXISTS (
    SELECT 1 FROM achiever_capabilities ac
    WHERE ac.achiever_id=a.id AND ac.capability_id=v.capability_id
  );

COMMIT;

SELECT 'final_count', COUNT(*) FROM achievers
WHERE primary_era_id='showa_post' AND domain='media_journalism'
  AND source_team='codex_showa_post_media_journalism';

SELECT 'final_capability_rows', COUNT(*) FROM achiever_capabilities ac
JOIN achievers a ON a.id=ac.achiever_id
WHERE a.source_team='codex_showa_post_media_journalism'
  AND a.primary_era_id='showa_post'
  AND a.domain='media_journalism';

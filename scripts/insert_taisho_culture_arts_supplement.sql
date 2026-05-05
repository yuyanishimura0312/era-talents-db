BEGIN;

WITH people(name,birth,death,sub,summary,works,great,local) AS (VALUES
('南薫造',1883,1950,'fine_arts','水彩・油彩・版画を横断し、詩情ある風景表現で大正期洋画の多様化に寄与した。','["水彩画作品"]',0,0),
('森田恒友',1881,1933,'fine_arts','洋画・日本画・挿絵を横断し、自然主義的な視線で風景と生活を描いた。','["方寸同人作品"]',0,0),
('石井柏亭',1882,1958,'fine_arts','洋画家・美術評論家として美術団体と出版を通じた近代美術の普及に関わった。','["方寸","日本水彩画会"]',0,0),
('山下新太郎',1881,1966,'fine_arts','滞欧経験をもとに、穏健な写実と色彩感覚で大正期洋画壇を支えた。','["読書"]',0,0),
('和田三造',1883,1967,'design','洋画・色彩研究・図案を横断し、舞台美術や服飾を含む近代デザインに影響した。','["南風","色名総鑑"]',1,0),
('田辺至',1886,1968,'fine_arts','滞欧経験を踏まえ、人物画を中心に端正な構成と色彩を追求した。','["洋画作品"]',0,0),
('中村研一',1895,1967,'fine_arts','帝展系洋画で人物画を中心に制作し、写実的表現の制度的展開を担った。','["コタ・バル"]',0,0),
('須田国太郎',1891,1961,'fine_arts','西洋絵画研究と重厚な画面構成により、独自の近代洋画を確立した。','["犬"]',1,0),
('安宅安五郎',1884,1960,'fine_arts','洋画教育と制作を通じて地方美術の基盤形成にも寄与した。','["洋画作品"]',0,1),
('藤井厚二',1888,1938,'architecture_design','住宅設計と環境工学を結びつけ、日本の気候に即した近代住宅を実験した。','["聴竹居"]',1,0),
('吉田謙吉',1897,1982,'stage_design','舞台美術・装丁・考現学を横断し、都市生活の観察を視覚文化へ結びつけた。','["考現学採集"]',0,0)
)
INSERT INTO achievers (
  name_ja, birth_year, death_year, primary_era_id, domain, sub_domain,
  achievement_summary, notable_works, fame_source, fame_score,
  is_traditional_great, is_local_excellent, data_completeness,
  source_team, source_url, notes
)
SELECT name, birth, death, 'taisho', 'culture_arts', sub, summary, works,
       'wikipedia_ja', CASE WHEN great=1 THEN 7.0 ELSE 4.5 END,
       great, local, 80, 'codex_taisho_culture_arts',
       'https://ja.wikipedia.org/wiki/' || name,
       '大正文化芸術補充バッチ: 美術・装丁・生活デザイン'
FROM people p
WHERE NOT EXISTS (SELECT 1 FROM achievers a WHERE a.name_ja=p.name AND a.birth_year=p.birth);

COMMIT;

BEGIN;

WITH target AS (
  SELECT id, name_ja, sub_domain, achievement_summary, source_url
  FROM achievers
  WHERE source_team='codex_taisho_culture_arts'
),
cap_plan(achiever_id, capability_id, score, evidence_quote, evidence_source, notes) AS (
  SELECT id, 'cog_creativity', 8, achievement_summary, source_url, '表現形式やジャンルの創造性'
  FROM target
  UNION ALL
  SELECT id, 'cre_cross_domain', 7, achievement_summary, source_url, 'メディア・ジャンル・伝統と近代の横断'
  FROM target
  UNION ALL
  SELECT id,
         CASE
           WHEN sub_domain IN ('architecture_design','design','stage_design') THEN 'cog_systems'
           WHEN sub_domain IN ('film_actor','theater','popular_performance','rakugo','rokyoku') THEN 'soc_interpersonal'
           WHEN sub_domain IN ('craft_design','music','print') THEN 'val_traditional'
           ELSE 'age_social_change'
         END,
         7, achievement_summary, source_url, '領域特性に応じた主要能力'
  FROM target
  UNION ALL
  SELECT id,
         CASE
           WHEN sub_domain IN ('popular_lit','manga_illustration','illustration','film') THEN 'age_social_change'
           WHEN sub_domain IN ('fine_arts','design','print','architecture_design','stage_design') THEN 'age_meta_learning'
           WHEN sub_domain IN ('rakugo','rokyoku','craft_design','music') THEN 'val_traditional'
           ELSE 'age_resilience'
         END,
         6, achievement_summary, source_url, '大正期の文化変動への適応と継承'
  FROM target
)
INSERT INTO achiever_capabilities (
  achiever_id, capability_id, score, evidence_quote, evidence_source, notes
)
SELECT achiever_id, capability_id, score, evidence_quote, evidence_source, notes
FROM cap_plan cp
WHERE NOT EXISTS (
  SELECT 1 FROM achiever_capabilities ac
  WHERE ac.achiever_id=cp.achiever_id AND ac.capability_id=cp.capability_id
);

COMMIT;

SELECT 'supplement_count', COUNT(*) FROM achievers WHERE source_team='codex_taisho_culture_arts';
SELECT 'supplement_capability_count', COUNT(*)
FROM achiever_capabilities
WHERE achiever_id IN (SELECT id FROM achievers WHERE source_team='codex_taisho_culture_arts');

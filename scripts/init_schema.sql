-- Era Talents DB Schema v0.1
-- 時代別活躍人材DB
-- L1: 当時の能力言説 / L2: 事後評価 / L3: 活躍者特性 / L4: 未来予測

PRAGMA foreign_keys = ON;

-- 時代区分マスタ
CREATE TABLE IF NOT EXISTS eras (
    id              TEXT PRIMARY KEY,        -- meiji, taisho, showa_pre, showa_post, heisei, reiwa, future_2030, future_2050, future_2100
    name_ja         TEXT NOT NULL,
    name_en         TEXT NOT NULL,
    year_start      INTEGER NOT NULL,
    year_end        INTEGER NOT NULL,
    is_future       INTEGER NOT NULL DEFAULT 0,
    description     TEXT,
    sort_order      INTEGER
);

-- 能力次元マスタ（OECD Learning Compass + JPMS-DB 5次元 + 拡張）
CREATE TABLE IF NOT EXISTS capability_dimensions (
    id              TEXT PRIMARY KEY,        -- cog_creativity, val_tolerance, etc
    code            TEXT NOT NULL,           -- cog/val/soc/age/cre
    code_label      TEXT NOT NULL,           -- cognitive/values/social/agency/creativity
    name_ja         TEXT NOT NULL,
    name_en         TEXT NOT NULL,
    description     TEXT,
    framework       TEXT,                    -- OECD/P21/UNESCO/JPMS/Society5.0
    parent_id       TEXT REFERENCES capability_dimensions(id)
);

-- L1: 当時の言説（その時代に「これが必要」と語られた力）
CREATE TABLE IF NOT EXISTS era_discourses (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    era_id          TEXT NOT NULL REFERENCES eras(id),
    capability_id   TEXT REFERENCES capability_dimensions(id),
    discourse_type  TEXT,                    -- education_decree, curriculum, business_proposal, social_commentary, textbook
    source_title    TEXT NOT NULL,
    source_author   TEXT,
    source_year     INTEGER,
    source_url      TEXT,
    quote_ja        TEXT,
    summary_ja      TEXT NOT NULL,
    relevance_score INTEGER CHECK(relevance_score BETWEEN 1 AND 10),
    notes           TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

-- L2: 事後評価（現代から振り返って実際に効いた力）
CREATE TABLE IF NOT EXISTS era_retrospectives (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    era_id          TEXT NOT NULL REFERENCES eras(id),
    capability_id   TEXT REFERENCES capability_dimensions(id),
    perspective     TEXT,                    -- historical_sociology, education_research, biography_studies
    source_title    TEXT NOT NULL,
    source_author   TEXT,
    source_year     INTEGER,
    source_url      TEXT,
    finding_ja      TEXT NOT NULL,
    relevance_score INTEGER CHECK(relevance_score BETWEEN 1 AND 10),
    diverges_from_l1 INTEGER DEFAULT 0,      -- L1当時言説とのズレフラグ
    notes           TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

-- L3: 活躍人材本体（その時代に実際に活躍した人物）
CREATE TABLE IF NOT EXISTS achievers (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ja         TEXT NOT NULL,
    name_en         TEXT,
    name_kana       TEXT,
    birth_year      INTEGER,
    death_year      INTEGER,
    birth_place     TEXT,
    primary_era_id  TEXT NOT NULL REFERENCES eras(id),  -- 主に活躍した時代
    secondary_era_id TEXT REFERENCES eras(id),
    domain          TEXT NOT NULL,           -- politics, business, science, technology, culture_arts, sports, social_movement, education, religion, media, agriculture_local, professional, craft
    sub_domain      TEXT,
    achievement_summary TEXT NOT NULL,
    notable_works   TEXT,                    -- JSON array
    -- 階層・背景（Bourdieu型）
    family_class    TEXT,                    -- aristocrat, samurai, merchant, farmer, working_class, other
    family_education TEXT,
    -- 教育経歴
    education_path  TEXT,
    mentors         TEXT,                    -- JSON array
    -- 著名度指標
    fame_source     TEXT,                    -- wikipedia_ja_size, pantheon_hpi, ndl_authority, prize
    fame_score      REAL,
    -- データ品質
    is_traditional_great INTEGER DEFAULT 0,  -- 偉人カテゴリ
    is_local_excellent   INTEGER DEFAULT 0,  -- 無名の卓越者
    data_completeness INTEGER DEFAULT 0,
    source_team     TEXT,                    -- codex_meiji, codex_taisho, claude_synthesis
    source_url      TEXT,
    notes           TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

-- L3-能力スコアリング（人物×能力）
CREATE TABLE IF NOT EXISTS achiever_capabilities (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    achiever_id     INTEGER NOT NULL REFERENCES achievers(id),
    capability_id   TEXT NOT NULL REFERENCES capability_dimensions(id),
    score           INTEGER CHECK(score BETWEEN 1 AND 10),
    evidence_quote  TEXT,
    evidence_source TEXT,
    notes           TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

-- L4: 未来の要求能力予測
CREATE TABLE IF NOT EXISTS future_demands (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    era_id          TEXT NOT NULL REFERENCES eras(id),  -- future_2030 / future_2050 / future_2100
    capability_id   TEXT REFERENCES capability_dimensions(id),
    scenario        TEXT,                    -- baseline, ssp1, ssp3, post_growth, posthuman
    source_title    TEXT NOT NULL,
    source_org      TEXT,                    -- OECD, WEF, METI, IPCC, etc
    source_year     INTEGER,
    source_url      TEXT,
    finding_ja      TEXT NOT NULL,
    confidence      INTEGER CHECK(confidence BETWEEN 1 AND 10),
    is_unique_to_era INTEGER DEFAULT 0,      -- その時代固有か
    notes           TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);

-- ギャップ知見（L1とL2のズレ、L4と過去の対比）
CREATE TABLE IF NOT EXISTS gap_insights (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    insight_type    TEXT,                    -- l1_l2_gap, era_to_future, cross_era
    title_ja        TEXT NOT NULL,
    description_ja  TEXT NOT NULL,
    related_eras    TEXT,                    -- JSON array
    related_capabilities TEXT,               -- JSON array
    implications_education TEXT,
    implications_hiring    TEXT,
    implications_org       TEXT,
    confidence      INTEGER CHECK(confidence BETWEEN 1 AND 10),
    created_at      TEXT DEFAULT (datetime('now'))
);

-- 学術ベンチマーク参照
CREATE TABLE IF NOT EXISTS academic_references (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    citation        TEXT NOT NULL,
    author          TEXT,
    year            INTEGER,
    title           TEXT,
    framework_tag   TEXT,                    -- simonton, csikszentmihalyi, subotnik, bourdieu, granovetter, merton
    relevance_to_layer TEXT,                 -- L1, L2, L3, L4, methodology
    doi             TEXT,
    notes           TEXT
);

-- 収集進捗トラッキング
CREATE TABLE IF NOT EXISTS collection_progress (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    era_id          TEXT NOT NULL,
    domain          TEXT,
    target_count    INTEGER,
    current_count   INTEGER,
    status          TEXT,                    -- pending, in_progress, completed
    team            TEXT,                    -- codex_team_1, codex_team_2, claude
    started_at      TEXT,
    completed_at    TEXT
);

-- インデックス
CREATE INDEX IF NOT EXISTS idx_achievers_era ON achievers(primary_era_id);
CREATE INDEX IF NOT EXISTS idx_achievers_domain ON achievers(domain);
CREATE INDEX IF NOT EXISTS idx_achievers_birth ON achievers(birth_year);
CREATE INDEX IF NOT EXISTS idx_discourses_era ON era_discourses(era_id);
CREATE INDEX IF NOT EXISTS idx_retrospectives_era ON era_retrospectives(era_id);
CREATE INDEX IF NOT EXISTS idx_future_era ON future_demands(era_id);
CREATE INDEX IF NOT EXISTS idx_capabilities_achiever ON achiever_capabilities(achiever_id);

-- 時代マスタ初期データ
INSERT OR IGNORE INTO eras (id, name_ja, name_en, year_start, year_end, is_future, sort_order) VALUES
('meiji',       '明治',     'Meiji',           1868, 1912, 0, 1),
('taisho',      '大正',     'Taisho',          1912, 1926, 0, 2),
('showa_pre',   '昭和前期', 'Showa Pre-war',   1926, 1945, 0, 3),
('showa_post',  '昭和後期', 'Showa Post-war',  1946, 1989, 0, 4),
('heisei',      '平成',     'Heisei',          1989, 2019, 0, 5),
('reiwa',       '令和',     'Reiwa',           2019, 2030, 0, 6),
('future_2030', '2030年代', '2030s',           2030, 2040, 1, 7),
('future_2050', '2050年代', '2050s',           2050, 2060, 1, 8),
('future_2100', '2100年代', '2100s',           2100, 2110, 1, 9);

-- 能力次元初期データ（analysis.htmlから抽出 + 理論フレーム拡張）
INSERT OR IGNORE INTO capability_dimensions (id, code, code_label, name_ja, name_en, framework) VALUES
('cog_creativity',         'cog', 'cognitive',  '創造性',           'Creativity',                    'OECD/P21'),
('cog_critical',           'cog', 'cognitive',  '批判的思考',       'Critical Thinking',             'OECD/P21'),
('cog_logical',            'cog', 'cognitive',  '論理的思考',       'Logical Thinking',              'P21'),
('cog_math',               'cog', 'cognitive',  '数学的リテラシー', 'Mathematical Literacy',         'PISA'),
('cog_info',               'cog', 'cognitive',  '情報リテラシー',   'Information Literacy',          'P21'),
('cog_ai_collab',          'cog', 'cognitive',  'AI協働リテラシー', 'AI Collaboration Literacy',     'WEF2025'),
('val_tolerance',          'val', 'values',     '寛容性',           'Tolerance',                     'UNESCO'),
('val_collective',         'val', 'values',     '集団協調性',       'Collective Cooperation',        'JPMS'),
('val_traditional',        'val', 'values',     '伝統文化尊重',     'Traditional Culture Respect',   'JPMS'),
('soc_interpersonal',      'soc', 'social',     '対人関係スキル',   'Interpersonal Skills',          'P21'),
('age_oecd_transformative','age', 'agency',     'OECD変革コンピテンシー','OECD Transformative Competency','OECD2030'),
('age_social_autonomy',    'age', 'agency',     '社会的自立性',     'Social Autonomy',               'JPMS'),
('age_entrepreneur',       'age', 'agency',     '起業家精神',       'Entrepreneurship',              'Schumpeter'),
('age_social_change',      'age', 'agency',     '社会変革志向',     'Social Change Orientation',     'OECD'),
('cre_cross_domain',       'cre', 'creativity', '異分野統合志向',   'Cross-domain Integration',      'Csikszentmihalyi'),
('cog_systems',            'cog', 'cognitive',  'システム思考',     'Systems Thinking',              'OECD2030'),
('val_eco',                'val', 'values',     'エコロジカルリテラシー','Ecological Literacy',       'IPCC'),
('age_resilience',         'age', 'agency',     'レジリエンス',     'Resilience',                    'WEF'),
('age_meta_learning',      'age', 'agency',     '学習戦略・適応性', 'Meta-learning',                 'OECD2030');

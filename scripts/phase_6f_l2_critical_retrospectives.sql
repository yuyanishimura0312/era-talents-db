BEGIN TRANSACTION;

INSERT INTO era_retrospectives
  (era_id, capability_id, perspective, source_title, source_author, source_year, source_url, finding_ja, relevance_score, diverges_from_l1, notes, source_team)
VALUES
('meiji','cog_critical','critical','日本近代文学の起源','柄谷行人',1980,NULL,'明治の文学制度を天才の発露ではなく、言文一致・内面・風景といった近代的装置の成立として読む。L1の文明開化礼賛から、制度が何を可視化し何を不可視化したかへ評価軸を移す。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','cog_logical','critical','Translation and Subjectivity','酒井直樹',1997,NULL,'翻訳を国語と国民主体の形成過程として捉え、明治の語学能力や啓蒙知を単純な西洋受容ではなく、境界線を作る実践として再評価する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','age_social_change','critical','日本近代文学の起源','柄谷行人',1980,NULL,'近代的主体は自然発生したものではなく教育・出版・文学批評の装置で作られたという視点から、明治の人材評価を個人業績中心からメディア環境中心へ補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','cog_systems','critical','博覧会の政治学','吉見俊哉',1992,NULL,'博覧会を産業振興だけでなく、帝国・都市・消費者を結びつける視覚的統治のシステムとして分析する。明治の技術展示や実業家評価に政治性を加える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','val_tolerance','critical','Japan''s Modern Myths','Carol Gluck',1985,NULL,'明治国家のイデオロギー形成を、伝統の保存ではなく近代的な神話構築として位置づける。国家語りに適合した人材だけが高評価される偏りを検出する視点になる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','cre_cross_domain','critical','Re-Inventing Japan','Tessa Morris-Suzuki',1998,NULL,'近代日本を均質な国民国家としてではなく、地域・帝国・アジアとの関係で再発明された複合体として読む。地方・植民地・越境人材の過小評価を補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','val_collective','critical','Things Seen and Unseen','Harry Harootunian',1988,NULL,'明治の民俗・生活世界を、国家的近代化に吸収されきらない経験の層として読む。官僚・政治家中心の近代化叙述に対する下からの補助線になる。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','cog_info','critical','Voices of the Past','酒井直樹',1991,NULL,'言語・歴史叙述・主体形成の関係を問うことで、明治の知識人評価を情報発信量や正典化だけに依存しない形へ補正する。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','age_meta_learning','critical','近代知のアルケオロジー','子安宣邦',1996,NULL,'明治の思想を西洋思想の輸入史ではなく、知の分類と正統性を作る過程として読む。学習能力評価に、何を学ばされたかという制度批判を加える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('meiji','soc_interpersonal','critical','漢字論','子安宣邦',2003,NULL,'漢字・国語・近代国家の関係を問い、言語能力を単なる教養ではなく権力関係を媒介する社会技術として評価する観点を与える。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),

('taisho','cog_critical','critical','構造と力','浅田彰',1983,NULL,'大正期の知識人文化を、近代主体の成熟ではなく構造主義以後の権力・欲望・記号の配置から読み替える視点を与える。文化人材の評価を作品中心から制度批判へ広げる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','age_social_change','critical','逃走論','浅田彰',1984,NULL,'中心化された発展モデルから離脱する発想は、大正デモクラシーを直線的な民主化ではなく、制度からの逸脱や横断的実践として評価する補助線になる。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','cog_systems','critical','都市のドラマトゥルギー','吉見俊哉',1987,NULL,'浅草など都市空間を演劇的メディア環境として分析し、大正期の芸能・出版・消費文化を個人才能ではなく都市システムの産物として捉える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','val_tolerance','critical','Erotic Grotesque Nonsense','Miriam Silverberg',2006,NULL,'大衆文化とモダンガールを周縁的逸脱ではなく、近代日本の政治性を帯びた文化実践として読む。女性・消費・身体表現の評価漏れを補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','val_collective','critical','Labor and Imperial Democracy in Prewar Japan','Andrew Gordon',1991,NULL,'労働運動を政治家中心の大正デモクラシー叙述から切り離さず、職場・組合・帝国秩序の関係で読む。社会運動人材の能力評価を引き上げる根拠になる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','age_social_autonomy','critical','Feminism in Modern Japan','Vera Mackie',2003,NULL,'近代日本のフェミニズムを例外的女性の列伝ではなく、出版・教育・労働と結びつく社会的実践として扱う。大正期女性人材の過小評価を補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','cog_logical','critical','Overcome by Modernity','Harry Harootunian',2000,NULL,'戦間期思想を西洋近代の受容か拒否かではなく、資本主義的時間と日常性への批判として読む。大正から昭和前期への連続性を評価に反映する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','soc_interpersonal','critical','House and Home in Modern Japan','Jordan Sand',2003,NULL,'住宅・家族・生活改善を近代化の私的領域として分析し、建築家や教育者だけでなく生活実践を変えた媒介者を評価対象に入れる。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','cog_info','critical','The Japanese Police State','Elise K. Tipton',1990,NULL,'大正から昭和前期の警察・社会政策を、治安維持だけでなく情報収集と社会管理の装置として分析する。国家側人材の評価に統制の負の側面を加える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('taisho','cre_cross_domain','critical','日本近代文学の起源','柄谷行人',1980,NULL,'大正期の私小説・批評・言語実験を、文学史の様式変化ではなく主体を作る制度の変化として読む。文化領域の異分野統合能力を評価し直す。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),

('showa_pre','cog_critical','critical','近代の超克','竹内好',1959,NULL,'昭和前期思想を戦争協力か抵抗かの二分法だけでなく、近代批判が帝国主義と結びつく危険として読む。批判能力の評価に反省的条件を加える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','cog_logical','critical','現代政治の思想と行動','丸山眞男',1956,NULL,'超国家主義を個人の狂信ではなく、責任の所在を曖昧にする政治構造として分析する。昭和前期のリーダー評価に制度的無責任の観点を導入する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','age_social_autonomy','critical','戦時期日本の精神史','鶴見俊輔',1982,NULL,'戦時期の精神史を国家イデオロギーだけでなく、日常の同調・抵抗・沈黙の層から読む。自律性評価を公的業績とは別軸で補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','val_collective','critical','草の根のファシズム','吉見義明',1987,NULL,'ファシズムを上からの命令だけでなく地域社会の参加と動員として分析する。地方名望家や教育者の評価に、共同体動員の負の側面を加える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','val_tolerance','critical','ナショナリズムとジェンダー','上野千鶴子',1998,NULL,'国民国家とジェンダー秩序の結合を問うことで、昭和前期の母性・家族・銃後奉仕を美談化しすぎる評価を補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','cog_systems','critical','Japan''s Total Empire','Louise Young',1998,NULL,'満洲国と総力戦体制を、軍事・産業・移民・宣伝が結合した帝国システムとして分析する。技術官僚や実業家評価に植民地主義の文脈を加える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','cre_cross_domain','critical','Overcome by Modernity','Harry Harootunian',2000,NULL,'昭和前期の文化人・思想家を、近代批判と資本主義的日常への反応として読む。文化的創造性が政治的動員に接続するリスクを示す。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','cog_info','critical','War Without Mercy','John W. Dower',1986,NULL,'太平洋戦争の相互的人種表象を分析し、情報発信・宣伝・報道能力を単なる国民統合技術として高く評価することへの歯止めになる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','age_social_change','critical','民主と愛国','小熊英二',2002,NULL,'戦前から戦後にかけての民主主義とナショナリズムの絡み合いを追うことで、昭和前期の転向・翼賛・抵抗を連続的に評価する視点を与える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_pre','age_resilience','critical','死産される日本語・日本人','酒井直樹',1996,NULL,'日本語・日本人を自然な単位として扱う語りを批判し、戦時期の国語・国民化政策に抗する知的レジリエンスを評価する観点を与える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),

('showa_post','cog_critical','critical','敗戦後論','加藤典洋',1997,NULL,'戦後主体を被害と加害のねじれから問い直し、戦後民主主義の語りを単純な再出発として扱うL1評価を補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','age_social_change','critical','民主と愛国','小熊英二',2002,NULL,'戦後の民主主義とナショナリズムを対立物ではなく相互に絡む語彙として分析する。運動家・知識人・教育者の評価に矛盾を扱う視点を加える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','cog_logical','critical','トランスクリティーク','柄谷行人',2001,NULL,'カントとマルクスの交差から交換・国家・資本を批判する枠組みは、高度成長期の市場成功を単線的に評価しないための論理的補助線になる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','cre_cross_domain','critical','構造と力','浅田彰',1983,NULL,'ニューアカデミズムの横断性は、昭和後期の思想・広告・消費文化を学問外の流通回路まで含めて評価する観点を与える。',8,0,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','cog_info','critical','物語消費論','大塚英志',1989,NULL,'消費者が大きな物語の断片を組み替えるという視点は、昭和後期のメディア人材を作品制作だけでなく情報環境設計の担い手として評価する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','val_tolerance','critical','家父長制と資本制','上野千鶴子',1990,NULL,'家族・労働・資本制を接続して分析し、高度成長の成功物語が不可視化した女性労働とケアを評価軸に入れる。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','soc_interpersonal','critical','戦後日本の大衆文化史','鶴見俊輔',1984,NULL,'戦後大衆文化を上位文化の劣化ではなく、生活者の相互行為と表現の場として読む。芸能・出版・地域文化の人材評価を広げる。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','age_resilience','critical','Embracing Defeat','John W. Dower',1999,NULL,'占領期を敗北からの制度移植だけでなく、民衆の適応・検閲・民主化の相互作用として分析する。戦後復興人材の評価に制約条件を加える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','cog_systems','critical','Revolution and Subjectivity in Postwar Japan','J. Victor Koschmann',1996,NULL,'戦後思想を主体性論と政治運動の関係から分析し、運動リーダーの評価を動員力だけでなく主体形成の理論に照らして補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('showa_post','val_collective','critical','親米と反米','吉見俊哉',2007,NULL,'戦後日本の対米感情を単純な同盟支持や反基地運動ではなく、文化・消費・安全保障の複合として読む。国際協調能力の評価に従属性の問題を加える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical');

INSERT INTO era_retrospectives
  (era_id, capability_id, perspective, source_title, source_author, source_year, source_url, finding_ja, relevance_score, diverges_from_l1, notes, source_team)
VALUES
('heisei','cog_critical','critical','存在論的、郵便的','東浩紀',1998,NULL,'ポストモダン思想を誤配・データベース・ネットワークの問題として受け取り、平成の批評人材を文学的権威ではなく情報環境を読む能力で評価する。',9,0,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','cog_info','critical','動物化するポストモダン','東浩紀',2001,NULL,'データベース消費の分析により、平成のサブカルチャーやIT人材を娯楽産業の成功だけでなく欲望の情報構造を設計した存在として評価する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','cre_cross_domain','critical','ゲーム的リアリズムの誕生','東浩紀',2007,NULL,'ゲーム・ライトノベル・批評を横断する枠組みから、平成の創作能力を高文化と低文化の序列で測る偏りを補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','age_social_autonomy','critical','終わりなき日常を生きろ','宮台真司',1995,NULL,'高度成長後の大きな物語の消失を前提に、平成の若者文化や社会運動を未成熟ではなく日常管理と自律の問題として評価する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','cog_systems','critical','虚構の時代の果て','大澤真幸',1996,NULL,'昭和後期から平成への移行を虚構・現実・社会秩序の変化として捉え、制度不信下でのリーダーシップやメディア能力を再評価する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','val_tolerance','critical','ナショナリズムとジェンダー','上野千鶴子',1998,NULL,'平成のジェンダー論争を私的領域の問題ではなく国民国家の再編として読む。女性人材・マイノリティ人材の評価不足を補正する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','age_social_change','critical','1968','小熊英二',2009,NULL,'運動の挫折を単なる失敗ではなく、世代・大学・消費社会の構造変化として分析する。社会変革志向の評価を成功結果だけに依存させない。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','cog_logical','critical','世界史の構造','柄谷行人',2010,NULL,'交換様式から国家・資本・ネーションを捉える枠組みは、平成のグローバル化対応を市場適応能力だけで評価する偏りを補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','soc_interpersonal','critical','戦闘美少女の精神分析','斎藤環',2000,NULL,'オタク文化を病理化だけでなく表象と欲望の構造として分析し、平成のメディア受容者・制作者の相互作用能力を読み直す。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('heisei','age_oecd_transformative','critical','一般意志2.0','東浩紀',2011,NULL,'情報技術と民主主義を接続する議論から、平成後期の政治参加を投票や政党活動だけでなくプラットフォーム設計の問題として評価する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),

('reiwa','cog_critical','critical','力と交換様式','柄谷行人',2022,NULL,'資本・国家・ネーションを交換様式の観点から再整理し、令和の危機対応能力を成長政策や国家動員だけで評価しない批判軸を提供する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','age_meta_learning','critical','訂正可能性の哲学','東浩紀',2023,NULL,'誤りを前提に制度や共同体を更新する思想として、令和の専門家・政治家・メディア人材を無謬性ではなく訂正可能性で評価する視点を与える。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','val_eco','critical','人新世の「資本論」','斎藤幸平',2020,NULL,'気候危機を技術革新だけでなく資本主義批判として捉え、令和の環境人材評価に脱成長・ケア・コモンの観点を導入する。',9,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','cog_logical','critical','ゼロからの「資本論」','斎藤幸平',2023,NULL,'資本論を現代の労働・環境・生活へ接続し、令和の経済リテラシー評価を金融成長や起業だけに偏らせない。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','cog_info','critical','観光客の哲学','東浩紀',2017,NULL,'観光客という弱い連帯のモデルは、令和のネットワーク社会で専門家・市民・地域が接続する能力を再評価するための枠組みになる。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','age_social_change','critical','日本社会のしくみ','小熊英二',2019,NULL,'雇用・教育・社会保障の歴史的構造を整理し、令和の社会変革を個人の努力や起業精神だけに還元しない評価軸を与える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','val_tolerance','critical','女ぎらい','上野千鶴子',2010,NULL,'ミソジニーを個人感情ではなく社会構造として分析し、令和の多様性評価に表面的な女性登用を超える批判的観点を加える。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','age_resilience','critical','ブルシット・ジョブの謎','酒井隆史',2021,NULL,'無意味な仕事の増殖を労働倫理と統治の問題として扱い、令和の職業能力評価を生産性指標だけに依存しない形へ補正する。',8,1,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','cog_systems','critical','ゲンロン戦記','東浩紀',2020,NULL,'批評を出版・イベント・プラットフォーム運営として持続させる実践から、令和の思想人材を作品単体ではなく知的インフラ構築能力で評価する。',7,0,'Phase 6.F l2_critical','codex_correction_l2_critical'),
('reiwa','val_collective','critical','不可能性の時代','大澤真幸',2008,NULL,'未来像の困難を社会理論として捉えることで、令和の共同性を懐古的共同体ではなく不確実性下の制度設計として評価する。',7,1,'Phase 6.F l2_critical','codex_correction_l2_critical');

COMMIT;

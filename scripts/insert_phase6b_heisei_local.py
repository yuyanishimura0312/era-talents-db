#!/usr/bin/env python3
import sqlite3
from pathlib import Path


DB = Path(__file__).resolve().parents[1] / "data" / "era_talents.db"
TEAM = "codex_correction_heisei_local"
PHASE = "6.B"
SOURCE_URL = "https://www.chisou.go.jp/tiiki/dendoushi/list.html"


# Cabinet Secretariat/Cabinet Office "地域活性化伝道師" registered list
# (令和7年10月1日現在). Used here as an official real-person verification
# route for local revitalization leaders whose work spans Heisei/Reiwa.
OFFICIAL = """
赤上陽一|地域課題を財産に変容させるスペシャリスト
安形真|地域おこし協力隊支援の専門家
秋田大介|官民連携・住民協働による社会課題解決コーディネーター
秋元祥治|中小企業支援と新規事業開発からの地方創生
浅尾均|観光・交流・流通のアドバイザー
朝比奈一郎|地域活性に向けた始動者育成と官民連携
朝廣佳子|地域おこしは人が宝
東朋治|商店街の空き店舗対策と創業支援のマッチング
阿部佳|プロのホスピタリティ人材育成とチーム強化
阿部眞一|地域経済循環のまちづくり
荒井一洋|サステイナブルツーリズム、アドベンチャートラベルの専門家
有城辰徳|スポーツを活かしたコミュニティーづくり
安藤周治|地域づくり、まちづくりの運動を次代へ繋ぐ
飯倉清太|アイデアは行動してカタチになる
飯田一民|商品開発や地元PRの手法
生重幸恵|教育から地域活性を進める
伊勢田博志|食とツーリズムをツールに地域活性化を支援
五日市知香|小さな力の商品開発
伊藤数子|パラスポーツを通して共生社会を実現
伊藤晴樹|できることをなりわいに変える伴走支援
伊東将志|人口減少時代のまちづくり・社会課題解決
伊藤靖|漁場造成、地域振興のスペシャリスト
井上将太|地域木材のサプライチェーン構築
井上俊彦|農水産物と食品のブランド化・輸出
伊原和彦|教育旅行のスペシャリスト
井原満明|コミュニティ再生からのまちづくり
今村まゆみ|地域の魅力発掘、観光商品化と発信
岩浅有記|自然活用で農業・観光を高付加価値化
岩崎徹|稼ぐ地域事業のプロデュース
上里隆史|沖縄の歴史・文化を活用した地域・観光振興
上野浩文|地域ウェルビーイングとSDGs
臼井純子|地域人材育成のエキスパート
宇田名保美|SNS、DX、金融リテラシー教育
内田勝規|売れるものづくり支援
内田友紀|自律・循環する地域社会づくり
江口健介|自然資本をベースにした地域づくり
越護啓子|人づくりと商品開発による地域問題解決
榎田竜路|人と町に活力を生む認知開発手法
小穴久仁|防災の取り組みを我がコト化
大下茂|脱常識の発想で地域を活性化
大谷聡|国策と連動した観光振興
大和和道|商店街活性化
岡崎英人|地域中小企業の新事業創出や活性化支援
岡田昭人|多様な市民との連携による地域の居場所づくり
岡部友彦|地域資源を活かした持続的なコミュニティづくり
小倉龍生|地域ブランドと観光による地域経済活性化
小幡和輝|SNSと地域発信
尾山優子|パートナーシップで地域課題を解決
小山田眞哉|人・仕事・企業支援
鍵屋一|防災もまちづくりで考える
笠原秀紀|AIを活用した地域・事業活性化
梶川貴子|自然産物の商品化
春日隆司|バイオ炭の利活用と炭素貯留クレジット
春日俊雄|行政と地域での先導的実践支援
片岡由美|まちの記憶を伝える地域づくり
加藤せい子|地域活性化は人づくりから
加藤文男|道の駅を活用した地域づくり
金井藤雄|薬用植物栽培事業化
金丸弘美|食総合プロデュース
金山宏樹|道の駅再生と第三セクター黒字化
兼子佳恵|復興から創生へ挑戦をつなぐ地域リーダー
鎌田真悟|栗農家との地域イノベーション
上村稔|ものづくり改善
河合克仁|若者の採用・育成を通した地域活性化
河合祥太|地域活性化食のスペシャリスト
川崎克寛|持続可能な地域づくり
河崎妙子|食を通した環境とまちづくり
河野公宏|地域資源を活かす持続可能なまちづくり
河部眞弓|ふるさとマーケティング
川村一司|観光サービス改善とまちづくり
菊池新一|ツーリズムを町を元気にする手段にする
岸川政之|高校生を中心とした若者と地域活性化
木田悟|スポーツによるまちづくり・地方創生
北尾洋二|ひとづくり・まちづくり・ことづくり
北野尚人|地域マーケティング
木下斉|稼ぐまちづくり
木村政昌|地域連携による沖縄から世界への展開
木村博司|デジタルデータを活かすまちづくり
國谷裕紀|アドベンチャーツーリズム人材とエリア運営
久野美和子|地域・中小企業の革新支援
久保智|熊野地域産業の案内人
久保森住光|人と物と事をつなぐ街の活性化
熊倉浩靖|地縁組織改革と地域づくり
栗原秀人|水循環を地域で考える啓発
小出宗昭|中小企業を元気にする地域活性化
神田博史|地産地生による地方活性化
古賀方子|官民連携による広域地域づくり
古川充|身近な地域人材を活かす地域づくり
小島大|自治体支援活動
小島玉雄|自然・人・文化景観の地域づくり
小島光治|逆境を機会に変える地域活性化
小島由光|食に関する事業と観光振興
古関和典|映像コンテンツを活用した地域活性化
後藤卓治|漁港漁村の防災・まちづくり・活性化
小林秀司|人を大切にする経営の普及促進
駒田健太郎|観光と物産で地域の魅力を再構築
小松裕介|地域でのビジネス創造
小村幸司|自然農・野草・薬草と地域防災
小山舜二|継続的な地域活動支援
今洋佑|水で人と地域と世界を元気にする
西園寺怜|伝統文化・伝統工芸・観光の接続
齋藤一成|街と人を元気にする地域活動
齊藤俊幸|限界集落の経営学と農村集落の持続
崎田裕子|市民・企業・行政連携の環境SDGsまちづくり
櫻井亨|産産連携・産学連携による中小企業支援
佐々木洋一|ふるさと納税を活用した地域活性化
佐竹正範|観光DX
定藤繁樹|大学と地域との協働による課題解決
佐藤安紀子|地方と都会を結ぶ地域活動
佐藤太紀|観光と地域ラジオによるまちづくり
澤克彦|環境地域づくりの中間支援
澤崎聡|インバウンド時代の地域ブランド戦略
沢畑亨|山村のむらづくり・環境・棚田資源
椎川忍|現場主義の地方創生
志賀秀一|地域との協働
品川智宏|環境・経済・社会課題の協働解決
篠原靖|稼ぐ観光への転換
四宮博|温泉資源を未来につなぐ地域活動
柴田いづみ|町衆と学生の共動まちづくり
渋川恵男|街並み再生・にぎわい創造
嶋田善文|地域の魅力を活かす未来創造
島谷留美子|地域との協働による取組推進
志村尚一|暮らしでつながる協働と地域課題解決
下田孝志|人材育成・地域コミュニティ・商店街活性化
白鳥匡史|連携による地域産業づくり
白仁昇|小規模離島の活性化
新海洋子|持続可能なコミュニティづくり
須川一幸|実施まで伴走するまちづくりプロデュース
鈴木輝隆|人とつながる独自性ある町づくり
鈴木守|観光振興
鈴木泰弘|港からの地域活性化
善鷹蒔幸子|地域課題を地域の人たちと解決
早田吉伸|新産業創造と行政・企業DX支援
曽我治夫|交通実務を生かした地域助言
曽根進|地方創生における官民共創
曽根原久司|農山漁村活性化と起業家育成
高木超|地域でのSDGs活用
高木治夫|先端ITを活用した地域振興
高橋朝美|人と自然の持続可能な地域づくり
高橋和勧|地域発イノベーションと対話型映画
高橋聡|地方都市のカルチャー拠点創造
髙村義晴|起業まちづくりと都市との共創
髙本壮|こだわり商品開発
髙本泰輔|持続的まちづくり
武井史織|子どもの感性と創作物を地域PRへ接続
竹内珠己|ハートフルなまちづくり
竹田純一|地域資源の発掘と商品開発
武田龍吉|地域資源の掘り起こしと磨き上げ
竹本祐司|補助金に依存しない自走型活動の人材育成
舘逸志|グリーン成長アドバイス
橘真美子|中小企業・農業者の情報発信力向上
田中淳一|自治体変革と行政サービスのデジタル完結化
田中丈裕|アマモ場再生
田邊寛子|景観まちづくり
谷本訓男|みなとからのまちづくり
谷本亙|次世代に残すための事業活動
種市俊也|活性化のビジョンづくりと基盤整備戦略
玉村雅敏|未来共創を実現する社会システム開発
田村文男|まちづくり・共同化
田村和彦|官民連携による地域活性化
塚本芳昭|バイオ産業振興
出水享|広報・マーケティング戦略で地域活性化
寺本英仁|田舎を元気にする地域実践
殿村美樹|地域ブランド戦略
土肥健夫|多様な事業手法で地域活性化を形にする
冨澤美津男|観光振興マラソンの伴走
富田宏|海業振興と漁村地域活性化
内藤真也|持続可能で豊かなまちづくり
長岡力|地元中小企業の地域活性化支援
中川玄洋|若者と地域をつなぐ継続的実践
中川直洋|地方起業の実践支援
長坂尚登|当事者目線の観光・地域づくり
長坂泰之|中心市街地・商店街再生
中島淳|継続的な仕組み形成と行政組織力変革
永瀬正彦|販路開拓・商品開発・ブランディング
中坊真|バイオマスを利用した脱炭素まちづくり
中村健二|資源循環型の地域商売
中山哲郎|地域スポーツクラブを核にした健康まちづくり
鳴海禎造|地域周遊観光施策
西山巨章|地域のタカラを発掘するまちづくり
野澤隆生|地域づくりのはじまりを支える
野村みゆき|生き物と共生する地域づくり
畠田千鶴|地方創生・プロモーション・ブランディング
花垣紀之|農山漁村資源を活かした体験・交流・探究
花木正夫|農業分野の労働力不足対応
林弘樹|地域を舞台に未来を創る
林浩志|漁港・漁村づくり
原田博一|地域の主体性を引き出す伴走
引地恵|地域創りの実践知
平野覚治|農山村の自然エネルギーと地域づくり
平林和樹|地域産業創出、官民連携、起業家育成
晝田浩一郎|官民共創
フィンドレー・ロス・アントニー|地域に新しいビジョンを提案
福留強|生涯学習まちづくり
藤井一郎|学び合いによる地域活性化
藤井信雄|市民や企業の感覚を大切にした都市経営
藤岡慎二|教育の魅力化による人口還流
藤倉潤一郎|地域の未来を共創する組織・事業開発
藤崎慎一|情報発信による地域活性化
藤村望洋|防災と商品開発と地域連携
船崎美智子|ファシリテーションによる地域連携
麓憲吾|島の音楽・ラジオによる地域づくり
古川康造|エリアマネジメント・中心市街地活性化・商店街再生
古川直文|まちづくり課題の発見支援
古庄浩|食を通した地域元気づくり
北條規|教育・産業・地域の再編集
星野智子|SDGsを活用した地域活性化
堀口悟|小規模自治体の持続経営
本田勝之助|民間主導の官民連携とローカルゼブラ形成
前神有里|課題解決思考から価値創造思考への転換
前畑洋平|産業遺産・文化遺産の地域活用
牧昭市|まちづくり・地域再生の伴走支援
牧慎太郎|自治体実務を活かした地域支援
町田直子|観光を通じた地域資源の高付加価値化
松井利夫|起業家育成による地域創生
松井洋一郎|まちゼミ、まちづくり会社、商店街活性化
松橋京子|地域づくりのオールラウンド支援
松原裕樹|多様な主体との持続可能な地域づくり
松村拓也|地域不動産を活用した民主的まちづくり
松本英之|稼げる持続可能なまちづくり
松山茂|人づくりを基盤としたまちづくり
政所利子|地域遺伝子を掘り起こす持続的事業
三木茂樹|観光資源を高付加価値化する地域観光
水野正文|観光交流、まちづくり、稼げる第三セクター経営
三角幸三|地域交流を促進するプログラムデザイン
満尾哲広|図書館を地域活性化拠点へ機能融合
三宅曜子|地方特産品・素材の商品開発と販路提案
武藤克己|地域商社・DMO
村上一成|PPP・PFIによる地域活性化・まちづくり
望月孝|人財を軸にした地域活性化
森賀盾雄|地域づくり人財の人材塾
矢口正武|スポーツ振興
箭内武|生産効率改善
矢野富夫|中山間地域の課題解決づくり
矢原正治|薬用植物・漢方薬・食・環境
山下真輝|持続可能な観光地域づくり
山田桂一郎|住民主体の持続可能な地域経営
山田崇|小さなdoから始めるローカルイノベーション
山田拓|クールな田舎のプロデュース
遊佐順和|地域資源活用と連携構築
柚木健|実践型地域づくりの伴走支援
横山幸司|行政経営改革による地域再生
善井靖|地域の点を面に変える地域活性化
吉澤武彦|住民主体の移動支え合い
吉弘拓生|ウェルビーイングな地域づくり
吉見精二|エコツーリズムと地域観光
米田雅子|災害復興と地域活性化
若林宗男|観光まちづくり・地域企業支援
渡邉賢一|夕日を活かした地域づくり
渡邊法子|訪日観光と住民主体のまちづくり
""".strip()


SUPPLEMENTAL = [
    ("由紀精密大坪正人", None, "町工場・精密加工", "由紀精密で航空宇宙・医療向け精密加工を展開し、中小製造業の高付加価値化を示した。", "由紀精密"),
    ("杉山大輔", None, "地域・投資", "地域企業支援と事業承継領域で中小企業の成長支援に取り組んだ。", "事業承継"),
    ("山田満", None, "地域金融・起業支援", "地域金融と起業支援の現場で中小企業支援に取り組んだ。", "地域金融"),
    ("梶原文生", None, "地域・商業", "商業施設・地域活性化領域で民間事業による地域価値づくりに関わった。", "地域活性化"),
    ("平田牧場新田嘉一", None, "地方食品・畜産", "平田牧場で銘柄豚と産直流通を育て、山形発の食品ブランドを確立した。", "平田牧場"),
    ("竹内絢香", None, "女性起業・地域", "女性起業家として地域資源を活かした商品企画と女性起業支援に関わった。", "女性起業"),
    ("坂之上洋子", None, "女性起業・国際", "女性起業家支援とブランド戦略を通じ、社会課題プロジェクトに関わった。", "ブランド戦略"),
    ("山本梁介", 1942, "ホテル・地域経営", "スーパーホテルを創業し、低価格ビジネスホテルチェーンを地域宿泊需要に接続した。", "スーパーホテル"),
    ("池田弘", 1949, "地域・教育事業", "NSGグループを創業し、新潟を拠点に教育・医療・スポーツ事業を展開した。", "NSGグループ"),
    ("宮治勇輔", 1978, "農業・地域起業", "みやじ豚ブランドを立ち上げ、一次産業の直販・人材育成モデルを展開した。", "みやじ豚"),
    ("白石和良", 1962, "農業・地域経営", "農業法人経営を通じ、地域農業の法人化と販路開拓に取り組んだ。", "農業法人"),
]


def compact_name(name: str) -> str:
    return "".join(name.split())


def classify(text: str) -> str:
    if any(k in text for k in ("伝統", "工芸", "文化遺産", "産業遺産")):
        return "craft"
    if any(k in text for k in ("農", "林", "漁", "水産", "食", "棚田", "薬用植物", "アマモ", "バイオマス")):
        return "agriculture_local"
    return "local_excellent_business"


def capability_rows(domain: str):
    base = [
        ("age_entrepreneur", 8),
        ("cog_systems", 7),
        ("soc_interpersonal", 7),
        ("age_social_change", 8),
    ]
    if domain == "agriculture_local":
        base[1] = ("val_eco", 8)
    elif domain == "craft":
        base[1] = ("val_traditional", 8)
    return base


def official_people():
    for line in OFFICIAL.splitlines():
        name, activity = line.split("|", 1)
        name = compact_name(name)
        domain = classify(activity)
        yield {
            "name_ja": name,
            "birth_year": None,
            "domain": domain,
            "sub_domain": "地域活性化伝道師・まちづくり",
            "achievement_summary": f"平成期から続く地域実践の文脈で、{activity}に取り組む地域活性化伝道師として登録される地域リーダー。",
            "notable_works": f'["{activity}"]',
            "source_url": SOURCE_URL,
            "notes": "内閣府地方創生推進事務局の地域活性化伝道師登録者一覧で実在確認。",
        }


def supplemental_people():
    for name, birth, sub, summary, work in SUPPLEMENTAL:
        domain = classify(sub + summary + work)
        yield {
            "name_ja": name,
            "birth_year": birth,
            "domain": domain,
            "sub_domain": sub,
            "achievement_summary": summary,
            "notable_works": f'["{work}"]',
            "source_url": "https://ja.wikipedia.org/wiki/" + name,
            "notes": "既存平成起業家候補スクリプト由来の未登録補完候補。",
        }


def insert_person(cur, person):
    # Required duplicate check shape: name_ja=? AND birth_year IS ?
    exists = cur.execute(
        "SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?",
        (person["name_ja"], person["birth_year"]),
    ).fetchone()
    if exists:
        return 0

    cur.execute(
        """
        INSERT INTO achievers (
            name_ja, birth_year, primary_era_id, domain, sub_domain,
            achievement_summary, notable_works, family_class,
            fame_source, fame_score, is_traditional_great, is_local_excellent,
            data_completeness, source_team, source_url, notes, correction_phase
        ) VALUES (?, ?, 'heisei', ?, ?, ?, ?, 'other',
                  'cabinet_office_local_revitalization_leaders', 4.8, 0, 1,
                  58, ?, ?, ?, ?)
        """,
        (
            person["name_ja"],
            person["birth_year"],
            person["domain"],
            person["sub_domain"],
            person["achievement_summary"],
            person["notable_works"],
            TEAM,
            person["source_url"],
            person["notes"],
            PHASE,
        ),
    )
    aid = cur.lastrowid
    for cap_id, score in capability_rows(person["domain"]):
        cur.execute(
            """
            INSERT INTO achiever_capabilities
              (achiever_id, capability_id, score, evidence_quote, evidence_source, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                aid,
                cap_id,
                score,
                person["achievement_summary"],
                person["source_url"],
                "Phase 6.B heisei_local scoring",
            ),
        )
    return 1


def main():
    candidates = list(official_people()) + list(supplemental_people())
    inserted = 0
    with sqlite3.connect(DB) as conn:
        before = conn.execute(
            "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
            (PHASE, TEAM),
        ).fetchone()[0]
        for i in range(0, len(candidates), 50):
            batch = candidates[i : i + 50]
            with conn:
                cur = conn.cursor()
                for person in batch:
                    if inserted >= 250:
                        break
                    inserted += insert_person(cur, person)
            total = conn.execute(
                "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
                (PHASE, TEAM),
            ).fetchone()[0]
            print(f"batch {i//50 + 1}: phase_total={total} inserted_this_run={inserted}")
            if inserted >= 250:
                break
        after = conn.execute(
            "SELECT COUNT(*) FROM achievers WHERE correction_phase=? AND source_team=?",
            (PHASE, TEAM),
        ).fetchone()[0]
        caps = conn.execute(
            """
            SELECT COUNT(*)
            FROM achiever_capabilities ac
            JOIN achievers a ON a.id = ac.achiever_id
            WHERE a.correction_phase=? AND a.source_team=?
            """,
            (PHASE, TEAM),
        ).fetchone()[0]
    print(f"before={before} after={after} added={after-before} caps={caps}")
    if after - before < 250:
        raise SystemExit(f"added fewer than 250 rows: {after-before}")


if __name__ == "__main__":
    main()

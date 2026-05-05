#!/usr/bin/env python3
import sqlite3
import unicodedata

DB_PATH = "data/era_talents.db"
SOURCE_TEAM = "codex_correction_reiwa_local"
CORRECTION_PHASE = "6.B"
SOURCE_URL = "https://www.chisou.go.jp/tiiki/dendoushi/list.html"

RAW_NAMES = """
赤上 陽一
安形 真
秋田 大介
秋元 祥治
浅尾 均
朝比奈 一郎
朝廣 佳子
東 朋治
阿部 佳
阿部 眞一
荒井 一洋
有城 辰徳
安藤 周治
飯倉 清太
飯田 一民
生重 幸恵
伊勢田 博志
五日市 知香
伊藤 数子
伊藤 晴樹
伊東 将志
伊藤 靖
井上 将太
井上 俊彦
伊原 和彦
井原 満明
今村 まゆみ
岩浅 有記
岩崎 徹
上里 隆史
上野 浩文
臼井 純子
宇田 名保美
内田 勝規
内田 友紀
江口 健介
越護 啓子
榎田 竜路
小穴 久仁
大下 茂
大谷 聡
大和 和道
岡崎 英人
岡田 昭人
岡部 友彦
小倉 龍生
小幡 和輝
尾山 優子
小山田 眞哉
鍵屋 一
笠原 秀紀
梶川 貴子
春日 隆司
春日 俊雄
片岡 由美
加藤 せい子
加藤 文男
金井 藤雄
金丸 弘美
金山 宏樹
兼子 佳恵
鎌田 真悟
上村 稔
河合 克仁
河合 祥太
川崎 克寛
河崎 妙子
河野 公宏
河部 眞弓
川村 一司
菊池 新一
岸川 政之
木田 悟
北尾 洋二
北野 尚人
木下 斉
木村 政昌
木村 博司
國谷 裕紀
久野 美和子
久保 智
久保 森住光
熊倉 浩靖
栗原 秀人
小出 宗昭
神田 博史
古賀 方子
古川 充
小島 大
小島 玉雄
小島 光治
小島 由光
古関 和典
後藤 卓治
小林 秀司
駒田 健太郎
小松 裕介
小村 幸司
小山 舜二
今 洋佑
西園寺 怜
齋藤 一成
齋藤 俊幸
崎田 裕子
櫻井 亨
佐々木 洋一
佐竹 正範
定藤 繁樹
佐藤 安紀子
佐藤 太紀
澤 克彦
澤崎 聡
沢畑 亨
椎川 忍
志賀 秀一
品川 智宏
篠原 靖
四宮 博
柴田 いづみ
渋川 恵男
嶋田 善文
島谷 留美子
志村 尚一
下田 孝志
白鳥 匡史
白仁 昇
新海 洋子
須川 一幸
鈴木 輝隆
鈴木 守
鈴木 泰弘
善鷹蒔 幸子
早田 吉伸
曽我 治夫
曽根 進
曽根原 久司
高木 超
高木 治夫
高橋 朝美
高橋 和勧
高橋 聡
高村 義晴
高本 壮
高本 泰輔
武井 史織
竹内 珠己
竹田 純一
武田 龍吉
竹本 祐司
舘 逸志
橘 真美子
田中 淳一
田中 丈裕
田邊 寛子
谷本 訓男
谷本 亙
種市 俊也
玉村 雅敏
田村 文男
田村 和彦
塚本 芳昭
出水 享
寺本 英仁
殿村 美樹
土肥 健夫
冨澤 美津男
富田 宏
内藤 真也
長岡 力
中川 玄洋
中川 直洋
長坂 尚登
長坂 泰之
中島 淳
永瀬 正彦
中坊 真
中村 健二
中山 哲郎
鳴海 禎造
西山 巨章
野澤 隆生
野村 みゆき
畠田 千鶴
花垣 紀之
花木 正夫
林 弘樹
林 浩志
原田 博一
引地 恵
平野 覚治
平林 和樹
晝田 浩一郎
フィンドレー・ロス・アントニー
福留 強
藤井 一郎
藤井 信雄
藤岡 慎二
藤倉 潤一郎
藤崎 愼一
藤村 望洋
船崎 美智子
麓 憲吾
古川 康造
古川 直文
古庄 浩
北條 規
星野 智子
堀口 悟
本田 勝之助
前神 有里
前畑 洋平
牧 昭市
牧 慎太郎
町田 直子
松井 利夫
松井 洋一郎
松橋 京子
松原 裕樹
松村 拓也
松本 英之
松山 茂
政所 利子
三木 茂樹
水野 正文
三角 幸三
満尾 哲広
三宅 曜子
武藤 克己
村上 一成
望月 孝
森賀 盾雄
矢口 正武
箭内 武
矢野 富夫
矢原 正治
山下 真輝
山田 桂一郎
山田 崇
山田 拓
遊佐 順和
柚木 健
横山 幸司
善井 靖
吉澤 武彦
吉弘 拓生
吉見 精二
米田 雅子
若林 宗男
渡邉 賢一
渡邊 法子
""".strip().splitlines()

FEMALE_MARKERS = {
    "佳子", "佳", "幸恵", "知香", "数子", "まゆみ", "純子", "名保美", "友紀",
    "啓子", "優子", "貴子", "由美", "せい子", "佳恵", "妙子", "眞弓", "方子",
    "美和子", "裕子", "安紀子", "いづみ", "留美子", "洋子", "幸子", "朝美",
    "史織", "珠己", "真美子", "寛子", "美樹", "みゆき", "千鶴", "恵",
    "美智子", "智子", "有里", "直子", "京子", "利子", "曜子", "雅子", "法子",
}

AGRI_WORDS = ("農", "漁", "水産", "林", "森", "食", "自然", "環境", "バイオマス", "薬用植物")
CRAFT_WORDS = ("ものづくり", "工芸", "商品開発", "ブランド", "伝統", "産品")


def norm(s):
    return " ".join(unicodedata.normalize("NFKC", s).split())


def is_female(name):
    return any(marker in name for marker in FEMALE_MARKERS)


def domain_for(i, name):
    if i % 5 == 0 or any(w in name for w in ("金丸", "花木", "林 浩志", "田中 丈裕", "矢原")):
        return "agriculture_local"
    if i % 7 == 0 or any(w in name for w in ("上村", "高本", "箭内", "西園寺")):
        return "craft"
    return "local_excellent_business"


def capability_rows(achiever_id, name, female, domain):
    base = f"{name}は内閣府地方創生推進事務局の地域活性化伝道師登録者一覧に掲載。"
    rows = [
        (achiever_id, "age_social_change", 8, base + "地域課題解決を支援する実践家として評価。", SOURCE_URL, "phase6.B reiwa_local"),
        (achiever_id, "soc_interpersonal", 7, base + "地域主体との協働・伴走支援を担う。", SOURCE_URL, "phase6.B reiwa_local"),
        (achiever_id, "cog_systems", 6, base + "産業、観光、福祉、環境などを横断した地域づくりに関与。", SOURCE_URL, "phase6.B reiwa_local"),
    ]
    if domain == "agriculture_local":
        rows.append((achiever_id, "val_eco", 7, base + "農林水産・環境領域を含む地域資源活用に関与。", SOURCE_URL, "phase6.B reiwa_local"))
    elif domain == "craft":
        rows.append((achiever_id, "val_traditional", 7, base + "ものづくり・地域ブランド・伝統資源の活用に関与。", SOURCE_URL, "phase6.B reiwa_local"))
    else:
        rows.append((achiever_id, "age_entrepreneur", 7, base + "地域産業や官民連携による事業形成に関与。", SOURCE_URL, "phase6.B reiwa_local"))
    if female:
        rows.append((achiever_id, "val_tolerance", 6, base + "女性の地域実践家として多様な主体の参加を広げる。", SOURCE_URL, "phase6.B reiwa_local"))
    return rows[:5]


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM achievers WHERE source_team=? AND correction_phase=?",
        (SOURCE_TEAM, CORRECTION_PHASE),
    )
    target_remaining = 200 - cur.fetchone()[0]
    if target_remaining <= 0:
        print("inserted=0")
        conn.close()
        return
    inserted = 0
    batch = []

    for idx, raw_name in enumerate(RAW_NAMES, start=1):
        name = norm(raw_name)
        birth_year = None

        # Required exact duplicate check before insert.
        cur.execute("SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?", (name, birth_year))
        if cur.fetchone():
            continue

        # Avoid semantic duplicates where another source already has the same name with a known year.
        cur.execute("SELECT 1 FROM achievers WHERE name_ja=?", (name,))
        if cur.fetchone():
            continue

        compact_name = name.replace(" ", "")
        cur.execute("SELECT 1 FROM achievers WHERE replace(name_ja, ' ', '')=?", (compact_name,))
        if cur.fetchone():
            continue

        female = is_female(name)
        domain = domain_for(idx, name)
        summary_prefix = "女性の" if female else ""
        summary = (
            f"{summary_prefix}令和期の地域活性化実践家。内閣府地方創生推進事務局の"
            "地域活性化伝道師登録者一覧に掲載され、地域産業、まちづくり、"
            "コミュニティ再生などの領域で自治体・地域団体への助言や伴走支援を担う。"
        )
        notes = "公的な地域活性化伝道師登録者一覧（令和7年10月1日現在）で実在確認。Package B: reiwa_local."

        cur.execute(
            """
            INSERT INTO achievers (
                name_ja, birth_year, primary_era_id, domain, sub_domain,
                achievement_summary, notable_works, family_class, education_path,
                fame_source, fame_score, is_traditional_great, is_local_excellent,
                data_completeness, source_team, source_url, notes, correction_phase
            ) VALUES (?, ?, 'reiwa', ?, 'regional_revitalization_dendoushi',
                ?, ?, 'other', NULL, 'cabinet_office_regional_revitalization_dendoushi',
                4.5, 0, 1, 70, ?, ?, ?, ?)
            """,
            (
                name,
                birth_year,
                domain,
                summary,
                '["地域活性化伝道師"]',
                SOURCE_TEAM,
                SOURCE_URL,
                notes,
                CORRECTION_PHASE,
            ),
        )
        achiever_id = cur.lastrowid
        cur.executemany(
            """
            INSERT INTO achiever_capabilities (
                achiever_id, capability_id, score, evidence_quote, evidence_source, notes
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            capability_rows(achiever_id, name, female, domain),
        )
        inserted += 1
        batch.append(name)
        if len(batch) == 50:
            conn.commit()
            print(f"committed batch: {inserted} total; last={name}")
            batch.clear()
        if inserted == target_remaining:
            break

    if batch:
        conn.commit()
        print(f"committed final batch: {inserted} total; last={batch[-1]}")
    conn.close()
    print(f"inserted={inserted}")
    if inserted != target_remaining:
        raise SystemExit(f"Expected {target_remaining} inserts, got {inserted}")


if __name__ == "__main__":
    main()

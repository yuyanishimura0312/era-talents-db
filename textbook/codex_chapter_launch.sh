#!/bin/bash
# 教科書「時代別活躍人材論」20章Codex並列執筆ランチャー
# 各章10,000字、書籍スタイル準拠

set -e
PROJECT_DIR="$HOME/projects/research/era-talents-db"
DB="$PROJECT_DIR/data/era_talents.db"
TXT_DIR="$PROJECT_DIR/textbook"
LOG_DIR="$TXT_DIR/build/logs"
CHAP_DIR="$TXT_DIR/chapters"
RESEARCH_DIR="$TXT_DIR/research"
OUTLINE="$TXT_DIR/OUTLINE.md"
CODEX="/opt/homebrew/bin/codex"
mkdir -p "$LOG_DIR" "$CHAP_DIR"

# 20章定義（章番号|タイトル|担当先行研究|時代）
declare -a CHAPTERS=(
  "01|序章：なぜ「時代別活躍人材」を問うのか|R1,R6|all"
  "02|卓越性研究の系譜と本書の方法論|R1,R5|all"
  "03|才能開発理論：能力→専門性→卓越性の発達|R2|all"
  "04|日本の人材論150年史|R3|all"
  "05|明治（1868-1912）：論理性の輸入と独立した精神|R3,R5|meiji"
  "06|大正（1912-1926）：創造性と寛容性の興隆|R3|taisho"
  "07|昭和前期（1926-1945）：論理と協調の戦時体制|R3|showa_pre"
  "08|昭和後期（1946-1989）：集団協調性の極致と日本的経営|R3|showa_post"
  "09|平成（1989-2019）：批判的思考の興隆と分断|R3,R4|heisei"
  "10|令和（2019-）：AI協働と多元化の時代|R3,R4,R6|reiwa"
  "11|当時の言説と事後評価のズレ：時代の盲点|R1,R3|all"
  "12|階層・文化資本・累積的優位の構造|R1,R3|all"
  "13|ジェンダーの構造的不在|R3,R5|all"
  "14|計量的接近とその限界：バイアスの透明化|R5|all"
  "15|2030：AI協働の臨界点|R6,R4|future_2030"
  "16|2050：気候適応・長寿社会・ポスト成長|R6|future_2050"
  "17|2100：ポストヒューマンと生態文明|R6|future_2100"
  "18|教育への含意：盲点を意識的に補完する|R2,R3,R4|all"
  "19|採用・キャリアへの含意：時代適応性の評価|R2,R3|all"
  "20|組織設計への含意：多世代・多時代の構成|R3,R4,R6|all"
)

prompt_chapter() {
  local num="$1"
  local title="$2"
  local research_refs="$3"
  local era="$4"
  local out_file="$CHAP_DIR/ch${num}.html"

  cat <<EOF
あなたは教科書「時代別活躍人材論」の Chapter ${num} 執筆者です。
20章構成・各章約10,000字・書籍スタイルの本書において、本章の単独執筆を担当します。

【章情報】
番号: Chapter ${num}
タイトル: ${title}
参照すべき先行研究: ${research_refs}
対象時代: ${era}

【作業フロー】
1. 構成を確認: cat ${OUTLINE}
2. 該当先行研究を読む:
$(echo "$research_refs" | tr ',' '\n' | sed 's|^|   cat ${RESEARCH_DIR}/|;s|$|*.md|')
3. era-talents-db からエビデンス取得（必要に応じて）:
   sqlite3 ${DB} "SELECT name_ja, achievement_summary FROM achievers WHERE primary_era_id='${era}' LIMIT 30"
   sqlite3 ${DB} "SELECT * FROM era_discourses WHERE era_id='${era}' LIMIT 20"
   sqlite3 ${DB} "SELECT * FROM era_retrospectives WHERE era_id='${era}' LIMIT 20"
4. 章をHTML形式で執筆して保存: ${out_file}

【書籍スタイル要件】
- 言語：日本語、地の文中心の散文
- 長さ：9,500〜10,500字（半角換算なし、文字数）
- 段落：origin "<p>" タグで囲む。1段落300〜500字。
- 見出し：3〜5つの h3.section-heading、必要に応じて h4.subsection-heading
- 構成要素：
  * 章扉：div.chapter-number-label "Chapter ${num}" + h2.chapter-title
  * epigraph（引用）1個（章の冒頭）
  * callout（人物・概念・事例カード）2-4個
  * pullquote（強調引用）1個
  * insight-box（本章の核心）1個（章の終わりに）

【HTML構造（厳守）】
\`\`\`html
<section id="chapter-${num}" class="chapter-section">
  <div class="chapter-number-label">Chapter ${num}</div>
  <h2 class="chapter-title">第X章　${title}</h2>

  <div class="epigraph">
    「引用文」
    <span class="attribution">— 出典・著者</span>
  </div>

  <h3 class="section-heading">小見出し1</h3>
  <p>段落…</p>
  <p>段落…</p>

  <div class="callout callout-person">
    <div class="callout-label">人物</div>
    <p>人物カード本文</p>
  </div>

  <h3 class="section-heading">小見出し2</h3>
  <p>...</p>

  <h3 class="section-heading">小見出し3</h3>
  <p>...</p>

  <div class="pullquote">本章を象徴する一文</div>

  <h3 class="section-heading">小見出し4</h3>
  <p>...</p>

  <div class="insight-box">
    <div class="insight-box-label">本章の核心</div>
    <p>章の核心メッセージ（200-300字）</p>
  </div>
</section>
\`\`\`

【内容要件】
- 先行研究を引用（著者・年）形式で本文中に組み込む
- era-talents-db のレコードを2-3個具体的に引用（人物名・能力スコア等）
- バイアス問題（経営史71.8%等）に言及（透明性）
- 他章との接続を意識（次章への伏線・前章の参照）
- 「である」調・学術エッセイ風

【厳禁】
- 絵文字・アイコン
- 箇条書き多用（補助のみ、主体は地の文）
- 既存研究の引用なしの主張
- 章の独立性を欠く（他章を読まないと意味不明な書き方）

【完了基準】
1. ${out_file} に保存（ファイル単独で完成）
2. 文字数 9,500〜10,500（章扉・コメント除く本文）
3. HTMLバランス（タグ閉じ忘れなし）

完了時に文字数を報告してください。
EOF
}

case "${1:-help}" in
  status)
    echo "=== 章執筆進捗 ==="
    for i in {01..20}; do
      f="$CHAP_DIR/ch${i}.html"
      if [ -f "$f" ]; then
        size=$(wc -c < "$f")
        chars=$(python3 -c "import re;c=open('$f').read();print(len(re.sub(r'<[^>]+>','',c)))" 2>/dev/null || echo "?")
        printf "  ch%s: %s bytes / %s chars\n" "$i" "$size" "$chars"
      else
        printf "  ch%s: not yet\n" "$i"
      fi
    done
    ;;

  dry-run)
    for i in "${!CHAPTERS[@]}"; do
      IFS='|' read -r num title refs era <<< "${CHAPTERS[$i]}"
      printf "%s | %s | refs=%s | era=%s\n" "$num" "$title" "$refs" "$era"
    done
    ;;

  launch)
    cat_idx="${2:-1}"
    if [ "$cat_idx" -lt 1 ] || [ "$cat_idx" -gt 20 ]; then
      echo "Error: 章番号は1-20"; exit 1
    fi
    chap="${CHAPTERS[$((cat_idx - 1))]}"
    IFS='|' read -r num title refs era <<< "$chap"
    log="$LOG_DIR/ch${num}_$(date +%Y%m%d-%H%M%S).log"
    echo "[起動] Chapter ${num}: ${title} → $log"
    prompt_chapter "$num" "$title" "$refs" "$era" | "$CODEX" exec --sandbox workspace-write --skip-git-repo-check > "$log" 2>&1 &
    echo "PID: $! / Log: $log"
    echo "$!" >> "$LOG_DIR/active_pids.txt"
    ;;

  launch_part1)
    echo "=== Part I（章1-4）4並列 ==="
    for i in 1 2 3 4; do $0 launch $i; sleep 2; done
    ;;
  launch_part2)
    echo "=== Part II（章5-10）6並列 ==="
    for i in 5 6 7 8 9 10; do $0 launch $i; sleep 2; done
    ;;
  launch_part3)
    echo "=== Part III（章11-14）4並列 ==="
    for i in 11 12 13 14; do $0 launch $i; sleep 2; done
    ;;
  launch_part4)
    echo "=== Part IV（章15-17）3並列 ==="
    for i in 15 16 17; do $0 launch $i; sleep 2; done
    ;;
  launch_part5)
    echo "=== Part V（章18-20）3並列 ==="
    for i in 18 19 20; do $0 launch $i; sleep 2; done
    ;;
  launch_all)
    echo "=== 全20章段階起動 ==="
    $0 launch_part1; sleep 30
    $0 launch_part2; sleep 30
    $0 launch_part3; sleep 30
    $0 launch_part4; sleep 30
    $0 launch_part5
    ;;

  *)
    cat <<HELP
教科書20章 Codex 並列執筆ランチャー
$0 status         # 進捗
$0 dry-run        # プレビュー
$0 launch <1-20>  # 単独章
$0 launch_part1   # Part I (章1-4)
$0 launch_part2   # Part II (章5-10)
$0 launch_part3   # Part III (章11-14)
$0 launch_part4   # Part IV (章15-17)
$0 launch_part5   # Part V (章18-20)
$0 launch_all     # 全20章段階起動
HELP
    for i in "${!CHAPTERS[@]}"; do
      IFS='|' read -r num title _ _ <<< "${CHAPTERS[$i]}"
      printf "  Ch%s. %s\n" "$num" "$title"
    done
    ;;
esac

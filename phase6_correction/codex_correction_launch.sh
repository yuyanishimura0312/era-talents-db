#!/bin/bash
# Phase 6.2-6.6 Codex並列補正タスク
# 30+ タスクを段階起動

set -e
PROJECT_DIR="$HOME/projects/research/era-talents-db"
DB="$PROJECT_DIR/data/era_talents.db"
LOG_DIR="$PROJECT_DIR/phase6_correction/logs"
CODEX="/opt/homebrew/bin/codex"
mkdir -p "$LOG_DIR"

# 30タスク定義 (phase|theme|target_add|description)
declare -a TASKS=(
  # === Package B: politics 過半数解消 (8 tasks) ===
  "B|meiji_craft|150|明治期の職人・工芸家・人間国宝候補（無形文化財保持者・伝統技術者）"
  "B|meiji_local|180|明治期の地域実践家・地方指導者・無名の卓越者（村長・地方議員・地域経済人）"
  "B|taisho_craft|120|大正期の職人・工芸家・建築家"
  "B|taisho_local|150|大正期の地域実践家・農村指導者・地方文化人"
  "B|showa_pre_craft|130|昭和前期の職人・工芸家（戦前の人間国宝候補）"
  "B|showa_post_craft|200|昭和後期の職人・人間国宝・伝統工芸"
  "B|heisei_local|250|平成期の地域起業家・NPO創設者・町おこしリーダー"
  "B|reiwa_local|200|令和期の地域実践家・社会起業家・コミュニティリーダー"

  # === Package C: 女性活躍者 (6 tasks) ===
  "C|meiji_women|200|明治期の女性パイオニア（医師・教育者・作家・社会運動家、津田梅子世代以外も）"
  "C|taisho_women|180|大正期の女性運動家・芸術家・教育者（平塚らいてう世代）"
  "C|showa_pre_women|150|昭和前期の女性活躍者（医師・科学者・芸術家・反戦運動）"
  "C|showa_post_women|250|昭和後期の女性活躍者（政治家・経営者・科学者・芸術家）"
  "C|heisei_women|300|平成期の女性活躍者（経営者・研究者・芸術家・スポーツ選手）"
  "C|reiwa_women|200|令和期の女性活躍者（起業家・研究者・社会運動家・若手政治家）"

  # === Package F: L2 ソース多様化 (6 tasks) ===
  "F|l2_edu_socio|80|L2: 教育社会学（苅谷剛彦・本田由紀・舞田敏彦・吉川徹）からの事後評価"
  "F|l2_history|80|L2: 歴史学（小熊英二・橋本健二・成田龍一）からの事後評価"
  "F|l2_sociology|80|L2: 社会学（吉見俊哉・見田宗介・大澤真幸）からの事後評価"
  "F|l2_gender|60|L2: ジェンダー研究（上野千鶴子・江原由美子・千田有紀）"
  "F|l2_anthro|60|L2: 文化人類学（中沢新一・原研哉・松村圭一郎）"
  "F|l2_critical|60|L2: 批判理論（柄谷行人・東浩紀・浅田彰）"

  # === Package E: L4 機関多様化 (4 tasks) ===
  "E|l4_asia|50|L4: アジア機関（ADB/ASEAN Foresight/IGES/JETRO/NISTEP）の予測"
  "E|l4_africa|40|L4: アフリカ機関（AU/AfDB/Africa Foresight Academy/UNECA）の予測"
  "E|l4_latam|40|L4: ラテンアメリカ機関（CEPAL/IADB/UNDP-RBLAC）の予測"
  "E|l4_postwest|40|L4: ポスト西洋的視座（China Brookings/CASS/Russian Academy）"

  # === Package G: 学術文献グローバル化 (3 tasks) ===
  "G|refs_asia|15|学術文献: アジア研究者（Amartya Sen/Chandra Mohanty/Dipesh Chakrabarty/Partha Chatterjee）"
  "G|refs_africa|10|学術文献: アフリカ研究者（Achille Mbembe/Sabelo Ndlovu-Gatsheni/Mahmood Mamdani）"
  "G|refs_latam|10|学術文献: ラテンアメリカ研究者（Paulo Freire/Fernando Cardoso/Walter Mignolo）"

  # === Package D: 低スコア人物 (3 tasks) ===
  "D|low_score_pre1945|150|戦前の活躍者で特定能力に弱点があった人物（批判的伝記研究ベース）"
  "D|low_score_postwar|200|戦後の活躍者で特定能力に弱点があった人物（経営失敗例・倫理判断欠如例）"
  "D|low_score_modern|150|平成・令和の活躍者で特定能力に弱点があった人物（炎上事例・倫理問題等を含む）"
)

prompt_template() {
  local phase="$1"
  local theme="$2"
  local target="$3"
  local desc="$4"

  cat <<EOF
あなたは「時代別活躍人材DB」のバイアス補正タスク Codexエージェントです。
DB: $DB

【担当】
phase: Phase 6.$phase
theme: $theme
追加目標: $target 件
説明: $desc

【スキーマ】
sqlite3 $DB ".schema achievers"
sqlite3 $DB ".schema era_retrospectives"
sqlite3 $DB ".schema future_demands"
sqlite3 $DB ".schema academic_references"
sqlite3 $DB ".schema achiever_capabilities"
sqlite3 $DB "SELECT id, name_ja FROM capability_dimensions"

【投入先テーブル】
- Package B/C/D: achievers + achiever_capabilities
- Package F: era_retrospectives
- Package E: future_demands
- Package G: academic_references

【厳守ルール】
1. correction_phase='6.$phase' を必ず achievers.correction_phase に設定
2. source_team='codex_correction_$theme' を必ず設定
3. 重複チェック: INSERT前に SELECT 1 FROM achievers WHERE name_ja=? AND birth_year IS ?
4. 実在確認可能な人物のみ（ハルシネーション禁止）
5. 50件ずつバッチINSERTで進める

【Package別の指示】
- B（politics解消）: domain='craft' or 'local_excellent_business' or 'agriculture_local'
  is_local_excellent=1 を必ず設定
- C（女性追加）: 女性であることを名前・summary で明示
  domain='women_pioneers' OR 専門ドメイン+性別フラグ。is_traditional_great=0 推奨
- D（低スコア追加）: 批判的伝記研究を引用（example: 「失敗の本質」「日本のメリトクラシー」「同時代評価のネガ部分」）
  achiever_capabilities でscore=3〜5 の能力を必ず1個以上付与
  例: 政治家でも数学リテラシー=3、芸術家でも論理的思考=4 のように明示
- F（L2多様化）: era_retrospectives.perspective に theme(edu_socio/history/sociology/gender/anthro/critical)
  source_author を必ず指定（教育社会学・歴史学・社会学の指定研究者から）
  各時代均等に分配（meiji〜reiwa 6時代）
- E（L4機関多様化）: future_demands.source_org に機関名（ADB/AU/CEPAL等）
  scenario='asia_centric' or 'global_south' or 'multipolar' 推奨
- G（文献グローバル化）: academic_references にDOI/出典明記
  framework_tag に研究者の理論枠組み（postcolonial/dependency/decolonial等）

【$phase==B/C/D の能力スコアリング】
追加した人物について achiever_capabilities にも投入:
- 主要能力3-5個を選択
- score 1-10 の範囲を意識的に分散させる（特にPackage D は低スコア必須）
- evidence_quote と evidence_source を必ず記載

完了後、追加件数を sqlite3 で確認し報告。
EOF
}

case "${1:-help}" in
  status)
    echo "=== Phase 6 補正進捗 ==="
    echo "achievers Phase 6 由来:"
    sqlite3 "$DB" "SELECT correction_phase, COUNT(*) FROM achievers WHERE correction_phase IS NOT NULL GROUP BY correction_phase"
    echo ""
    echo "source_team 別:"
    sqlite3 "$DB" "SELECT source_team, COUNT(*) FROM achievers WHERE source_team LIKE 'codex_correction_%' GROUP BY source_team ORDER BY 2 DESC"
    ;;

  dry-run)
    echo "=== 30タスクプレビュー ==="
    for i in "${!TASKS[@]}"; do
      IFS='|' read -r ph th tg ds <<< "${TASKS[$i]}"
      printf "%2d. [%s] %-25s (+%4s) — %s\n" "$((i+1))" "$ph" "$th" "$tg" "$ds"
    done
    ;;

  launch)
    cat_idx="${2:-1}"
    if [ "$cat_idx" -lt 1 ] || [ "$cat_idx" -gt 30 ]; then
      echo "Error: タスク番号は1-30"; exit 1
    fi
    task="${TASKS[$((cat_idx - 1))]}"
    IFS='|' read -r ph th tg ds <<< "$task"
    log="$LOG_DIR/p6_${ph}_${th}_$(date +%Y%m%d-%H%M%S).log"
    echo "[起動 #$cat_idx] Package $ph / $th → $log"
    prompt_template "$ph" "$th" "$tg" "$ds" | "$CODEX" exec --sandbox workspace-write --skip-git-repo-check > "$log" 2>&1 &
    echo "PID: $! / Log: $log"
    echo "$!" >> "$LOG_DIR/active_pids.txt"
    ;;

  launch_b)
    echo "=== Package B: politics 過半数解消 (8並列) ==="
    for i in {1..8}; do $0 launch $i; sleep 2; done
    ;;

  launch_c)
    echo "=== Package C: 女性活躍者 (6並列) ==="
    for i in {9..14}; do $0 launch $i; sleep 2; done
    ;;

  launch_f)
    echo "=== Package F: L2 ソース多様化 (6並列) ==="
    for i in {15..20}; do $0 launch $i; sleep 2; done
    ;;

  launch_e)
    echo "=== Package E: L4 機関多様化 (4並列) ==="
    for i in {21..24}; do $0 launch $i; sleep 2; done
    ;;

  launch_g)
    echo "=== Package G: 学術文献 (3並列) ==="
    for i in {25..27}; do $0 launch $i; sleep 2; done
    ;;

  launch_d)
    echo "=== Package D: 低スコア人物 (3並列) ==="
    for i in {28..30}; do $0 launch $i; sleep 2; done
    ;;

  launch_all)
    echo "=== 全30並列段階起動 ==="
    $0 launch_b; sleep 30
    $0 launch_c; sleep 30
    $0 launch_f; sleep 30
    $0 launch_e; sleep 15
    $0 launch_g; sleep 15
    $0 launch_d
    ;;

  *)
    cat <<HELP
Phase 6 補正タスクランチャー

Usage:
  $0 status           # 進捗
  $0 dry-run          # 30タスクプレビュー
  $0 launch <1-30>    # 単独タスク
  $0 launch_b         # Package B (politics解消, 8並列)
  $0 launch_c         # Package C (女性追加, 6並列)
  $0 launch_f         # Package F (L2多様化, 6並列)
  $0 launch_e         # Package E (L4機関, 4並列)
  $0 launch_g         # Package G (学術文献, 3並列)
  $0 launch_d         # Package D (低スコア, 3並列)
  $0 launch_all       # 全30タスク段階起動
HELP
    ;;
esac

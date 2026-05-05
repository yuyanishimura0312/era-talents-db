#!/bin/bash
# Era Talents DB - 35並列Codex体制（Phase 2.5 拡張収集）
# academic-db-builder オーケストレーター下での大規模並列実行
#
# 使い方:
#   ./codex_team35_launch.sh status         # 進捗確認
#   ./codex_team35_launch.sh dry-run        # 35タスクのプレビュー
#   ./codex_team35_launch.sh launch <1-35>  # 単独タスク起動
#   ./codex_team35_launch.sh launch_wave1   # Wave1: 12並列起動（明治・大正・昭和前期 4分野×3時代）
#   ./codex_team35_launch.sh launch_wave2   # Wave2: 12並列起動（昭和後期・平成・令和 4分野×3時代）
#   ./codex_team35_launch.sh launch_wave3   # Wave3: 11並列起動（L1/L2拡張・関係・専門深化）
#   ./codex_team35_launch.sh launch_all     # 全35並列起動（要確認）

set -e

PROJECT_DIR="$HOME/projects/research/era-talents-db"
DB="$PROJECT_DIR/data/era_talents.db"
LOG_DIR="$PROJECT_DIR/phase2_collection/logs"
CHECKLIST="$PROJECT_DIR/phase1_scoping/must_have_checklist.md"
PLAN="$PROJECT_DIR/phase0_planning/integrated_foundation_plan.md"
CODEX="/opt/homebrew/bin/codex"

mkdir -p "$LOG_DIR"

# 35タスク定義（era_id|domain|target_add|description）
declare -a TASKS=(
  # === Wave 1: 明治・大正・昭和前期の分野別深化（12タスク） ===
  "meiji|business|100|明治期の実業家・企業家を多分野深化（地方銀行創業者・産業創始者・女性起業家）"
  "meiji|science_tech|80|明治期の科学技術者・在野研究者・発明家・職人技術者"
  "meiji|culture_arts|100|明治期の文化芸術（文学・美術・音楽・伝統芸能・大衆芸能）"
  "meiji|education_thought|80|明治期の教育者・思想家・宗教家・現場教師"

  "taisho|business|80|大正期の実業家・新興産業家・モダニズム企業家"
  "taisho|culture_arts|100|大正期の文化芸術（白樺派・モダニズム・大衆芸術・新劇）"
  "taisho|social_movement|80|大正期の社会運動家・労働運動・女性運動・自由教育"
  "taisho|local_craft|60|大正期の地域実践家・職人・工芸家・人間国宝予備"

  "showa_pre|business|100|昭和前期の実業家・戦時体制下の企業家・産業界リーダー"
  "showa_pre|science_tech|80|昭和前期の科学技術者（湯川秀樹世代・原子物理・基礎科学）"
  "showa_pre|culture_arts|100|昭和前期の文化芸術（戦前文学・映画・建築・写真）"
  "showa_pre|social_movement|60|昭和前期の社会運動・抵抗運動・女性活動家"

  # === Wave 2: 昭和後期・平成・令和の分野別深化（12タスク） ===
  "showa_post|business|150|昭和後期の実業家（高度成長期・バブル期・在野経営者・地方創業者）"
  "showa_post|science_tech|100|昭和後期の科学技術者・ノーベル賞受賞者・在野発明家"
  "showa_post|sports|80|昭和後期のスポーツ（プロ野球・大相撲・五輪選手・在野指導者）"
  "showa_post|media_journalism|80|昭和後期のメディア・ジャーナリスト・編集者・キャスター"

  "heisei|business|200|平成期の実業家（IT起業家・スタートアップ・地方創業者）"
  "heisei|science_tech|150|平成期の科学技術者（iPS関連・宇宙・AI・量子）"
  "heisei|culture_arts|150|平成期の文化芸術（村上春樹世代・宮崎駿・アニメ・現代美術・音楽）"
  "heisei|sports|100|平成期のスポーツ（イチロー世代・サッカー・五輪・パラ五輪）"

  "reiwa|business|100|令和期のスタートアップ・SaaS創業者・SDGs起業家・地域起業家"
  "reiwa|science_tech|80|令和期のAI研究者・量子計算・宇宙・気候変動研究者"
  "reiwa|culture_arts|80|令和期の文化芸術（米津玄師世代・新海誠・現代アート）"
  "reiwa|social_movement|60|令和期の社会運動・市民活動・NPO第二世代・環境運動"

  # === Wave 3: 横断・深化・関係構築（11タスク） ===
  "all|women_pioneers|200|全時代の女性パイオニア（医師・研究者・起業家・芸術家）追加収集"
  "all|local_excellent|200|全時代の無名の卓越者（地域指導者・職人・人間国宝・地方創業者）"
  "all|religion_thought|100|全時代の宗教家・思想家・哲学者の体系拡張"
  "all|education_practice|100|全時代の教育実践家（現場教師・校長・教育改革者）"
  "all|diaspora_ainu_okinawa|80|全時代の在日コリアン・在日中国人実業家・アイヌ・沖縄リーダー"

  "discourse|expand|500|L1当時言説の追加（明治～令和の教育白書・経団連歴代提言・修身教科書詳細）"
  "retrospective|expand|300|L2事後評価の拡張（教育社会学・歴史社会学・経営史の主要研究）"

  "future|scenarios_2030|50|L4 2030年の追加シナリオ深化（AI/気候/地政学分岐の能力差）"
  "future|scenarios_2050|50|L4 2050年の追加シナリオ深化（ポスト成長・気候/AI複合）"
  "future|scenarios_2100|50|L4 2100年の超長期予測追加（宇宙/ポストヒューマン/生態文明）"

  "verification|quality|0|全DBの整合性検証・ハルシネーション検出・重複統合・時代分類確認"
)

prompt_template() {
  local era_id="$1"
  local domain="$2"
  local target_add="$3"
  local desc="$4"

  cat <<EOF
あなたは「時代別活躍人材DB」構築チームのCodexエージェントです。
academic-db-builder オーケストレーター下で35並列体制の1タスクを担当します。

【プロジェクト基盤】
基礎計画: $PLAN
チェックリスト: $CHECKLIST
DB: $DB

【今回の担当】
時代/層: $era_id
ドメイン: $domain
追加目標: $target_add 件
説明: $desc

【参照スキーマ】
sqlite3 $DB ".schema achievers"
sqlite3 $DB ".schema era_discourses"
sqlite3 $DB ".schema era_retrospectives"
sqlite3 $DB ".schema future_demands"
sqlite3 $DB ".schema academic_references"
sqlite3 $DB "SELECT id, name_ja FROM capability_dimensions"

【作業フロー】
1. 既存データの確認:
   sqlite3 $DB "SELECT name_ja, domain FROM achievers WHERE primary_era_id='$era_id' AND domain LIKE '%$domain%'"
2. 重複しないように、未登録の人物・言説・予測を $target_add 件追加
3. 50件ずつバッチINSERTし、COUNTで確認しながら進める

【ドメイン別の追加方針】
- business: 大手企業創業者だけでなく、町工場・地方創業者・女性起業家も含める
- science_tech: アカデミックだけでなく、在野研究者・発明家・職人技術者も含める
- culture_arts: メインストリームだけでなく、伝統芸能・大衆文化・サブカルチャーも含める
- sports: スター選手だけでなく、コーチ・指導者・在野アスリートも含める
- social_movement: 著名活動家だけでなく、地域実践者・現場リーダーも含める
- women_pioneers: 各時代の医師・研究者・起業家・芸術家・教育者の女性
- local_excellent: 教科書に載らないが地域や業界で決定的影響を与えた人物
- diaspora_ainu_okinawa: 在日コリアン・中国人実業家・アイヌ・沖縄の文化指導者

【$era_id == discourse の場合】
era_discourses テーブルに、各時代の能力に関する言説を $target_add 件追加。
discourse_type: education_decree | curriculum | business_proposal | social_commentary | textbook | white_paper
ソース例: 教育勅語の解釈、修身教科書（戦前6学年）、学習指導要領（1947-2017全版）、
  経団連歴代提言（1962-現在の代表的提言20+）、経済同友会、文部省/文科省白書、
  福澤諭吉以降の教育思想、大正自由教育論、戦後民主教育、ゆとり教育答申、
  Society 5.0人材像、未来人材ビジョン2022、生涯学習答申

【$era_id == retrospective の場合】
era_retrospectives テーブルに、現代から振り返った各時代の能力評価を $target_add 件追加。
ソース例: 竹内洋『日本のメリトクラシー』『教養主義の没落』、苅谷剛彦『階層化日本』、
  Bourdieu文化資本、Merton マタイ効果、丸山眞男『日本の思想』、見田宗介、
  橋本治、宮本又郎経営史、Chandler産業組織論、Zuckerman科学エリート、
  社会学評論・教育社会学研究の主要論文（最低50本）

【$era_id == future の場合】
future_demands テーブルに、対象年代の能力予測を $target_add 件追加。
シナリオ: baseline / ssp1-5 / post_growth / posthuman / ai_singularity / space_civilization 等
ソース: OECD/WEF/McKinsey/IPCC/UN/JAXA/Long Now/Effective Altruism

【$era_id == verification の場合】
品質検証タスク。以下を実行:
1. 同名人物の重複検出: SELECT name_ja, COUNT(*) FROM achievers GROUP BY name_ja HAVING COUNT(*)>1
2. 時代整合性: SELECT name_ja, birth_year, primary_era_id FROM achievers WHERE
   (primary_era_id='meiji' AND birth_year > 1880) で異常値を検出
3. ハルシネーション疑い: source_url が空・実在不明な人物のフラグ付与
4. 結果を /Users/nishimura+/projects/research/era-talents-db/reports/verification_log.md に記録

【厳守ルール】
1. 重複チェック必須: INSERT前に SELECT 1 FROM achievers WHERE name_ja=? AND birth_year=?
2. 偉人偏重を避ける: is_traditional_great=1 は40%以下、残りは無名・地域・女性
3. 実在確認: 国立国会図書館/Wikipedia/業界DB等で検証可能な人物のみ
4. ハルシネーション禁止: 架空人物・時代錯誤を絶対に避ける
5. source_team='codex_${era_id}_${domain}' を必ず設定
6. 完了後、件数を sqlite3 で確認し報告

【能力スコアリング（achievers テーブルへの追加投入時）】
追加した人物について、achiever_capabilities テーブルにも能力スコアを投入:
各人物の最も顕著な能力次元を3-5個選び、score (1-10) と evidence_quote を記録。

完了後、最終件数を sqlite3 で確認し、簡潔に報告してください。
EOF
}

case "${1:-help}" in
  status)
    echo "=== Era Talents DB Phase 2.5 進捗 ==="
    echo ""
    echo "[活躍人材]"
    sqlite3 "$DB" "SELECT primary_era_id, COUNT(*) FROM achievers GROUP BY primary_era_id ORDER BY primary_era_id"
    echo ""
    echo "[層別]"
    echo "L1 言説: $(sqlite3 "$DB" "SELECT COUNT(*) FROM era_discourses")"
    echo "L2 事後評価: $(sqlite3 "$DB" "SELECT COUNT(*) FROM era_retrospectives")"
    echo "L4 未来予測: $(sqlite3 "$DB" "SELECT COUNT(*) FROM future_demands")"
    echo "学術文献: $(sqlite3 "$DB" "SELECT COUNT(*) FROM academic_references")"
    echo ""
    achievers=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achievers")
    cap=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achiever_capabilities")
    echo "活躍人材: $achievers / 8,000 (Phase2.5目標)"
    echo "能力スコア: $cap / 25,000"
    ;;

  dry-run)
    echo "=== 35並列タスクプレビュー ==="
    for i in "${!TASKS[@]}"; do
      IFS='|' read -r era domain target desc <<< "${TASKS[$i]}"
      printf "%2d. %-12s | %-20s | +%4s — %s\n" "$((i+1))" "$era" "$domain" "$target" "$desc"
    done
    ;;

  launch)
    cat_idx="${2:-1}"
    if [ "$cat_idx" -lt 1 ] || [ "$cat_idx" -gt 35 ]; then
      echo "Error: タスク番号は1-35"
      exit 1
    fi
    task="${TASKS[$((cat_idx - 1))]}"
    IFS='|' read -r era domain target desc <<< "$task"
    log="$LOG_DIR/w35_${era}_${domain}_$(date +%Y%m%d-%H%M%S).log"
    echo "[起動 #$cat_idx] $era / $domain → $log"
    prompt_template "$era" "$domain" "$target" "$desc" | "$CODEX" exec --sandbox workspace-write --skip-git-repo-check > "$log" 2>&1 &
    echo "PID: $! / Log: $log"
    echo "$!" >> "$LOG_DIR/active_pids_w35.txt"
    ;;

  launch_wave1)
    echo "=== Wave 1: 明治・大正・昭和前期 12並列起動 ==="
    for i in {1..12}; do
      $0 launch $i
      sleep 2
    done
    ;;

  launch_wave2)
    echo "=== Wave 2: 昭和後期・平成・令和 12並列起動 ==="
    for i in {13..24}; do
      $0 launch $i
      sleep 2
    done
    ;;

  launch_wave3)
    echo "=== Wave 3: 横断・深化・関係 11並列起動 ==="
    for i in {25..35}; do
      $0 launch $i
      sleep 2
    done
    ;;

  launch_all)
    echo "=== 警告: 35並列起動はAPI消費が極めて大きいです ==="
    read -p "続行しますか？ (yes/no): " confirm
    [ "$confirm" != "yes" ] && exit 0
    echo ""
    echo "=== 段階的起動: Wave1 → 30秒 → Wave2 → 30秒 → Wave3 ==="
    $0 launch_wave1
    sleep 30
    $0 launch_wave2
    sleep 30
    $0 launch_wave3
    ;;

  kill_all)
    echo "=== 35並列ジョブを全停止 ==="
    if [ -f "$LOG_DIR/active_pids_w35.txt" ]; then
      while read pid; do
        kill "$pid" 2>/dev/null && echo "Killed: $pid"
      done < "$LOG_DIR/active_pids_w35.txt"
      mv "$LOG_DIR/active_pids_w35.txt" "$LOG_DIR/active_pids_w35.txt.$(date +%s)"
    fi
    ;;

  *)
    cat <<HELP
Era Talents DB - 35並列Codex体制（Phase 2.5）

Usage:
  $0 status            # 進捗確認
  $0 dry-run           # 35タスクのプレビュー
  $0 launch <1-35>     # 単独タスク起動
  $0 launch_wave1      # Wave1: 12並列（明治・大正・昭和前期）
  $0 launch_wave2      # Wave2: 12並列（昭和後期・平成・令和）
  $0 launch_wave3      # Wave3: 11並列（横断・深化・関係）
  $0 launch_all        # 全35並列段階起動（要確認）
  $0 kill_all          # 全ジョブ停止

35タスク:
HELP
    for i in "${!TASKS[@]}"; do
      IFS='|' read -r era domain target desc <<< "${TASKS[$i]}"
      printf "  %2d. %-12s | %-20s | +%4s — %s\n" "$((i+1))" "$era" "$domain" "$target" "$desc"
    done
    ;;
esac

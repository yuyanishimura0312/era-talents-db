#!/bin/bash
# Era Talents DB - Codex並列収集ランチャー
# 目的: 6時代×多分野で活躍人材データを並列収集
#
# 使い方:
#   ./codex_parallel_launch.sh status          # 進捗確認
#   ./codex_parallel_launch.sh dry-run         # 全カテゴリ目標プレビュー
#   ./codex_parallel_launch.sh launch <1-8>    # 単独カテゴリ起動（バックグラウンド）
#   ./codex_parallel_launch.sh launch_core     # コア4並列起動（推奨スタート）
#   ./codex_parallel_launch.sh launch_all      # 8並列起動（API消費大、確認あり）

set -e

PROJECT_DIR="$HOME/projects/research/era-talents-db"
DB="$PROJECT_DIR/data/era_talents.db"
LOG_DIR="$PROJECT_DIR/phase2_collection/logs"
CHECKLIST="$PROJECT_DIR/phase1_scoping/must_have_checklist.md"
PLAN="$PROJECT_DIR/phase0_planning/integrated_foundation_plan.md"
CODEX="/opt/homebrew/bin/codex"

mkdir -p "$LOG_DIR"

# 8並列タスク定義 ── era_id:target:description
declare -a CATEGORIES=(
  "meiji:460:明治期(1868-1912)の活躍人材を多分野で収集"
  "taisho:360:大正期(1912-1926)の活躍人材を多分野で収集"
  "showa_pre:410:昭和前期(1926-1945)の活躍人材を多分野で収集"
  "showa_post:680:昭和後期(1946-1989)の活躍人材を多分野で収集"
  "heisei:660:平成期(1989-2019)の活躍人材を多分野で収集"
  "reiwa:450:令和期(2019-)の活躍人材を多分野で収集"
  "discourse_l1:300:全時代の当時の能力言説（教育勅語・経団連提言・修身教科書等）"
  "retrospective_l2:200:全時代の事後評価（歴史社会学・教育学・伝記研究）"
)

prompt_template() {
  local era_id="$1"
  local target="$2"
  local desc="$3"
  local current=0
  if [ "$era_id" = "discourse_l1" ]; then
    current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM era_discourses" 2>/dev/null || echo 0)
  elif [ "$era_id" = "retrospective_l2" ]; then
    current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM era_retrospectives" 2>/dev/null || echo 0)
  else
    current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achievers WHERE primary_era_id='$era_id'" 2>/dev/null || echo 0)
  fi
  local needed=$((target - current))

  cat <<EOF
あなたは「時代別活躍人材DB」構築エージェントです。

【プロジェクト概要】
日本の明治〜令和の各時代に「求められた力」と「実際に活躍した人物」を収集する大規模学術DB。
基礎計画: $PLAN
チェックリスト: $CHECKLIST
DB: $DB

【今回の担当】
カテゴリ: $era_id ($desc)
現在件数: $current 件
目標: $target 件（残 $needed 件を新規追加）

【参照スキーマ】
sqlite3 $DB ".schema achievers"
sqlite3 $DB ".schema era_discourses"
sqlite3 $DB ".schema era_retrospectives"
sqlite3 $DB ".schema capability_dimensions"

【作業フロー】
1. 既存登録の確認: sqlite3 $DB "SELECT name_ja FROM achievers WHERE primary_era_id='$era_id'"
2. チェックリスト($CHECKLIST)の該当時代セクションを必ず読み、未登録人物を最優先で投入
3. その後、無名の卓越者・地域実践者・職人・女性活躍者を意識的に拡張
4. 50件ずつバッチでINSERT → COUNT確認 → 次バッチ

【人物データ収集（achievers テーブル）】
必須フィールド: name_ja, primary_era_id='$era_id', domain, achievement_summary
推奨フィールド: name_en, name_kana, birth_year, death_year, birth_place,
  sub_domain, notable_works (JSON配列), family_class, education_path,
  mentors (JSON配列), is_traditional_great (0 or 1),
  is_local_excellent (0 or 1), source_team='codex_${era_id}',
  source_url

【能力スコアリング（achiever_capabilities テーブル）】
各人物について、最も顕著な能力次元を3-5個選び、score (1-10) と
evidence_quote/evidence_source を記録。
利用可能な能力ID: sqlite3 $DB "SELECT id, name_ja FROM capability_dimensions"

【厳守ルール】
1. 同名人物の重複チェック: INSERT前に SELECT 1 FROM achievers WHERE name_ja=? AND birth_year=?
2. 偉人偏重を避ける: is_traditional_great=1 は40%以下、残りは無名の卓越者・女性・地域人材
3. 多分野バランス: 政治・実業・科学・文化・教育・社会運動・スポーツ・地域・職人・女性横断を意識
4. 実在確認: 国立国会図書館/Wikipedia/人事興信録DB等で検証可能な人物のみ
5. 生没年記載必須（不明な場合のみNULL可、ただし時代整合性チェック）
6. ハルシネーション禁止: 架空人物・時代錯誤を避ける

【$era_id == discourse_l1 の場合の特別指示】
era_discourses テーブルに各時代の「求められた能力に関する言説」を投入。
discourse_type: education_decree | curriculum | business_proposal | social_commentary | textbook
9時代×複数能力次元×複数ソース=300件目標。
ソース例: 教育勅語、福澤諭吉、修身教科書、学習指導要領歴代、経団連歴代提言、
  経済同友会、大正デモクラシー論考、ゆとり教育答申、Society 5.0人材像、未来人材ビジョン

【$era_id == retrospective_l2 の場合の特別指示】
era_retrospectives テーブルに「現代から振り返った各時代の能力評価」を投入。
ソース例: 竹内洋『日本のメリトクラシー』、苅谷剛彦『階層化日本』、
  Bourdieu文化資本、Merton マタイ効果、丸山眞男、宮本又郎経営史、
  社会学評論、教育社会学研究の主要論文

【完了報告】
最終件数を sqlite3 で確認し、報告してください。
EOF
}

case "${1:-help}" in
  status)
    echo "=== Era Talents DB 進捗 ==="
    echo ""
    echo "[活躍人材 by 時代]"
    sqlite3 "$DB" "SELECT primary_era_id, COUNT(*) FROM achievers GROUP BY primary_era_id ORDER BY primary_era_id"
    echo ""
    echo "[当時言説 L1 / 事後評価 L2]"
    echo "L1: $(sqlite3 "$DB" "SELECT COUNT(*) FROM era_discourses")"
    echo "L2: $(sqlite3 "$DB" "SELECT COUNT(*) FROM era_retrospectives")"
    echo "L4: $(sqlite3 "$DB" "SELECT COUNT(*) FROM future_demands")"
    echo ""
    total=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achievers")
    cap=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achiever_capabilities")
    echo "活躍人材総数: $total / 3,020（Phase2目標）"
    echo "能力スコア: $cap"
    ;;

  dry-run)
    echo "=== カテゴリ別目標プレビュー ==="
    for cat in "${CATEGORIES[@]}"; do
      IFS=':' read -r era target desc <<< "$cat"
      if [ "$era" = "discourse_l1" ]; then
        current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM era_discourses")
      elif [ "$era" = "retrospective_l2" ]; then
        current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM era_retrospectives")
      else
        current=$(sqlite3 "$DB" "SELECT COUNT(*) FROM achievers WHERE primary_era_id='$era'")
      fi
      printf "  %-20s 現在 %4d / 目標 %4d  (残 %4d) — %s\n" "$era" "$current" "$target" "$((target - current))" "$desc"
    done
    ;;

  launch)
    cat_idx="${2:-1}"
    if [ "$cat_idx" -lt 1 ] || [ "$cat_idx" -gt 8 ]; then
      echo "Error: カテゴリ番号は1-8"
      exit 1
    fi
    cat="${CATEGORIES[$((cat_idx - 1))]}"
    IFS=':' read -r era target desc <<< "$cat"
    log="$LOG_DIR/${era}_$(date +%Y%m%d-%H%M%S).log"
    echo "[起動] $era → $log"
    prompt_template "$era" "$target" "$desc" | "$CODEX" exec --full-auto > "$log" 2>&1 &
    echo "PID: $! / Log: $log"
    echo "$!" >> "$LOG_DIR/active_pids.txt"
    ;;

  launch_core)
    echo "=== コア4並列起動: 明治・昭和後期・平成・L1当時言説 ==="
    echo "（残り4並列はlaunch_allで後追加）"
    for i in 1 4 5 7; do
      $0 launch $i
      sleep 3
    done
    echo ""
    echo "=== 起動完了 ==="
    echo "ログ監視: tail -f $LOG_DIR/*.log"
    echo "進捗確認: $0 status"
    ;;

  launch_all)
    echo "=== 警告: 8並列起動はAPI消費大 ==="
    read -p "続行しますか？ (yes/no): " confirm
    [ "$confirm" != "yes" ] && exit 0
    for i in {1..8}; do
      $0 launch $i
      sleep 5
    done
    ;;

  kill_all)
    echo "=== 全Codexジョブを停止 ==="
    if [ -f "$LOG_DIR/active_pids.txt" ]; then
      while read pid; do
        kill "$pid" 2>/dev/null && echo "Killed: $pid"
      done < "$LOG_DIR/active_pids.txt"
      mv "$LOG_DIR/active_pids.txt" "$LOG_DIR/active_pids.txt.$(date +%s)"
    fi
    ;;

  *)
    cat <<HELP
Era Talents DB - Codex Parallel Launcher

Usage:
  $0 status            # 進捗確認
  $0 dry-run           # 各カテゴリの目標と残件数
  $0 launch <1-8>      # 単独カテゴリ起動（バックグラウンド）
  $0 launch_core       # コア4並列（明治・昭和後期・平成・L1当時言説）
  $0 launch_all        # 全8並列（要確認）
  $0 kill_all          # 全ジョブ停止

Categories:
HELP
    for i in "${!CATEGORIES[@]}"; do
      IFS=':' read -r era target desc <<< "${CATEGORIES[$i]}"
      printf "  %d. %-20s (目標 %4d) — %s\n" "$((i+1))" "$era" "$target" "$desc"
    done
    ;;
esac

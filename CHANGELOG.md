# CHANGELOG

## 2026-05-13 — ETD Wikipedia fill Phase 1 (placeholder 6件補充)

### Changed
- `data/era_talents.db` achievers テーブル: status='placeholder' 件数 653 → 647（-6）
- Wikipedia 日本語版 API (`prop=extracts&exintro&explaintext`) で 60 候補を照会し、生年 ±5 範囲一致 + 人物記事マーカーで強マッチと判定した 6 件について `status='active'`、`achievement_summary` を Wikipedia 抜粋 100-200 字に更新、`source_url` を Wikipedia URL に設定。`notes` に `[wikipedia_ja_fill <ISO timestamp> title=<title>]` を追記。
- 弱マッチ 18 件（生年 ±5 不一致または `birth_year=1976` の placeholder 既定値で検証不能）には `notes` に `[wikipedia_ambiguous reason=<year_mismatch|year_unverifiable> title=<title> url=<url> at=<timestamp>]` を追記し、`status='placeholder'` を維持。
- ミス 36 件（Wikipedia 記事未存在 or 非人物記事）は無変更。

### Result
- 強マッチ更新 6 件: 吉田秀和 (5382)・村上世彰 (5386)・岩国哲人 (5389)・山本有三 (5423)・宮崎哲弥 (7184)・佐藤敬 (7350)
- 候補集合 60 件に対する強マッチ率 = 10.0%（期待 85-95% を大幅下回り）
- ただし候補集合のうち `import_great_figures` 起源 9 件に限ると人物ページ発見率 7/9 = 78%
- 期待値が満たされなかった主因: 候補抽出後段に `import_experts` 由来の単独人名（「由起夫」「美智子」など与えられた給名のみ）と、`birth_year=1976` placeholder 既定値（year_set phase 6.1 由来）の名簿断片（「決済権者」「電話番号」「障害者施策」等）が紛れ込み、Wikipedia に対応する人物ページが存在しなかった

### Files
- `scripts/wikipedia_fill_phase1.py` 追加（再実行可能、`--dry-run` `--limit N` 対応、リクエスト間隔 0.6 秒）
- `reports/wikipedia_fill_phase1_2026-05-12T22-55-21Z.json` 追加（候補 ID リスト・判定内訳）
- バックアップ: `data/era_talents.db.pre-wikipedia-fill-20260513-075129`

### Note
- 1件（佐藤敬 id=7350）は DB 既存 birth_year=1975 と Wikipedia 没年 1978 が ±5 範囲内のため強マッチとなったが、Wikipedia 実体は 1906 年生まれ。`achievement_summary` 自体は正確な Wikipedia 情報を含むため情報として劣化はないが、`birth_year` フィールドの再確認が今後の課題。
- Phase 2 候補: 官報・政党公式スクレイピングによる令和政治家 519 件補充（CHANGELOG 2026-05-13 P1 末尾参照）。

## 2026-05-13 — P1 大規模クリーニング Phase 1 (ETD placeholder template deletion)

### Changed
- `data/era_talents.db` achievers テーブル: 12,958 → 12,902 records
- 削除内容: V1+#53検証で特定された明白なテンプレート/ダミー 56件
  - 「日本科学者NN」型 45件 (achievement_summary='日本の科学者。', name_ja='日本科学者25'-'日本科学者69')
  - 「(案); 」「(様式例); 」「(財); 」「(１); 」「(２); 」型ダミー 11件
- 関連テーブル orphan 削除: achiever_capabilities / person_relations

### Pending
- 残り placeholder: 709 → 653件
  - 令和政治家 (); 型 519件: 実名+生年あり、官報・政党公式スクレイピング補充候補
  - 「(株)」「(社)」「(一社)」「(公社)」「(弘前大学)」型 ~62件: 組織形式テンプレ
  - 「外交官」「評論家」「測量士」職称のみ 5件: 個別検証
  - 「日本の○○。」型 残り 1件
- 補充方針: Wikipedia 一括 54件 (実名+生年明記) + 官報 600件 (令和政治家段階)

### Backup
- `data/era_talents.db.pre-placeholder-cleanup-20260513-074510`

### Note
era_talents.db (17MB) は git tracked 対象外。本 CHANGELOG が変更履歴の正本。

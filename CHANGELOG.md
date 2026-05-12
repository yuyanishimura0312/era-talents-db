# CHANGELOG

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

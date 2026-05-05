# verification quality log

検証日時: 2026-05-05 13:01:20 JST

担当: verification / quality  
担当チーム識別子: codex_verification_quality  
追加投入: 0 件

## 実行範囲

全DBについて、以下を中心に整合性検証を実施した。

- `achievers` の同名重複検出
- `achievers` の時代分類と生没年整合性チェック
- `source_url` 欠落および検証可能性の確認
- 外部キー相当の参照整合性チェック
- 能力スコア紐付け、偉人偏重率、補助テーブル件数の確認

DBは並列更新中の可能性があり、検証中に `meiji` の件数が 460 件から 510 件へ変化した。以下の数値は上記検証日時近辺のスナップショットである。

## 最終件数スナップショット

### achievers

総件数: 3,270 件

| primary_era_id | 件数 |
|---|---:|
| heisei | 660 |
| meiji | 510 |
| reiwa | 450 |
| retrospective_l2 | 200 |
| showa_post | 680 |
| showa_pre | 410 |
| taisho | 360 |

`retrospective_l2` は `eras` テーブルに存在しないため、`achievers.primary_era_id` としては参照整合性違反である。L2事後評価は本来 `era_retrospectives` に格納する設計のため、200件は移行または分類修正候補。

### 関連テーブル

| table | 件数 |
|---|---:|
| achiever_capabilities | 9,973 |
| era_discourses | 300 |
| era_retrospectives | 36 |
| future_demands | 247 |
| academic_references | 40 |
| gap_insights | 0 |
| collection_progress | 1 |

`achiever_capabilities` は孤立レコード 0 件、能力未付与の `achievers` 0 件で、人物と能力スコアの紐付けは全件存在する。

## 主要検証結果

### 1. 同名人物の重複検出

実行SQL:

```sql
SELECT name_ja, COUNT(*)
FROM achievers
GROUP BY name_ja
HAVING COUNT(*) > 1;
```

結果:

- 同名重複グループ: 282
- 同一 `name_ja + birth_year` 重複グループ: 58
- 同名重複グループに属する行: 573

上位例:

| name_ja | n | ids | eras |
|---|---:|---|---|
| 上野千鶴子 | 3 | 229,2575,3112 | reiwa,heisei,showa_post |
| 利根川進 | 3 | 129,2853,3106 | reiwa,retrospective_l2,showa_post |
| 坂本龍一 | 3 | 188,2669,3111 | reiwa,heisei,showa_post |
| 孫正義 | 3 | 31,2443,3105 | reiwa,heisei,showa_post |
| 宮崎駿 | 3 | 163,2636,3110 | reiwa,heisei,showa_post |
| 村上春樹 | 3 | 189,2603,3109 | reiwa,heisei,showa_post |
| 永守重信 | 3 | 94,2450,3104 | reiwa,heisei,showa_post |
| 田中耕一 | 3 | 128,2857,3108 | reiwa,retrospective_l2,showa_post |
| 野依良治 | 3 | 130,2854,3107 | reiwa,retrospective_l2,showa_post |

判定:

- 多くは時代横断の継続活躍・再評価として登録された可能性が高い。
- ただし `name_ja + birth_year` が同一で、同一人物が複数時代に重複登録されているケースは、分析時の二重計上リスクが高い。
- 統合方針として、人物本体は1行に寄せ、複数時代性は `secondary_era_id`、別テーブル、または人物時代関連テーブルで表現するのが望ましい。
- 今回は機械的削除は実施していない。理由は、時代横断登録が意図的である可能性があり、削除すると各時代チームの投入意図を破壊するため。

### 2. 時代整合性

指定SQL:

```sql
SELECT name_ja, birth_year, primary_era_id
FROM achievers
WHERE primary_era_id = 'meiji' AND birth_year > 1880;
```

結果: 29 件

該当例:

| id | name_ja | birth_year | primary_era_id | domain |
|---:|---|---:|---|---|
| 1223 | 五島慶太 | 1882 | meiji | business |
| 1410 | 有島生馬 | 1882 | meiji | culture_arts |
| 1444 | 青木繁 | 1882 | meiji | culture_arts |
| 1482 | 北一輝 | 1883 | meiji | social_movement |
| 1271 | 大賀一郎 | 1883 | meiji | science |
| 1407 | 志賀直哉 | 1883 | meiji | culture_arts |
| 1416 | 高村光太郎 | 1883 | meiji | culture_arts |
| 1510 | 金栗四三 | 1891 | meiji | sports |
| 1405 | 佐藤春夫 | 1892 | meiji | culture_arts |
| 1511 | 西竹一 | 1902 | meiji | sports |

判定:

- 明治期に成人前または活動前の人物が含まれている。特に西竹一（1902年生）は明治の主活動人物とは言いにくく、昭和前期などへの修正候補。
- 文学・思想では明治末から大正にまたがる人物が多く、`taisho` への移行または `secondary_era_id` での表現が妥当なケースがある。

追加チェック:

- 死亡年が時代開始年より前: 1 件

| id | name_ja | birth_year | death_year | primary_era_id | domain |
|---:|---|---:|---:|---|---|
| 1348 | 広瀬淡窓 | 1782 | 1856 | meiji | education |

判定:

- 広瀬淡窓は明治開始前に没しており、`primary_era_id='meiji'` は時代錯誤。前近代影響人物として別扱いにするか、DB対象外にする必要がある。

### 3. ハルシネーション疑い・出典検証性

`achievers.source_url` 欠落:

- 空またはNULL: 0 件
- 非HTTP形式: 0 件

ただし、出典URLの粒度に問題あり:

- `https://www.ndl.go.jp/portrait/`: 449 件
- `https://meiji.bakumatsu.org/men/`: 11 件

判定:

- URL欄は埋まっているが、NDLの個別人物ページではなくトップまたは一覧ページ相当のURLが大量に入っているため、行単位の実在確認リンクとしては弱い。
- 明治チームの 460 件のうち、多数が同一のNDLルートURLであり、ハルシネーション検出には個別ページURL、NDL典拠ID、Wikidata ID、または個別資料名が必要。
- 現時点で `source_url` 欠落による即時フラグ対象はないが、「出典粒度不足」として明治データ449件を要再検証対象にする。

生年欠落:

- `birth_year IS NULL`: 1,976 件

内訳:

| primary_era_id | total | missing_birth | pct_missing_birth |
|---|---:|---:|---:|
| heisei | 660 | 610 | 92.4% |
| meiji | 510 | 3 | 0.6% |
| reiwa | 450 | 450 | 100.0% |
| retrospective_l2 | 200 | 0 | 0.0% |
| showa_post | 680 | 612 | 90.0% |
| showa_pre | 410 | 242 | 59.0% |
| taisho | 360 | 59 | 16.4% |

判定:

- 平成・令和・昭和後期は生年欠落率が高く、同名判定・時代整合性判定の精度が落ちる。
- 特に令和は全450件で生年が欠落しており、時代錯誤や同姓同名の検出に弱い。

### 4. 参照整合性

`achievers.primary_era_id` の `eras` 未登録値:

- 200 件
- 値: `retrospective_l2`

`era_discourses.era_id`, `era_retrospectives.era_id`, `future_demands.era_id` は全件 `eras` に存在。

`achiever_capabilities.capability_id` は全件 `capability_dimensions` に存在。

判定:

- `retrospective_l2` を `achievers.primary_era_id` として使うのはスキーマ上不整合。
- L2人物リストとして保持したい場合でも、時代IDではなく別のタグ列または別テーブルで管理するべき。

### 5. 偉人偏重率

全体:

- 総件数: 3,270
- `is_traditional_great=1`: 757
- 比率: 23.1%
- `is_local_excellent=1`: 2,164

判定:

- 全体では「偉人40%以下」ルールを満たしている。
- ただし平成 38.9%、令和 39.3% は上限に近い。今後の追加では無名・地域・女性・現場実践者を優先する必要がある。

## 修正優先度

高:

1. `retrospective_l2` の200件を `achievers.primary_era_id` から除去または正規の時代へ再分類する。
2. 広瀬淡窓の `primary_era_id='meiji'` を修正する。
3. 明治の `birth_year > 1880` 29件を確認し、主活動時代が大正・昭和前期の人物を移す。

中:

1. 同一 `name_ja + birth_year` 重複58グループを統合候補としてレビューする。
2. 明治データ449件のNDL URLを個別人物URLまたは典拠IDへ更新する。
3. 平成・令和・昭和後期の生年を補完し、同名・時代整合性チェックを可能にする。

低:

1. `gap_insights` が0件のため、L1/L2/L3/L4接続後に差分知見を追加する。
2. `academic_references` はURL列を持たないため、DOIや書誌情報の補完ルールを別途定義する。

## 今回のDB変更

人物・言説・予測の追加: 0 件  
重複削除・統合: 0 件  
DB本体のUPDATE: 0 件  
作成・更新した成果物: `reports/verification_log.md`

## 追補: 並列更新後の観測値

追補確認日時: 2026-05-05 13:03:00 JST 以降

本ログ作成直後にも他チームの追加投入が続き、DB件数が変化した。最終報告では下記の後続観測値を優先する。

### 後続観測件数

| table | 件数 |
|---|---:|
| achievers | 4,151 |
| achiever_capabilities | 12,646 |
| era_discourses | 800 |
| era_retrospectives | 36 |
| future_demands | 397 |
| academic_references | 40 |

`achievers` の後続観測内訳:

| primary_era_id | 件数 |
|---|---:|
| all | 100 |
| heisei | 710 |
| meiji | 649 |
| reiwa | 600 |
| retrospective_l2 | 200 |
| showa_post | 860 |
| showa_pre | 554 |
| taisho | 478 |

後続観測での追加注意点:

- `primary_era_id='all'` が100件出現した。その後 `eras` に横断的収集用の擬似時代IDとして追加されたため、最終観測時点では外部キー違反ではない。ただし時代別分析では通常時代と分離して扱う必要がある。
- `retrospective_l2` 200件は引き続き `eras` に存在しないため、`achievers.primary_era_id` の参照整合性違反。
- 死亡年が時代開始年より前の人物は3件に増加した。確認例: 黒住宗忠（1850年没、meiji）、広瀬淡窓（1856年没、meiji）、日下部四郎太（1924年没、showa_pre）。
- 同名重複グループは348件まで増加した。並列投入後の重複レビューを再実行する必要がある。

### 最終観測値

最終確認時点の `sqlite3` 観測値:

| table | 件数 |
|---|---:|
| achievers | 4,466 |
| achiever_capabilities | 14,056 |
| era_discourses | 800 |
| era_retrospectives | 36 |
| future_demands | 397 |
| academic_references | 40 |

`achievers` の最終観測内訳:

| primary_era_id | 件数 |
|---|---:|
| all | 180 |
| heisei | 714 |
| meiji | 650 |
| reiwa | 600 |
| retrospective_l2 | 200 |
| showa_post | 945 |
| showa_pre | 592 |
| taisho | 585 |

最終観測時点の要点:

- 同名重複グループ: 352
- `achievers.primary_era_id` の `eras` 未登録値: 200件、すべて `retrospective_l2`
- `achievers.source_url` 欠落: 0件

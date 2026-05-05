# Phase 3 監査レポート

**実行時刻**: 2026-05-05T13:08:34.396825

## 0. 監査前の総レコード数
- achievers: 9,731
- achiever_capabilities: 18,921
- era_discourses: 800
- era_retrospectives: 927
- future_demands: 397
- academic_references: 40

## 1. 不正era_id の削除/再配分
- 削除: 0 件 (codex_retrospective_l2由来)
- 再配分: 0 件 (all→生年から推定)

## 2. experts-db 由来データの時代再配分
- 再配分: 0 件 (任命年→推定生年→時代)

## 3. 同名重複の検出
- 重複名: 357 ケース

上位重複（マージ前）:
| 名前 | 件数 | 生年 | 時代 | source |
|---|---|---|---|---|
| 永守重信 | 3 | 1944,1944 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 村上春樹 | 3 | 1949,1949 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 宮崎駿 | 3 | 1941,1941 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 孫正義 | 3 | 1957,1957 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 坂本龍一 | 3 | 1952,1952 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 上野千鶴子 | 3 | 1948,1948 | reiwa,heisei,showa_post | codex_reiwa,codex_heisei,codex_showa_post |
| 黒田辰秋 | 2 | 1904 | showa_post,showa_pre | codex_showa_post,codex_showa_pre |
| 黒田清輝 | 2 | 1866,1866 | meiji,taisho | codex_meiji,codex_taisho |
| 黒田チカ | 2 | 1884 | showa_post,meiji | codex_showa_post,codex_meiji |
| 黒沢清 | 2 | 1955 | heisei,reiwa | codex_heisei,codex_reiwa_culture_arts |
| 黒橋禎夫 | 2 | 1963 | reiwa,heisei | codex_reiwa_science_tech,codex_heisei_science_tech |
| 鹿島久嗣 | 2 | 1975 | reiwa,heisei | codex_reiwa_science_tech,codex_heisei_science_tech |
| 鳥井信治郎 | 2 | 1879 | showa_post,meiji | codex_showa_post,codex_meiji |
| 高野松山 | 2 | 1889 | taisho,showa_pre | codex_taisho,codex_showa_pre |
| 高見順 | 2 | 1907 | showa_pre,showa_pre | codex_showa_pre,codex_showa_pre_culture_arts |

## 4. 重複マージ結果
- マージ: 356 件 (生年が一致または片方NULL)

```
  [MERGE] 永守重信 (kept id=94, merged 2)
  [MERGE] 村上春樹 (kept id=189, merged 2)
  [MERGE] 宮崎駿 (kept id=163, merged 2)
  [MERGE] 孫正義 (kept id=31, merged 2)
  [MERGE] 坂本龍一 (kept id=188, merged 2)
  [MERGE] 上野千鶴子 (kept id=229, merged 2)
  [MERGE] 黒田辰秋 (kept id=1930, merged 1)
  [MERGE] 黒田清輝 (kept id=1442, merged 1)
  [MERGE] 黒田チカ (kept id=674, merged 1)
  [MERGE] 黒沢清 (kept id=2642, merged 1)
  [MERGE] 黒橋禎夫 (kept id=3534, merged 1)
  [MERGE] 鹿島久嗣 (kept id=3540, merged 1)
  [MERGE] 鳥井信治郎 (kept id=581, merged 1)
  [MERGE] 高野松山 (kept id=1898, merged 1)
  [MERGE] 高見順 (kept id=3257, merged 1)
  [MERGE] 高群逸枝 (kept id=955, merged 1)
  [MERGE] 高橋政代 (kept id=159, merged 1)
  [MERGE] 高柳健次郎 (kept id=3152, merged 1)
  [MERGE] 高村光太郎 (kept id=1416, merged 1)
  [MERGE] 高木貞治 (kept id=653, merged 1)
  [MERGE] 高峰秀子 (kept id=1095, merged 1)
  [MERGE] 高山岩男 (kept id=2236, merged 1)
  [MERGE] 高坂正顕 (kept id=888, merged 1)
  [MERGE] 養老孟司 (kept id=259, merged 1)
```

## 5. 時代分類の整合性
- 不一致疑い: 89 件

```
  伊藤圭介 (生年1803, 時代meiji)
  広瀬淡窓 (生年1782, 時代meiji)
  中山みき (生年1798, 時代meiji)
  黒住宗忠 (生年1780, 時代meiji)
  三井高福 (生年1808, 時代meiji)
  田中久重 (生年1799, 時代meiji)
  柴田是真 (生年1807, 時代meiji)
  高橋是清 (生年1854, 時代taisho)
  清浦奎吾 (生年1850, 時代taisho)
  浅野総一郎 (生年1848, 時代taisho)
  益田孝 (生年1848, 時代taisho)
  森村市左衛門 (生年1839, 時代taisho)
  宮川香山 (生年1842, 時代taisho)
  山葉寅楠 (生年1851, 時代taisho)
  村山龍平 (生年1850, 時代taisho)
  上野理一 (生年1848, 時代taisho)
  本山彦一 (生年1853, 時代taisho)
  片倉兼太郎 (生年1849, 時代taisho)
  貝島太助 (生年1845, 時代taisho)
  湯浅七左衛門 (生年1850, 時代taisho)
```

## 6. データ品質チェック
- source_url 空のCodex生成: 0 件
- achievement_summary 不足(<30字): 4273 件

## 7. 監査後の総レコード数
- achievers: 9,375 (-356)
- achiever_capabilities: 18,921 (+0)
- era_discourses: 800 (+0)
- era_retrospectives: 927 (+0)
- future_demands: 397 (+0)
- academic_references: 40 (+0)

## 8. 時代別最終分布
| 時代 | 合計 | 偉人 | 無名卓越 |
|---|---|---|---|
| heisei | 1177 | 270 | 619 |
| meiji | 866 | 144 | 665 |
| reiwa | 4752 | 204 | 4222 |
| showa_post | 1236 | 235 | 886 |
| showa_pre | 667 | 104 | 464 |
| taisho | 677 | 118 | 424 |

## 9. ドメイン別分布
| ドメイン | 件数 |
|---|---|
| politics | 4314 |
| business | 904 |
| culture_arts | 855 |
| sports | 478 |
| science_tech | 455 |
| social_movement | 387 |
| science | 296 |
| education | 243 |
| women_pioneers | 200 |
| agriculture_local | 172 |
| professional | 153 |
| craft | 135 |
| media | 130 |
| education_practice | 100 |
| religion_thought | 88 |

## 10. Phase 4 への推奨アクション
- 残った重複（生年異なる同名）を手動レビュー
- 整合性不一致の生年を国立国会図書館典拠で照合
- ハルシネーション疑いのCodex生成データを Web verify
- 関係ネットワーク（師弟・メンター）の構築
- L1/L2のギャップ知見抽出（gap_insights テーブル充填）
#!/usr/bin/env python3
import sqlite3
from seed_showa_post import wiki_url

DB = "data/era_talents.db"

FIXES = {
    "安竹宮": "松野頼三",
    "吉野家松田瑞穂": "松田瑞穂",
    "京セラ西口泰夫": "西口泰夫",
    "小田急安藤楢六": "安藤楢六",
    "相鉄相模鉄道大塚陸毅": "大塚陸毅",
    "杉田玄白再評価者": "緒方富雄",
    "高峰譲吉再評価": "櫻井錠二",
    "柳田國男再評価者": "関敬吾",
    "西田幾多郎再評価者": "高坂正顕",
    "和辻哲郎再評価者": "湯浅泰雄",
    "金子みすゞ再評価者": "矢崎節夫",
    "青い芝の会横田弘": "横田弘",
    "伊江島阿波根昌鴻": "真喜志好一",
}


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    con.execute("BEGIN")
    for old, new in FIXES.items():
        cur.execute("SELECT id FROM achievers WHERE primary_era_id='showa_post' AND name_ja=?", (old,))
        row = cur.fetchone()
        if not row:
            continue
        aid = row[0]
        cur.execute("SELECT 1 FROM achievers WHERE primary_era_id='showa_post' AND name_ja=? AND id<>?", (new, aid))
        if cur.fetchone():
            raise SystemExit(f"Replacement would duplicate: {old} -> {new}")
        url = wiki_url(new)
        cur.execute("UPDATE achievers SET name_ja=?, source_url=? WHERE id=?", (new, url, aid))
        cur.execute("UPDATE achiever_capabilities SET evidence_source=? WHERE achiever_id=?", (url, aid))
    con.commit()
    cur.execute(
        """
        SELECT COUNT(*) FROM achievers
        WHERE primary_era_id='showa_post'
          AND (name_ja LIKE '%再評価%' OR name_ja LIKE '%小田急%' OR name_ja LIKE '%相鉄%'
               OR name_ja LIKE '%吉野家%' OR name_ja LIKE '%京セラ%' OR name_ja LIKE '%青い芝%'
               OR name_ja LIKE '%伊江島%' OR name_ja='安竹宮' OR name_ja LIKE '%スタッフ%')
        """
    )
    print("remaining_suspicious", cur.fetchone()[0])


if __name__ == "__main__":
    main()

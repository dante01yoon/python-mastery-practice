import sqlite3

con = sqlite3.connect("books.db")
con.execute("CREATE TABLE IF NOT EXISTS books (title TEXT UNIQUE, author TEXT, rating INTEGER)")
books = [
    ("데미안", "헤르만 헤세", 5),
    ("어린 왕자", "생텍쥐페리", 4),
    ("노인과 바다", "헤밍웨이", 3),
]
con.executemany("INSERT OR IGNORE INTO books VALUES (?, ?, ?)", books)  # 같은 제목이 있으면 건너뜀
con.commit()
print("책", con.execute("SELECT COUNT(*) FROM books").fetchone()[0], "권")
con.close()

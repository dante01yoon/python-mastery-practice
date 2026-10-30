import sqlite3

con = sqlite3.connect("books.db")
con.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, rating INTEGER)")

books = [
    ("데미안", "헤르만 헤세", 5),
    ("어린 왕자", "생텍쥐페리", 4),
    ("노인과 바다", "헤밍웨이", 3),
]
con.executemany("INSERT INTO books VALUES (?, ?, ?)", books)
con.commit()
con.close()
print("책 3권을 저장했어요")

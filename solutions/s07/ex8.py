import sqlite3

con = sqlite3.connect("books.db")
title = input("책 제목: ").strip()
row = con.execute("SELECT rating FROM books WHERE title = ?", (title,)).fetchone()
if row is None:
    print("없는 책이에요")
else:
    print(f"{title}의 별점은 {row[0]}점이에요")
con.close()

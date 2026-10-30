import sqlite3

con = sqlite3.connect("books.db")
for row in con.execute("SELECT title, author, rating FROM books"):
    print(row)

print("--- 별점 4 이상, 높은 순")
sql = "SELECT title, rating FROM books WHERE rating >= ? ORDER BY rating DESC"
for title, rating in con.execute(sql, (4,)):
    print(title, "★" * rating)
con.close()

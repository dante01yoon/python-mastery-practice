import sqlite3

con = sqlite3.connect("books.db")
best = con.execute("SELECT title, rating FROM books ORDER BY rating DESC LIMIT 1").fetchone()
print("가장 높은 별점:", best[0], best[1])
con.close()

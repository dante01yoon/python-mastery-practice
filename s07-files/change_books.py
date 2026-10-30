import sqlite3

con = sqlite3.connect("books.db")
con.execute("UPDATE books SET rating = ? WHERE title = ?", (5, "노인과 바다"))
con.execute("DELETE FROM books WHERE title = ?", ("어린 왕자",))
con.commit()

for row in con.execute("SELECT title, rating FROM books"):
    print(row)
con.close()

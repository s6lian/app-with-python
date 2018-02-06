import sqlite3

def connect():
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key,title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",
    (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("/Users/yourname/Documents/Github/udemyCoding/bookstore_exe/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

# connect()
# insert('intro to c++','Jay',1982, 294523)
# delete(1)
# update(2,'hello world','John Smith', 2008,39243)
# print(view())
# print(search(author = "Jay"))

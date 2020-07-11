import sqlite3

conn = sqlite3.connect('book.db')
cur = conn.cursor()
cur.execute('CREATE TABLE lib(id INTE, name TEXT, lastname TEXT, code INT)')
conn.commit()
conn.close()


import sqlite3

link = sqlite3.connect('app.db')
cur = link.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
found = cur.fetchall()

print('В базе есть таблицы:', found)

link.close()

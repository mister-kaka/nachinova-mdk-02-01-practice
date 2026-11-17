import sqlite3

link = sqlite3.connect('app.db')

cur = link.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id     INTEGER PRIMARY KEY,
        title  TEXT NOT NULL,
        status TEXT DEFAULT 'new'
    )
""")

link.commit()

link.close()

print('Готово: в app.db есть таблица tasks.')

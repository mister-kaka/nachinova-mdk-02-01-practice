import sqlite3
from flask import Flask, render_template

site = Flask(__name__)

DB_FILE = 'app.db'


def open_db():
    link = sqlite3.connect(DB_FILE)
    link.row_factory = sqlite3.Row
    return link


@site.route('/')
def main_page():
    # подключаемся к базе
    link = open_db()
    cur = link.cursor()

    # читаем все задачи
    cur.execute("SELECT id, title, status FROM tasks ORDER BY id")
    all_rows = cur.fetchall()

    link.close()

    return render_template('index.html', todo_list=all_rows)


if __name__ == '__main__':
    site.run(debug=True, port=5000)


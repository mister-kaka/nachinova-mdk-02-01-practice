import sqlite3
from flask import Flask, render_template, request, redirect, url_for

site = Flask(__name__)

DB_FILE = 'app.db'


def open_db():
    link = sqlite3.connect(DB_FILE)
    link.row_factory = sqlite3.Row
    return link


def read_tasks():
    link = open_db()
    cur = link.cursor()
    cur.execute("SELECT id, title, status FROM tasks ORDER BY id")
    all_rows = cur.fetchall()
    link.close()
    return all_rows


@site.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        name = request.form.get('title', '').strip()

        if not name:
            return render_template(
                'index.html',
                todo_list=read_tasks(),
                warning='Введите название задачи, пустое поле не принимается.'
            )

        link = open_db()
        cur = link.cursor()
        cur.execute("INSERT INTO tasks (title) VALUES (?)", (name,))
        link.commit()
        link.close()

        return redirect(url_for('main_page'))

    return render_template('index.html', todo_list=read_tasks())


if __name__ == '__main__':
    site.run(debug=True, port=5000)
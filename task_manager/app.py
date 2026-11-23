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
    try:
        cur = link.cursor()
        cur.execute("SELECT id, title, status FROM tasks ORDER BY id")
        return cur.fetchall()
    except sqlite3.Error as err:
        print(f"[DB ERROR] чтение: {err}")
        return []
    finally:
        link.close()


def add_task(name):
    link = open_db()
    try:
        cur = link.cursor()
        cur.execute("INSERT INTO tasks (title) VALUES (?)", (name,))
        link.commit()
        return True, None
    except sqlite3.Error as err:
        link.rollback()
        print(f"[DB ERROR] добавление: {err}")
        return False, "Не удалось сохранить задачу."
    finally:
        link.close()


def switch_status(num):
    link = open_db()
    try:
        cur = link.cursor()
        cur.execute(
            """
            UPDATE tasks
            SET status = CASE WHEN status = 'done' THEN 'new' ELSE 'done' END
            WHERE id = ?
            """,
            (num,)
        )
        link.commit()
        return cur.rowcount
    except sqlite3.Error as err:
        link.rollback()
        print(f"[DB ERROR] смена статуса: {err}")
        return 0
    finally:
        link.close()


def remove(num):
    link = open_db()
    try:
        cur = link.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?", (num,))
        link.commit()
        return cur.rowcount
    except sqlite3.Error as err:
        link.rollback()
        print(f"[DB ERROR] удаление: {err}")
        return 0
    finally:
        link.close()


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

        ok, text = add_task(name)
        if not ok:
            return render_template(
                'index.html',
                todo_list=read_tasks(),
                warning=text
            )

        return redirect(url_for('main_page'))

    return render_template('index.html', todo_list=read_tasks())


@site.route('/toggle/<int:num>', methods=['POST'])
def switch_done(num):
    changed = switch_status(num)
    if changed == 0:
        return render_template(
            'index.html',
            todo_list=read_tasks(),
            warning=f'Задача #{num} не найдена.'
        )
    return redirect(url_for('main_page'))


@site.route('/delete/<int:num>', methods=['POST'])
def remove_task(num):
    changed = remove(num)
    if changed == 0:
        return render_template(
            'index.html',
            todo_list=read_tasks(),
            warning=f'Задача #{num} не найдена.'
        )
    return redirect(url_for('main_page'))


if __name__ == '__main__':
    site.run(debug=True, port=5000)
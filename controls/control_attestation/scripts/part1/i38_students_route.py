# Задание 38. Flask: полный маршрут «Добавить + Показать»
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)
DB_PATH = 'students.db'

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        grade_text = request.form.get('grade', '').strip()
        if name == '':
            return render_template('students.html', students=[], error='Имя не может быть пустым')
        try:
            grade = int(grade_text)
        except ValueError:
            return render_template('students.html', students=[], error='Оценка должна быть целым числом от 1 до 5')
        if grade < 1 or grade > 5:
            return render_template('students.html', students=[], error='Оценка должна быть целым числом от 1 до 5')
        conn = sqlite3.connect(DB_PATH)
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            return render_template('students.html', students=[], error=str(e))
        finally:
            conn.close()
        return redirect(url_for('students'))

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, grade FROM students')
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        conn.rollback()
        return render_template('students.html', students=[], error=str(e))
    finally:
        conn.close()
    return render_template('students.html', students=rows)


if __name__ == '__main__':
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, grade INTEGER)')
    conn.close()

    client = app.test_client()
    r = client.post('/students', data={'name': 'Анна', 'grade': '5'}, follow_redirects=True)
    print('POST ok', r.status_code)
    print(r.get_data(as_text=True))
    r = client.post('/students', data={'name': '', 'grade': '5'})
    print('empty name', r.status_code)
    print(r.get_data(as_text=True))
    r = client.post('/students', data={'name': 'Борис', 'grade': '9'})
    print('bad grade', r.status_code)
    print(r.get_data(as_text=True))
    r = client.get('/students')
    print('GET', r.status_code)
    print(r.get_data(as_text=True))

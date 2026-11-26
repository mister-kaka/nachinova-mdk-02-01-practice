# Задание 37. SQLite: CRUD-функция
import os
import sqlite3

DB_PATH = 'students.db'

def add_student(name, grade):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
        conn.commit()
        return True
    except sqlite3.Error:
        conn.rollback()
        return False
    finally:
        conn.close()

def get_all_students():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, grade FROM students')
        result = []
        for row in cursor.fetchall():
            result.append((row['id'], row['name'], row['grade']))
        return result
    except sqlite3.Error:
        conn.rollback()
        return []
    finally:
        conn.close()

def update_grade(student_id, new_grade):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE students SET grade = ? WHERE id = ?', (new_grade, student_id))
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error:
        conn.rollback()
        return 0
    finally:
        conn.close()

def delete_failing():
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE grade < ?', (3,))
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error:
        conn.rollback()
        return 0
    finally:
        conn.close()


if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
conn.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, grade INTEGER)')
conn.close()

print('add', add_student('Анна', 5))
print('add', add_student('Борис', 2))
print('add', add_student('Вера', 4))
print('all', get_all_students())
print('update', update_grade(1, 4))
print('all', get_all_students())
print('delete_failing', delete_failing())
print('all', get_all_students())

# Задание 38. Flask: маршрут «Фильтр по автору»
from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)
DB_PATH = 'library.db'

@app.route('/books')
def books():
    author = request.args.get('author')
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        if author:
            cursor.execute('SELECT id, title, author, year FROM books WHERE author = ?', (author,))
        else:
            cursor.execute('SELECT id, title, author, year FROM books')
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        conn.rollback()
        return render_template('books.html', books=[], error=str(e))
    finally:
        conn.close()
    return render_template('books.html', books=rows)


if __name__ == '__main__':
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER)')
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Война и мир', 'Толстой', 1869)")
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Анна Каренина', 'Толстой', 1877)")
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Отцы и дети', 'Тургенев', 1862)")
    conn.commit()
    conn.close()

    client = app.test_client()
    r = client.get('/books')
    print('all books')
    print(r.get_data(as_text=True))
    r = client.get('/books?author=Толстой')
    print('author Толстой')
    print(r.get_data(as_text=True))

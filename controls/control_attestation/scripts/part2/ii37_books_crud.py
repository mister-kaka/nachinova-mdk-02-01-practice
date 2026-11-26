# Задание 37. SQLite: полный CRUD для таблицы books
import os
import sqlite3

DB_PATH = 'library.db'

def add_book(title, author, year):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
        conn.commit()
        return True
    except sqlite3.Error:
        conn.rollback()
        return False
    finally:
        conn.close()

def get_books_by_author(author):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, year FROM books WHERE author = ?', (author,))
        result = []
        for row in cursor.fetchall():
            result.append((row['id'], row['title'], row['year']))
        return result
    except sqlite3.Error:
        conn.rollback()
        return []
    finally:
        conn.close()

def update_year(book_id, new_year):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET year = ? WHERE id = ?', (new_year, book_id))
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error:
        conn.rollback()
        return 0
    finally:
        conn.close()

def delete_old_books(before_year):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE year < ?', (before_year,))
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
conn.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER)')
conn.close()

print('add', add_book('Война и мир', 'Толстой', 1869))
print('add', add_book('Анна Каренина', 'Толстой', 1877))
print('add', add_book('Отцы и дети', 'Тургенев', 1862))
print('by Толстой', get_books_by_author('Толстой'))
print('update', update_year(1, 1865))
print('by Толстой', get_books_by_author('Толстой'))
print('delete_old', delete_old_books(1870))
print('by Толстой', get_books_by_author('Толстой'))

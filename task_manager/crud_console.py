import sqlite3


def open_db():
    return sqlite3.connect('app.db')


def print_menu():
    print("\n--- Мои задачи ---")
    print("1 - показать список")
    print("2 - новая задача")
    print("3 - отметить выполненной")
    print("4 - удалить задачу")
    print("0 - выйти")


def show_tasks():
    link = open_db()
    cur = link.cursor()
    cur.execute("SELECT id, title, status FROM tasks ORDER BY id")
    all_rows = cur.fetchall()
    link.close()

    if not all_rows:
        print("Список пуст, добавьте первую задачу.")
        return

    print("\nСписок задач:")
    for line in all_rows:
        num, name, status = line
        sign = "[x]" if status == 'done' else "[ ]"
        print(f"{num:>3}) {sign} {name}  ({status})")


def run():
    while True:
        print_menu()
        pick = input("Ваш выбор: ").strip()

        if pick == '1':
            show_tasks()
        elif pick == '2':
            new_task()
        elif pick == '3':
            finish_task()
        elif pick == '4':
            remove_task()
        elif pick == '0':
            print("Пока!")
            break
        else:
            print("Нет такого пункта, попробуйте ещё раз.")


if __name__ == '__main__':
    run()

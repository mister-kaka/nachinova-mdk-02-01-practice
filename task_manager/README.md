# Task Manager

Учебное приложение «Список задач» (SQLite + Flask).
Сейчас готово: практические работы 1-7.

## Файлы

- [`init_db.py`](init_db.py) - создаёт базу `app.db` и таблицу `tasks`
- [`check_db.py`](check_db.py) - показывает, какие таблицы есть в базе
- [`crud_console.py`](crud_console.py) - консольное приложение: показать задачи, добавить, отметить выполненной, удалить
- [`app.py`](app.py) - веб-приложение на Flask
- [`static/hourglass.webp`](static/hourglass.webp) - картинка для страницы
- [`templates/index.html`](templates/index.html) - страница со списком задач

## Запуск

```
python init_db.py
python crud_console.py   # консольная версия
pip install flask
python app.py
```

Сайт открывается по адресу http://127.0.0.1:5000. Консольная версия и сайт работают с одной базой `app.db`.

## Что добавлялось по работам

| Работа | Что сделано | Отчёт |
|--------|-------------|--------|
| [ПР1](../reports/pr1_init_db/) | база SQLite, таблица `tasks`, проверка таблицы | [смотреть](../reports/pr1_init_db/%D0%9F%D0%A01%20%D0%98%D0%BD%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%91%D0%94%20SQLite_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР2](../reports/pr2_console_crud/) | консольное приложение: чтение, добавление, отметка, удаление | [смотреть](../reports/pr2_console_crud/%D0%9F%D0%A02%20%D0%9A%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20CRUD_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР3](../reports/pr3_hello_flask/) | первый сервер Flask, маршруты `/` и `/about` | [смотреть](../reports/pr3_hello_flask/%D0%9F%D0%A03%20Hello%20Flask_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР4](../reports/pr4_read_templates/) | шаблон `index.html`, чтение задач из базы | [смотреть](../reports/pr4_read_templates/%D0%9F%D0%A04%20%D0%A7%D1%82%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20Flask%20SQLite_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР5](../reports/pr5_add_form/) | форма добавления задачи, POST и redirect | [смотреть](../reports/pr5_add_form/%D0%9F%D0%A05%20%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20Flask%20SQLite_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР6](../reports/pr6_error_handling/) | обработка ошибок базы (try/except/finally) | [смотреть](../reports/pr6_error_handling/%D0%9F%D0%A06%20%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%BE%D1%88%D0%B8%D0%B1%D0%BE%D0%BA_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |
| [ПР7](../reports/pr7_task_manager/) | смена статуса и удаление задач, защита от неверных запросов | [смотреть](../reports/pr7_task_manager/%D0%9F%D0%A07%20%D0%9C%D0%B8%D0%BD%D0%B8-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87_%D0%9D%D0%B0%D1%87%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D0%9C.%20%D0%94._3-%D0%98%D0%A1%D0%9F9-54.md) |

Отчёты по работам лежат в папке [`reports`](../reports/) (в корне репозитория).

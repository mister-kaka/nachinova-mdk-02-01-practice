from flask import Flask

site = Flask(__name__)


@site.route('/')
def main_page():
    return "Привет, Flask!"


@site.route('/about')
def about_page():
    return "Учебный сайт со списком задач на Flask и SQLite. Практическая работа 3, Начинова Мария."


if __name__ == '__main__':
    site.run(debug=True, port=5000)


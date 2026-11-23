from flask import Flask

site = Flask(__name__)


@site.route('/')
def main_page():
    return "Привет, Flask!"


if __name__ == '__main__':
    site.run(debug=True, port=5000)


from flask import Flask

site = Flask(__name__)

STYLE = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dela+Gothic+One&family=Golos+Text:wght@400;500&display=swap" rel="stylesheet">
<style>
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; background: #141313; color: #eee9e1; font: 400 16px "Golos Text", "Segoe UI", sans-serif; }
    .kolonka { position: relative; max-width: 900px; margin: 0 auto; padding: 36px 24px 60px; overflow: hidden; min-height: 100vh; }
    .logo { font: 20px "Dela Gothic One", Impact, sans-serif; }
    .logo i { display: inline-block; width: 28px; height: 28px; line-height: 28px; text-align: center; background: #7a0f14; font-style: normal; font-size: 14px; margin-right: 10px; }
    h1 { font: 400 clamp(44px, 9vw, 84px)/1 "Dela Gothic One", Impact, sans-serif; margin: 60px 0 0; max-width: 11ch; }
    h1 span { color: #a3161d; }
    p { color: #8f8a84; max-width: 46ch; line-height: 1.6; margin: 24px 0 0; }
    .ssylka { display: inline-block; margin-top: 34px; padding: 14px 22px; background: #7a0f14; color: #eee9e1; text-decoration: none;
              font-size: 12px; letter-spacing: .14em; text-transform: uppercase; }
    .ssylka:hover { background: #a3161d; }
    .chasy { position: absolute; right: -30px; bottom: -40px; width: 300px; opacity: .9; pointer-events: none; }
    @media (max-width: 600px) { .chasy { width: 200px; right: -50px; } }
</style>
"""


@site.route('/')
def main_page():
    return """
    <html>
        <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Мои дела</title>""" + STYLE + """</head>
        <body><div class="kolonka">
            <div class="logo"><i>✦</i>Дела</div>
            <h1>Мои <span>дела</span></h1>
            <p>Тут появятся задачи из базы данных.</p>
            <a class="ssylka" href="/about">О проекте</a>
            <img class="chasy" src="/static/hourglass.webp" alt="">
        </div></body>
    </html>
    """


@site.route('/about')
def about_page():
    return "Учебный сайт со списком задач на Flask и SQLite. Практическая работа 3, Начинова Мария."


if __name__ == '__main__':
    site.run(debug=True, port=5000)


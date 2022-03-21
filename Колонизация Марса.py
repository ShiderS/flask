from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '<b>Миссия Колонизация Марса<b>'


@app.route('/index')
def index():
    return "<b>И на Марсе будут яблони цвести!<b>"


@app.route('/promotion')
def promotion():
    return f"""<h3>Человечество вырастает из детства.<h3>
           <h3>Человечеству мала одна планета.<h3>
           <h3>Мы сделаем обитаемыми безжизненные пока планеты.<h3>
           <h3>И начнем с Марса!<h3>
           <h3>Присоединяйся!<h3>"""


@app.route('/image_mars')
def image_mars():
    return f"""<head>
    <title>Привет, Марс!<title><head>
                   <body><h2>Жди нас, Марс<h2><body>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

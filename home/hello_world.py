import datetime

from flask import Flask

app = Flask(__name__)

day_to_word_map = {
    0: "хорошего понедельника",
    1: "хорошего вторника",
    2: "хорошего среды",
    3: "хорошего четверга",
    4: "хорошего пятницы",
    5: "хорошего субботы",
    6: "хорошего воскресенья",
}


@app.route('/hello_world/<username>')
def hello_word(username: str) -> str:
    current_day = datetime.datetime.today().weekday()
    greetings = day_to_word_map[current_day]
    return f'Привет {username}. {greetings}!'


if __name__ == '__main__':
    app.run(debug=True)

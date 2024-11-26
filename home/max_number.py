# Реализуйте endpoint, начинающийся с /max_number,
# в который можно передать список чисел, разделённых слешем /.
# Endpoint должен вернуть текст «Максимальное переданное число {number}»,
# где number — выделенное курсивом наибольшее из переданных чисел.
#
# Примеры:
#
# /max_number/10/2/9/1
# Максимальное число: 10
#
# /max_number/1/1/1/1/1/1/1/2
# Максимальных число: 2

from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str):
    numbers_as_num = (int(it) for it in numbers.split("/"))
    return f'максимальное переданное число: <i>{max(numbers_as_num)}</i>'

# def max_number(numbers: str) -> tuple[str, int]:
#     numbers_split: list[str] = numbers.split('/')
#     try:
#         max_number: float = max(map(float, numbers_split))
#         return f"Максимальное число: <i>{max_number}</i>", 200
#     except ValueError:
#         return "Передано не корректно", 400


if __name__ == '__main__':
    app.run(debug=True)

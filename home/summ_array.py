from flask import Flask, request

app = Flask(__name__)


@app.route("/sum", methods=["GET"])
def _sum():
    array1 = request.args.getlist("array1", type=int)
    array2 = request.args.getlist("array2", type=int)

    result = ",".join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f"Array of sums is [{result}]"


if __name__ == '__main__':
    app.run(debug=True)

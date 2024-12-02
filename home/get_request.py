from typing import List, Optional
from flask import Flask, request

app = Flask(__name__)


@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"Ты должен выбрать из списка", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")

    protocols: List[str] = request.args.getlist("protocol")

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )

    return (f"Поиск по {cell_tower_ids} номерам городским. "
            f"Поиск по критериям:"
            f"телефонная приставка={phone_prefixes},"
            f"протокол={protocols},"
            f"уровень сигнала={signal_level}")


if __name__ == '__main__':
    app.run(debug=True)

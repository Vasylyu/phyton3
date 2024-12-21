import shlex
import string
from simple import subprocess_run
from typing import List

from flask import Flask, request

app = Flask(__name__)

@app.route("/ps", methods=["GET"])
def _ps():
    arquments: List[str] = request.args.getlist("arg")
    arquments_cleaned = [shlex.quote(s) for s in arquments]
    command_str = f"ps {''.join(arquments_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()
    return string.Template(f"<pre>${output}</pre>").substitute(output=output)


if __name__ == '__main__':
    app.run(debug=True)

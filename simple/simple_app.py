import flask
import signal
import subprocess_run

app = flask.Flask(__name__)


@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint was called!'


if __name__ == '__main__':
    app.run()

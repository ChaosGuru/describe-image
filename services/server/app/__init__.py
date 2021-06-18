from flask import Flask

app = Flask(__name__)


@app.route('/')
def test_if_works():
    return "Hello, World!"
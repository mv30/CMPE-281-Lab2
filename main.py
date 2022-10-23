from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return """
        <h1>Hello from CMPE-281 Lab 2 by Mayank Verma</h1>
    """
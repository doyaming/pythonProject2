from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/data/<num>")
def test(num):

    if int(num) >= 200:
        return "大於200"
    else:
        return "小於200"

if __name__ == '__main__':
        app.run(debug=True)

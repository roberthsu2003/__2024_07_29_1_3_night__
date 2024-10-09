from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>星期三,您好!</h1>"
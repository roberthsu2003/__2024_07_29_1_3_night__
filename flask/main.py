from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<h1>這是python的project</h1>
            <p>這是在codespace環境開發的</p>
        '''
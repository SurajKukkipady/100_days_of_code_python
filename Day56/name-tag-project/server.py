from flask import Flask
from flask import render_template

from Day45.main_live import index

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

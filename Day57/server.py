from flask import Flask
from flask import render_template
import random
import datetime


app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    timestamp = datetime.datetime.now().strftime("%Y")
    return render_template("index.html", number=random_number, timestamp=timestamp)


if __name__ == "__main__":
    app.run(debug=True)
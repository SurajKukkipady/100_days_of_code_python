from flask import Flask
from flask import render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(1, 10)
    timestamp = datetime.datetime.now().strftime("%Y")
    return render_template("index.html", number=random_number, timestamp=timestamp)


@app.route("/guess/<name>")
def guess(name):
    url_age = "https://api.agify.io"
    url_gender = "https://api.genderize.io"
    params = {"name": name}

    response = requests.get(url_age, params=params)
    age = response.json()['age']

    response = requests.get(url_gender, params=params)
    gender = response.json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
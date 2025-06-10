from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hi")
def hi_world():
    return "<p>Hi, World!</p>"

if __name__ == "__main__":
    app.run()


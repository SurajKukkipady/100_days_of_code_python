from flask import Flask
from functools import wraps

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2xkZXhvYWY3MDgwdTlnNDFqdWRocWgzdGNnOW1yNDBpczd3dmc4ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26DOJwj9M4npUa54A/giphy.gif" width=200>')

def underline(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)
        return f"<u>{result}</u>"
    return decorated_function

@app.route("/bye")
@underline
def bye():
    return "<b>Bye, World!</b>"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello there, {name}!</p>"

if __name__ == "__main__":
    app.run(debug=True)


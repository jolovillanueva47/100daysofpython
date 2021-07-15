from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def wrapper():
        text=func()
        return f"<b>{text}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        text=func()
        return f"<em>{text}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        text=func()
        return f"<u>{text}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
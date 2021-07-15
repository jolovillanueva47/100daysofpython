from flask import Flask
app = Flask(__name__)

def logging_decorator(function):
    def wrapper(*args,**kwargs):
        if args or kwargs:
            print(f"Function name:{function.__name__} Arguments:{kwargs}")
        else:
            print(f"Function name:{function.__name__} No arguments passed")
        return function(*args,**kwargs)
    wrapper.__name__ = function.__name__
    return wrapper

@app.route('/')
@logging_decorator
def hello_world():
    return 'Hello, World!'

@app.route('/test/<name>')
@logging_decorator
def trial(name):
    return name

@app.route('/bye')
@logging_decorator
def bye():
    return "Bye!"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
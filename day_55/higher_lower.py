from flask import Flask
import random
app = Flask(__name__)
rand_num=random.randint(0,9)

def formatter(func):
    def wrapper(*args, **kwargs):
        format=func(*args, **kwargs)
        return (f"<h1 style='color:{format[0]};'>{format[1]}</h1>\n"
            f"<img src={format[2]}>")
    return wrapper

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

@app.route('/<int:number>')
@formatter
def guess(number):
    if number<rand_num:
        return ["red","Too low, try again","https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"]
    elif number>rand_num:
        return ["purple","Too high, try again","https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"]
    else:
        return ["green","You found me!","https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"]

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template
from datetime import date
import requests
import random
app = Flask(__name__)

date_today=date.today()

@app.route('/')
def home():
    rand_num=random.randint(1,10)
    year=date_today.year
    return render_template("index.html",num=rand_num,year=year)

@app.route('/guess/<name>')
def guess(name):
    params ={
        "name":name
    }
    response_genderize=requests.get("https://api.genderize.io",params=params)
    response_agify=requests.get("https://api.agify.io",params=params)
    return render_template("guess.html",name=name.title(),gender=response_genderize.json()["gender"],age=response_agify.json()["age"])

@app.route("/blog")
def blog():
    blog_url="https://api.npoint.io/724f764122069226fb74"
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html",posts=all_posts)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
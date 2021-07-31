from flask import Flask, render_template
import requests
app = Flask(__name__)


blog_url="https://api.npoint.io/724f764122069226fb74"
response=requests.get(blog_url)
all_posts=response.json()
author="Jolo Villanueva"
date="July 31, 2021"

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts,author=author,date=date)

@app.route('/about')
def go_to_about():
    return render_template("about.html")

@app.route('/contact')
def go_to_contact():
    return render_template("contact.html")

@app.route("/post/<blog_id>")
def get_post(blog_id):
    post=all_posts[int(blog_id)-1]
    return render_template("post.html",post=post,author=author,date=date)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
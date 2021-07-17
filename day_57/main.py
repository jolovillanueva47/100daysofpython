from flask import Flask, render_template
import requests
app = Flask(__name__)


blog_url="https://api.npoint.io/724f764122069226fb74"
response=requests.get(blog_url)
all_posts=response.json()

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts)

@app.route("/post/<blog_id>")
def get_post(blog_id):
    post=all_posts[int(blog_id)-1]
    return render_template("post.html",posts=all_posts,post=post)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__)


blog_url="https://api.npoint.io/724f764122069226fb74"
response=requests.get(blog_url)
all_posts=response.json()
author="Jolo Villanueva"
date="July 31, 2021"
my_email=""
password=""

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts,author=author,date=date)

@app.route('/about')
def go_to_about():
    return render_template("about.html")

@app.route("/post/<blog_id>")
def get_post(blog_id):
    post=all_posts[int(blog_id)-1]
    return render_template("post.html",post=post,author=author,date=date)

@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        phone_number=request.form['phone']
        message=request.form['message']
        print(my_email)
        print(password)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Hello\n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}")
        return render_template("contact.html",sent_msg=True)
    else:
        return render_template("contact.html",sent_msg=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
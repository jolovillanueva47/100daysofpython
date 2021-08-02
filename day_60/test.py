from flask import Flask, render_template
from flask import request
app = Flask(__name__)



@app.route('/')
def contact_form():
    return render_template('index2.html')

@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['pwd']
        return f"<h1>Name: {username}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



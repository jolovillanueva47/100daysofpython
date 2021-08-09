from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,Length
from wtforms.fields.html5 import EmailField
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'any secret string'
Bootstrap(app)

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(),Email(message="Invalid email address")])
    password=PasswordField(label='Password', validators=[DataRequired(),Length(message="Field must be 8 characters long",min=8)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
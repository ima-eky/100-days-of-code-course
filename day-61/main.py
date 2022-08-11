import os.path

from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email,Length,InputRequired
from flask_bootstrap import Bootstrap

class Form(FlaskForm):
    valid_mail = Email(message="not a valid email")

    email = StringField(label='Email', validators=[DataRequired(), valid_mail])

    password=PasswordField(label='Password',validators=[InputRequired(),Length(min=8)])
    submit=SubmitField(label='Log in')

app = Flask(__name__)
Bootstrap(app)

app.secret_key="2707"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def login():
    new_form=Form()
    if request.method == 'POST':
        if new_form.validate_on_submit():
            if new_form.email.data == "admin@email.com" and new_form.password.data == "12345678":
             return render_template('success.html')
        else:
            return render_template('denied.html',)
    return render_template("login.html",form=new_form)


if __name__ == '__main__':
    app.run(debug=True)
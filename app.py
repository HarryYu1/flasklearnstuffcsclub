from flask import Flask
from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "DONTUSETHISASYOURSECRETKEY"

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/index")
def show_index():
    return render_template('confirmation.html')

class MyForm(FlaskForm):
    name = StringField('Hey! Enter your name: ', validators=[InputRequired()])
    submit = SubmitField('Submit')

@app.route("/form", methods = ["POST", "GET"])
def handle_form():

    form = MyForm()


    if form.validate_on_submit():
        
        print("We recieved the following info:" +  form.name.data)
        return redirect('/index')

        #now redirect to landing or something

    return render_template("myform.html" ,form=form)
from flask import Flask, render_template, request, redirect
from models import db, connect_db
from forms import UserRegisterForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "sssssssssssssssst"


connect_db(app)

with app.app_context():
    db.create_all()



@app.route("/")
def redirect_to_register():
    return redirect ("/register")


@app.route("/register", methods = ["POST", "GET"])
def show_register_form():
    form = UserRegisterForm()
    return render_template("register.html", form = form)
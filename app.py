from flask import Flask, render_template, request, redirect
from models import db, connect_db, User
from forms import UserRegisterForm
from flask_bcrypt import Bcrypt



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
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        email = form.email.data
        last_name = form.last_name.data
        first_name = form.first_name.data
        user = User.register(password = password, username = username, last_name = last_name, first_name = first_name, email = email)
        db.session. add(user)
        db.session.commit()
        return redirect("/")
    
    else:
        return render_template("register.html", form = form)
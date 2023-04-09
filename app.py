from flask import Flask, session, render_template, request, redirect
from models import db, connect_db, User
from forms import UserRegisterForm, UserLoginForm
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
        registered_user = User.query.filter_by(username = username).first()
        session['user_id']=registered_user.id
    


        return redirect("/secret")
    
    else:
        return render_template("register.html", form = form)
    
@app.route("/login", methods = ["POST", "GET"])
def login_user():
    form = UserLoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        user = User.query.filter_by(username = username).first()
        if User.login(username = username, password = password):
            session['user_id']=user.id
            return redirect ("/secret")
        else: 
            return redirect ("/login")
    else:
        return render_template("login.html", form = form)


@app.route("/secret")
def show_secret():
    if 'user_id' in session:
        return render_template("secret.html")
    else:
        return redirect ("/login")
    
@app.route("/logout")
def log_user_out():
    session.pop('user_id')
    return redirect ("/login")
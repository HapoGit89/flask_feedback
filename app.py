from flask import Flask, render_template, request, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import Petform


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.debug = True
app.config['SECRET_KEY'] = 'SehrgEheim'
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()


@app.route("/pets")
def show_pets():
    pets = Pet.query.all()
    return render_template("petlist.html", pets=pets)

@app.route ("/pets/add")
def show_add_form():
    form = Petform()
    return render_template("addpet.html", form = form)
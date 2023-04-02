from flask import Flask, render_template, request, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetAddForm, PetEditForm


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
    """Show List of Pets"""
    pets = Pet.query.all()
    return render_template("petlist.html", pets=pets)

@app.route ("/add", methods = ["GET", "POST"])
def show_add_form():
    """ Show Add Form and Handle POST request"""
    form = PetAddForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image_url = form.image_url.data
        if image_url == "":
            image_url = "https://www.officeb2b.de/dx/10/9/425_425/59151/301.jpg"
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name = name, species = species, image_url = image_url, age = age, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/pets")
    else:
        return render_template("addpet.html", form = form)
    
@app.route("/pets/<petid>/details", methods = ["GET", "POST"])
def show_pet_details(petid):
    """ Show Pet details and handle POST request"""
    pet = Pet.query.get_or_404(petid)
    form = PetEditForm(obj = pet)
    if form.validate_on_submit():
        if form.image_url.data == "":
            pet.image_url = "https://www.officeb2b.de/dx/10/9/425_425/59151/301.jpg"
        else:
            pet.image_url = form.image_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/pets")
    else:
        return render_template("petdetails.html", form = form, pet=pet)
    
@app.route("/<petid>/delete")

def delete_pet_listing(petid):
    """Handle Delete Request"""
    pet = Pet.query.get_or_404(petid)
    db.session.delete(pet)
    db.session.commit()
    return redirect("/pets")



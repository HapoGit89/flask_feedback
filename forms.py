from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, AnyOf, NumberRange

class PetAddForm(FlaskForm):
    """ Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired("Please type in a name")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('procupine', 'Procupine')])
    image_url = StringField("Pic URL", validators = [URL("This is not a URL"), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField("available")

class PetEditForm(FlaskForm):
      """ Form for editing pets"""

      image_url = StringField("Pic URL", validators = [URL("This is not a URL"), Optional()])
      notes = StringField("Notes")
      available = BooleanField("available")

    
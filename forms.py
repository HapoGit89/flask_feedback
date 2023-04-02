from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField

class Petform(FlaskForm):
    """ Form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species")
    image_url = StringField("Pic URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
    available = BooleanField("available")

    
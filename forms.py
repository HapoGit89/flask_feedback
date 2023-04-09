from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, AnyOf, NumberRange

class UserRegisterForm(FlaskForm):
    """ Form for Registering User"""

    username = StringField("Username", validators=[InputRequired("Please type in a Username")])
    password= PasswordField('Password',  validators= [InputRequired("Please type in a Password")])
    first_name = StringField("First Name",  validators=[InputRequired("Please type in your First Name")])
    last_name = StringField("Last Name",  validators=[InputRequired("Please type in your Last Name")])
    email = EmailField("Email",  validators=[InputRequired("Please type in your Email")])
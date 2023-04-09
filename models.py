from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)



class User (db.Model):
    """User"""

    __tablename__ = "users"

    # def __repr__(self):
    #     """SH"""


    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    username = db.Column(db.Text,
                         nullable = False)
    password = db.Column (db.Text,
                          nullable = False
                          )
    first_name = db.Column(db.String(20),
                          nullable = False)
    last_name = db.Column(db.String(20),
                          nullable = False)
    email = db.Column(db.String(50),
                      nullable = False)
    
    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        return cls(username = username, password = hashed_utf8, first_name = first_name, last_name = last_name, email = email )

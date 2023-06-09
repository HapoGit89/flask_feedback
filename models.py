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
    username = db.Column(db.Text, unique = True,
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
        return cls(username = username, password = hashed_utf8, first_name= first_name, last_name = last_name, email=email)
      
    @classmethod
    def login(cls, username, password):
        user = User.query.filter_by(username = username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
        
class Feedback(db.Model):
        """User Feedback"""

        __tablename__ = "feedback"

        id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
        title = db.Column(db.String(30),
                         nullable = False)
        content = db.Column(db.Text,
                          nullable = False)
        username = db.Column(db.Text, db.ForeignKey('users.username'))
        
        


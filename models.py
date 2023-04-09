from flask_sqlalchemy import SQLAlchemy


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
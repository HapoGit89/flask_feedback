from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connect to db"""

    db.app = app
    db.init_app(app)


class Pet (db.Model):
        """Pet for adoption"""

        __tablename__ = "pets"

        id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
        name = db.Column(db.String(20),
                          nullable = False)
        species = db.Column(db.String(20),
                          nullable = False)
        image_url = db.Column(db.Text,      
                          default = "https://as2.ftcdn.net/v2/jpg/00/31/32/99/1000_F_31329924_hGwoiEiGQELkjd0ZShrSOAwi60tZc4S9.jpg")
        age = db.Column(db.Integer)
        notes = db.Column(db.Text)
        available = db.Column(db.Boolean,
                              nullable = False,
                              default = True)
        

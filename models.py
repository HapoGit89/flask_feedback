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
                          default = "https://cdn.shopify.com/s/files/1/2994/3128/products/Essex_Paint_Black_Cat_1024x1024@2x.jpeg")
        age = db.Column(db.Integer)
        notes = db.Column(db.Text)
        available = db.Column(db.Boolean,
                              nullable = False,
                              default = True)
        

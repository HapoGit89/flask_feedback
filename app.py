from flask import Flask, render_template, request, redirect
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'

connect_db(app)
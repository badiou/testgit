from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask

app=Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

class Etudiant(db.Model):
    __tablename__='etudiants'
    id = db.Column(db.Integer, primary_key=True)
    nom= db.Column(db.String(200))
    prenom= db.Column(db.String(200))
    

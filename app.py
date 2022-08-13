from xml.dom.xmlbuilder import DOMEntityResolver
from flask import Flask,redirect,url_for,render_template,request
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import Etudiant,db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Etudiant, db,app

migrate = Migrate(app, db)

@app.route('/',methods=['GET','POST'])
def home():
    return 'Bonjour'


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
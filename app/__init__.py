from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
app.config['SECRET_KEY']=getenv('KEY')
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt=Bcrypt(app)
db = SQLAlchemy(app)
from app import routes


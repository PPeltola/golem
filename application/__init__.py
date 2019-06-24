from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///golem.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.users import models, views
from application.campaigns import models, views

from application.users.models import User
from os import urandom

app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "You must be logged in"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass
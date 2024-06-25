from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
#if os.getenv("DEBUG") == 0:
#    link_banco = os.getenv("DATABASE_URL")
#else:
#    link_banco =  "sqlite:///pictures.db"
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://bd_fakepinter_user:t7MSdPj3I8kHjypFzfWVcC7Kn4auXrnU@dpg-cpt4es6ehbks73etvup0-a.oregon-postgres.render.com/bd_fakepinter"
app.config["SECRET_KEY"] = "17d3ec830ce32f7aef7e423e0ebb9a94"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinter import routes
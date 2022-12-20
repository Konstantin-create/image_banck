# Base imports
import os

# My modules imports
from config import Config

# Flask imports
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, send_file

# Flask login import
from flask_login import LoginManager


from app.routes.error_code_pages import *

# Flask init
app = Flask(__name__)
app.config.from_object(Config)
app.register_error_handler(404, page_not_found)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask login
login_manager = LoginManager(app)

app_folder = os.path.dirname(__file__)

from app.modules.models import *
from app.routes.admin import admin_login
from app.routes.user import *
from app.routes.admin import *

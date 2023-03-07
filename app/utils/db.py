from flask_sqlalchemy import SQLAlchemy
from ..create_app import app

db = SQLAlchemy(app)
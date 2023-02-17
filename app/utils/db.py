from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from create_app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)
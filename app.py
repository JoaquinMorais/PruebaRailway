from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:c3koV2O5uaUGyYFIskBa@containers-us-west-78.railway.app:6912/railway"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db=SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def repr(self):
        return f'<Student {self.firstname}>'
    

@app.route('/')
def hola():
    return 'Hola'





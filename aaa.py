from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:i3eXbNRZa4GIGFN37K8s@containers-us-west-151.railway.app:5647/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))
    
    def __init__(self,title,description):
        self.title = title
        self.description = description
    
    def __repr__(self):
        return f'Titulo: {self.title}, Descripcion: {self.description}\n'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if Task.query.all():
        newInstance = Task(f'TareaPiola{Task.query.order_by(Task.id.desc()).first().id}','jijijajajajajajaj')
    else:
        newInstance = Task(f'TareaPiolaOriginal','fui primero jijijija')
    db.session.add(newInstance)
    db.session.commit()
    return f'Oremos dios mio aaaa {Task.query.all()}'

if __name__ == '__main__':
    app.run(debug=True)



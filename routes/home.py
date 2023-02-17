from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.tasks import Task

Home = Blueprint("Home",__name__)

@Home.route("/")
def home():
    if Task.query.all():
        newInstance = Task(f'TareaPiola{Task.query.order_by(Task.id.desc()).first().id}','jijijajajajajajaj')
    else:
        newInstance = Task(f'TareaPiolaOriginal','fui primero jijijija')
    db.session.add(newInstance)
    db.session.commit()
    return f'Oremos dios mio aaaa {Task.query.all()}'
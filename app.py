from create_app import app
from utils.db import db
from models.tasks import Task

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

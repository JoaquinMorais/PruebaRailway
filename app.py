from create_app import app
from utils.db import db
from models.tasks import Task

from routes.home import Home



with app.app_context():
    db.create_all()
    
app.register_blueprint(Home)

if __name__ == '__main__':
    app.run(debug=True)

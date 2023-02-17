from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from create_app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return 'Hello World 3!'

if __name__ == '__main__':
    app.run(debug=True)
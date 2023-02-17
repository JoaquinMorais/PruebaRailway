from create_app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'holis'

if __name__ == '__main__':
    app.run(debug=True)

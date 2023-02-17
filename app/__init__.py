from create_app import app
from utils.db import db

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return 'Hello World 3!'

if __name__ == '__main__':
    app.run(debug=True)
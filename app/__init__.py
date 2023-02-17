from app import app, db, ma

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'holis'

if __name__ == '__main__':
    app.run(debug=True)

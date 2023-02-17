from create_app import app

@app.route('/')
def hello():
    return 'Hello World 2!'

if __name__ == '__main__':
    app.run(debug=True)
from apps.app import app

from routes.calidades.calidades import Calidades

app.register_blueprint(Calidades)

if __name__ == '__main__':
    app.run(debug=True)
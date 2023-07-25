from apps import app, app2

from routes.calidades.calidades import Calidades
from routes.main.main import Main

app.register_blueprint(Calidades)
app2.register_blueprint(Main)

if __name__ == '__main__':
    app.run(debug=True)

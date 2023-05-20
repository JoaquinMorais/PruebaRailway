from app import app
from utils.db import db
from models.models import *

#Lussary
from routes.lussary_config.settings import Home
from routes.lussary_config.Lussary_galeria import Lussary_galeria
from routes.lussary_config.lussary_contact import Lussary_contact
from routes.lussary_config.lussary_colaborador import Lussary_contribuidores
from routes.lussary_config.info_politica import Info_Politica
#VEME
from routes.clientes.VEME.VEME_home import VEME_home
#Fermag
from routes.clientes.Fermag.Fermag_home import Fermag_home
from routes.clientes.Fermag.Fermag_proyectos import Fermag_proyectos
from routes.clientes.Fermag.Fermag_contacto import Fermag_contacto
#Grupo CDL
from routes.clientes.CDL.cdl_home import CDL_home
from routes.clientes.CDL.cdl_servicios import CDL_servicios

#"""
with app.app_context():
    db.create_all()
#"""

#Lussary
app.register_blueprint(Home)
app.register_blueprint(Lussary_galeria)
app.register_blueprint(Info_Politica)
app.register_blueprint(Lussary_contact)
app.register_blueprint(Lussary_contribuidores)
#VEME
app.register_blueprint(VEME_home)
#Fermag
app.register_blueprint(Fermag_home)
app.register_blueprint(Fermag_proyectos)
app.register_blueprint(Fermag_contacto)
#GrupoCDL
app.register_blueprint(CDL_home)
app.register_blueprint(CDL_servicios)




if __name__ == '__main__':
    app.run(debug=True)
     
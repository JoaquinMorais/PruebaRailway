from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

from models.models import SubProyecto
Fermag_home = Blueprint("Fermag_home",__name__)

def getNavBar():
    return [
        ('Empresa','url_for','Fermag_home.FermagHome'),
        ('Noticias','url_for','Fermag_home.FermagNoticias'),
        ('Servicios','id','#servicios-servicios'),
        ('Ubicacion','link','https://www.google.com/maps/?hl=es'),
        ('Contacto','url_for','Fermag_contacto.FermagContacto')
    ]


#Yeah
@Fermag_home.route('/Fermag')
def FermagHome():
    NavBar = getNavBar()
    query = SubProyecto.query.filter_by(descripcion = 'servicio').all()
    Servicios = []
    for i in query:
        diccionario = {}
        diccionario.update({'servicio':i.id_subproyecto})
        diccionario.update({'titulo':i.titulo})

        atributos = i.atributos
        for j in atributos:
            diccionario.update({f'{j.titulo}':f'{j.valor}'})
        Servicios.append(diccionario)
    return render_template('/clientes/Fermag/fermag.html', navBar = NavBar, servicios = Servicios)


@Fermag_home.route('/Fermag/noticias')
def FermagNoticias():
    NavBar = getNavBar()
    Notis = [
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...'),
        ('https://thumbs.dreamstime.com/t/animaci%C3%B3n-del-s%C3%ADmbolo-signo-de-interrogaci%C3%B3n-en-fondo-negro-abstracta-un-120634323.jpg', '???', 'Proximamente...')
    ]
    return render_template('/clientes/Fermag/noticias.html', navBar = NavBar,notis = Notis)

@Fermag_home.route("/Fermag")
def getPrincipalPageFermag():
    return render_template("clientes/Fermag/fermag.html")
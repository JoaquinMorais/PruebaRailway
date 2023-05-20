from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

CDL_home = Blueprint("CDL_home",__name__)



@CDL_home.route('/CDL')
def CDLHome():
    Servicios = [
        ('Traslados de', 'Discapacidad', 'https://cdn.discordapp.com/attachments/709860868720033867/1106583124382588968/discapacidad.jpeg', '#CC0000', '/CDL/discapacidad'),
        ('Traslados de', 'ART', 'https://www.losdefensores.com/wp-content/uploads/2022/10/WorkComp7-1440x357-1.jpg', '#990000', '/CDL/art'),
        ('Traslados en', 'Ambulancias de Baja Complejidad', 'static/src/clientes/CDL/auto1.webp', '#660000', '/CDL/adl')
    ]
    return render_template('/clientes/CDL/cdl.html', servicios = Servicios, navbar = True)



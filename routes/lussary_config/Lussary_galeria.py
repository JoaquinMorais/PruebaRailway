from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

Lussary_galeria = Blueprint("Lussary_galeria",__name__)

@Lussary_galeria.route('/galeria')
def LussaryGaleria():
    Galeria = [
        ('src/Lussary/LogoFermag.webp', 'FERMAG S.A.', 'src/Lussary/FermagPreview.webp', 'Fermag'),
        ('src/Lussary/LogoVeme.webp', 'VEME', 'src/Lussary/VemePreview.webp', 'VEME'),
        ('/src/Lussary/logoCDL.webp', 'GRUPO CDL', 'src/Lussary/CDL_Preview.webp', 'CDL')
    ]
    return render_template('lussary_config/galeria.html', galeria = Galeria,navbar = True)
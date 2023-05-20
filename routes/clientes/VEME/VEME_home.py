from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
import random
VEME_home = Blueprint("VEME_home",__name__)

def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

@VEME_home.route("/VEME")
def getPrincipalPageVEME():
    prendas = ['remeras','vestidos','pantalones','camperas']
    navbar_imgs = []
    for i in prendas:
        navbar_imgs.append(f'{i}6')
        navbar_imgs.append(f'{i}7')
    
    print(mezclar_lista(navbar_imgs[:7]))
    return render_template("clientes/VEME/VEME.html",prendas = mezclar_lista(prendas),navbar_imgs = mezclar_lista(navbar_imgs[:7]))
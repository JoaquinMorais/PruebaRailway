from flask import Blueprint,render_template,redirect,url_for
from utils.db import db
from models.models import *
import random


Lussary_contribuidores = Blueprint("Lussary_contribuidores",__name__)


@Lussary_contribuidores.route("/colaboradores")
def getContribuidores():

    iconos = [
        'Trebol.webp',
        'Heart.webp',
        'Diamond.webp',
        'Spade.webp',
    ]

    cartas = [
        {
            'url_foto':'Diaz1.webp',
            'simbol' : 'J',
            'cant_simbol' : 1,
            'icon' : iconos[3],
            'redirect':'1'
        },
        {
            'url_foto':'Salonia1.webp',
            'simbol' : '4',
            'cant_simbol' : 4,
            'icon' : iconos[2],
            'redirect':'2'
        },
        {
            'url_foto':'Fini1.webp',
            'simbol' : 'Q',
            'cant_simbol' : 1,
            'icon' : iconos[1],
            'redirect':'3'
        },
        {
            'url_foto':'Blazquez1.webp',
            'simbol' : 'A',
            'cant_simbol' : 1,
            'icon' : iconos[0],
            'redirect':'4'
        },
        {
            'url_foto':'Morais1.webp',
            'simbol' : 'A',
            'cant_simbol' : 1,
            'icon' : iconos[3],
            'redirect':'5'
        },
        
    ]
    random.shuffle(cartas)
    return render_template("lussary_config/colaboradores.html",navbar = True,cant_cards = len(cartas),cartas = cartas )




@Lussary_contribuidores.route("/colaborador/<int:id>")
def getContribuidor(id):
    colaborador = Colaborador.query.filter_by(id_colaborador = id).first()
    persona = Persona.query.filter_by(id_persona = id).first()
    contactos = Contacto.query.filter_by(id_persona = id).all()
    descripcionColaborador = DescripcionColaborador.query.filter_by(id_colaborador = id).all()
    
    data = {
        'nombre' : persona.nombre,
        'apellido' : persona.apellido,
        'rol':colaborador.getActividades().title(),
        'url_img' : persona.apellido.split()[0]+'2.webp',
        'descripcion':persona.descripcion,
        'atributos': [{'atributo':'EDAD','descripcion': colaborador.calcularEdad()}]+
        [{'atributo':x.titulo,'descripcion': x.descripcion} for x in descripcionColaborador]
        ,
        'socialMedia':
            [{'clase':x.getIcono(),'link': x.getLink()} for x in contactos if (x.isLink()==True)]
    }


    return render_template("lussary_config/colaborador.html",navbar = True,colaborador = data)
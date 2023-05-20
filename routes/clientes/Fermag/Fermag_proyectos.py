from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

from models.models import *

Fermag_proyectos = Blueprint("Fermag_proyectos",__name__)

@Fermag_proyectos.route("/Fermag/servicio/<x>")    
def FermagProyectos(x):
    query = SubProyecto.query.join(SubDependencia, SubDependencia.id_subhijo == SubProyecto.id_subproyecto).filter(SubDependencia.id_subpadre == x).all()
    titulo = SubProyecto.query.filter_by(id_subproyecto=x).first()
    titulo = titulo.titulo
    datos = []
    pasar = {}
    pasar.update({'titulo':titulo})
    for i in query:
        atributos = i.atributos
        diccionario = {}
        diccionario.update({'titulo':i.titulo})
        diccionario.update({'titulo':i.titulo})
        diccionario.update({'id_subproyecto': int(i.id_subproyecto)})
        for j in atributos:
            if j.categoria.titulo == 'padre':
                diccionario.update({f'{j.titulo}_padre':f'{j.valor}'})
                diccionario.update({f'{j.titulo}_hijos':f'{j.hijos}'})
            else:
                diccionario.update({f'{j.titulo}':f'{j.valor}'})
        datos.append(diccionario)
    pasar.update({'datos':datos})
    return render_template("clientes/Fermag/proyectos.html", datos=pasar)


@Fermag_proyectos.route("/Fermag/servicio/proyecto/<x>")
def FermagProyectoInd(x):
    query = SubProyecto.query.filter_by(id_subproyecto = x).first()
    lista = SubProyecto.query.filter(SubProyecto.id_subproyecto.in_(db.session.query(SubDependencia.id_subpadre).filter_by(id_subhijo = x).subquery()), SubProyecto.titulo != 'Todos').all()
    datos = {}
    servicios = []
    for i in lista:
        servicios.append([f'{i.titulo}', i.id_subproyecto])
    datos.update({'titulo':query.titulo})
    datos.update({'categorias':servicios})
    atributos = query.atributos
    for i in atributos:
        if i.categoria.titulo == 'padre':
            datos.update({f'{i.titulo}_padre':f'{i.valor}'})
            datos.update({f'{i.titulo}_hijos':i.hijos})
        else:
            datos.update({f'{i.titulo}':f'{i.valor}'})
    return render_template("clientes/Fermag/proyectoss.html", datos=datos)

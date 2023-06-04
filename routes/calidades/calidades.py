from flask import Blueprint, render_template

Calidades = Blueprint("Calidades",__name__)

@Calidades.route("/calidades")
def calidades():
    return 'calidades 2'
from flask import Blueprint, render_template, request,url_for,redirect

Main = Blueprint("Main",__name__)

@Main.route("/", methods=['GET','POST'])
def main():
    return 'hola2'
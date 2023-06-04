from flask import Blueprint, render_template, request,url_for,redirect

Calidades = Blueprint("Calidades",__name__)

@Calidades.route("/", methods=['GET','POST'])
def calidades():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            return f'valores: username = {username}, password = {password}'
        except:
            redirect(url_for('Calidades.calidades'))
    else:
        
        return render_template('home.html')
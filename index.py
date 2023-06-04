from flask import Flask,jsonify,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('home.html')

@app.route("/home")
def GetHome():
    print(url_for('GetValue',n='pepe'))
    return redirect(url_for('Home'))

@app.route("/value/<n>")
def GetValue(n):
    return render_template('valor.html',valor = n)


if __name__ == '__main__':
    app.run(debug=True)
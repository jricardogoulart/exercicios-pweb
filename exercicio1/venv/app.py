from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pgprincipal():
    return render_template('pgprincipal.html',titulo='Página Principal')

@app.route("/login")
def login():
    return render_template('login.html',titulo='Login')

@app.route('/clientes')
def pgclientes():
    return render_template('pgclientes.html',titulo='Página Clientes')

app.run()
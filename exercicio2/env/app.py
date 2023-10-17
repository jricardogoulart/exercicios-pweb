from flask import Flask, render_template, request,redirect, url_for


app = Flask(__name__)
usuarios_permitidos = {"admin": "123"}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username in usuarios_permitidos and usuarios_permitidos[username] == password:
        return redirect(url_for('sucesso'))
    else:
        return redirect(url_for('erro'))

@app.route('/sucesso')
def sucesso():
    return render_template('tabela.html')
    


@app.route('/erro')
def erro():
    return "Usuário ou senha incorretos. Tente novamente."

    
if __name__ == '__main__':
    app.run(debug=True)
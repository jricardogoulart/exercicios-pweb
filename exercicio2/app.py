from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)
usuarios_permitidos = {"admin": "123"}

@app.route('/')
def index():
    return render_template('index.html')

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
    return "Login realizado com sucesso!"

@app.route('/erro')
def erro():
    return "Usuário ou senha incorretos. Tente novamente."
#ChatGPT tá Salvando essas Aulas
    
if __name__ == '__main__':
    app.run(debug=True)
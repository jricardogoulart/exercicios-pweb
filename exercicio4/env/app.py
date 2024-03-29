from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)
usuarios_permitidos = {"admin": "123"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def logineffect():
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username in usuarios_permitidos and usuarios_permitidos[username] == password:
        return redirect(url_for('sucesso'))
    else:
        return redirect(url_for('erro'))

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/sucesso')
def sucesso():
    return render_template('table.html', titulo="Lista dos Clientes")

@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Obtém os dados do formulário
    username = request.form.get('username')
    password = request.form.get('password')

    # Verifica se o usuário já existe no dicionário de usuários permitidos
    if username in usuarios_permitidos:
        return "Usuário já cadastrado"

    # Adiciona o novo usuário ao dicionário
    usuarios_permitidos[username] = password

    alert_message = "Usuário Cadastrado com Sucesso"
    return render_template('alert.html', alert_message=alert_message)
    

@app.route('/erro')
def erro():
    return "Usuário ou senha incorretos. Tente novamente."
#ChatGPT tá Salvando essas Aulas
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request,redirect, url_for,flash
import mysql.connector

app = Flask(__name__)
usuarios_permitidos = {"admin": "123"}

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registrar')
def criar():
    db = mysql.connector.connect(
        host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user='aluno_fatec',
        password='aluno_fatec',
        database='meu_banco'
    )
    mycursor = db.cursor()
    query = "select usuario, senha from ze_TB_user"
    mycursor.execute(query)
    resultado = mycursor.fetchall()


    return render_template('register.html', usuarios = resultado)

@app.route('/registrando',methods=['POST'])
def register():
    db = mysql.connector.connect(
        host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user='aluno_fatec',
        password='aluno_fatec',
        database='meu_banco'
    )
    username = request.form.get('usuario')
    password = request.form.get('senha')

    mycursor = db.cursor()
    query = "INSERT INTO ze_TB_user (usuario,senha) VALUES(%s,%s)"
    values = (username, password)
    mycursor.execute(query,values)
    db.commit()
    return 'Usuário Cadastrado com sucesso!'



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
    return render_template('tabela.html',titulo='Cadastros Clientes')
    
@app.route('/deleteUser/<usuario>')
def delete(usuario):
    db = mysql.connector.connect(
        host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user='aluno_fatec',
        password='aluno_fatec',
        database='meu_banco'
    )
    mycursor = db.cursor()
    query = "delete from ze_TB_user where usuario = '"+ usuario + "'"
    print(query)
    mycursor.execute(query)
    db.commit()
    return redirect(url_for('criar'))

@app.route('/changeUser/<usuario>')
def change(usuario):
    db = mysql.connector.connect(
        host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
        user='aluno_fatec',
        password='aluno_fatec',
        database='meu_banco'
    )
    mycursor = db.cursor()
    query="select usuario,senha from ze_TB_user where usuario = '"+ usuario +"'"
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('change.html', usuarios=resultado) 
    

@app.route('/erro')
def erro():
    return "Usuário ou senha incorretos. Tente novamente."

    
if __name__ == '__main__':
    app.run(debug=True)
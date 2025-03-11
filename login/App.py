from bottle import Bottle, run, template, request

app = Bottle()

# Lista de usuários e senhas de exemplo
usuarios = {
    "usuario1@example.com": "senha123",
    "usuario2@example.com": "senha456"
}

@app.route('/login', method='GET')
def login_form():
    return template('login_form')

@app.route('/login', method='POST')
def login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    
    # Verificar se o email e senha são válidos
    if email in usuarios and usuarios[email] == senha:
        return "Encontrado"
    else:
        return "Inexistente"

run(app, host='localhost', port=8080)

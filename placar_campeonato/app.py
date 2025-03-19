from bottle import Bottle, request, template, redirect

app = Bottle()

# Listas para armazenar dados
equipes = []
confrontos = []

@app.route('/')
def index():
    return template('''
        <h2>Placar de Campeonato</h2>
        <a href="/cadastro">Cadastrar Equipe</a> | 
        <a href="/equipes">Listar Equipes</a> | 
        <a href="/confronto">Registrar Confronto</a> | 
        <a href="/resultados">Resultados</a>
    ''')

@app.route('/cadastro', method=['GET', 'POST'])
def cadastro_equipe():
    if request.method == 'POST':
        nome = request.forms.get('nome')
        tecnico = request.forms.get('tecnico')
        capitao = request.forms.get('capitao')
        equipes.append({'nome': nome, 'tecnico': tecnico, 'capitao': capitao})
        return redirect('/equipes')
    return template('''
        <h2>Cadastrar Equipe</h2>
        <form action="/cadastro" method="post">
            Nome: <input type="text" name="nome" required><br>
            Técnico: <input type="text" name="tecnico" required><br>
            Capitão: <input type="text" name="capitao" required><br>
            <input type="submit" value="Cadastrar">
        </form>
    ''')

@app.route('/equipes')
def listar_equipes():
    return template('''
        <h2>Equipes Cadastradas</h2>
        <ul>
        % for equipe in equipes:
            <li>{{equipe['nome']}} - Técnico: {{equipe['tecnico']}}, Capitão: {{equipe['capitao']}}</li>
        % end
        </ul>
        <a href="/">Voltar</a>
    ''', equipes=equipes)

@app.route('/confronto', method=['GET', 'POST'])
def registrar_confronto():
    if request.method == 'POST':
        equipe1 = request.forms.get('equipe1')
        equipe2 = request.forms.get('equipe2')
        placar1 = request.forms.get('placar1')
        placar2 = request.forms.get('placar2')
        confrontos.append({'equipe1': equipe1, 'placar1': placar1, 'equipe2': equipe2, 'placar2': placar2})
        return redirect('/resultados')
    return template('''
        <h2>Registrar Confronto</h2>
        <form action="/confronto" method="post">
            Equipe 1: <input type="text" name="equipe1" required><br>
            Placar: <input type="number" name="placar1" required><br>
            Equipe 2: <input type="text" name="equipe2" required><br>
            Placar: <input type="number" name="placar2" required><br>
            <input type="submit" value="Registrar">
        </form>
    ''')

@app.route('/resultados')
def mostrar_resultados():
    return template('''
        <h2>Resultados dos Confrontos</h2>
        <ul>
        % for jogo in confrontos:
            <li>{{jogo['equipe1']}} {{jogo['placar1']}} x {{jogo['placar2']}} {{jogo['equipe2']}}</li>
        % end
        </ul>
        <a href="/">Voltar</a>
    ''', confrontos=confrontos)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)

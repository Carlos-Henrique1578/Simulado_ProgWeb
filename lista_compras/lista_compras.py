from bottle import Bottle, request, template, redirect

app = Bottle()

# Lista de compras simulada
lista_compras = []

@app.route('/')
def index():
    return template('''
        <h2>Lista de Compras</h2>
        <form action="/add" method="post">
            Descrição: <input type="text" name="descricao" required><br>
            Quantidade: <input type="number" name="quantidade" required><br>
            Solicitante: 
            <select name="solicitante">
                <option value="Pai">Pai</option>
                <option value="Mãe">Mãe</option>
                <option value="Filhos">Filhos</option>
            </select><br>
            <input type="submit" value="Adicionar">
        </form>
        <h3>Itens:</h3>
        <table border="1">
            <tr><th>Descrição</th><th>Quantidade</th><th>Solicitante</th></tr>
            % for item in lista:
                <tr>
                    <td>{{item['descricao']}}</td>
                    <td>{{item['quantidade']}}</td>
                    <td>{{item['solicitante']}}</td>
                </tr>
            % end
        </table>
        <form action="/limpar" method="post">
            <input type="submit" value="Limpar Lista">
        </form>
    ''', lista=lista_compras)

@app.route('/add', method='POST')
def add_item():
    descricao = request.forms.get('descricao')
    quantidade = request.forms.get('quantidade')
    solicitante = request.forms.get('solicitante')
    
    lista_compras.append({'descricao': descricao, 'quantidade': quantidade, 'solicitante': solicitante})
    return redirect('/')

@app.route('/limpar', method='POST')
def limpar_lista():
    lista_compras.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)

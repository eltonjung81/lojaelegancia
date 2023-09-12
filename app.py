
from flask import Flask, request, render_template, jsonify, g
import sqlite3
from flask_cors import CORS  # Importe a extensão CORS

app = Flask(__name__)
CORS(app)
# Configuração do banco de dados
DATABASE = 'dados_cliente.db'

# Função para obter uma conexão com o banco de dados
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Função para fechar a conexão com o banco de dados após a solicitação
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Cria a tabela se ela não existir
def criar_tabela():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            celular TEXT NOT NULL,
            cep TEXT NOT NULL,
            cidade TEXT NOT NULL,
            bairro TEXT NOT NULL,
            rua TEXT NOT NULL,
            numero TEXT NOT NULL,
            tamanho TEXT NOT NULL
        )
    ''')
    conn.commit()

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome = request.form['nome']
        celular = request.form['celular']
        cep = request.form['cep']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']
        tamanho = request.form['tamanho']

        # Insira os dados no banco de dados
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nome, celular, cep, cidade, bairro, rua, numero, tamanho) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (nome, celular, cep, cidade, bairro, rua, numero, tamanho))
        conn.commit()

    return render_template('index.html')

# Rota para o formulário
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Lógica de processamento do formulário, se necessário
        pass  # Substitua por sua lógica de processamento

    return render_template('formulario.html')

# Rota para receber os dados do formulário via AJAX
@app.route('/enviar-formulario', methods=['POST'])
def receber_formulario():
    if request.method == 'POST':
        # Receba os dados do formulário como JSON
        dados_formulario = request.json

        # Extraia os dados do objeto JSON
        nome = dados_formulario.get('nome')
        celular = dados_formulario.get('celular')
        cep = dados_formulario.get('cep')
        cidade = dados_formulario.get('cidade')
        bairro = dados_formulario.get('bairro')
        rua = dados_formulario.get('rua')
        numero = dados_formulario.get('numero')
        tamanho = dados_formulario.get('tamanho')

        # Valide os dados, se necessário

        # Insira os dados no banco de dados
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nome, celular, cep, cidade, bairro, rua, numero, tamanho) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (nome, celular, cep, cidade, bairro, rua, numero, tamanho))
        conn.commit()

        # Responda com uma mensagem de sucesso
        return jsonify({'message': 'Dados recebidos e inseridos com sucesso!'}), 200
    else:
        return jsonify({'error': 'Método não permitido'}), 405

# Rota para visualizar os dados do banco de dados
@app.route('/ver-dados', methods=['GET'])
def ver_dados():
    # Consulta os dados da tabela clientes
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    dados_clientes = cursor.fetchall()  # Obtém todos os registros

    # Renderiza uma página HTML para exibir os dados
    return render_template('ver_dados.html', dados=dados_clientes)
@app.route('/qrcode')
def qrcode():
    # Qualquer lógica de processamento necessário aqui
    return render_template('qrcode.html')

if __name__ == '__main__':
    with app.app_context():
        criar_tabela()  # Certifica-se de criar a tabela antes de iniciar o aplicativo
    app.run(debug=True)

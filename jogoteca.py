from pickle import TRUE
from flask import Flask, render_template, request, redirect, session, flash, url_for, abort, g
import usuarios


class Game:
    def __init__(self, nome, categoria, video_game):
        self.nome = nome
        self.categoria = categoria
        self.video_game = video_game


game0 = Game('God of War', 'Ação', 'PS2')
game1 = Game('CS:GO', 'FPS', 'PC')
game2 = Game('Horizon Zero Dawn', 'RPG', 'PS4')
game3 = Game('Batman Arkhan Knight', 'RPG', 'PS3/PS4 & XboxOne')

lista = [game0, game1, game2, game3]

app = Flask(__name__)
app.secret_key = 'ifmg'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Meus Jogos', jogos=lista)


@app.route('/novo')
def new():
    if not usuario_logado():
        abort(403)

    return render_template('novo.html', titulo="Meus Jogos")


@app.route('/criar', methods=['POST', ])
def create():
    if not usuario_logado():
        abort(403)

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Game(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

# Esse código é para quando for rodar no Replit
#app.run(host='0.0.0.0', debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = usuarios.buscar(email, senha)
        if usuario is None:
            flash('Usuário/ Senha Inválidos.')
        else:
            session['usuario_email'] = usuario.email
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario_nome', None)
    return redirect(url_for('index'))


def usuario_logado():
    return 'usuario_email' in session


@app.errorhandler(403)
def acesso_negado(erro):
    return render_template('acesso_negado.html', titulo='Ops!'), 403


@app.before_request
def carregar_usuario():
    if 'usuario_email' in session:
        g.usuario = usuarios.buscar_por_email(session['usuario_email'])


app.run(debug=True)

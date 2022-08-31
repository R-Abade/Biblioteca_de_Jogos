from pickle import TRUE
from flask import Flask, render_template, request


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

class Usuario:
    def_init_(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

lista_usuarios = [
    Usuario('Abade', raphaelabade10@gmail.com, '123')
    Usuario('Diego', diegoplays@gmail.com, 'YameteKudasai')
    ]

dict_usuario = {
    usuario.email usuario for usuario in lista_usuarios
}

def buscar(email, senha):
    usuario = dict_usuario.get(email)
    if usuario != None and usuario.senha == senha:
        return usuario
    else:
        return None


app = Flask(__name__)

app.secret_key = 'ifmg'


@app.route('/')
def hi():
    return render_template('lista.html', titulo='Meus Jogos', jogos=lista)


@app.route('/novo')
def new():
    return render_template('novo.html', titulo="Meus Jogos")


@app.route('/criar', methods=['post', ])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Game(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo="Jogos", jogos=lista)

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


app.run(debug=True)

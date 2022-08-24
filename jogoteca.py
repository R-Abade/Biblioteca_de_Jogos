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

app = Flask(__name__)


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


app.run(debug=True)

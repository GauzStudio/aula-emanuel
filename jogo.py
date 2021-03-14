from classes.Game import Game
from classes.Mundo import Mundo
from classes.atores.atores import Bandido, Heroi
from classes.ObjetoDoMundo import ObjetoDoMundo
import sys


def geraLinhaInicial(comprimento, valor='.'):
    linha = []
    for _ in range(comprimento):
        linha.append(valor)
    return linha


# TABULEIRO


def geraTabuleiroInicial(comprimento, altura, valor='.'):
    tabuleiro = []
    for _ in range(altura):
        tabuleiro.append(geraLinhaInicial(comprimento, valor))
    return tabuleiro


# JOGO


# JOGADOR
def geraInstrucoes():
    return {}

# def geraInstrucoesASeremImpressas(instrucoes, dimensoes, offsetX = 0, offsetY = 0):
#     newDictionary = {}
#     for k,v in instrucoes.items():

#         x,y = k.split(',')
#         x = int(x)
#         y = int(y)

#         if x >= offsetX and x <= dimensoes['x'] + offsetX and y >= offsetY and y <= dimensoes['y'] + offsetY:
#             newDictionary[geraCoordenada(x + offsetX, y + offsetY)] = v
#     return newDictionary


# variáveis
comprimento = 10
largura = 10

# INICIO

# cria a classe Mundo
mundo = Mundo(comprimento, largura)

# adiciona personagens
# aqui é aonde podemos colocar aleatoriedade no jogo
mundo.adicionaObjeto(ObjetoDoMundo(Heroi('Emanuel'), 0, 0))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Cid'), 2, 2))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Raton'), 4, 6))

# cria a classe Game
game = Game(mundo)


# continuar o loop enquanto 'sair' for 'False'
def rodarTurnos(turno):
    sair = False
    while sair == False:
        turno, sair = game.turnoTotal(turno)


rodarTurnos(0)
# fim do jogo

repetir = input('Quer jogar novamente?')
if (repetir == 's'):
    print('Vamos lá!')
else:
    print('Até a proxima!')
    sys.exit()

from objetos import Bandido, Game, Heroi, Mundo, ObjetoDoMundo
from funcoes import geraCoordenada
import os
def clear(): return os.system('cls')

def geraLinhaInicial(comprimento, valor='.'):
    linha = []
    for _ in range(comprimento):
        linha.append(valor)
    return linha


def tranformarItemsEmString(linha):
    linhaSoDeString = []
    for item in linha:
        linhaSoDeString.append(str(item))
    return linhaSoDeString


def imprimeLinha(linha):
    linhaSoDeString = tranformarItemsEmString(linha)
    print(' '.join(linhaSoDeString))

# TABULEIRO


def geraTabuleiroInicial(comprimento, altura, valor='.'):
    tabuleiro = []
    for _ in range(altura):
        tabuleiro.append(geraLinhaInicial(comprimento, valor))
    return tabuleiro


def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        imprimeLinha(linha)

# JOGO


def geraLinha(altura, comprimento, dicionario, valorBase='.'):
    linha = []
    for numero in range(comprimento):
        try:
            coordenada = geraCoordenada(numero, altura)
            valor = dicionario[coordenada]
        except(KeyError):
            valor = valorBase
        linha.append(valor)
    return linha


def geraTabuleiro(dimensoes, dicionario, valorBase='.'):
    tabuleiro = []
    for y in range(dimensoes['y']):
        linha = geraLinha(y, dimensoes['x'], dicionario, valorBase)
        tabuleiro.append(linha)
    return tabuleiro


# JOGADOR
def geraInstrucoes():
    return {}




def geraDimensoes(comprimento, altura):
    return {
        'x': comprimento,
        'y': altura,
    }

# def geraInstrucoesASeremImpressas(instrucoes, dimensoes, offsetX = 0, offsetY = 0):
#     newDictionary = {}
#     for k,v in instrucoes.items():
        
#         x,y = k.split(',')
#         x = int(x)
#         y = int(y)

#         if x >= offsetX and x <= dimensoes['x'] + offsetX and y >= offsetY and y <= dimensoes['y'] + offsetY:
#             newDictionary[geraCoordenada(x + offsetX, y + offsetY)] = v
#     return newDictionary

def mostraTabuleiro(dimensoes, instrucoes):
    # instrucoesASeremImpressas = geraInstrucoesASeremImpressas(instrucoes, dimensoes, offsetX, offsetY)
    tabuleiro = geraTabuleiro(dimensoes, instrucoes)
    imprimeTabuleiro(tabuleiro)

# Utilidades


def novoTurno(dimensoes, instrucoes, mundo:Mundo):
    # finge que espera input e limpa a tela
    clear()
    for item in mundo.getItens():
        print(item.objeto.simbolo, ' => ', item.objeto.nome)
    print('\n')

    # for item in mundo.getItens():
    #     if item.objeto.simbolo == '@':
    mostraTabuleiro(dimensoes, instrucoes)


# INICIALIZA
mundo = Mundo(15, 15)
heroi = mundo.adicionaObjeto(ObjetoDoMundo(Heroi('Emanuel'), 0, 0))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Cid'), 2, 2))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Raton'), 4, 6))
game = Game(mundo)
# instrucoes = mundo.geraInstrucoes()

# turno 0
# dimensoes = geraDimensoes(10, 10)
# inicializaPlayer(instrucoes, dimensoes)
dimensoes = geraDimensoes(mundo.comprimento(), mundo.profundidade())

for turno in range(30):
    # turno inicial
    if turno != 0:
        game.turno(heroi)
    instrucoes = mundo.geraInstrucoes()
    novoTurno(dimensoes, instrucoes, mundo)
    
    # ver se o player venceu
    if len(mundo.items) == 1:
        print("Parabéns, voce venceu!")
        exit()

# Próxima Aula

# -> Limitar movimento para tamanho do tabuleiro
# -> Ganhar o Jogo
# -> Criar um executável do Jogo

# -> Criar a inteligencia artificial dos bandidos
# -> Melhorar o tabuleiro
# -> Permitir que o Jogador faça jogadas
# -> unificar o comportamento do turno em uma só função

# TESTES2
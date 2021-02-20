import time
import random
from dataclasses import dataclass
from typing import List, Optional, Union

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


def geraCoordenada(x, y):
    return "%d,%d" % (x, y)


def geraLinha(altura, comprimento, dicionario, valorBase='.'):
    linha = []
    for numero in range(comprimento):
        try:
            coordenada = geraCoordenada(altura, numero)
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


def insereObjectoEmPosicao(instrucoes, objeto, coordenada):
    # no momento, só aceita objectos com 1 caractere
    if(len(objeto) > 1):
        raise Exception("O objeto não pode ter mais que um caractere.")

    novasInstrucoes = {k: v for k, v in instrucoes.items()}
    novasInstrucoes[coordenada] = objeto
    return novasInstrucoes


def removeObjectoEmPosicao(instrucoes, coordenada):
    objeto = instrucoes[coordenada]

    novasInstrucoes = {k: v for k, v in instrucoes.items()}
    novasInstrucoes.pop(coordenada)
    return novasInstrucoes, objeto


def moveObjecto(instrucoes, de, para):
    instrucoesDepoisDeRemover, objeto = removeObjectoEmPosicao(instrucoes, de)
    instrucoesDepoisDeInserir = insereObjectoEmPosicao(
        instrucoesDepoisDeRemover, objeto, para)
    return instrucoesDepoisDeInserir


def geraDimensoes(comprimento, altura):
    return {
        'x': comprimento,
        'y': altura,
    }

def mostraTabuleiro(dimensoes, instrucoes):
    tabuleiro = geraTabuleiro(dimensoes, instrucoes)
    imprimeTabuleiro(tabuleiro)

# INICIAR
# dicionarioLinear = {
#     "0": "#",
#     "3": "@",
#     "6": "*",
# }
# linha = geraLinha(10, dicionarioLinear)
# imprimeLinha(linha)

# Utilidades


def novoTurno(dimensoes, instrucoes):
    # finge que espera input e limpa a tela
    time.sleep(1)
    print('\n\n\n\n')
    mostraTabuleiro(dimensoes, instrucoes)

@dataclass
class Heroi:
    def __init__(self, nome):
        self.nome = nome
    simbolo = '@'

@dataclass
class Bandido:
    def __init__(self, nome = 'Bandido'):
        self.nome = nome
    simbolo = '%'

@dataclass
class ObjetoDoMundo:
    def __init__(self, objeto, x, y):
        self.objeto = objeto
        self.x = x
        self.y = y

    #id para classificar objetos no mundo
    id: Optional[str]

    x:Optional[int]
    y:Optional[int]
    objeto: Union[Heroi, Bandido]

"""
O Mundo é equivalente as instruções.

Ele tem uma lista de objetos que estão dentro do mundo.

Essa lista contém classes do tipo: ObjetoDoMundo

maxX é equivalente à dimensoes['x']
maxY é equivalente à dimensoes['y']
"""
class Mundo:

    #dimensões
    maxX:int # comprimento
    maxY:int # altura

    #items no mundo
    items:List[ObjetoDoMundo] = []

    def __init__(self, x, y):
        self.maxX = x
        self.maxY = y
    
    def comprimento(self):
        return self.maxX

    def profundidade(self):
        return self.maxY

    def adicionaObjeto(self, objeto:ObjetoDoMundo):
        # gera id aleatório
        id = str(random.randint(1,1000000))

        objeto.id = id
        self.items.append(objeto)

        return objeto

    def removeObjeto(self, objeto:ObjetoDoMundo):
        for index, item in enumerate(self.items):
            if item.id == objeto.id:
                self.items.pop(index)

    def geraInstrucoes(self):
        instrucoes = {}
        for item in self.items:
            instrucoes[geraCoordenada(item.x, item.y)] = item.objeto.simbolo
        return instrucoes

    def getItens(self):
        return self.items



# instrucoesIniciais = {
#     "0,1": "#",
#     "6,7": "*",
# }


# def insereObjeto(instrucoes, min, max, objeto):
#     instrucoes[geraCoordenada(random.randint(
#         min, max), random.randint(min, max))] = objeto


# def inicializaPlayer(instrucoes, dimensoes):
#     insereObjeto(instrucoes, 0, dimensoes['x'] - 1, '@')

### INICIALIZA
mundo = Mundo(10,10)
mundo.adicionaObjeto(ObjetoDoMundo(Heroi('Emanuel'), 0,0))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Cid'), 2,2))
mundo.adicionaObjeto(ObjetoDoMundo(Bandido('El Raton'), 4,6))
instrucoes = mundo.geraInstrucoes()

# turno 0
# dimensoes = geraDimensoes(10, 10)
# inicializaPlayer(instrucoes, dimensoes)
profundidade = mundo.profundidade()
novoTurno(geraDimensoes(mundo.comprimento(), profundidade), instrucoes)

for item in mundo.getItens():
    print(item.objeto.simbolo, ' => ', item.objeto.nome)

# # turno 1
# instrucoesTurno1 = moveObjecto(instrucoesIniciais, "0,0", "0,1")
# novoTurno(dimensoes, instrucoesTurno1)

# # turno 2
# instrucoesTurno2 = moveObjecto(instrucoesTurno1, "0,1", "0,2")
# novoTurno(dimensoes, instrucoesTurno2)

# # turno 3
# instrucoesTurno3 = moveObjecto(instrucoesTurno2, "0,2", "0,3")
# novoTurno(dimensoes, instrucoesTurno3)

# Próxima Aula

# -> Mover o Jogador
# -> Melhorar o tabuleiro
# -> Permitir que o Jogador faça jogadas
# -> unificar o comportamento do turno em uma só função

# TESTES


def rodarTestes():
    print(geraLinhaInicial(8))
    print(geraLinhaInicial(8, ' '))
    print(geraLinhaInicial(8, 0))

    imprimeLinha(geraLinhaInicial(8))
    imprimeLinha(geraLinhaInicial(8, ' '))
    imprimeLinha(geraLinhaInicial(8, 0))

    imprimeTabuleiro(geraTabuleiroInicial(10, 10))
    imprimeTabuleiro(geraTabuleiroInicial(10, 10, ' '))
    imprimeTabuleiro(geraTabuleiroInicial(10, 10, 0))

# rodarTestes()

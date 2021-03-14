import sys
import os
import random
from dataclasses import dataclass
from typing import List, Optional, Union
import msvcrt

import utilidades
import graficos
import interface

# retorna o valor ou entre um intervalo max, min. Ex. se for 11 e o máximo 10, vai retornar 10


def clamp(n, smallest, largest): return max(smallest, min(n, largest))
def clear(): return os.system('cls')


@dataclass
class Heroi:
    def __init__(self, nome):
        self.nome = nome
    simbolo = graficos.graficos['simbolos']['heroi']


@dataclass
class Bandido:
    def __init__(self, nome='Bandido'):
        self.nome = nome
    simbolo = graficos.graficos['simbolos']['bandido']


@dataclass
class ObjetoDoMundo:
    def __init__(self, objeto, x, y):
        self.objeto = objeto
        self.x = x
        self.y = y

    # id para classificar objetos no mundo

    x: Optional[int]
    y: Optional[int]
    objeto: Union[Heroi, Bandido]

    id: str = '0'


"""
O Mundo é equivalente as instruções.

Ele tem uma lista de objetos que estão dentro do mundo.

Essa lista contém classes do tipo: ObjetoDoMundo

maxX é equivalente à dimensoes['x']
maxY é equivalente à dimensoes['y']
"""


class Mundo:

    # dimensões
    maxX: int  # comprimento
    maxY: int  # altura

    # items no mundo
    items: List[ObjetoDoMundo] = []

    def __init__(self, x, y):
        self.maxX = x
        self.maxY = y

    def comprimento(self):
        return self.maxX

    def profundidade(self):
        return self.maxY

    def adicionaObjeto(self, objeto: ObjetoDoMundo):
        # gera id aleatório
        id = str(random.randint(1, 1000000))

        objeto.id = id
        self.items.append(objeto)

        return objeto

    def removeObjeto(self, objeto: ObjetoDoMundo):
        _, index = self.getItemPorId(objeto)  # type: ignore
        if index:
            self.items.pop(index)

    def getItemPorId(self, objeto: ObjetoDoMundo):
        for index, item in enumerate(self.items):
            if item.id == objeto.id:
                return item, index
        return None, None

    def getItemPorSimbolo(self, simbolo):
        items = []
        for _, item in enumerate(self.items):
            if item.objeto.simbolo == simbolo:
                items.append(item)
        return items

    def moveObjeto(self, objeto: ObjetoDoMundo, x: int, y: int):
        objetoAchado, _ = self.getItemPorId(objeto)
        if objetoAchado == None:
            return False

        # checar se já existem items no mesmo lugar
        itemNaPosicao = self.getObjetosEmPosicao(x, y)
        if len(itemNaPosicao) > 0:
            self.onContatoNaMesmaPosicao(x, y, objeto)
        objetoAchado.x = x
        objetoAchado.y = y

        return True

    def onContatoNaMesmaPosicao(self, x: int, y: int, objeto: ObjetoDoMundo):
        items = self.getObjetosEmPosicao(x, y)
        for item in items:
            if item.id != objeto.id:
                self.removeObjeto(item)

        return True  # False se não puder mover

    def getObjetosEmPosicao(self, x: int, y: int):
        items: List[ObjetoDoMundo] = []
        for item in self.items:
            if item.x == x and item.y == y:
                items.append(item)
        return items

    def geraInstrucoes(self):
        instrucoes = {}
        for item in self.items:
            instrucoes[utilidades.geraCoordenada(
                item.x, item.y)] = item.objeto.simbolo
        return instrucoes

    def getItens(self):
        return self.items


def getDirection(key):
    try:
        direction = interface.controle[key]
        return direction
    except(KeyError):
        return None


class Game:
    mundo: Mundo

    def __init__(self, mundo):
        self.mundo = mundo

    def getBandidos(self):
        return self.mundo.getItemPorSimbolo(graficos.graficos['simbolos']['bandido'])

    def moveObjeto(self, objeto, x, y):

        # checa se está querendo continuar parado
        if x == 0 and y == 0:
            return

        # soma a posição anterior mais o vetor de movimento 'x' e 'y'
        paraX = objeto.x + x
        paraY = objeto.y + y

        # checa se movimento já está impedido
        if paraX == self.mundo.comprimento() - 1 and paraY == self.mundo.profundidade() - 1:
            return

        # checa se o para{x ou y} é maior que o comprimento e profundidade do mundo

        paraX = clamp(paraX, 0, self.mundo.comprimento() - 1)
        paraY = clamp(paraY, 0, self.mundo.profundidade() - 1)

        self.mundo.moveObjeto(
            objeto, paraX, paraY)

    def pegaOInputDoTurno(self):
        # recebe o input
        # recebe uma caracter (ex. a, s, k, 1, v) sem o usuário precisar dar 'Enter'
        char = msvcrt.getwch()

        # se for '0' sai do jogo
        if char == '0':
            print('Adios!!!')
            sys.exit()
        return char

    def turnoLogico(self):
        char = self.pegaOInputDoTurno()

        # procura vetor de movimento
        direction = getDirection(char)

        # se não tiver vetor de movimento (direção) retorna
        if direction == None:
            print('Esse caminho não vai para lugar nenhum.')
            return

        # roda os turnos dos personagens

        # pega o herois (no caso só tem um)
        lista = self.mundo.getItemPorSimbolo(
            graficos.graficos['simbolos']['heroi'])
        heroi = lista[0]

        # move o herói baseado no movimento escolhido
        self.moveObjeto(heroi, direction[0], direction[1])

        # pega os outros personagens
        for bandido in self.getBandidos():

            # por enquanto eles se movem aleatóriamente
            self.moveObjeto(bandido, random.randint(-1, 1),
                            random.randint(-1, 1))

    def turnoTotal(self, turno: int):
        # se for o turno inicial gera o mapa antes do primeiro movimento
        if turno != 0:
            # turno lógico
            self.turnoLogico()

        # aumenta o número do turno
        turno += 1

        # gera as primeiras instruções
        instrucoes = self.mundo.geraInstrucoes()

        # gera as dimensões do jogo
        dimensoes = utilidades.geraDimensoes(
            self.mundo.comprimento(), self.mundo.profundidade())
        self.turnoGrafico(dimensoes, instrucoes, self.mundo)

        # ver se o player venceu
        if len(self.mundo.items) == 1:
            print("Parabéns, o %s venceu!" % self.mundo.items[0].objeto.nome)
            return turno, True
        return turno, False

    def turnoGrafico(self, dimensoes, instrucoes, mundo: Mundo):
        # limpa a tela
        clear()

        # cria a legenda
        for item in mundo.getItens():
            print(item.objeto.simbolo, ' => ', item.objeto.nome)

        print('\n')

        graficos.mostraTabuleiro(dimensoes, instrucoes)


class Screen:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def getComprimento(self):
        return self.comprimento

    def getLargura(self):
        return self.largura

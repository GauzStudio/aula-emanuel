from funcoes import geraCoordenada
import random
from dataclasses import dataclass
from typing import List, Optional, Union
import msvcrt

# retorna o valor ou entre um intervalo max, min. Ex. se for 11 e o máximo 10, vai retornar 10
def clamp(n, smallest, largest): return max(smallest, min(n, largest))
@dataclass
class Heroi:
    def __init__(self, nome):
        self.nome = nome
    simbolo = '@'


@dataclass
class Bandido:
    def __init__(self, nome='Bandido'):
        self.nome = nome
    simbolo = '%'


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

    def removeObjeto(self, objeto:ObjetoDoMundo):
        _, index = self.getItemPorId(objeto) #type: ignore
        if index:
            self.items.pop(index)

    def getItemPorId(self, objeto: ObjetoDoMundo):
        for index, item in enumerate(self.items):
            if item.id == objeto.id:
                return item, index
        return None, None

    def moveObjeto(self, objeto: ObjetoDoMundo, x: int, y: int):
        objetoAchado, _ = self.getItemPorId(objeto)
        if objetoAchado == None:
            return False
        
        #checar se já existem items no mesmo lugar
        itemNaPosicao = self.getObjetosEmPosicao(x, y)
        if len(itemNaPosicao) > 0:
            self.onContatoNaMesmaPosicao(x,y, objeto)
        objetoAchado.x = x
        objetoAchado.y = y

        return True
    def onContatoNaMesmaPosicao(self, x: int, y: int, objeto: ObjetoDoMundo):
        # a principio só temos o heroi
        items = self.getObjetosEmPosicao(x, y)
        for item in items:
            # se for um bandido
            if item.objeto.simbolo == '%':
                self.removeObjeto(item)
        
        return True # False se não puder mover
        
    def getObjetosEmPosicao(self, x:int, y:int):
        items = []
        for item in self.items:
            if item.x == x and item.y == y:
                items.append(item)
        return items

    def geraInstrucoes(self):
        instrucoes = {}
        for item in self.items:
            instrucoes[geraCoordenada(item.x, item.y)] = item.objeto.simbolo
        return instrucoes

    def getItens(self):
        return self.items


translateKeys = {
    '1': [-1, 1],
    '2': [0, 1],
    '3': [1, 1],
    '4': [-1, 0],
    '5': [0, 0],
    '6': [1, 0],
    '7': [1, -1],
    '8': [0, -1],
    '9': [1, -1],
    'w': [0, -1],
    'd': [1, 0],
    'a': [-1, 0],
    's': [0, 1],
}


def getDirection(key):
    try:
        direction = translateKeys[key]
        return direction
    except(KeyError):
        return
class Game:
    mundo: Mundo

    def __init__(self, mundo):
        self.mundo = mundo

    def turno(self, heroi):
        # recebe o input 
        char = msvcrt.getwch()
        
        # se for '0' sai do jogo
        if char == '0':
            print('adios!!!')
            exit()
        
        # procura vetor de movimento
        direction = getDirection(char)

        # se não tiver vetor de movimento (direção) retorna
        if not direction:
            print('Esse caminho não vai para lugar nenhum.')
            return

        # soma a posição anterior mais o vetor de movimento 'x' e 'y'
        paraX = heroi.x + direction[0]
        paraY = heroi.y + direction[1]

        # checa se o para{x ou y} é maior que o comprimento e profundidade do mundo

        paraX = clamp(paraX, 0, self.mundo.comprimento() -1)
        paraY = clamp(paraY, 0, self.mundo.profundidade() -1)

        self.mundo.moveObjeto(
            heroi, paraX, paraY)

class Screen:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def getComprimento(self):
        return self.comprimento

    def getLargura(self):
        return self.largura
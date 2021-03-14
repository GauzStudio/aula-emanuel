import os
import interface


def geraDimensoes(comprimento, altura):
    return {
        'x': comprimento,
        'y': altura,
    }


def geraCoordenada(x, y):
    return "%d,%d" % (x, y)


def getDirection(key):
    try:
        direction = interface.controle[key]
        return direction
    except(KeyError):
        return None

# Outros

# retorna o valor ou entre um intervalo max, min. Ex. se for 11 e o máximo 10, vai retornar 10


def clamp(n, smallest, largest): return max(smallest, min(n, largest))
def clear(): return os.system('cls')

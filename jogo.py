import time

def geraLinhaInicial(comprimento, valor = '.'):
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
def geraTabuleiroInicial(comprimento, altura, valor = '.'):
    tabuleiro = []
    for _ in range(altura):
        tabuleiro.append(geraLinhaInicial(comprimento, valor))
    return tabuleiro

def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        imprimeLinha(linha)

# JOGO
def geraCoordenada(x,y):
    return "%d,%d" % (x,y)

def geraLinha(altura, comprimento, dicionario, valorBase = '.'):
    linha = []
    for numero in range(comprimento):
        try:
            coordenada = geraCoordenada(altura,numero)
            valor = dicionario[coordenada]
        except(KeyError):
            valor = valorBase
        linha.append(valor)
    return linha

def geraTabuleiro(comprimento, altura, dicionario, valorBase = '.'):
    tabuleiro = []
    for y in range(altura):
        linha = geraLinha(y, comprimento, dicionario, valorBase)
        tabuleiro.append(linha)
    return tabuleiro

instrucoes = {
    "0,0": "@",
    "0,1": "#",
    "6,7": "*",
}

# JOGADOR
def geraInstrucoes():
    return {}

def insereObjectoEmPosicao(instrucoes, objeto, coordenada):
    # no momento, só aceita objectos com 1 caractere
    if(len(objeto) > 1):
        raise Exception("O objeto não pode ter mais que um caractere.")

    instrucoes[coordenada] = objeto
    return instrucoes

def removeObjectoEmPosicao(instrucoes, coordenada):
    objeto = instrucoes[coordenada]

    novasInstrucoes = {k: v for k, v in instrucoes.items()}
    novasInstrucoes.pop(coordenada)
    return novasInstrucoes, objeto

def moveObjecto(instrucoes, de, para):
    novasInstrucoes, objeto = removeObjectoEmPosicao(instrucoes, de)
    insereObjectoEmPosicao(novasInstrucoes, objeto, para)
    return novasInstrucoes

# INICIAR
# dicionarioLinear = {
#     "0": "#",
#     "3": "@",
#     "6": "*",
# }
# linha = geraLinha(10, dicionarioLinear)
# imprimeLinha(linha)

# Utilidades
def novoTurno():
    time.sleep(1)
    print('\n\n\n\n')

# turno 0
geraTabuleiro(10,10,instrucoes)
tabuleiro = geraTabuleiro(10,10,instrucoes)
imprimeTabuleiro(tabuleiro)

# turno 1
novoTurno()
instrucoesTurno1 = moveObjecto(instrucoes, "0,0", "0,1")
tabuleiro = geraTabuleiro(10,10,instrucoesTurno1)
imprimeTabuleiro(tabuleiro)

# turno 2
novoTurno()
instrucoesTurno2 = moveObjecto(instrucoesTurno1, "0,1", "0,2")
tabuleiro = geraTabuleiro(10,10,instrucoesTurno2)
imprimeTabuleiro(tabuleiro)

# turno 3
novoTurno()
instrucoesTurno3 = moveObjecto(instrucoesTurno2, "0,2", "0,3")
tabuleiro = geraTabuleiro(10,10,instrucoesTurno3)
imprimeTabuleiro(tabuleiro)


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
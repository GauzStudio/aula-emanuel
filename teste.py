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
def geraLinha(comprimento, dicionario, valorBase = '.'):
    linha = []
    for numero in range(comprimento):
        try:
            valor = dicionario[str(numero)]
        except(KeyError):
            valor = valorBase
        linha.append(valor)
    return linha

def geraTabuleiro(comprimento, altura, dicionario, valorBase = '.'):
    tabuleiro = []
    for y in range(altura):
        linha = []
        for x in range(comprimento):
            try:
                coordenada = "%d,%d" % (x,y)
                valor = dicionario[coordenada]
            except(KeyError):
                valor = valorBase
            linha.append(valor)
        tabuleiro.append(linha)
    return tabuleiro

# INICIAR
# dicionarioLinear = {
#     "0": "#",
#     "3": "@",
#     "6": "*",
# }
# linha = geraLinha(10, dicionarioLinear)
# imprimeLinha(linha)


dicionario = {
    "0,1": "#",
    "3,1": "@",
    "6,7": "*",
}
tabuleiro = geraTabuleiro(10,10,dicionario)
imprimeTabuleiro(tabuleiro)

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
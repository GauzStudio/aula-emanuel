def geraLinha(comprimento, valor = '.'):
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
def geraTabuleiro(comprimento, altura, valor = '.'):
    tabuleiro = []
    for _ in range(altura):
        tabuleiro.append(geraLinha(comprimento, valor))
    return tabuleiro

def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        imprimeLinha(linha)

# INICIAR

# TESTES

def rodarTestes():
    print(geraLinha(8))
    print(geraLinha(8, ' '))
    print(geraLinha(8, 0))

    imprimeLinha(geraLinha(8))
    imprimeLinha(geraLinha(8, ' '))
    imprimeLinha(geraLinha(8, 0))

    imprimeTabuleiro(geraTabuleiro(10, 10))
    imprimeTabuleiro(geraTabuleiro(10, 10, ' '))
    imprimeTabuleiro(geraTabuleiro(10, 10, 0))

rodarTestes()
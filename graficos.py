
from utilidades import geraCoordenada


graficos = {
    'simbolos': {
        'heroi': '@',
        'bandido': '%',
    }
}


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


def tranformarItemsEmString(linha):
    linhaSoDeString = []
    for item in linha:
        linhaSoDeString.append(str(item))
    return linhaSoDeString

# impressão


def imprimeLinha(linha):
    linhaSoDeString = tranformarItemsEmString(linha)
    print(' '.join(linhaSoDeString))


def imprimeTabuleiro(tabuleiro):
    for linha in tabuleiro:
        imprimeLinha(linha)

# display


def mostraTabuleiro(dimensoes, instrucoes):
    # instrucoesASeremImpressas = geraInstrucoesASeremImpressas(instrucoes, dimensoes, offsetX, offsetY)
    tabuleiro = geraTabuleiro(dimensoes, instrucoes)
    imprimeTabuleiro(tabuleiro)

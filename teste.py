def geraLinha(comprimento, valor = '.'):
    linha = []
    for nummber in range(comprimento):
        linha.append(valor)
    return linha

def imprimeLinha(linha):
    linhaSoDeString = []
    for item in linha:
        linhaSoDeString.append(str(item))
    print(' '.join(linhaSoDeString))




# TESTES

print(geraLinha(8))
print(geraLinha(8, ' '))
print(geraLinha(8, 0))

imprimeLinha(geraLinha(8))
imprimeLinha(geraLinha(8, ' '))
imprimeLinha(geraLinha(8, 0))


# criar todos os resultados de somas possíveis
somas = dict()
for x in range(2, 10):
    for y in range(2, 10):
        key = str(x) + "," + str(y)
        reverseKey = str(y) + "," + str(x)
        if reverseKey in somas.keys():
            continue
        somas[key] = x + y

# criar todos os resultados de produtos possíveis
produtos = dict()
for x in range(2, 10):
    for y in range (2, 10):
        key = str(x) + "," + str(y)
        reverseKey = str(y) + "," + str(x)
        if reverseKey in produtos.keys():
            continue
        produtos[key] = x * y

# Mostrar os dicionários criados
for keys, values in somas.items():
    print(keys, " => ", values)

for keys, values in produtos.items():
    print(keys, " => ", values)

# Separa somas e produtos únicos

for key, value in somas.items():
    valoresIguais = []
    for v in somas.values():
        if v == values:
            valoresIguais.append(v)
        if len(valoresIguais) <= 1:
            # esse valor é único na lista 
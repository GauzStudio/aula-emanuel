usuarios = ['emanuel souza', 'fred reis gauz', 'giuliano souza']

index = 1
for usuario in usuarios:
    # cria uma lista separando por espaço
    listaDeNomes = usuario.split(" ")

    # pega o primeiro e segundo valor da lista
    primeiroNome = listaDeNomes[0]
    segundoNome = listaDeNomes[1]

    # junta as iniciais de cada nome
    iniciais = primeiroNome[0] + segundoNome[0]

    # imprime o formato desejado
    print(iniciais.upper(), '- 0' + str(index))
    
    # aumenta um index
    index += 1

# ES - 01
# FG - 02
# GS - 02   2


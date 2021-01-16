from colorama import Fore, Style
def printRed(text):
    print(Fore.RED + text + Style.RESET_ALL)
def printYellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)
def printBlue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)

class Vogal:
    # range -> 1-4
    # 1 -> aberto
    # 2 -> etc...
    abertura = 0

    # range -> 1-9
    # 1-3 -> frontal
    # 4-6 -> central
    # 7-9 -> traseiro
    profundidade = 0

    #nasal (canal fino)
    nasal = False

    #letra correspondente à vogal em português
    letra = ""

    #mais informações sobre a vogal
    def informacoes(self):
        print("A letra correspondente a esse fonema (vogal) é: " + self.letra + ".")
        
#aberturas padrões
abertura = {
    "aberta": 10,
    "semi-aberto":20,
    "semi-fechado": 30,
    "fechado": 40,
}

#profundidades padrões
profundidade = {
    "frontal"   : 2     * 10, # 1 - 3
    "central"   : 5     * 10, # 4 - 6
    "profundo"  : 8     * 10, # 7 - 9
}

#banco de dados
bancoDeDados_Vogais = {
    "a": {
        "abertura": abertura["aberta"],
        "profundidade": profundidade["frontal"],
    },
    "e": {
        "abertura": abertura["semi-aberto"],
        "profundidade": profundidade["frontal"],
    },
    "i": {
        "abertura": abertura["semi-aberto"],
        "profundidade": profundidade["central"],
    },
    "o": {
        "abertura": abertura["semi-fechado"],
        "profundidade": profundidade["profundo"],
    },
    "u": {
        "abertura": abertura["fechado"],
        "profundidade": profundidade["profundo"],
    },
}

def criaInstanciaDaReceitaDaVogal(letraCorrespondenteAVogal):
    instanciaDeVogal = Vogal()
    instanciaDeVogal.abertura = bancoDeDados_Vogais[letraCorrespondenteAVogal]["abertura"]
    instanciaDeVogal.profundidade = bancoDeDados_Vogais[letraCorrespondenteAVogal]["profundidade"]
    instanciaDeVogal.letra = letraCorrespondenteAVogal
    return instanciaDeVogal

#lista de instancias de classes (= objetos)
instanciasDeVogal = [
]

for letraEmFormatoDeString in bancoDeDados_Vogais:
    objeto = criaInstanciaDaReceitaDaVogal(letraEmFormatoDeString)
    instanciasDeVogal.append(objeto)

# for objectoVogal in instanciasDeVogal:
#     print(objectoVogal.abertura)
#     print(objectoVogal.profundidade)
#     print(objectoVogal.informacoes())

texto = input('Digite uma palavra:')
for caracter in texto:
    print('caracter: ' + caracter)
    for vogal in instanciasDeVogal:
        if caracter == vogal.letra:
            printYellow('o caracter: ' + caracter + ' é uma vogal.')


# tecladoPadraoBrasileiro = [
#         ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], # 0
#         ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
#         ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
#         ['*','"',',', ':', ';', '.']]

# tecladoPadraoGrego = [
#         ['q', 'OMEGA', '&', 'r', 't', 'y', 'u', 'i', 'o', 'p'], # 0
#         ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç'],
#         ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
#         ['*','"',',', ':', ';', '.']]


# class medidas:
    # raio = (0,0) #tupple (horizontal, vertical)
    # esticamento = (0,0)
    # profundidade = 0
    # intensificador =0


# def RegraDeSonoridade(valor):
#     fonema = vogais[valor]
#     fonemaARetornar =  {
#         "canalfino":fonema.nasal,
#         "canallargo": {
#             "abertura": fonema.abertura,
#             "profundidade": fonema.profundidade,
#         },
#     }

# regra = RegraDeSonoridade("a")

# print(regra["canalfino"])
# print(regra["canallargo"])



# def EstruturaEmissora(tecladoPadrao):
#     teclado = tecladoPadrao
#     return teclado


# teclado = EstruturaEmissora(tecladoPadraoGrego)
# #... roda o programa


# #roda funções em português
# teclado = EstruturaEmissora(tecladoPadraoBrasileiro)
# def testaTecladoBrasileiro():
#     tecla = teclado[0][2]
#     if(tecla != 'e'):
#         raise Exception("Esperava a tecla 'e', veio a tecla: '" + tecla + "'") 
# testaTecladoBrasileiro()


# struct medidas{
# 	float raio1, raio2, profundidade, esticamento1, esticamento2, intensificador;
# };
# void RegraDeSonoridade(){
# 	float expressao[2];
# 	medidas canalfino;
# 	medidas canallargo;
# 	canalfino.raio1 = 15;
# 	canallargo.raio1 = 70;
# 	canalfino.raio2 = 12;
# 	canallargo.raio2 = 30;
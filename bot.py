import utils,time

class Bot:
    nome = 'bot'
    idade = 0
    genero = 'android'

    def __init__(self, nome, genero):
        # super().__init__()

        self.nome = nome
        self.genero = genero

    def pegarNome(self):
        return self.nome

    def pegarIdade(self):
        return self.idade

    def envelhecer(self):
        self.idade = self.idade + 1

tob = Bot('tob', 'male android')

utils.printYellow('O primeiro aninho do ' + tob.pegarNome())
fraseComAIdade = 'A idade do ' + tob.pegarNome() + ' é: ' + str(tob.pegarIdade())
print(fraseComAIdade)

time.sleep(2)
tob.envelhecer()

utils.printYellow('O segundo aninho do ' + tob.pegarNome())
print('A nova idade do ' + tob.pegarNome() + ' é: ' + str(tob.pegarIdade()))

time.sleep(2)
tob.envelhecer()

utils.printYellow('O terceiro aninho do ' + tob.pegarNome())
print('A nova idade do ' + tob.pegarNome() + ' é: ' + str(tob.pegarIdade()))
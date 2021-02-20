import utils,time,threading
import asyncio

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

def aniversario():
    utils.printYellow('O ' + utils.converteParaNumeroOrdinal(tob.pegarIdade())  + ' aninho do ' + tob.pegarNome())
    # fraseComAIdade = 'A idade do ' + tob.pegarNome() + ' é: ' + str(tob.pegarIdade())
    # print(fraseComAIdade)

def envelherOBot():
        tob.envelhecer()
        aniversario()

print('começar a contar as idades:')
envelherOBot()
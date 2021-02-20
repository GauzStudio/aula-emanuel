# import utils
import time, threading

class Bot:
    nome = 'bot'
    idade = 0

    def __init__(self, nome):
        # super().__init__()

        self.nome = nome

    def dizerIdade(self):
        return self.idade

tob = Bot('tob')


def more1():
    print('mais 4 anos de vida!')
    timer = threading.Timer(4, more1)
    timer.start()

timer = threading.Timer(4, more1)
timer.start()

def loop():
    stop = 0
    while stop < 100:
        print(stop)
        stop += 1
        time.sleep(1)
loop()
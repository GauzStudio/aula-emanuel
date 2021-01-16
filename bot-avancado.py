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
print(tob.dizerIdade())


def more1():
    print('more 1 year')
    timer = threading.Timer(1, more1)
    timer.start()

timer = threading.Timer(1, more1)
timer.start()

def loop():
    stop = 0
    while stop < 100:
        print(stop)
        stop += 1
        time.sleep(1)
#
# Prompt
#
# printRed("Prompt Starting")
from colorama import Fore, Style
def printRed(text):
    print(Fore.RED + text + Style.RESET_ALL)
def printYellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)
def printBlue(text):
    print(Fore.BLUE + text + Style.RESET_ALL)
def printGreen(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

#
# Text To Speech
#
import pyttsx3
engine = pyttsx3.init() #cria o motor. Obs. 'engine' é arbitrario, podia ser qualquer outra coisa: 'motor', 'etc'

# falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()
    engine.stop()


#
# Numeros ordinais
#
from num2words import num2words
def converteParaNumeroOrdinal(numero):
    return num2words(numero, lang='pt-BR', to='ordinal')
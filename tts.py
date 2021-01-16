import pyttsx3

engine = pyttsx3.init()

# falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()
    engine.stop()



# # mudar voz para outra vcz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 200)

engine.say('俺たちは男だ！')
# for voice in voices:
#     print(voice)

# falar alguma coisa
#frase = "Happy new year, Emanuel!"

# criar um texto exemplo
texto = """Receita de Bolo
Primeiro você separa os ingredientes.
Depois você bate os ingredientes.
Após bater você coloca em uma vasilha e no forno.
Finalmente, você aprecia sua criação."""

# pega frases do texto e coloca em uma lista de frases
listaDeFrases = texto.split('\n')
# print('frases para falar :', listaDeFrases.count)

titulo = 'O rato roeu a roupa do rei de roma.'

falar(titulo)

falar('Ouça o texto com a velocidade normal.')
falar(titulo)

# modificar a velocidade da voz
velocidade = engine.getProperty('rate')
falar('A velocidade atual é: ' + str(velocidade))

falar('Ouça o texto com a velocidade 50% mais lenta.')
engine.setProperty('rate', 100)

falar(titulo)


#falar texto com etapas
# for index, frase in enumerate(listaDeFrases):
#     textoParaFalar = 'Etapa ' + str(index + 1) + ', ' + frase
#     print(textoParaFalar)
#     falar(textoParaFalar)
    





# # gravar para arquivo
# engine.save_to_file(texto, 'teste.mp3')
# engine.runAndWait()
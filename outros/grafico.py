from matplotlib import pyplot

# levando em consideração [ [x,y], [x,y], etc...]
pontos = [[10,10],[20,30]]

pontosX = []
pontosY = []
for ponto in pontos:
    pontosX.append(ponto[0])
    pontosY.append(ponto[1])

pyplot.scatter(pontosX, pontosY)
pyplot.axis([0,50,0,50])

pyplot.show()

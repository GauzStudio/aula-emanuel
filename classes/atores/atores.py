# esse arquivo é temporário

from dataclasses import dataclass
import graficos


@dataclass
class Heroi:
    def __init__(self, nome):
        self.nome = nome
    simbolo = graficos.graficos['simbolos']['heroi']


@dataclass
class Bandido:
    def __init__(self, nome='Bandido'):
        self.nome = nome
    simbolo = graficos.graficos['simbolos']['bandido']

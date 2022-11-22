###un fichier stockant l'ensemble des individus existant dans le plan

import random as rdm
import Constantes

class Fruit:
    """les fruits apparaissent de manière aléatoire, ne se déplacent pas et se font manger par les végétariens"""

    def __init__(self):
        self.position = [rdm.uniform(-Constantes.borduresplans[0], Constantes.borduresplans[0]), rdm.uniform(-Constantes.borduresplans[1], Constantes.borduresplans[1])]
        self.indice = 0

class Vegetarien:
    """les végetariens se reproduisent en mangeant des fruits, se déplacent dans le plan et se font manger par les chasseurs"""

    def __init__(self):
        self.
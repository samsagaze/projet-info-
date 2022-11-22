#un fichier contenant quelques fonctions pour se déplacer dans le plan

import Constantes

def mettredansleplan(position):
    [x, y] = position
    [xmax, ymax] = Constantes.borduresplans
    return [x%xmax, y%ymax]

def deplacer(objet, positionfinale):
    objet.position = mettredansleplan(positionfinale)
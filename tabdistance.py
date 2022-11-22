#les fonctions permettant de créer un tableau de vecteurs entre un obet O et un tableau tab = [a0, a1, ...]
#le tableau résultant devra être de la forme [[0, [a0-O]], [1, [a1-O]]...]
#la classe tabvecteurs contient les tableaux vectoriels créées par les fonctions

import plan

def creertabvecteurs(objet):
    [x, y] = objet.position
    tabvecteursfruit = []
    lesfruits = plan.plan.dicofruit
    for indice in lesfruits:
        [xfruit, yfruit] = lesfruits[indice].position
        tabvecteursfruit.append([indice, [xfruit-x, yfruit-y]])
    tabvecteursvegetarien = []
    lesvegetariens = plan.plan.dicovegetarien
    for indice in lesvegetariens:
        [xvegetarien, yvegetarien] = lesvegetariens[indice].position
        tabvecteursvegetarien.append([indice, [xvegetarien - x, yvegetarien - y]])
    tabvecteurschasseur = []
    leschasseurs = plan.plan.dicochasseur
    for indice in leschasseurs:
        [xchasseur, ychasseur] = leschasseurs[indice].position
        tabvecteurschasseur.append([indice, [xchasseur-x, ychasseur-y]])
    return [tabvecteursfruit, tabvecteursvegetarien, tabvecteurschasseur]


class TabVecteurs:

    def __init__(self):
        self.tabvectfruit = []
        self.tabvectvegetarien = []
        self.tabvectchasseur = []

    def actualiser(self, objet):
        [self.tabvectfruit, self.tabvectvegetarien, self.tabvectchasseur] = creertabvecteurs(objet)

    pass



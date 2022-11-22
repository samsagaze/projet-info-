#un fichier stockant l'ensemble des individus existant dans le plan

import random as rdm
import Constantes
import fctionsduplan
import plan
import tabdistance as td
import geometrie as geo
import vecteursdirection


class Fruit:
    """les fruits apparaissent de manière aléatoire, ne se déplacent pas et se font manger par les végétariens"""

    def __init__(self):
        self.position = [rdm.uniform(-Constantes.borduresplans[0], Constantes.borduresplans[0]), rdm.uniform(-Constantes.borduresplans[1], Constantes.borduresplans[1])]
        self.indice = 0
        self.nouveaufruit()

    def nouveaufruit(self):
        self.indice = plan.plan.nombrefruit()
        plan.plan.addfruit(self)

    def supprimerfruit(self):
        plan.plan.delfruit(self.indice)

    pass


class Vegetarien:
    """les végetariens se reproduisent en mangeant des fruits, se déplacent dans le plan et se font manger par les chasseurs"""

    def __init__(self):
        self.position = [rdm.uniform(-Constantes.borduresplans[0], Constantes.borduresplans[0]), rdm.uniform(-Constantes.borduresplans[1], Constantes.borduresplans[1])]
        self.indice = 0
        self.energie = Constantes.energievegetarien
        self.tabvecteurs = td.TabVecteurs()
        self.vecteurs = vecteursdirection.Vecteurs()
        self.nouveauvegetarien()

    def deplacer(self, positionfinale):
       fctionsduplan.deplacer(self, positionfinale)

    def nouveauvegetarien(self):
        self.indice = plan.plan.nombrevegetarien()
        plan.plan.addvegetarien(self)

    def supprimervegetarien(self):
        plan.plan.delvegetarien(self.indice)

    def actualisertabvecteurs(self):
        self.tabvecteurs.actualiser(self)

    def mangerfruit(self):
        tabvectfruit = self.tabvecteurs.tabvectfruit
        for case in tabvectfruit:
            [indice, vecteur] = case
            dis = geo.longeurvecteur(vecteur)
            if dis < Constantes.errormargin:
                if indice in plan.plan.dicofruit:
                    plan.plan.dicofruit[indice].supprimerfruit()
                    self.energie += Constantes.gainenergievegetarien
                    if self.energie >= Constantes.maxenergievegetarien:
                        self.division()

    def division(self):
        [x, y] = self.position
        energie = self.energie
        nouveauvegetarien = Vegetarien()
        nouvelleenergie = energie / 2
        self.energie = nouvelleenergie
        nouveauvegetarien.energie = nouvelleenergie
        [xe, ye] = Constantes.ecartement
        xecartement = rdm.uniform(-xe, xe) / 2
        yecartement = rdm.uniform(-ye, ye) / 2
        fctionsduplan.deplacer(self, [x + xecartement, y + yecartement])
        fctionsduplan.deplacer(nouveauvegetarien, [x - xecartement, y - yecartement])
        nouveauvegetarien.vecteurs = self.vecteurs.copy()
        nouveauvegetarien.vecteurs.mutation()

    def actualiservegetarien(self):
        if self.energie==0:
            self.supprimervegetarien()
        else:
            self.mangerfruit()

    def sedeplacer(self):
        vecteurdeplacement = self.vecteurs.calculvecteurdirection(self.tabvecteurs)
        fctionsduplan.deplacer(self, geo.multiplication(Constantes.vitesse, geo.addition(self.position, vecteurdeplacement)))


    pass


class Chasseur:
    """les chasseurs se reproduisent en mangeant des végétariens, se déplacent dans le plan et ne se font pas manger"""

    def __init__(self):
        self.position = [rdm.uniform(-Constantes.borduresplans[0], Constantes.borduresplans[0]), rdm.uniform(-Constantes.borduresplans[1], Constantes.borduresplans[1])]
        self.indice = 0
        self.energie = Constantes.energiechasseur
        self.tabvecteurs = td.TabVecteurs()
        self.vecteurs = vecteursdirection.Vecteurs()
        self.nouveauchasseur()

    def deplacer(self, positionfinale):
        fctionsduplan.deplacer(self, positionfinale)

    def nouveauchasseur(self):
        self.indice = plan.plan.nombrechasseur()
        plan.plan.addchasseur(self)

    def supprimerchasseur(self):
        plan.plan.delchasseur(self.indice)

    def actualisertabvecteurs(self):
        self.tabvecteurs.actualiser(self)

    def mangervegetarien(self):
        tabvectvegetarien = self.tabvecteurs.tabvectvegetarien
        for case in tabvectvegetarien:
            [indice, vecteur] = case
            dis = geo.longeurvecteur(vecteur)
            if dis < Constantes.errormargin:
                if indice in plan.plan.dicovegetarien:
                    plan.plan.dicovegetarien[indice].supprimervegetarien()
                    self.energie += Constantes.gainenergiechasseur
                    if self.energie >= Constantes.maxenergiechasseur:
                        self.division()

    def division(self):
        [x, y] = self.position
        energie = self.energie
        nouveauchasseur = Chasseur()
        nouvelleenergie = energie / 2
        self.energie = nouvelleenergie
        nouveauchasseur.energie = nouvelleenergie
        [xe, ye] = Constantes.ecartement
        xecartement = rdm.uniform(-xe, xe) / 2
        yecartement = rdm.uniform(-ye, ye) / 2
        fctionsduplan.deplacer(self, [x + xecartement, y + yecartement])
        fctionsduplan.deplacer(nouveauchasseur, [x - xecartement, y - yecartement])
        nouveauchasseur.vecteurs = self.vecteurs.copy()
        nouveauchasseur.vecteurs.mutation()

    def actualiserchasseur(self):
        if self.energie==0:
            self.supprimerchasseur()
        else:
            self.mangervegetarien()

    def sedeplacer(self):
        vecteurdeplacement = self.vecteurs.calculvecteurdirection(self.tabvecteurs)
        fctionsduplan.deplacer(self, geo.multiplication(Constantes.vitesse, geo.addition(self.position, vecteurdeplacement)))

    pass
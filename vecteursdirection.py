#nous allons ici définir une nouvelle classe contenant les coefficients permettant de calculer la direction, coefficients pouvant muter
#ainsi qu'une fonction permettant de calculer sa direction en possèdant sa direction

import triagetableau
import geometrie as geo
import Constantes
import random as rdm


class Vecteurs:
    """definit un vecteur directionnel"""

    def __init__(self):
        self.chasseurcoefficients = [0]
        self.vegetariencoefficients = [0]
        self.fruitcoefficients = [0]

    def copy(self):
        nouveauvecteurs = Vecteurs()
        nouveauvecteurs.vegetariencoefficients = self.vegetariencoefficients.copy()
        nouveauvecteurs.fruitcoefficients = self.fruitcoefficients.copy()
        nouveauvecteurs.chasseurcoefficients = self.chasseurcoefficients.copy()
        return  nouveauvecteurs

    def calculvecteurdirection(self, tabvecteurs):
        tabvectfruit = triagetableau.sorttabvecteur(tabvecteurs.tabvectfruit)
        resultatvecteur = [0 ,0]
        for i in range(len(tabvectfruit)):
            vecteur = tabvectfruit[i][1][1]
            if geo.longeurvecteur(vecteur) >= Constantes.errormargin:
                if len(self.fruitcoefficients)>i:
                    geo.addition(resultatvecteur, geo.multiplication(self.fruitcoefficients[i], vecteur))
                else:
                    geo.addition(resultatvecteur, vecteur)
                    self.fruitcoefficients.append(1)
        tabvectvegetarien = triagetableau.sorttabvecteur(tabvecteurs.tabvectvegetarien)
        for i in range(len(tabvectvegetarien)):
            vecteur = tabvectvegetarien[i][1][1]
            if geo.longeurvecteur(vecteur) >= Constantes.errormargin:
                if len(self.vegetariencoefficients)>i:
                    geo.addition(resultatvecteur, geo.multiplication(self.vegetariencoefficients[i], vecteur))
                else:
                    geo.addition(resultatvecteur, vecteur)
                    self.vegetariencoefficients.append(1)
        tabvectchasseur = triagetableau.sorttabvecteur(tabvecteurs.tabvectchasseur)
        for i in range(len(tabvectchasseur)):
            vecteur = tabvectchasseur[i][1][1]
            if geo.longeurvecteur(vecteur) >= Constantes.errormargin:
                if len(self.chasseurcoefficients) > i:
                    geo.addition(resultatvecteur, geo.multiplication(self.chasseurcoefficients[i], vecteur))
                else:
                    geo.addition(resultatvecteur, vecteur)
                    self.chasseurcoefficients.append(1)
        return resultatvecteur


    def mutation(self):
        for i in range(len(self.fruitcoefficients)):
            coefficient=self.fruitcoefficients[i]
            j=coefficient/Constantes.coefficientmutation
            valeurmutation=rdm.uniform(-j, j)
            self.fruitcoefficients[i]+=valeurmutation
        for i in range(len(self.chasseurcoefficients)):
            coefficient=self.chasseurcoefficients[i]
            j=coefficient/Constantes.coefficientmutation
            valeurmutation=rdm.uniform(-j, j)
            self.chasseurcoefficients[i]+=valeurmutation
        for i in range(len(self.vegetariencoefficients)):
            coefficient=self.vegetariencoefficients[i]
            j=coefficient/Constantes.coefficientmutation
            valeurmutation=rdm.uniform(-j, j)
            self.vegetariencoefficients[i]+=valeurmutation



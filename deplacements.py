import geometrie as geo
import random as rdm
import triagetableau as tt

class Vecteurs:
    """definit un vecteur directionnel"""

    def __init__(self):
        self.Chasseurcoefficients = []
        self.Chasseecoefficients = []
        self.Fruitscoefficients = []
        self.coefficientsmutation = 10

    def deplacements(self, objet, typeobjet, plan):  #typeobjet =  "Chasseur", "Chassee"
        valeurobjet = plan.dico.valeur(objet)
        vecteur=[0, 0]
        if typeobjet=="Chasseur":
            tabvectChasseur=tt.sorttableauvecteur(plan.matvectChasseurChasseur[valeurobjet])
            compteur = 0
            for i in range(len(tabvectChasseur)):
                vect=tabvectChasseur
                if vect!=-1 and geo.longeurvecteur(vect)<objet.awareness and i!=valeurobjet:
                    if i==len(self.Chasseurcoefficients):
                        self.Chasseurcoefficients+=[1]
                        vecteur+=geo.vecteurunitaire(vect)
                    else:
                        vecteur+=geo.multiplication(self.Chasseurcoefficients[compteur], geo.vecteurunitaire(vect))
                    compteur+=1
            tabvectChassee=tt.sorttableauvecteur(plan.matvectChasseurChassee[valeurobjet])
            compteur = 0
            for i in range(len(tabvectChassee)):
                vect=tabvectChassee[i]
                if vect!=-1 and geo.longeurvecteur(vect)<objet.awareness and i!=valeurobjet:
                    if i==len(self.Chasseecoefficients):
                        self.Chasseecoefficients+=[1]
                        vecteur+=geo.vecteurunitaire(vect)
                    else:
                        vecteur+=geo.multiplication(self.Chasseecoefficients[compteur], geo.vecteurunitaire(vect))
                    compteur+=1
            tabvectFruit = tt.sorttableauvecteur(plan.matvectChasseurFruit[valeurobjet])
            compteur = 0
            for i in range(len(tabvectFruit)):
                vect=tabvectFruit[i]
                if vect!=-1 and geo.longeurvecteur(vect)<objet.awareness and i!=valeurobjet:
                    if i==len(self.Fruitscoefficients):
                        self.Fruitscoefficients+=[1]
                        vecteur+=geo.vecteurunitaire(vect)
                    else:
                        vecteur+=geo.multiplication(self.Fruitscoefficients[compteur], geo.vecteurunitaire(vect))
                    compteur+=1
        elif typeobjet == "Chassee":
            tabvectChasseur = tt.sorttableauvecteur(plan.matvectChasseeChasseur[valeurobjet])
            compteur = 0
            for i in range(len(tabvectChasseur)):
                vect = tabvectChasseur[i]
                if vect != -1 and geo.longeurvecteur(vect) < objet.awareness and i != valeurobjet:
                    if i == len(self.Chasseurcoefficients):
                        self.Chasseurcoefficients += [1]
                        vecteur += geo.vecteurunitaire(vect)
                    else:
                        vecteur += geo.multiplication(self.Chasseurcoefficients[compteur], geo.vecteurunitaire(vect))
                compteur += 1
            tabvectChassee = tt.sorttableauvecteur(plan.matvectChasseeChassee[valeurobjet])
            compteur = 0
            for i in range(len(tabvectChassee)):
                vect = tabvectChassee[i]
                if vect != -1 and geo.longeurvecteur(vect) < objet.awareness and i != valeurobjet:
                    if i == len(self.Chasseecoefficients):
                        self.Chasseecoefficients += [1]
                        vecteur += geo.vecteurunitaire(vect)
                    else:
                        vecteur += geo.multiplication(self.Chasseecoefficients[compteur], geo.vecteurunitaire(vect))
                    compteur += 1
            tabvectFruit = tt.sorttableauvecteur(plan.matvectChasseeFruit[valeurobjet])
            compteur = 0
            for i in range(len(tabvectFruit)):
                vect = tabvectFruit[i]
                if vect != -1 and geo.longeurvecteur(vect) < objet.awareness and i != valeurobjet:
                    if i == len(self.Fruitscoefficients):
                        self.Fruitscoefficients += [1]
                        vecteur += geo.vecteurunitaire(vect)
                    else:
                        vecteur += geo.multiplication(self.Fruitscoefficients[compteur], geo.vecteurunitaire(vect))
                    compteur += 1
        return vecteur

    def mutation(self):
        for i in range(len(self.Fruitscoefficients)):
            coefficient=[self.Fruitscoefficients[i]]
            j=coefficient/10
            valeurmutation=rdm.uniform(-j, j)
            self.Fruitscoefficients[i]+=valeurmutation
        for i in range(len(self.Chasseurcoefficients)):
            coefficient=[self.Chasseurcoefficients[i]]
            j=coefficient/10
            valeurmutation=rdm.uniform(-j, j)
            self.Chasseurcoefficients[i]+=valeurmutation
        for i in range(len(self.Chasseecoefficients)):
            coefficient=[self.Chasseecoefficients[i]]
            j=coefficient/10
            valeurmutation=rdm.uniform(-j, j)
            self.Chasseecoefficients[i]+=valeurmutation


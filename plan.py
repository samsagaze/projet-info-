# la classe plan contient la simulation
import Constantes
import persoplans


class Plan:

    def __init__(self):
        self.dicofruit = {}
        self.dicovegetarien = {}
        self.dicochasseur = {}
        self.nbfruit = 0
        self.nbvegetarien = 0
        self.nbchasseur = 0

    def nombrefruit(self):
        return self.nbfruit

    def nombrevegetarien(self):
        return self.nbvegetarien

    def nombrechasseur(self):
        return self.nbchasseur

    def addfruit(self, objet):
        self.dicofruit[self.nbfruit] = objet
        self.nbfruit +=1

    def addvegetarien(self, objet):
        self.dicovegetarien[self.nbvegetarien] = objet
        self.nbvegetarien += 1

    def addchasseur(self, objet):
        self.dicochasseur[self.nbchasseur] = objet
        self.nbchasseur += 1

    def delfruit(self, indice):
        del(self.dicofruit[indice])

    def delvegetarien(self, indice):
        del(self.dicovegetarien[indice])

    def delchasseur(self, indice):
        del(self.dicochasseur[indice])

    def actualisertabvecteurs(self):
        for indice in self.dicovegetarien:
            self.dicovegetarien[indice].actualisertabvecteurs()
        for indice in self.dicochasseur:
            self.dicochasseur[indice].actualisertabvecteurs()

    def actualiserplan(self):
        for indice in list(self.dicovegetarien):
            self.dicovegetarien[indice].actualiservegetarien()
        for indice in list(self.dicochasseur):
            self.dicochasseur[indice].actualiserchasseur()

    def spawnfruit(self):
        for i in range(Constantes.fruitspawnrate):
            fruit = persoplans.Fruit


    def deplacement(self):
        for indice in self.dicovegetarien:
            self.dicovegetarien[indice].sedeplacer()
        for indice in self.dicochasseur:
            self.dicochasseur[indice].sedeplacer()


    pass


plan = Plan()  # le plan qui contient toute la simulation

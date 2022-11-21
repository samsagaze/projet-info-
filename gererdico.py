class Dictionnaire:
    "un dictionnaire stockant l'ensemble des objets du plan ainsi que leur valeur - chaque objet valant entre 0 et"""
    """n-1, où n est le nombre d'objet de ce type ayant existé dans le plan """

    def __init__(self):
        self.nbChassee = 0
        self.nbFruits = 0
        self.nbChasseurs = 0
        self.tailledico = self.nbChassee + self.nbChasseurs + self.nbFruits
        self.dico = {}
        self.tabChassee = []  # un tableau contenant l'ensemble des Chassee
        self.tabChasseur = []  # --------- des chasseurs
        self.tabFruit = []  # -------- des fruits

    def nouveauChassee(self, chassee):
        self.dico[chassee] = self.nbChassee
        self.tabChassee += [chassee]
        self.nbChassee += 1

    def nouveauChasseur(self, chasseur):
        self.dico[chasseur] = self.nbChasseurs
        self.tabChasseur += [chasseur]
        self.nbChasseurs += 1

    def nouveauFruit(self, fruit):
        self.dico[fruit] = self.nbFruits
        self.tabFruit += [fruit]
        self.nbFruits += 1

    def valeur(self, objet):
        return self.dico[objet]

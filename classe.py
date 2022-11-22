import gererdico as gd
import random as rdm
import calculdistance as cd
import geometrie as geo
import deplacements as dep


class Plan:
    "tout ce qu'il y a sur le plan"

    def __init__(self):
        self.bordure = [100,
                        100]  # la taille du plan (un rectangle centré sur 0 avec des longeurs et largeurs 2* la valeur dans cette variable
        self.matvectChasseurChasseur = []  # matvectxy represente la vecteur entre tt les objets de type x aux objets de type y
        self.matvectChasseurChassee = []
        self.matvectChasseeChasseur = []
        self.matvectChasseurFruit = []
        self.matvectChasseeFruit = []
        self.matvectChasseeChassee = []
        self.dico = gd.Dictionnaire()  # dico stockant la valeur de ttes les instances présentes sur le plan (numeroté de 0 à n-1)
        self.epsilon = 1
        self.spawnFruitrate = 10  # nb de fruits apparaissant par tour

    def accestableauChassee(self):
        return self.dico.tabChassee

    def accestableauChasseur(self):
        return self.dico.tabChasseur

    def accestableauFruit(self):
        return self.dico.tabFruit

    def actualisermatvectChasseurChasseur(self):
        self.matvectChasseurChasseur = cd.calculmatricevecteur(self.accestableauChasseur(), "Chasseur", self)

    def actualisermatvectChasseurChassee(self):
        self.matvectChasseurChassee = cd.calculmatricevecteur(self.accestableauChasseur(), "Chassee", self)
        self.matvectChasseeChasseur = cd.Transposeematrice(self.matvectChasseurChassee)

    def actualisermatvectChasseurFruit(self):
        self.matvectChasseurFruit = cd.calculmatricevecteur(self.accestableauChasseur(), "Fruit", self)

    def actualisermatvectChasseeChassee(self):
        self.matvectChasseeChassee = cd.calculmatricevecteur(self.accestableauChassee(), "Chassee", self)

    def actualisermatvectChasseeFruit(self):
        self.matvectChasseeFruit = cd.calculmatricevecteur(self.accestableauChassee(), "Fruit", self)

    def actualisermatvect(self):
        self.actualisermatvectChasseeFruit()
        self.actualisermatvectChasseeChassee()
        self.actualisermatvectChasseurFruit()
        self.actualisermatvectChasseurChasseur()
        self.actualisermatvectChasseurChassee()

    def actualiserChasseur(self):
        for chasseur in self.dico.tabChasseur:
            if chasseur.vivant:
                chasseur.mangerChassee(self)
            if chasseur.energie < self.epsilon:
                chasseur.vivant = False

    def actualiserChassee(self):
        for chassee in self.dico.tabChassee:
            if chassee.vivant:
                chassee.mangerFruit(self)
            if chassee.energie < self.epsilon:
                chassee.vivant = False

    def actualiserplan(self):
        self.actualisermatvect()

    def actualiserchasseurchassee(self):
        self.actualiserChasseur()
        self.actualiserChassee()

    def deplacementChasseur(self):
        for chasseur in self.dico.tabChasseur:
            if chasseur.vivant:
                chasseur.deplacementvecteur(self)

    def deplacementChassee(self):
        for chassee in self.dico.tabChassee:
            if chassee.vivant:
                chassee.deplacementvecteur(self)

    def spawnFruit(self, nb):
        for i in range(nb):
            fruit = Fruit()
            fruit.spawn(self)

    def spawnChassee(self, nb):
        for i in range(nb):
            chassee = Chassee()
            chassee.spawn(self)

    def spawnChasseur(self, nb):
        for i in range(nb):
            chasseur = Chasseur()
            chasseur.spawn(self)

    def deplacements(self):
        self.deplacementChassee()
        self.deplacementChassee()
        self.spawnFruit(self.spawnFruitrate)


class Fruit:

    def __init__(self):
        self.position = [0., 0.]
        self.vivant = True  # permet de savoir si le fruit est tjrs sur le plan

    def spawn(self, plan):
        x = rdm.uniform(-100., 100.)
        y = rdm.uniform(-100, 100)
        self.position = [x, y]
        plan.dico.nouveauFruit(self)


class Chassee:
    "Cette classe définit un certain type de personnage dans le plan"

    def __init__(self):
        self.position = [0., 0.]  # position du chassee dans le plan""
        self.vitesse = 1  # vitesse du chassee par tour"
        self.energie = 100  # energie du chassee (recuperation de x par fruit mangé, consomme k*vitesse/tour d'energie si deplacement"
        self.awareness = 25  # champ de vision du chassee"
        self.maxposition = [100, 100]
        self.maxenergie = 1000
        self.vivant = True  # permet de savoir si le chassee est tjrs en vie
        self.gain = 1000
        self.cout = 500
        self.ecartement = [1., 1.]
        self.errormargin = 1
        self.coefficientsvecteurs = dep.Vecteurs()

    def spawn(self, plan):
        x = rdm.uniform(-100., 100.)
        y = rdm.uniform(-100, 100)
        self.position = [x, y]
        plan.dico.nouveauChassee(self)

    def deplacement(self, x, y):
        [xmax, ymax] = self.maxposition
        if x <= xmax:
            if x >= -xmax:
                if y <= ymax:
                    if y >= -ymax:
                        self.position = [x, y]
                    else:
                        while y < -ymax:
                            y += 2 * ymax
                            self.position = [x, y]
                else:
                    while y > ymax:
                        y -= 2 * ymax
                        self.position = [x, y]
            else:
                while x < -xmax:
                    x += 2 * xmax
                if y <= ymax:
                    if y >= -ymax:
                        self.position = [x, y]
                    else:
                        while y < -ymax:
                            y += 2 * ymax
                            self.position = [x, y]
                else:
                    while y > ymax:
                        y -= 2 * ymax
                        self.position = [x, y]
        else:
            while x > xmax:
                x -= 2 * xmax
            if y <= ymax:
                if y >= -ymax:
                    self.position = [x, y]
                else:
                    while y < -ymax:
                        y += 2 * ymax
                        self.position = [x, y]
            else:
                while y > ymax:
                    y -= 2 * ymax
                    self.position = [x, y]

    def deplacementvecteur(self, plan):
        vecteur = self.coefficientsvecteurs.deplacements(self, "Chassee", plan)
        [x, y] = vecteur
        self.deplacement(x, y)

    def mangerFruit(self, plan):
        valeurChassee = plan.dico.valeur(self)
        print(len(plan.matvectChasseeFruit), valeurChassee)
        tabvect = plan.matvectChasseeFruit[valeurChassee]
        nbFruit = 0
        for vect in tabvect:
            if vect != -1 and geo.longeurvecteur(vect) < self.errormargin:
                plan.dico.tabFruit[nbFruit].vivant = False
                self.energie += self.gain
                if self.energie > self.maxenergie:
                    self.division(plan)
            nbFruit += 1

    def division(self, plan):
        [x, y] = self.position
        e = self.energie
        chassee = Chassee()
        chassee.coefficientsvecteurs.Chasseurcoefficients = self.coefficientsvecteurs.Chasseurcoefficients.copy()
        chassee.coefficientsvecteurs.Chasseecoefficients = self.coefficientsvecteurs.Chasseecoefficients.copy()
        chassee.coefficientsvecteurs.Fruitscoefficients = self.coefficientsvecteurs.Fruitscoefficients.copy()
        chassee.coefficientsvecteurs.mutation()
        ep = (e - self.cout) / 2
        self.energie = ep
        chassee.energie = ep
        [xe, ye] = self.ecartement
        xep = rdm.uniform(-xe, xe) / 2
        yep = rdm.uniform(-ye, ye) / 2
        self.deplacement(x + xep, y + yep)
        chassee.deplacement(x - xep, y - yep)
        plan.dico.nouveauChassee(chassee)

    def deplacementdirection(self, vecteur):
        [x, y] = self.position
        v = self.vitesse
        [x1, y1] = geo.vecteurunitaire(vecteur)
        [dx, dy] = [x1 * v, y1 * v]
        [x2, y2] = [x + dx, y + dy]
        self.position = [x2, y2]

    pass


class Chasseur:
    "Cette classe définit un certain type de personnage dans le plan"

    def __init__(self):
        self.position = [0., 0.]  # position du chassee dans le plan""
        self.vitesse = 1  # vitesse du chassee par tour"
        self.energie = 100  # energie du chassee (recuperation de x par fruit mangé, consomme k*vitesse/tour d'energie si deplacement"
        self.awareness = 50  # champ de vision du chassee"
        self.maxposition = [100, 100]
        self.maxenergie = 1000
        self.vivant = True  # permet de savoir si le chasseur est tjrs en vie
        self.errormargin = 1 / 2
        self.gain = 1000
        self.cout = 500
        self.ecartement = [1., 1.]
        self.coefficientsvecteurs = dep.Vecteurs()

    def spawn(self, plan):
        x = rdm.uniform(-100., 100.)
        y = rdm.uniform(-100, 100)
        self.position = [x, y]
        plan.dico.nouveauChasseur(self)

    def deplacement(self, x, y):
        [xmax, ymax] = self.maxposition
        if x <= xmax:
            if x >= -xmax:
                if y <= ymax:
                    if y >= -ymax:
                        self.position = [x, y]
                    else:
                        while y < -ymax:
                            y += 2 * ymax
                            self.position = [x, y]
                else:
                    while y > ymax:
                        y -= 2 * ymax
                        self.position = [x, y]
            else:
                while x < -xmax:
                    x += 2 * xmax
                if y <= ymax:
                    if y >= -ymax:
                        self.position = [x, y]
                    else:
                        while y < -ymax:
                            y += 2 * ymax
                            self.position = [x, y]
                else:
                    while y > ymax:
                        y -= 2 * ymax
                        self.position = [x, y]
        else:
            while x > xmax:
                x -= 2 * xmax
            if y <= ymax:
                if y >= -ymax:
                    self.position = [x, y]
                else:
                    while y < -ymax:
                        y += 2 * ymax
                        self.position = [x, y]
            else:
                while y > ymax:
                    y -= 2 * ymax
                    self.position = [x, y]

    def deplacementvecteur(self, plan):
        vecteur = self.coefficientsvecteurs.deplacements(self, "Chasseur", plan)
        [x, y] = vecteur
        self.deplacement(x, y)

    def mangerChassee(self, plan):
        valeurChasseur = plan.dico.valeur(self)
        print(len(plan.matvectChasseurChassee), valeurChasseur)
        tabvect = plan.matvectChasseurChassee[valeurChasseur]
        nbChassee = 0
        for vect in tabvect:
            if vect != -1 and geo.longeurvecteur(vect) < self.errormargin:
                plan.dico.tabChassee[nbChassee].vivant = False
                self.energie += self.gain
                if self.energie > self.maxenergie:
                    self.division(plan)
        nbChassee += 1

    def division(self, plan):
        [x, y] = self.position
        e = self.energie
        i = Chasseur()
        i.coefficientsvecteurs.Chasseurcoefficients = self.coefficientsvecteurs.Chasseurcoefficients.copy()
        i.coefficientsvecteurs.Chasseecoefficients = self.coefficientsvecteurs.Chasseecoefficients.copy()
        i.coefficientsvecteurs.Fruitscoefficients = self.coefficientsvecteurs.Fruitscoefficients.copy()
        i.coefficientsvecteurs.mutation()
        ep = (e - self.cout) / 2
        self.energie = ep
        i.energie = ep
        [xe, ye] = self.ecartement
        xep = rdm.uniform(-xe, xe) / 2
        yep = rdm.uniform(-ye, ye) / 2
        self.deplacement(x + xep, y + yep)
        i.deplacement(x - xep, y - yep)
        plan.dico.nouveauChasseur(i)

    pass

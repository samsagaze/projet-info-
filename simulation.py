import classe as c
import graphique as graph
class Jeu:
    "contient l'ensemble de la simulation"

    def __init__(self):
        self.plan = c.Plan()
        self.chassee = 100
        self.chasseur = 100
        self.fruit = 1000
        self.nbgenerations = 0

    def initialiserplan(self):
        self.plan.spawnChasseur(self.chasseur)
        self.plan.spawnFruit(self.fruit)
        self.plan.spawnChassee(self.chassee)

    def lancersimulation(self):
        self.initialiserplan()
        while True:
            self.plan.actualiserplan()
            self.plan.actualiserchasseurchassee()
            self.plan.deplacements()
            self.nbgenerations+=1
            print(self.nbgenerations)
            graph.montrerChassee(self.plan)

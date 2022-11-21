import classe
import random as rdm
import graphique
import simulation


def genererPlan():
    plan=classe.Plan()
    tab=[]
    for i in range(10):
        Chassee=classe.Chassee()
        [x, y]=[rdm.uniform(-100, 100), rdm.uniform(-100, 100)]
        Chassee.position=[x, y]
        tab+=[Chassee]
    plan.tabChassee=tab
    tab = []
    for i in range(10):
        Chassee = classe.Chassee()
        [x, y] = [rdm.uniform(-100, 100), rdm.uniform(-100, 100)]
        Chassee.position = [x, y]
        tab += [Chassee]
    plan.tabChassee = tab
    return

def generercoorandoms():
    [x, y]=[rdm.uniform(-100, 100), rdm.uniform(-100, 100)]
    return [x,y]

class Test:
    "classe de test"

    def __init__(self):
        self.test=0

    def increase(self):
        self.test+=1
        return self.test

j=simulation.Jeu()
j.lancersimulation()
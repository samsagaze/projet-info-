import persoplans as pp
import plan
import graphique


def creersimulation():
    tabdicofruit, tabdicovege, tabdicochasseur = [], [], []
    for i in range(10):
        nv = pp.Chasseur()
        nv1 = pp.Fruit()
        nv2 = pp.Vegetarien()
    compteur = 100
    while compteur>0:
        plan.plan.actualisertabvecteurs()
        plan.plan.actualiserplan()
        plan.plan.spawnfruit()
        plan.plan.deplacement()
        tabdicofruit.append(plan.plan.dicofruit)
        tabdicovege.append(plan.plan.dicovegetarien)
        tabdicochasseur.append(plan.plan.dicochasseur)
        compteur += -1
    return tabdicofruit, tabdicovege, tabdicochasseur


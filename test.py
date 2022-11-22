import persoplans as pp
import plan
import graphique



def creersimulation():
    for i in range(100):
        nv = pp.Chasseur()
        nv1 = pp.Fruit()
        nv2 = pp.Vegetarien()
    while True:
        plan.plan.actualisertabvecteurs()
        plan.plan.actualiserplan()
        plan.plan.spawnfruit()
        plan.plan.deplacement()
        graphique.montrerChassee()



creersimulation()
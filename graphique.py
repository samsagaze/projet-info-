import matplotlib.pyplot as plt
import classe


def montrerChassee(plan):
    tabChassee=plan.dico.tabChassee
    tx=[]
    ty=[]
    for i in tabChassee:
        [xi, yi]=i.position
        tx+=[xi]
        ty+=[yi]
    plt.scatter(tx, ty)
    plt.show()
    return


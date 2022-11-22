import matplotlib.pyplot as plt
import plan

def montrerChassee():
    dicovege=plan.plan.dicovegetarien
    tx=[]
    ty=[]
    for i in dicovege:
        [xi, yi]=dicovege[i].position
        tx+=[xi]
        ty+=[yi]
    plt.scatter(tx, ty)
    plt.show()
    return


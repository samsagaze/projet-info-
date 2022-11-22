import geometrie as geo

def sorttabvecteur(tabvecteur):     #permet de trier un tableau de vecteur du vecteur le plus court au vecteur le plus long
    nvtab = []
    dicovu = {}
    for i in range(len(tabvecteur)):
        mindis = 500
        minindice = -1
        for j in range(len(tabvecteur)):
            [indice, vecteur] = tabvecteur[j]
            if not (indice in dicovu):
                dis = geo.longeurvecteur(vecteur)
                if dis < mindis:
                    mindis = dis
                    minindice = indice
        if minindice<len(tabvecteur):
            nvtab.append([minindice, tabvecteur[minindice]])
            dicovu[minindice] = True
    return nvtab

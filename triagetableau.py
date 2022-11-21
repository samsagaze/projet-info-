import geometrie as geo

def sorttableauvecteur(tabvect):
    tabdis=[]
    n=len(tabvect)
    for i in range(n):
        vect=tabvect[i]
        if vect==-1:
            tabdis+=[[-1, i]]
        else:
            tabdis+=geo.longeurvecteur(vect)
    tabdis.sort(reverse=True)
    tabvecttrie=[[]]*n
    for j in range(n):
        tabvecttrie[j]=tabvect[tabdis[1]]
    return tabvecttrie


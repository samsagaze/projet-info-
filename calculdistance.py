import geometrie as geo

def distance(C, Cp):
    [x1, y1] = C.position
    [x2, y2] = Cp.position
    [x, y] = [x1 - x2, y1 - y2]
    return geo.longeurvecteur([x, y])

# calcule la distance dans le plan entre les 2 objets C et Cp

def vecteur(C, Cp):
    return [Cp[0] - C[0], Cp[1] - C[1]]

def vecteurChassee(objet, plan):
    tabChassee = plan.accestableauChassee()
    resultat = []
    for chassee in tabChassee:
        if chassee.vivant:
            coordchassee = chassee.position
            coordobjet = objet.position
            vect = vecteur(coordobjet, coordchassee)
            resultat += [vect]
        else:
            resultat += [-1]
    return resultat

def vecteurChasseur(objet, plan):
    tabChasseur = plan.accestableauChasseur()
    resultat = []
    for chasseur in tabChasseur:
        if chasseur.vivant:
            coordchasseur = chasseur.position
            coordobjet = objet.position
            vect = vecteur(coordobjet, coordchasseur)
            resultat += [vect]
        else:
            resultat += [-1]
    return resultat

def vecteurFruit(objet, plan):
    tabFruit = plan.accestableauFruit()
    resultat = []
    for fruit in tabFruit:
        if fruit.vivant:
            coordfruit = fruit.position
            coordobjet = objet.position
            vect = vecteur(coordobjet, coordfruit)
            resultat += [vect]
        else:
            resultat += [-1]
    return resultat

def calculmatricevecteur(tab1, typeobjet,
                         plan):  # typeobjet="Fruit", "Chassee", "Chasseur"            Calcule la matrice de vecteur entre les elements de tab1 et les elements du type typeobjet
    n = len(tab1)
    if n == 0:
        return []
    else:
        result = []
        if typeobjet == "Fruit":
            m = plan.dico.nbFruits
            for objet in tab1:
                if objet.vivant:
                    result += [vecteurFruit(objet, plan)]
                else:
                    result += [[-1] * m]
        elif typeobjet == "Chassee":
            m = plan.dico.nbChassee
            for objet in tab1:
                if objet.vivant:
                    result += [vecteurChassee(objet, plan)]
                else:
                    result += [[-1] * m]
        elif typeobjet == "Chasseur":
            m = plan.dico.nbChasseurs
            for objet in tab1:
                if objet.vivant:
                    result += [vecteurChasseur(objet, plan)]
                else:
                    result += [[-1] * m]
    return result

def Transposeematrice(mat):
    n = len(mat)
    if n == 0:
        return []
    else:
        mattransposee = []
        m = len(mat[0])
        for i in range(m):
            ligne = []
            for j in range(n):
                ligne += [mat[j][i]]
            mattransposee += [ligne]
    return mattransposee

def vecteurunitaire(vecteur):
    if len(vecteur)!=2:
        return "Erreur"
    [x, y]=vecteur
    u=((x**2)+(y**2))**(1/2)
    xp=x/u
    yp=y/u
    return [xp, yp]

def longeurvecteur(vecteur):
    if len(vecteur)!=2:
        return "Erreur"
    [x, y]=vecteur
    return ((x**2)+(y**2))**(1/2)

def addition(vecteur1, vecteur2):
    return [vecteur1[0]+vecteur2[0], vecteur1[1]+vecteur2[1]]

def multiplication(a, vecteur):
    return [a*vecteur[0], a*vecteur[1]]
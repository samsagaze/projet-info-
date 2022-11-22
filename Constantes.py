#Un fichier contenant l'ensemble des constantes du plan

borduresplans = [100, 100]             #le plan est un rectange centré sur 0 dont les cotês sont de longueur 2* les valeurs de bordureplans

energievegetarien = 500                 #l'énergie que possède un végétarien apparaissant

gainenergievegetarien = 1000                #l'énergie que gagne chaque vegetarien lorsque il mange un fruit (<maxenergievegetarien)

maxenergievegetarien = 1000             #l'énergie maximale que possède un vegetarien (s'il la dépasse il se divise - il ne peut se diviser qu'une fois par tour)

energiechasseur = 500                 #l'énergie que possède un chasseur apparaissant

gainenergiechasseur = 1000                #l'énergie que gagne chaque chasseur lorsque il mange un vegetarien (<maxenergiechasseur)

maxenergiechasseur = 1000            #l'énergie maximale que possède un chasseur (s'il la dépasse il se divise - il ne peut se diviser qu'une fois par tour)

errormargin = 1                      #si il y a moins de l'errormargin entre 2 entités, on considèrent qu'elles sont au même endroit

ecartement = [1., 1.]                #definit l'écartement maximal que peuvent avoir 2 entités issus d'une division (l'écartement réel est choisi aléatoirement entre ces deux valeurs)

awareness = 50                      #champ de vision des entités du plan

coefficientmutation = 10            #definit le rapport de mutation maximal qu'il peut y avoir

fruitspawnrate = 10

vitesse = 20                                #vitesse des entites
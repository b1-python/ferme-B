import plante

courgette = plante.creerPlante("courgette")
poireau = plante.Legume("poireau", 1, 3, 60)

print("Prix de vente de la courgette: " + str(courgette.vendre()))
print("Prix de vente du poireau: " + str(poireau.vendre()))

debutsaison = True
annee = 0
anneeMax = 1000


def acheterSemence():
    """ Fonction qui gère les interactions avec l'utilisateur pour l'achat des semences """
    pass


# 1ère boucle sur les saisons : chaque itération correspond à une saison en deux étapes, achats puis vente
while annee < anneeMax:

    ## Début de saison, on achète des plantes
    if debutsaison:
        # Demander si on veut acheter des semences ou finir la saison
        choix = input("Que voulez vous faire ? S = acheter une semence, Q = finir la saison")

        if choix == "S":
            acheterSemence()

        elif choix == "Q":
            # Finir la saison
            debutsaison = False

        else:
            print("Votre choix est invalide")

    else:
        # Fin de saison => Vente des semences
        pass



    ## Fin de saison, on vend nos plantes
    pass



import plante
import random

courgette = plante.creerPlante("courgette")
poireau = plante.Legume("poireau", 1, 3, 60)

print("Prix de vente de la courgette: " + str(courgette.vendre()))
print("Prix de vente du poireau: " + str(poireau.vendre()))

# On déclare les couleurs comme variables globales car ce sont des constantes
TOUTE_LES_COULEURS = ['rouge', 'vert', 'bleu', 'jaune', 'orange', 'rose', 'violet', 'blanc', 'noir']

class JeuDeFerme:

    def __init__(self):
        self.couleurDeLaSaison = 'to be defined' # Déclarée ici pour que tous les attributs soient définis dans le constructeur. La valeur sera positionnée correctement au début de la première saison
        self.debutsaison = True
        self.annee = 0
        self.anneeMax = 1000
        self.argentjoueur = 100
        self.legumes = []

    def acheterSemence(self):
        """ Fonction qui gère les interactions avec l'utilisateur pour l'achat des semences """
        nom = input("Graine de quel légume? ")
        legume = plante.creerPlante(nom)
        prixachat = legume.getPrixAchat()
        if prixachat > self.argentjoueur:
            print("Vous n'avez pas assez d'argent")
        else:
            self.argentjoueur -= prixachat
            self.legumes.append(legume)

    def vendreSemences(self):
        """ Vends toutes les semences achetée au début de la saison """
        for legume in self.legumes:
            prixDeVente = legume.vendre()

            # Vérification de la saison pour les fleurs
            if isinstance(legume, plante.Fleur):
                # Ici, on sait qu'on manipule une Fleur
                if legume.getCouleur() == self.couleurDeLaSaison:
                    print("Youpi, la " + legume.getNom() + " est a la mode cette année !")
                    prixDeVente *= 2

            print(legume.getNom() + " vendu " + str(prixDeVente) + "€")
            self.argentjoueur += prixDeVente
        self.legumes = []

    def commencerSaison(self):
        self.annee += 1
        self.debutsaison = True
        self.couleurDeLaSaison = random.choice(TOUTE_LES_COULEURS)


    def main(self):
        # 1ère boucle sur les saisons : chaque itération correspond à une saison en deux étapes, achats puis vente
        while self.annee < self.anneeMax:

            ## Début de saison, on achète des plantes
            if self.debutsaison:
                # Demander si on veut acheter des semences ou finir la saison
                choix = input("Vous avez " + str(self.argentjoueur) + "€. Que voulez vous faire ? S = acheter une semence, Q = finir la saison : ")

                if choix == "S":
                    self.acheterSemence()

                elif choix == "Q":
                    # Finir la saison
                    print("La couleur cette saison est le "+self.couleurDeLaSaison)
                    self.debutsaison = False

                else:
                    print("Votre choix est invalide")

            else:
                # Fin de saison => Vente des semences
                self.vendreSemences()
                self.commencerSaison()



jeu = JeuDeFerme()
jeu.main()

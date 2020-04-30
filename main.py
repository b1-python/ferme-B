import plante

courgette = plante.creerPlante("courgette")
poireau = plante.Legume("poireau", 1, 3, 60)

print("Prix de vente de la courgette: " + str(courgette.vendre()))
print("Prix de vente du poireau: " + str(poireau.vendre()))

class JeuDeFerme:

    def __init__(self):
        self.debutsaison = True
        self.annee = 0
        self.anneeMax = 1000
        self.argentjoueur = 100
        self.legumes = []

    def acheterSemence(self):
        """ Fonction qui gère les interactions avec l'utilisateur pour l'achat des semences """
        nom = input("Graine de quel légume?")
        legume = plante.creerPlante(nom)
        prixachat = legume.getPrixAchat()
        if prixachat > self.argentjoueur:
            print("Vous n'avez pas assez d'argent")
        else:
            self.argentjoueur -= prixachat
            self.legumes.append(legume)

    def vendreSemences(self):
        """ Vends toutes les semences achetée au début de la saison """
        

    def main(self):
        # 1ère boucle sur les saisons : chaque itération correspond à une saison en deux étapes, achats puis vente
        while self.annee < self.anneeMax:

            ## Début de saison, on achète des plantes
            if self.debutsaison:
                # Demander si on veut acheter des semences ou finir la saison
                choix = input("Vous avez" + str(self.argentjoueur) + "€. Que voulez vous faire ? S = acheter une semence, Q = finir la saison")

                if choix == "S":
                    self.acheterSemence()

                elif choix == "Q":
                    # Finir la saison
                    self.debutsaison = False

                else:
                    print("Votre choix est invalide")

            else:
                # Fin de saison => Vente des semences
                pass

            ## Fin de saison, on vend nos plantes
            pass



jeu = JeuDeFerme()
jeu.main()

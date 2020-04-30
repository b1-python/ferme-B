class Animal:

    def __init__(self, nom, pa, cri):
        self.nom = nom
        self.prix_achat = pa
        self.cri = cri
        self.age = 0

    def getNom(self):
        return self.nom

    def getPrixAchat(self):
        return self.prix_achat

    def getCri(self):
        return self.cri

    def vieillir(self):
        self.age += 1

    def vendreProduit(self):
        # ??? On ne sait pas, ça dépend du type d'animal
        pass

    def vendreAnimal(self):
        # ??? On ne sait pas, ça dépend du type d'animal
        pass


class Vache(Animal):

    def __init__(self):
        Animal.__init__(self, "vache", 100, "meuuuuh")
        # Rien de plus dans le constructeur car la Vache n'a pas d'attribut en plus de l'Animal

    def vendreProduit(self):
        # On redéfinit la méthode de la classe mère qui à un comportement spécifique pour la classe Fille
        # 10€/ans entre la 3ème et 10ème année
        if self.age >= 3 or self.age <= 10:
            return 10
        else:
            return 0

    def vendreAnimal(self):
        # On redéfinit la méthode de la classe mère qui à un comportement spécifique pour la classe Fille
        # 120€ lorsqu'elle produit du lait, 50€ sinon
        if self.vendreProduit() > 0:
            # la vache produit du lait
            return 120
        else:
            # La vache ne produit pas de lait
            return 0


class Oie(Animal):

    def __init__(self):
        Animal.__init__(self, "oie", 15, "kwac")
        # Rien de plus dans le constructeur car l'Oie n'a pas d'attribut en plus de l'Animal

    def vendreProduit(self):
        # On redéfinit la méthode de la classe mère qui à un comportement spécifique pour la classe Fille
        # l'oie ne produit rien
        return 0

    def vendreAnimal(self):
        # On redéfinit la méthode de la classe mère qui à un comportement spécifique pour la classe Fille
        # 50€ entre la 3ème et 5ème année, 15€ avant et 20€ après
        if self.age < 3:
            return 15
        elif self.age > 5:
            return 20
        else:
            return 50

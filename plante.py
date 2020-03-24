import random


class modele:
    """ documentation de la classe """

    def __init(self, param1, param2):
        """ Doc du constructeur """
        # Définition des attributs
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = "valeur par defaut"
        self.attr4 = param2 + param1

    def method1(self, param):
        """ doc de la méthode """
        pass


class Legume:

    def __init__(self, nom, ps, pv, proba ):
        self.nom = nom
        self.prix_semence = ps
        self.prix_vente = pv
        self.probabilite = proba

    def getNom(self):
        return self.nom

    def getPrixAchat(self):
        return self.prix_semence

    def vendre(self):
        vendable = random.randint(0,100)
        if (vendable <= self.probabilite):
            return self.prix_vente
        else:
            return 0


def creerPlante(nom):
    """ Renvoie le légume demandé """
    if nom == "courgette":
        return Legume("courgette", 0.5, 2, 75)
    elif nom == "tomate":
        return Legume("tomate", 0.4, 3, 50)
    elif nom == "patate":
        return Legume("patate", 0.9, 1.5, 90)
    else:
        raise ValueError()



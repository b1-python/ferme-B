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
        """
        Constructeur de la classe

        :param nom: nom de la plante
        :param ps: prix d'achat de la semence
        :param pv: prix de vente de la semence
        :param proba: probabilité entre 0 et 100 que la plante arrive à maturités
        """
        self.nom = nom
        self.prix_semence = ps
        self.prix_vente = pv
        self.probabilite = proba

    def getNom(self):
        """
        :return: Renvoie le nom de la plante
        """
        return self.nom

    def getPrixAchat(self):
        return self.prix_semence

    def vendre(self):
        vendable = random.randint(0,100)
        if (vendable <= self.probabilite):
            return self.prix_vente
        else:
            return 0


class Fleur(Legume):
    """ Une fleur est comme un légume, mais avec une couleur en plus"""

    def __init__(self, nom, ps, pv, proba, couleur):
        Legume.__init__(self, nom, ps, pv, proba)
        self.couleur = couleur

    def getCouleur(self):
        return self.couleur


def creerPlante(nom):
    """ Renvoie le légume demandé """
    if nom == "courgette":
        return Legume("courgette", 0.5, 2, 75)
    elif nom == "tomate":
        return Legume("tomate", 0.4, 3, 50)
    elif nom == "patate":
        return Legume("patate", 0.9, 1.5, 90)
    elif nom == "tulipe":
        return Fleur("tulipe", 2, 4, 80, "rose")
    elif nom == "rose":
        return Fleur("rose", 3, 7, 50, "rouge")
    elif nom == "muguet":
        return Fleur("muguet", 1, 2, 90, "blanc")
    else:
        raise ValueError()



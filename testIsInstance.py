import plante

tulipe = plante.Fleur("tulipe", 2, 4, 80, "rose")
courgette = plante.Legume("courgette", 0.5, 2, 75)
entier = 5
chaine = "toto"
float = 5.5

print("tulipe instance of Fleur => ", isinstance(tulipe,plante.Fleur)) # True
print("courgette instance of Legume => ", isinstance(courgette,plante.Legume)) # True

print("tulipe instance of Legume => ", isinstance(tulipe,plante.Legume)) # True (gràce à l'héritage)
print("courgette instance of Fleur => ", isinstance(courgette,plante.Fleur)) # False

print("entier instance of Legume => ", isinstance(entier,plante.Legume)) # False

# A retenir :
# Une classe fille peut être considéré du même type que sa classe mère, et utilisée en tant que telle
# => c'est ce qu'on a fait dans la fonction main en utilisant des Fleurs comme des Legumes
# A l'inverse, la classe mère ne peut pas être considéré du type d'une de ses classes fille

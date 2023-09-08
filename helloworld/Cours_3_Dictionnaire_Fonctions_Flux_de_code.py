#!/usr/bin/env/python3

# Ci dessous la création d'un dictionnaire ==> a gauche==> les chiffres représente la clé.
                                          #==> a droite ==> les mois représente la valeur.
                #  La clé peut etre une autre valeur qu'un chiffres ==> elle pourrait etre une chaine de caractère "1"
# /!\ La clé est unique ==> Comme dans un dictionnaire UN MOT = UNE DEFINITION

# conversionMois = {
#     1: "Janvier",
#     2: "Fevrier",
#     3: "Mars",
#     4: "Avril",
#     5: "Mai",
#     6: "Juin",
#     7: "Juillet",
#     8: "Aout",
#     9: "Septembre",
#     10: "Octpbre",
#     11: "Novembre",
#     12: "Decembre",
# }

# print(conversionMois[1])

# Methode alternative ==> print(conversionMois.get(1)) ==> Le resultat sera identique

#  Ci dessous un exemple de code permettant de concaténé une chaine de caractère avec un dictionnaire, le résultat sera
                            # Nous sommes le 8 Janvier

# print("Nous sommes le 8", conversionMois.get(1))

# La syntaxe si dessous sert a definir une fonction
#  Dans les parenthèse nous trouverons des PARAMETRE utilisé dans cette fonction

# print("Début du code")


# def dire_bonjour():
#     print("Dans la fonction")
#     print("Bonjour à tous !")
#     print("Fin de la fonction")
# Ci dessus on peu voir grace a la tabulation que nous sommes bien a l'interieur de la fonction.

# /!\ Si j'écris ICI , SANS tabulation je serai en dehors de ma fonction

# Il est recomander de laissé 2 lignes vide AVANT & 2 ligne vide APRES une fonction

# /!\ La fonction est ici juste créer et non appelée.
    # Nous allons donc l'appeler comme ceci : dire_bonjour()

# print("On appelle maintenant la fonction ! ")
# dire_bonjour()
#
# print("Fin du code")


# Ci dessous (prenom) est un PARAMETRE de la fonction dire_bonjour
def dire_bonjour( prenom):
    print("Bonjour " + prenom + "!")

dire_bonjour( "Michel")
dire_bonjour( "Jean-Edouard")
dire_bonjour( "Marie-Cystite")
dire_bonjour( "Kevin")
dire_bonjour( "Bryan")
dire_bonjour("Kimberley")


def addition(nombre1, nombre2):
    return nombre1 + nombre2
# Si dessus le therme ==> return ==> permet de retourné une valeur

resultat = addition(1200,500)
# Si dessus on créer une fonction apellé ==> resultat ==> cela permet de récupérer la valeur retourné par "return"
print(resultat)
#  Si dessus le therme ==> "print" permet d'ecrire la valeur récupéré dans la fonction "resultat"

#  Cette syntaxe permet d'utiliser des fonction dans une fonction :

resultat = addition(4, addition(2,2))
print(resultat)







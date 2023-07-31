
# si dessous le "shebang" :
#  definition issus de chatGPT :
# ------

#     Le symbole #! est la marque qui indique qu'il s'agit d'un shebang.
#     /usr/bin/env est une commande qui permet d'exécuter un programme trouvé
#     dans le répertoire système (/usr/bin) en utilisant l'environnement actuel.
#     python3 est l'interpréteur Python de la version 3.x.

#     En d'autres termes, cette ligne dit au système d'exploitation de chercher l'interpréteur Python 3
#      dans le chemin d'accès standard (/usr/bin/env) et d'utiliser cette version pour exécuter le script Python.
#     Cela permet de rendre le script portable, car il utilisera l'interpréteur Python 3 qui est disponible
#      dans l'environnement du système où il est exécuté.

# ------

# ---------------------------
#!/usr/bin/env/python3
# ----------------------------
# Ci dessous un module importé (voir information a partir de la ligne 99)
# import math
import subprocess

from math import*

# Nous pouvons utiliser tous type de variable dans une liste ===> ci dessous nous avons :
         # ["Des chaines de caractère       , des nombre, un booléen]
# couleurs = ["Bleu", "Blanc", "Rouge", "Vert", 0, 1.2    , True]
# Index :     0        1       2         3

# couleurs[2] = "Rose"
#  de cette manière on remplace la valeur de la variable a l'index 2 ===> Rouge deviens donc Rose

# en mettant un "." après  notre variable nous pouvons utiliser des methodes

# Ci dessous il faut EXECUTER la fonction ===> .append (ajouter) ===> AVANT pour pouvoir ajouter la couleur noir et ainssi ajouter a ma liste
         # à l'index [6] la couleur "Noir".
# couleurs.append("Noir")
# print(couleurs)

# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
# autreliste = [ 0, 1.2, True]
# .extend ===> ajouter une liste a une autre
#
# couleurs.extend(autreliste)
# print(couleurs)

# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
# autreliste = [ 0, 1.2, True]

#  .insert ===> Permet d'incérer ==> cette fonction utilise deux paramètres ( index,"ce quon insinrt)

# couleurs.insert(2, "Jaune")
# print(couleurs)

# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
# autreliste = [ 0, 1.2, True]

#  .pop ===> Permet de retirer le dernier elements

# couleurs.pop()
# print(couleurs)

# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
# autreliste = [ 0, 1.2, True]

#  .remove ===> permet de retirer un element de la liste

# couleurs.remove("Bleu")
# print(couleurs)

# Les fonction sont bien documenté dans l'auto-complétion de l'outils pycharm

# ---------------------

#  Ci dessous un TUPLES ou COUPLE DE DONNEES ===> Par exemple des coordonées
#  Les TUPLES et les LISTE sont sensiblement identique,  sauf que les TUPLES ne sont pas MODIFIABLE
#  Un TUPLE est immuable ====> NON MODIFIABLE
#  Par convention un TUPLE s'exprime entre parenthese et non entre crochet

# coordonées = (1,2)

# /!\ si je fais ==> coordonées[0] = 4 ===> Cela ne fonctionnera pas car les TUPLES ne sont PAS MODIFIABLE

#  Ci dessous deux LISTES
#  Par convention une liste s'exprime entre crochet et non entre parenthese

# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
# autreliste = [ 0, 1.2, True]
#
# couleurs.remove("Bleu")
# print(couleurs)

#  Nous pouvons aussi mettre des TUPLES dans une LISTE

# coordonées = (11.154,2.14)
#
# autreliste = [0, 1.2, True, (1,2)]
# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]
#
# print(couleurs)
# print(autreliste)

# En Python il éxiste des MODULES qui permettent de faire beaucoup d'operations,
# par exemple :
                # ==> Les opérations mathematique
                    # la plupart des module doivent être importé ===> J'ajoute en haut du code ceci
                    # ===> import math
                    # ===> afin d'importer le module mathématique.
# par exemple :
                # ==> Des appel de commande Linux au seins du code Python ==> J'ajoute à la suite en haut du code ceci
                # ===> "import subprocess"


# coordonées = (11.154,2.14)
#
# autreliste = [0, 1.2, True, (1,2)]
# couleurs = ["Bleu", "Blanc", "Rouge", "Vert"]

# Ci dessous ==> Permet de calculer le cossinus de 180° grace au module math
# print(math.cos(180))

#  Ci dessous ==> Permet d'utiliser la commande "ls" (avec cette syntaxe subrocess.call("ls")
#  le est une commande du terminal de Linux qui permet de lister le contenue d'un repertoire

# subprocess.call("ls")

# Il y a deux manière d'importé un module.
#  1) ==> import LE NOM DE MON MODULE
#  2) ==> from LE NOM DE MON MODULE import* ==> cela permet de ne plus utiliser le therme "math" dans la fonction
#     ==> celle ci s'écrirai donc ==> print(cos(180))

print(cos(180))

#  /!\ Il est cependant recommander d'utiliser la syntaxe suivante ===> import math




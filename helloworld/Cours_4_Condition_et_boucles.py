#!/usr/bin/env/python3

# Si dessous "majeur" est une variable et "True" signifie vrai. donc majeur vos Vrai
# majeur = True
#
# if exprime une condition,  == signifie "est ce que majeur est égal a vrai ? "
# Ce bloc de code signifie : Si majeur vos Vrai ,  alors l'interpreteur écrira "vous etes majeur" /
# sinon l'interpreteur écrira "vous êtes pas majeur", En l'occurence sur la ligne précédente nous avons déclaré que
#  la variable  majeur était vrai.
# if majeur == True:
#     print("Vous êtes majeur")
# else:
#     print("Vous n'êtes pas majeur")

# ----------------------------------------------------------

# Si nous passons la valeur a False (faux) alors le code ira dans la second partie de la conditionelle else et
# donc l'interpreteur remontera : "vous n'etes pas majeur " .
# majeur = False
#
# if majeur == True:
#     print("Vous êtes majeur")
# else:
#     print("Vous n'êtes pas majeur")

# ----------------------------------------------------------

# majeur = False
# Ici on peu simplifier en écrivant : if majeur: sans déclaré de condition a la variable majeur
# puisque au dessus on a écris que majeur valais faux (ce n'est possible que parce que True et False sont des booléens)
# if majeur:
#     print("Vous êtes majeur")
# else:
#     print("Vous n'êtes pas majeur")

# ----------------------------------------------------------
# Si dessous on définis une valeur age ,  age vos donc 19 ans
# age = 19
# Si dessous on écris : Si l'age est supérieur ou égal a 18 alors vous etes majeur,  sinon ,  vous ne l'etes pas
# if age >= 18:
#     print("Vous etes majeur")
# else:
#     print("Vous n'etes pas majeur")

# ----------------------------------------------------------

# Nous pouvons également cumulé les variables :

# age = 19
# homme = True
# si dessous on cumule la condition age et etre un homme
# if age >= 18 and homme :
#     print("Vous etes majeur  et vous êtes un homme ")
# si dessous elif signifie "sinon si "
# elif age < 18 and homme:
#     print("Vous n'etes pas majeur et vous etes un homme")
# si dessous elif signifie toujours "sinon si",  et and not veux dire et ne vos pas vrai a la variable homme
# elif age >=  18 and not homme:
#     print("Vous êtes majeur et vous n'etes pas un homme")
# elif age < 18 and not homme:
#     print("Vous n'êtes pas majeur et vous n'êtes pas une homme")
# ici le else n'est pas nécéssaire, car tous les cas son traité par les conditions du dessus

# ----------------------------------------------------------

# ici on vas utilisé or a la place de and ,  or signifie ou

# age = 17
# homme = True

# Si dessous on écris : si age est supérieur ou égal a 18 ou si vous etes un homme
#  ici l'une ou l'autre des condition est vérifié
# if age >= 18 or homme:
# Ici l'interpréteur écrira vous etes majeur OU vous etes un homme , car l'une ou l'autre est vérifiable
#     print("Vous etes majeur  ou vous êtes un homme ")
#
# elif age < 18 and homme:
#     print("Vous n'etes pas majeur et vous etes un homme")
# elif age >=  18 and not homme:
#     print("Vous êtes majeur et vous n'etes pas un homme")
# elif age < 18 and not homme:
#     print("Vous n'êtes pas majeur et vous n'êtes pas une homme")

# ----------------------------------------------------------

# i = 0

#  si dessous while veux dire "tant que" ,  /!\ attention au boucle infinie avec while
# while i <= 10:
    #  si dessous str veux dire stringify ==> transformer en chaine de caractère
    # print("i vaut : " + str(i))
# Si on s'arrète ici nous avons une boucle illimité car i vos toujours 0
#  Si dessous nous allons donc incrémenté la variable i ==> de cette manière la boucle
#  s'arretera quand i sera égale a 10
#     i = i + 1

# ----------------------------------------------------------

# amis = ["Pierre", "Paul", "Jacques"]
# si dessous on écrit  pour chaque ami dans la liste amiS
# for chaqueami in amis:
#     print(chaqueami)

# ----------------------------------------------------------

# amis = ["Pierre", "Paul", "Jacques"]
# Si dessous on ecrit une boucle qui va fournir chaque caractère de la chaine de caractère amis
# for carac in "amis":
#     print(carac)

# ----------------------------------------------------------

# amis = ["Pierre", "Paul", "Jacques"]
# Si dessous on utilise lz fonction range qui permetra de généré une sequence d'entier,  ici on comptera de 0 à 9,
# ce qui correspond au dix premier "rang"
# for nb in range(10) :
#     print(nb)

# ----------------------------------------------------------

amis = ["Pierre", "Paul", "Jacques"]
#  si dessous range(4,10) signifie que l'on comptera du rang 4 à 10 ==> 4 5 6 7 8 9 ( 0 étant au rang 1 et 10 au rang 9)
for nb in range(4, 10) :
    print(nb)
#!/usr/bin/env/python3

# "Chaine de caractères ==> entre Guillemet
# "coucou"
#
#
#  les chifres" "===> sans guillemet
# 123
# 1.23
#
# vrai
# True
#
# faux
# False

variable= "Ma chaîne modifiée"
         # 0123456.... ==> utilisé ".count"
         #  pour avoir le premier caractère a l'index ===> M ====> utiliser [0]
         #  pour modifier une chaine de caractère ===>
         #    ".replace"(premier paramètre de la fonction = "ancien caractère", second paramètre = "nouveau caractère")
         #  Les fonction sont imbricable ===> une fonction dans une fonction dans une fonction ...
variable2= 2
vartiable3= 3.0
variable4= True
est_majeur= True

print(variable.replace("modifiée", "remodifiée"))




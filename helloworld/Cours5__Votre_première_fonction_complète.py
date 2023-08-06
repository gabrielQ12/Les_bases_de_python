#!/usr/bin/env/python3

# Création d'un "casseur de mot de passe"

# si dessous on import le module random pour généré de l'aleatoire
import random
import time
import string

# mot_de_passe = "motdepasse"  # sera donc le mot de passe à trouver


# def mot_aleatoire(longueur):
#     lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x', 'y','z']
#     mot_genere = ""
#     for carac in range(0, longueur):
#   si dessous on utilise  la methode randint dans le module random, cette methode permet de créer un nombre entier aléatoir entre une plage de valeur
#         mot_genere = mot_genere + lettres [random.randint(0, len(lettres) - 1)]
#     return mot_genere


# debut = time.time()
# while True:
#     mot_alea = mot_aleatoire(len(mot_de_passe))
#     print("Mot de passe testé : " + mot_alea)
#     if mot_de_passe == mot_alea:
#         print("Mot de passe trouvé : " + mot_alea)
#         fin = time.time() - debut
#         print("Trouvé en " + str(fin) + " secondes")
#         break
# Si dessus on utilise break pour cassé la boucle while si le mdp est trouvé

# J'ai essayé avec 10 caractère et ai abandonné après plus de 1h d'essai.

# ----------------------------------------------------------

# Nous allons maintenant essayer d'ameliorer le code


mot_de_passe = input("Quel est le mot de passe : ")

# test

def mot_aleatoire():
    lettres = string.ascii_letters
    suiv = ""
    resultat = ""
    for i in range(len(mot_de_passe)):
        while mot_de_passe[i] != suiv:
            print(resultat + suiv)
            suiv = random.choice(lettres)
        resultat += suiv
    return resultat


debut = time.time()
print(mot_aleatoire())
print("Durée : " + str(time.time() - debut) + " secondes")


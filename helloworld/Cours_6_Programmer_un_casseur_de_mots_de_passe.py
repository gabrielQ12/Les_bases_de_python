#!/usr/bin/env/python3


import random
import time
import string
import hashlib
import sys

mot_de_passe = input ("Quel est le mot de passe :")
mot_de_passe_md5 = hashlib.md5(mot_de_passe.encode("utf8")).hexdigest()
print(mot_de_passe_md5)


## def mot_aleatoire():
##     lettres=string.ascii_letters
##     suiv=""
##     resultat=""
##     for i in range(len(mot_de_passe)):
##         while mot_de_passe[i] != suiv:
##             print(resultat + suiv)
##             time.sleep(0.05)
##             suiv= random.choice(lettres)
##         resultat += suiv
##         return resultat

def hash_crack():
    try:
        mots_fr = open("/home/kali/Bureau/liste_francais.txt", "r")
        trouve = False
        for mot in mots_fr.readlines():
            mot = mot.strip("\n").encode("utf8")
            hashmd5 = hashlib.md5(mot).hexdigest()
            if hashmd5 == mot_de_passe_md5:
                print("Mot de passe trouvé : " + str(mot) + "(" + hashmd5 + ")")
                trouve = True
        if not trouve:
            print("Mot de passe non trouvé")
        mots_fr.close()
    except FileNotFoundError:
        print("Erreur : nom de dossier ou fichier introuvable")
        sys.exit(1)
    except Exception as err:
        print("Erreur" + str(err))
        sys.exit(2)

debut = time.time()
hash_crack()
print("Durée : " + str(time.time() - debut) + "second")






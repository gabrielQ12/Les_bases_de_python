#!/usr/bin/env/python3
#conding:utf-8

import time
import argparse
import atexit

from cracker import *


"""
Module d'une librairie externe ==> ligne de commande ==> pip install python-pdf

Fonctionement (voir la doc):

import pydf
pdf = pydf.generate_pdf('<h1>this is html<h1>')
with open('test_doc.pdf','wb') as f:
    f.write(pdf)
    
"""





def affiche_duree():
    """
    Affiche la durée d'execution du programme
    :return:
    """

    print("Durée écoulée :" + str(time.time() - debut) + "second")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Casseur de mot de passe en Python")

    parser.add_argument("-f", "--file", dest="file", help="PChemin du fichier de mots clés" ,
                    required=False)
    parser.add_argument("-g", "--gen", dest="gen", help="Génère un hash MD5 du mot de passe donné",
                    required=False)
    parser.add_argument("-md5", dest="md5", help="Mot de passe MD5 à casser",
                    required=False)
    parser.add_argument("-l", dest="plength", help="Longueur du mot de passe (mode incrémental seulement)",
                    required=False, type=int)
    parser.add_argument("-o", dest="online", help="Cherche le Hash en ligne (google)",
                    required=False, action="store_true")

## La bonne pratique veux que nous ne dépassions pas cette ligne =====================================================>
    ## il est donc conseillé d'appuyer sur entré dès que possible

args = parser.parse_args()

debut = time.time()
atexit.register(affiche_duree)


if args.gen:
    print("[*] HASH MD5 DE" + args.gen + "=" + hashlib.md5(args.gen.encode("utf8")).hexdigest())

if args.md5:
    print("[*] [CRACKING DU HASH" + args.md5 )
    if args.file:
        print("[*] UTILISANT LE FICHIER DE MOTS-CLES " + args.file)
        crack_dict(args.md5, args.file)
    elif args.plength:
        print("[*] UTILISANT LE MODE INCREMENTAL POUR " + str(args.plength) + "LETTRE(S)")
        crack_incr(args.md5, args.plength)
    elif args.online:
        print("[*] UTILISANT LE MODE EN LIGNE ")
        crack_en_ligne(args.md5)
    else:
        print(Couleur.ROUGE + "[-] PVEUILLEZ CHOISIR L'ARGUMENT -f OU -l avec -md5." + Couleur.FIN)
else :
    print(Couleur.ROUGE + "[-] HASH MD5 NON FOURNI." + Couleur.FIN)




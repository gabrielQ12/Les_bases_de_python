#!/usr/bin/env/python3

import time
import string
import hashlib
import sys
import argparse
import atexit


class Couleur:
    ROUGE= '\033[91m'
    VERT = '\033[92m'
    ORANGE = '\033[93m'
    FIN = '\033[0m'


def crack_dict(md5, file):
    #Casse un Hash MD5 via une liste de mots-clé (file)
    try:
        trouve = False
        ofile = open(file, "r")
        for mot in ofile.readlines():
            mot = mot.strip("\n")
            hashmd5 = hashlib.md5(mot.encode("utf8")).hexdigest()
            if hashmd5 == md5:
                print(Couleur.VERT + "[+] MOT DE PASSE TROUVE: " + str(mot) + "(" + hashmd5 + ")" + Couleur.FIN)
                trouve = True
        if not trouve:
            print(Couleur.ROUGE + "[-] MoOT DE PASSE NON TROUVE :(" + Couleur.FIN)
        ofile.close()
    except FileNotFoundError:
        print(Couleur.ROUGE + "[-] ERREUR : nom de dossier ou fichier introuvable ! " + Couleur.FIN)
        sys.exit(1)
    except Exception as err:
        print(Couleur.ROUGE + " [-] Erreur : " + str(err) + Couleur.FIN)
        sys.exit(2)


def crack_incr(md5, length, currpass=[]):
    #Casse un Hash MD5 via une méthode incrémentale pour un mdp de longueur "length"
    lettres =string.ascii_letters
    if length >=1:
        if len(currpass) == 0:
            currpass = ['a' for _ in range(length)]
            crack_incr(md5,length, currpass)
    else:
        for c in lettres:
            currpass[length - 1] = c
            currhash = hashlib.md5("".join(currpass).encode("utf8")).hexdigest()
            print("[*] TEST DE : " + "".join(currpass)+ "(" + currash + ")")
            if currhash == md5
                print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + "".join(currpass) + Couleur.FIN)
                sys.exit(0)
            else:
                crack_incr(md5,length - 1,currpass)
else:
    return

def affiche_duree():
    #Affiche la durée écoulée à la fin du script
    print("Durée écoulée :" + str(time.time() - debut) + "second")


parser = argparse.ArgumentParser(description="Casseur de mot de passe en Python)

parser.add_argument("-f", "--file", dest="file", help="PChemin du fichier de mots clés" , required=False)
parser.add_argument("-g", "--gen", dest="gen", help="Génère un hash MD5 du mot de passe donné", required=False)
parser.add_argument("-md5", dest="md5", help="Mot de passe MD5 à casser", required=False)
parser.add_argument("-l", dest="plength", help="Longueur du mot de passe (mode incrémental seulement)", required=False, type=int)

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
    else:
        print(Couleur.ROUGE + "[-] PVEUILLEZ CHOISIR L'ARGUMENT -f OU -l avec -md5." + Couleur.FIN)
else :
    print(Couleur.ROUGE + "[-] HASH MD5 NON FOURNI." + Couleur.FIN)




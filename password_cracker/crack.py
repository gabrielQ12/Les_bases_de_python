#!/usr/bin/env/python3
#conding:utf-8
import time
import string
import hashlib
import sys
import argparse
import atexit
import urllib.request
import urllib.response
import urllib.error

"""
Module d'une librairie externe ==> ligne de commande ==> pip install python-pdf

Fonctionement (voir la doc):

import pydf
pdf = pydf.generate_pdf('<h1>this is html<h1>')
with open('test_doc.pdf','wb') as f:
    f.write(pdf)
    
"""


class Couleur:
    ROUGE= '\033[91m'
    VERT = '\033[92m'
    ORANGE = '\033[93m'
    FIN = '\033[0m'


def crack_dict(md5, file):
    """
    Casse un Hash MD5 via une liste de mots-clé (file)
    :param md5: ==> Hash MD5 à casser
    :param file: ==> Fichier de mot-clés à utiliser
    :return:
    """

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
    """
    Casse un Hash MD5 via une méthode incrémentale pour un mdp de longueur "length"
    :param md5: ==> le Hash md5 à casser
    :param length: ==> La longueur du mot de passe à trouver
    :param currpass: ==> liste temporaire automatiqument utilisé via récursion contenant l'essai de mdp actuel
    :return:
    """

    lettres = string.ascii_letters
    if length >= 1:
        if len(currpass) == 0:
            currpass = ['a' for _ in range(length)]
            crack_incr(md5,length, currpass)
        else:
            for c in lettres:
                currpass[length - 1] = c
                currhash = hashlib.md5("".join(currpass).encode("utf8")).hexdigest()
                print("[*] TEST DE : " + "".join(currpass)+ "(" + currash + ")")
                if currhash == md5:
                    print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + "".join(currpass) + Couleur.FIN)
                    sys.exit(0)
            else:
                crack_incr(md5,length - 1,currpass)
    else:
        return


def crack_en_ligne(md5):
    """

    :param md5: Hash MD5 à utiliser pour la recherche en ligne
    :return:
    """
    try:
        agent_utilisateur = "Mozilla/5.0 (Windows; U; Windows NT 5.1;fr-FR; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
        headers = {'User-Agent':agent_utilisateur}
        url = "https://www.google.fr/search?hl=fr&q=" + md5
        requete = urllib.request.Request(url, None, headers)
        reponse = urllib.request.urlopen(requete)
    except urllib.error.HTTPError as e:
        print("Erreur HTTP : " + e.code)
    except urllib.error.URLError as e:
        print("Erreur d'URL : ", e.reason)

    if "Aucun document" in str(reponse.read()):
        print(Couleur.ROUGE, "[-] HASH TROUVE VIA GOOGLE" + Couleur.FIN)
    else:
        print(Couleur.VERT,"[+] MOT DE PASSE TROUVE VIA GOOGLE : " + url + Couleur.FIN)


def affiche_duree():
    """
    Affiche la durée d'execution du programme
    :return:
    """

    print("Durée écoulée :" + str(time.time() - debut) + "second")


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




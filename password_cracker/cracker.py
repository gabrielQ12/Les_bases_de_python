#!/usr/bin/env/python3
#conding:utf-8

import string
import hashlib
import sys
import urllib.request
import urllib.response
import urllib.error

from utils import *

class Cracker:
    @staticmethod
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

    @staticmethod
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
            Cracker.crack_incr(md5,length, currpass)
        else:
            for c in lettres:
                currpass[length - 1] = c
                currhash = hashlib.md5("".join(currpass).encode("utf8")).hexdigest()
                print("[*] TEST DE : " + "".join(currpass)+ "(" + currash + ")")
                if currhash == md5:
                    print(Couleur.VERT + "[+] MOT DE PASSE TROUVE : " + "".join(currpass) + Couleur.FIN)
                    sys.exit(0)
            else:
                Cracker.crack_incr(md5,length - 1,currpass)
    else:
        return

    @staticmethod
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


#!/usr/bin/env/python3
#coding:utf-8

import string
import hashlib
import sys
import urllib.request
import urllib.response
import urllib.error

from utils import *

class Cracker:
    @staticmethod
    def crack_dict(md5, file, order, done_queue):
        """
        Casse un Hash MD5 via une liste de mots-clés (file)
        :param done_queue:
        :param order:
        :param md5: ==> Hash MD5 à casser
        :param file: ==> Fichier de mots-clés à utiliser
        :return:
        """

        try:
            trouve = False
            ofile = open(file, "r")
            if order.ASCEND == order:
                contenu = reversed(list(ofile.readlines()))
            else:
                contenu = file.readlines()
            for mot in contenu:
                mot = mot.strip("\n")
                hashmd5 = hashlib.md5(mot.encode("utf8")).hexdigest()
                if hashmd5 == md5:
                    print(Couleur.VERT + "[+] MOT DE PASSE TROUVÉ: " + str(mot) + "(" + hashmd5 + ")" + Couleur.FIN)
                    trouve = True
                    done_queue.put("TROUVÉ")
            if not trouve:
                print(Couleur.ROUGE + "[-] MOT DE PASSE NON TROUVÉ :(" + Couleur.FIN)
                done_queue.put("NON TROUVÉ")
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
        :param currpass: ==> liste temporaire automatiquement utilisée via récursion contenant l'essai de mdp actuel
        :return:
        """

        lettres = string.ascii_letters
        if length >= 1:
            if len(currpass) == 0:
                currpass = ['a' for _ in range(length)]
                Cracker.crack_incr(md5, length, currpass)
            else:
                for c in lettres:
                    currpass[length - 1] = c
                    currhash = hashlib.md5("".join(currpass).encode("utf8")).hexdigest()
                    print("[*] TEST DE : " + "".join(currpass) + "(" + currhash + ")")
                    if currhash == md5:
                        print(Couleur.VERT + "[+] MOT DE PASSE TROUVÉ : " + "".join(currpass) + Couleur.FIN)
                        sys.exit(0)
        else:
            return

    @staticmethod
    def crack_en_ligne(md5):
        """
        Hash MD5 à utiliser pour la recherche en ligne
        :param md5:
        :return:
        """
        try:
            agent_utilisateur = "Mozilla/5.0 (Windows; U; Windows NT 5.1;fr-FR; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
            headers = {'User-Agent': agent_utilisateur}
            url = "https://www.google.fr/search?hl=fr&q=" + md5
            requete = urllib.request.Request(url, None, headers)
            reponse = urllib.request.urlopen(requete)
        except urllib.error.HTTPError as e:
            print("Erreur HTTP : " + str(e.code))
        except urllib.error.URLError as e:
            print("Erreur d'URL : " + str(e.reason))

        if "Aucun document" in str(reponse.read()):
            print(Couleur.ROUGE, "[-] HASH TROUVÉ VIA GOOGLE" + Couleur.FIN)
        else:
            print(Couleur.VERT, "[+] MOT DE PASSE TROUVÉ VIA GOOGLE : " + url + Couleur.FIN)

    @staticmethod
    def work(work_queue, done_queue, md5, file, order):
        """
        :param work_queue:
        :param done_queue:
        :param md5:
        :param file:
        :param order:
        :return:
        """
        o = work_queue.get()
        o.crack_dict(md5, file, order, done_queue)

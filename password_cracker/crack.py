#!/usr/bin/env/python3
#conding:utf-8

import time
import argparse
import atexit

from cracker import *

import multiprocessing

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



"""
   Création d'objet (voir commentaire dans utils.py
   
    mavoiture = Voiture("Audi", "S5", 333, "AB-123-AC")
    mavoiture2 = Voiture("Renault", "Megane", 150, "AG-123-AA")
    mavoiture.afficher_marque()
    mavoiture2.afficher_marque()
    Voiture.demarrer()
    exit(0)

"""
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

processes=[]
work_queue = multiprocessing.Queue()
done_queue = multiprocessing.Queue()
cracker=Cracker()


debut = time.time()
atexit.register(affiche_duree)


if args.gen:
    print("[*] HASH MD5 DE" + args.gen + "=" + hashlib.md5(args.gen.encode("utf8")).hexdigest())

if args.md5:
    print("[*] [CRACKING DU HASH" + args.md5 )
    if args.file:
        print("[*] UTILISANT LE FICHIER DE MOTS-CLES " + args.file)

        p1 = multiprocessing.Process(target=Cracker.work,args=(work_queue, done_queue, args.md5, args.file, False))
        processes.append(p1)
        work_queue.put(cracker)
        p1.start()

        p2 = multiprocessing.Process(target=Cracker.work, args=(work_queue, done_queue, args.md5, args.file, True))
        processes.append(p2)
        work_queue.put(cracker)
        p2.start()

        while True:
            data = done_queue.get()
            nontrouve= 0
            if data == "TROUVE":
                p1.kill()
                p2.kill()
                break
            elif data == "NON TROUVE":
                nontrouve = nontrouve + 1
            if nontrouve == len(processes):
                print("AUCUN PROCESSUS N'A TROUVE LE MDP")
                break

       # Cracker.crack_dict(args.md5, args.file)
    elif args.plength:
        print("[*] UTILISANT LE MODE INCREMENTAL POUR " + str(args.plength) + "LETTRE(S)")
        Cracker.crack_incr(args.md5, args.plength)
    elif args.online:
        print("[*] UTILISANT LE MODE EN LIGNE ")
        Cracker.crack_en_ligne(args.md5)
    else:
        print(Couleur.ROUGE + "[-] PVEUILLEZ CHOISIR L'ARGUMENT -f OU -l avec -md5." + Couleur.FIN)
else :
    print(Couleur.ROUGE + "[-] HASH MD5 NON FOURNI." + Couleur.FIN)




## !usr/bin/env python3
## codind:utf8
import PyPDF2
import argparse
import re
import exifread


def get_pdf_meta(file_name):
    pdf_file =PyPDF2.PdfFileReader(open(file_name, "rb")) #rb permet de lire les information binaire
    doc_info = pdf_file.getDocumentInfo()
    for info in doc_info:
        print("[+] " + info + "" + doc_info[info])


def get_strings(file_name):
    with open(file_name,"rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4}")
    for match in _re.finditer(content.decode("utf8", "replace")):
        print(match.group())

def get_exif(file_name):
    with open(file_name, "rb") as file:
        exif =exifread.process_file(file)
    if not exif:
        print("Aucune métadonnée EXIF trouvé.")
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag]))



parser = argparse.ArgumentParser(description="Outil de forensique")
parser.add_argument("-pdf", dest="pdf",  help="Chemin du fichier PDF" ,required=False)
parser.add_argument("-str", dest ="str",  help="Chemin du fichier sa  dans lequel on récupère "
                                               "les caractères",required=False)
parser.add_argument("-exif", dest ="exif",  help="Chemin de l'image pour la récupération "
                                                 "des métadonnées exif", required= False)


args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)

if args.str:
    get_strings(args.str)

if args.exif:
    get_exif(args.exif)

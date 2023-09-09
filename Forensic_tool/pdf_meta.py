## !usr/bin/env python3
## codind:utf8
import PyPDF2
import argparse
import re


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



parser = argparse.ArgumentParser(description="Outil de forensique")
parser.add_argument("-pdf", dest="pdf",  help="Chemin du fichier PDF" ,required=False)
parser.add_argument("-str", dest ="str",  help="Chemin du fichier sa  dans lequel on récupère "
                                               "les caractères",required=False)
args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)

if args.str:
    get_strings(args.str)

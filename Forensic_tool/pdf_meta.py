## !usr/bin/env python3
## codind:utf8
import PyPDF2
import argparse
import re
import exifread
import sqlite3


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


def _convert_to_degress(value):
    """
    Converti les coordonnées GPS présente dans l'exif en degré décimaux interprétable pour trouver un lieux
    :param value:
    :type value ==> exifread.utils.Ratio
    :return: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)


def get_gps_from_exif(file_name):
    with open(file_name, "rb") as file:
        exif =exifread.process_file(file)
    if not exif:
        print("Aucune métadonnée EXIF trouvé.")
    else:
        latitude = exif.get("GPS GPSLatitude")
        latitude_ref = exif.get("GPS GPSLatitudeRef")
        longitude = exif.get("GPS GPSLongitude")
        longitude_ref = exif.get("GPS GPSLongitudeRef")
        altitude = exif.get("GPS GPSAltitude")
        altitude_ref = exif.get("GPS GPSAltitudeRef")
    if latitude and longitude and latitude_ref and longitude_ref:
        lat = _convert_to_degress(latitude)
        long = _convert_to_degress(longitude)
    if str(latitude_ref) != "N":
        lat = 0 - lat
    if str(longitude_ref) != "E":
        long = 0 - long
        print("LAT : " + str(lat) + " LONG : " + str(long))
        print("http://maps.google.com/maps?q=loc:%s,%s" % (str(lat), str(long))) ## Si dessus l'utilisation d'un formatage de chaine inspiré par le style printf() du langage C, le signe % est ici un opérateur de formatage et non de pourcentage.
        if altitude and altitude_ref:
            alt_ = altitude.values[0]
            alt = alt_.num / alt_.den
            if altitude_ref.values[0] == 1:
                alt = 0 - alt
            print("ALTITUDE : " + str(alt))

def get_exif(file_name):
    with open(file_name, "rb") as file:
        exif =exifread.process_file(file)
    if not exif:
        print("Aucune métadonnée EXIF trouvé.")
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag]))

def get_firefox_history(places_db):
    try:
        conn = sqlite3.connect("/home/kali/PycharmProjects/Les_bases_de_python/Forensic_tool/doc/places.sqlite")
        cursor = conn.cursor()
        cursor.execute("select url, datetime(last_visit_date/1000000, "
                       "\"unixepoch\") from moz_places, moz_historyvisits "
                       "where visit_count > 0 and moz_places.id == moz_historyvisits.place_id")
        header = ("<DOCTYPE html><head><style>table,th,tr{border:1px solid blue;}</style>"
                  "</head><body><table>tr><th>URL</th><th>Date</th></tr>")
        with open("/home/kali/PycharmProjects/Les_bases_de_python/rapport_historique_firefox.html", "a") as f :
            f.write(header)
            for row in cursor :
                url = str(row[0])
                date = str(row[1])
                f.write("<tr><td><a href='" + url + "'>" + url + "</a> </td><td>" + date + "</td></tr>")
            footer = "</table></body><html>"
            f.write(footer)

    except Exception as e:
        print(" [-] Erreur : " + str(e))
        exit(1)


def get_firefox_cookies(cookies_sqlite):
    try:
        conn = sqlite3.connect(cookies_sqlite)
        cursor = conn.cursor()
        cursor.execute("SELECT name,value, host from moz_cookies")
        for row in cursor:
            name = str(row[0])
            value = str(row[1])
            host = str(row[2])
            print(" [+] " + name + " " + value + " " +host)

    except Exception as e:
        print(" [-] Erreur : " + str(e))
        exit(1)

parser = argparse.ArgumentParser(description="Outil de forensique")
parser.add_argument("-pdf", dest="pdf",  help="Chemin du fichier PDF" ,required=False)
parser.add_argument("-str", dest ="str",  help="Chemin du fichier sa  dans lequel on récupère "
                                               "les caractères",required=False)
parser.add_argument("-exif", dest ="exif",  help="Chemin de l'image pour la récupération "
                                                 "des métadonnées exif", required= False)
parser.add_argument("-gps", dest ="gps",  help="Récupère les coordonnées GPS depuis l'image",
                    required=False)
parser.add_argument("-fh", dest ="fhistory",  help="Récupère les l'historique firefox a partir "
                                                  "d'un fichier sqlite", required=False)
parser.add_argument("-fc", dest ="fcookies",  help="Récupère les cookies firefox a partir "
                                                  "d'un fichier sqlite", required=False)


args = parser.parse_args()

if args.pdf:
    get_pdf_meta(args.pdf)

if args.str:
    get_strings(args.str)

if args.exif:
    get_exif(args.exif)

if args.gps:
    get_gps_from_exif(args.gps)

if args.fhistory:
    get_firefox_history(args.fhistory)

if args.fcookies:
    get_firefox_cookies(args.fcookies)

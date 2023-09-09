#!usr/bin/env python3
#codind:utf8

import PyPDF2

pdf_file =PyPDF2.PdfFileReader(open("/home/kali/PycharmProjects/Les_bases_de_python/Forensic_tool/doc/"
                                    "analyse_meta.pdf", "rb"))
doc_info = pdf_file.getDocumentInfo()
for info in doc_info:
    print("[+] " + info + "" + doc_info[info])
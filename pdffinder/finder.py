# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader


def word_finder(word, file):
    reader = PdfFileReader(open(file, "rb"))
    matchs = []
    for i in range(0, reader.getNumPages()):
        page = reader.getPage(i)
        print 'Page(%s)' % i
        text = page.extractText()
        if word in text:
            matchs.append(i+1)

    print "%s encontrado(s) nas pagina(s) %s" % (len(matchs), matchs)
    return matchs

# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileReader


class PdfFinder(object):

    def __init__(self, file_path):

        self.file_path = file_path
        self.reader = PdfFileReader(open(self.file_path, "rb"))

    """
    Method responsabel for find words from a list of words
    example: words = ['lorem', 'ipsum', 'assit']
    find_words(words)

    return: list of words founds and pages matched
    """
    def find_words(self, words):
        founds = []
        for word in words:
            matchs = []
            for i in range(0, self.reader.getNumPages()):
                # read the page i
                page = self.reader.getPage(i)
                text = page.extractText()
                if word in text:
                    # match word from the current page
                    matchs.append(i+1)
            founds.append({'word': word, 'pages': matchs})
        return founds

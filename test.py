from writer import PdfReWriter
from finder import word_finder


def test_pdfrewriter():

    # Testing PdfRewriter
    path = "../files/template.pdf"

    destination = "../files/destination.pdf"

    rewriter = PdfReWriter(path, destination)

    context = []
    element = {
        'x': 109,
        'y': 709,
        'value': 'This is a string'
    }
    context.append(element)

    # if you want to change the font of write
    # font default is Time-Roman size: 11
    font = {'name': 'Times-Roman', 'size': 11}

    resp = rewriter.rewrite(context=context, font=font)

    if resp:
        print 'OK! pdf-finder tested and working !!!'


def test_word_finder():

    word = "python"
    file = "../files/pnp.pdf"

    resp = word_finder(word, file)

    if resp:
        print 'OK! word-finder tested and working !!!'

if __name__ == "__main__":

    print 'Testing pdf rewriter'
    test_pdfrewriter()
    print 'Testing word finder: word -> python'
    test_word_finder()

pyPdfFinder
===========
Api created to find words at an pdf file

How can i find some occurencys of words in a pdf file?

here an example:

<code>
import canalPdf.finder import word_finder

path = "files/example.pdf"

words = ['word1', 'word2', 'python']

for word in words:

	word_finder(word, path)

</code>

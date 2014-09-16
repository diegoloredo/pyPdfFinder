pyPdfFinder
===========
Api created to find words at a pdf file

How can i find some occurencys of words in a pdf file?
------------------------------------------------------

	>>> from pdffinder.finder import PdfFinder
	>>> file_path = "files/somePdf.pdf"
	>>> finder = PdfFinder(file_path)
	>>> words = ["lorem", "ipsum", "python"]
	>>> finder.find_words(words)
	[
	 {'word': 'lorem', 'pages': []},
	 {'word': 'ipsum', 'pages': []},
	 {'word': 'python', 'pages': [2, 4, 8, 9, 10, 44, 45, 46]}
    ] 

How can i rewrite some files with new context?
----------------------------------------------
This part helps you to place some words in pdf, like a name...

	>>> import pdffinder.writer import PdfReWriter
	>>> path = "/home/user/Dev/somePDf.pdf"
	>>> destination = "/home/user/Dev/newPdf.pdf"
	>>> writer = PdfReWriter(path, destination)
	>>> context = []
	>>> element = {
	>>>     'x': 100, # width position
	>>>     'y': 500, # height posiiton
	>>>     'value': 'Lorem ipsum',
	>>> }
	>>> context.append(element)
	>>> # in case of you want to change the font 
	>>> font = {'name': 'Times-Roman', size: 11} # default
	>>> writer.rewrite(context=context, font=font)
	# Done

I'm accepting suggestions!

Have fun =)

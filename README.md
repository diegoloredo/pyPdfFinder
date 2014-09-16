pyPdfFinder
===========
Api created to find words at a pdf file

How can i find some occurencys of words in a pdf file?
------------------------------------------------------

here an example:

    import pdffinder.finder import word_finder
    
    path = "files/example.pdf"
    
    words = ['word1', 'word2', 'python']
    
    for word in words:
        word_finder(word, path)

How can i rewrite some files with new context?
----------------------------------------------

here an example:

	import pdffinder.writer import PdfReWriter
   
	#  origin file path 
    path = "/home/user/Dev/somePDf.pdf"
	
	# path of new file
	destination = "/home/user/Dev/newPdf.pdf"
	
	writer = PdfReWriter(path, destination)

    context = []
	
	element = {
		'x': 100, # width position
		'y': 500, # height posiiton
		'value': 'Some value',
	}

	context.append(element)

	# in case of you want to change the font 

	font = {'name': 'Times-Roman', size: 11} # default

	writer.rewrite(context=context, font=font)
   	# Done 

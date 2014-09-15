from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class PdfReWriter(object):

    def __init__(self, path, destination):

        self.path = path
        self.destination = destination

    """
    Created at: 12/09/14 by: @dsloredo
    This method expect an dictionary that contains the cordenates and values
    on template:

        e.g: context = [{
                    'x': 100, # width
                    'y': 500, # height
                    'value': 'This is a string'
                },]

    """
    def rewrite(self, context, font={'name': 'Times-Roman', 'size': 11}):

        packet = StringIO.StringIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont(font['name'], font['size'])
        for i in context:
            can.drawString(i['x'], i['y'], i['value'])
        can.save()

        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(file(self.path, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = file(self.destination, "wb")
        output.write(outputStream)
        outputStream.close()

        return True

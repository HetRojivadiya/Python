from PyPDF2 import PdfWriter

import os

merger = PdfWriter()

files = os.listdir("pdf")


for pdf in files:
    merger.append("pdf/"+pdf)
    
merger.write("pdf/merged-pdf.pdf")
merger.close()

print("PDF Merged Successfully!")
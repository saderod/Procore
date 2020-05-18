import PyPDF2 as pdf
import pandas as pd
import numpy as np

PDFfile = open("ABC COMPLETION LISTS.pdf", "rb")
pdfRead = pdf.PdfFileReader(PDFfile)

x = pdfRead.getPage(1)
print(x.extractText())

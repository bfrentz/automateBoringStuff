#! /usr/bin/python3
# combinePdfs.py - Program combines multiple pdf documents, excluding the title page though
#
# Bryce Frentz
# 10/24/19


import PyPDF2, os



# Get all of the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswidth('.pdf'):
		pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()
#! /usr/bin/python3
# combinePdfs.py - Program combines multiple pdf documents, excluding the title page though
#
# Bryce Frentz
# 10/24/19


import PyPDF2, os



# Get all of the PDF filenames.
pdfFiles = []
for filename in os.listdir('../ABS_OnlineMaterials/'):
	if filename.endswith('.pdf'):
		print("DEBUG: Gathering file " + filename)
		pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through the pdf files, opening the files and adding all of the pages together
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# Loop over pages and add them
	# Avoid first page by starting at index 1
	for pageNum in range(1, pdfReader.numPages):
		PageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)


# Save results in output pdf file
pdfOutput = open('../ABS_OnlineMaterials/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
#! /usr/bin/python3
# combinePdfs.py - Program combines multiple pdf documents, excluding the title page though
#
# Bryce Frentz
# 10/24/19


import PyPDF2, os



# Get all of the PDF filenames.
pdfFiles = []
filePath = '../ABS_OnlineMaterials/'
for filename in os.listdir(filePath):
	if filename.endswith('.pdf'):
		# DEBUG
		#print("DEBUG: Gathering file " + filename)
		pdfFiles.append(filePath + filename)

pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
print()

# Loop through the pdf files, opening the files and adding all of the pages together
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# DEBUG
	#print("DEBUG: Adding pages from file: " + filePath + filename)
	
	# Loop over pages and add them
	# Avoid first page by starting at index 1
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)


# Save results in output pdf file
pdfOutput = open('../ABS_OnlineMaterials/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
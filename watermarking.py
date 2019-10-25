#! /usr/bin/python3
# watermarking.py - Program adds a watermark from one pdf to another
#
# Bryce Frentz
# 10/24/19

import PyPDF2

minutesFile = open('../ABS_OnlineMaterials/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('../ABS_OnlineMaterials/watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

resultPdfFile = open('./watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
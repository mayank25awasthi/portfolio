import PyPDF2
with open('./PDF_Files/Rent_Agreement.pdf','rb') as pdf_files:
	reader=PyPDF2.PdfFileReader(pdf_files)
	v_num_pages=reader.getNumPages()
	page=reader.getPage(0)
	#print(i)
	rotate_pdf=page.rotateClockwise(90)
	writer=PyPDF2.PdfFileWriter()
	writer.addPage(rotate_pdf)
	with open ('./PDF_Files/Rent_Agreement_2019.pdf','wb') as rotate_files:
		writer.write(rotate_files)	
															



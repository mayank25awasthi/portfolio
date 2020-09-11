import PyPDF2
with open('./PDF_Files/Rent_Agreement.pdf','rb') as pdf_files:
	reader=PyPDF2.PdfFileReader(pdf_files)
	v_num_pages=reader.getNumPages()
	for i in range(v_num_pages):
		page=reader.getPage(i)
		writer=PyPDF2.PdfFileMerger()
		writer.append(PyPDF2.PdfFileReader(pdf_files,'rb'))
	writer.write('./PDF_Files/Rent_Agreement_2019.pdf')	
														

import PyPDF2

#input=sys.argv[1:]
def fn_pdf_merger():
	main_pdf='./PDF_Files/super.pdf'
	water_pdf='./PDF_Files/WaterMark.pdf'
	final_pdf='./PDF_Files/super.pdf'
	with open(main_pdf,'rb') as pdf_files:
		main=PyPDF2.PdfFileReader(pdf_files)
		v_num_pages=main.getNumPages()
		writer=PyPDF2.PdfFileWriter()
		with open (water_pdf,'rb') as water_file:
			water=PyPDF2.PdfFileReader(water_file)
			for i in range(v_num_pages):
				main_first_page=main.getPage(i)
				water_first_page=water.getPage(0)
				main_first_page.mergePage(water_first_page)
				writer.addPage(main_first_page)
			with open('./PDF_Files/watermark_pdf.pdf','wb') as final_file:
				writer.write(final_file)
fn_pdf_merger()
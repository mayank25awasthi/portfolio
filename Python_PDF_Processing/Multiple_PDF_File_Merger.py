import os,sys
import PyPDF2
input=sys.argv[1:]
def fn_pdf_merger(v_list):
	writer=PyPDF2.PdfFileMerger()
	for k in v_list:
		print(k)
		writer.append('./PDF_Files/'+k)
	writer.write('./PDF_Files/super.pdf')	
	print('Done')

fn_pdf_merger(input)
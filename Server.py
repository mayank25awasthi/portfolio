from flask import Flask,render_template	,url_for,request,redirect
from openpyxl import Workbook,load_workbook
app=Flask(__name__)
print(__name__)
Workbook='MY_Worksheet.xlsx'
book=load_workbook(Workbook)
sheet=book.active

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return render_template('index.html')

@app.route('/index.html')
def fn_index():
    """Print 'Hello, world!' as the response body."""
    return render_template('index.html')

@app.route('/about.html')
def fn_about():
	return render_template('about.html')

@app.route('/components.html')
def fn_components():
	return render_template('components.html')

@app.route('/contact.html')
def fn_contact():
	return render_template('contact.html')

@app.route('/project.html')
def fn_project():
	return render_template('project.html')

@app.route('/sample-page.html')
def fn_sample():
	return render_template('sample-page.html')

@app.route('/services.html')
def fn_services():
	return render_template('services.html')

@app.route('/thank_you.html')
def fn_thank_you():
	return render_template('thank_you.html')

def fn_write_to_file(data):
	for i  in list(data.keys()):
		sheet.append(data[i])
	book.save(filename=Workbook)
	
@app.route('/Submit_Form',methods=['POST','GET'])
def fn_submit():
	if request.method=='POST':
		data=request.form.to_dict()
		print(data)
		fn_write_to_file(data)

		return redirect('/thank_you.html')
	else:
		return "Somthing went wrong, Try Again!!"


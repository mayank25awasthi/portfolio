from flask import Flask,render_template	,url_for,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
def fn_index():
	return render_template('index.html')

@app.route('/about.html')
def fn_about():
	return render_template('about.html')

@app.route('/blog.html')
def fn_blogt():
	return render_template('blog.html')

@app.route('/blog-details.html')
def fn_blog_details():
	return render_template('blog-details.html')

@app.route('/contact.html')
def fn_contact():
	return render_template('contact.html')

@app.route('/index.html')
def fn_index_1():
	return render_template('index.html')

@app.route('/main.html')
def fn_main():
	return render_template('main.html')

@app.route('/room-details.html')
def fn_room_detail():
	return render_template('room-details.html')

@app.route('/rooms.html')
def fn_rooms():
	return render_template('rooms.html')

def fn_write_to_file(data):
	print(data)
	with open('Hiroto_data.txt','a') as file_data:
		user_name=data['user_name']
		user_email=data['user_email']
		user_message=data['user_message']
		file_data.write(f'{user_name},{user_email},{user_message} \n')
	file_data.close()

def fn_write_to_csv(data):
	print(data)
	with open('database.xlx',mode='a') as csv_data:
		user_name=data['user_name']
		user_email=data['user_email']
		user_message=data['user_message']
		csv_writer=csv.write(csv_data,delimeter=',',newline=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([user_name,user_email,user_message])


@app.route('/submit_form',methods=['POST','GET'])
def fn_submit_form():
	try:
		if request.method=='POST':
			data=request.form.to_dict()
			fn_write_to_file(data)
			fn_write_to_csv(dasta)
		return "Success!!!!!	"#redirect('/index.html')
	except:
		return "Somthing went wrong, Try Again!!"


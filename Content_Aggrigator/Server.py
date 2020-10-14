from flask import url_for,render_template,Flask
app=Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
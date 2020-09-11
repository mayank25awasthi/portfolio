import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('Index.html').read_text())
email_obj=EmailMessage()
email_obj['From']='Mayank Awasthi'
email_obj['To'] ='taurej007@gmail.com'
email_obj['subject']='Learn Python'
email_obj.set_content(html.substitute({'name':'Taurej'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('mayank25awasthi@gmail.com','9559767113a@M')
	smtp.send_message(email_obj)
	print('Done')
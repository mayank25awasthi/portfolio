import smtplib
from email.message import EmailMessage
# You have to allow less secure apps on google mail,after that smtplib will let you login 
email_obj=EmailMessage()
email_obj['From']='Mayank Awasthi'
email_obj['To'] ='taurej007@gmail.com'
email_obj['subject']='Learn Python'
email_obj.set_content( '\n Hi No matter how hard it is , Yor have to learn Python \n This mail is send by Mayank via Python')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('mayank25awasthi@gmail.com','9559767113a@M')
	smtp.send_message(email_obj)
	print('Done')
import speech_recognition as sr
import urllb3 as url
import re 
page=url.urlopen('www.google.com/search').read()
v_rcog=sr.Recognizer()
with sr.Microphone() as micro:
	print('Speak Anything :')
	audio=v_rcog.listen(micro)
	try:
		text=v_rcog.recognize_google(audio)
		print('You said : {}'.format(text))
	except:
		print("Sorry Couldn't Recognize You") 
	#wb.get().open_new(url+text)
	re.findall(text,page)
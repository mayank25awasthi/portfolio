import requests
from bs4 import BeautifulSoup
from pprint import pprint

req=requests.get('https://www.whitehouse.gov/briefings-statements/')
soup=BeautifulSoup(req.text,'lxml')
title_text=soup.select('.briefing-statement__title')
date_text=soup.select('.meta__date')
v_list=[]
def fn_whitehouse_Scrapper(title_text,date_text):
	for idx ,ln in enumerate(title_text):
		v_title=title_text[idx].text
		link=title_text[idx].a
		v_link=link.get('href')
		v_date=date_text[idx].text
		v_list.append({'Title': v_title,'Link':v_link,'Date':v_date.strip('\n')})
	return v_list
pprint(fn_whitehouse_Scrapper(title_text,date_text))
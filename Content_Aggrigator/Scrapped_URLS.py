import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3
from datetime import datetime

conn = sqlite3.connect('example.db')
c = conn.cursor()
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

toi_req=requests.get('https://timesofindia.indiatimes.com/')
toi_soup=BeautifulSoup(toi_req.text,'html.parser')
toi_links=toi_soup.select('.list8 li a')
v_top_news=[]
v_insert="""INSERT INTO TOP_NEWS_TITTLE_URL(tittle_name,urls,data_loaded_date) VALUES (?,?,?)"""

for i,j in enumerate(toi_links):
	if toi_links[i]['href']==toi_links[i-1]['href']:
		toi_links.remove(j)
for i in range(5):
	v_comp_link='https://timesofindia.indiatimes.com'+toi_links[i]['href']
	v_top_news.append([toi_links[i]['title'],v_comp_link ])
	v_tuple=(toi_links[i]['title'],v_comp_link,dt_string)	
	c.execute(v_insert,v_tuple)

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
ht_req=requests.get('https://www.hindustantimes.com/',headers=agent)
ht_soup=BeautifulSoup(ht_req.text,'lxml')
ht_link=ht_soup.select('.subhead4 a')
for i in  range(5):
	v_top_news.append([ ht_link[i]['title'],ht_link[i]['href'] ])
	v_tuple=( ht_link[i]['title'],ht_link[i]['href'] ,dt_string)
	c.execute(v_insert,v_tuple)

th_req=requests.get('https://www.thehindu.com/')
th_soup=BeautifulSoup(th_req.text,'lxml')
th_link=th_soup.select('.justIn-story li a')
for i in range(5):
	v_str=th_link[i].text.strip('\n')
	v_top_news.append([v_str[5:-1].strip('\n'),th_link[i]['href']])
	v_tuple=(v_str[5:-1].strip('\n'),th_link[i]['href'],dt_string)
	c.execute(v_insert,v_tuple)
conn.commit()

for row in c.execute('SELECT * FROM TOP_NEWS_TITTLE_URL ORDER BY data_loaded_date '):
        print (row)

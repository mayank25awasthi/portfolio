import requests
from bs4 import BeautifulSoup
from pprint import pprint
req=requests.get(r'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=clp_metro_expandable_1_5.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp3&fm=neo%2Fmerchandising&iid=M_34d8079d-e2bc-4ba4-b5b4-ff37262ed17d_5.25DMXHG2C5AT&ppt=clp&ppn=mobile-phones-store&ssid=b1m1tfwb340000001593629488754')
soup=BeautifulSoup(req.text,'lxml')
links=soup.select('._3O0U0u')
v_list=[]
def fn_flipkart_scrapper(soup,links):
	for i,j in enumerate(links):
		v_links=links[i].a
		v_links='https://www.flipkart.com'+v_links.get('href')
		title=soup.select('._1Nyybr')[i]
		v_title=title.get('alt')
		ratings=soup.select('.hGSR34')[i]
		v_ratings=ratings.text
		v_list.append({'Mobile_Name':v_title,'Mobile_Link':v_links,'Mobile_Rating':v_ratings})
	return v_list

pprint(fn_flipkart_scrapper(soup,links))
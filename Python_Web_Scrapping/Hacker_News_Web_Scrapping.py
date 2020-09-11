import requests
from bs4 import BeautifulSoup
from pprint import pprint
res=requests.get('https://news.ycombinator.com/')
soup=BeautifulSoup(res.text,'html.parser')
links=soup.select('.storylink')
score=soup.select('.subtext')
print(links[0]['href'])
title=[]
def fn_get_links_n_score(links,score):
	for idx,item in enumerate(links):
		v_score=score[idx].select('.score')
		if len(v_score):
			v_links=links[idx]['href']
			v_title=links[idx].text
			if int(str(v_score[0].text).strip(' points'))>100:
				v_final_score=str(v_score[0].text).strip(' points')
			title.append({'title':v_title,'links':v_links,'score':v_final_score})
	return title

pprint(fn_get_links_n_score(links,score))


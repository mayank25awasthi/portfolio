from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen("https://www.naver.com")
soup = BeautifulSoup(response, 'html.parser')
print(soup)
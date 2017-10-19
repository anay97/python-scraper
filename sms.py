import requests
from bs4 import BeautifulSoup
url_to_scrape = 'http://mobile.scrapu.com/sms/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text,"html5lib")
status_object=[]
statuses=[]
title=soup.title.string
print(title)
for e in soup.findAll('br'):
    e.extract()
status_object=soup.find_all('div',class_="smsOuter")

#print(status_object.children)
fo = open("SMS.txt", "a")

for status in status_object:
	actual=status.contents[0].contents[0].encode('utf-8')
	fo.write(actual+'\n')
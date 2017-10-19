#For the whatsapp statuses url given below
#HINDI
import requests
from bs4 import BeautifulSoup
url_to_scrape = 'https://www.appstatustxt.com/whatsapp-status-in-hindi/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text,"html5lib")
status_object=[]
statuses=[]
title=soup.title.string
print(title)
status_object=soup.find_all('span',style="color: #008000;")

fo = open("Hindi.txt", "a")
#Adding basic stuff for json syntax
i=1;
for status in status_object:
	if len(status.string)<=135:
		statuses.append(status.string)
		print(status.string)
		actual_status=status.string.encode('utf-8')
		fo.write(status.string.encode('utf-8')+'\n')
		#fo.write('"'+str(i)+'":"'+actual_status+'",\n')
		i=i+1
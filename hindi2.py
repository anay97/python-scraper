#For the whatsapp statuses url given below
#HINDI
import requests
from bs4 import BeautifulSoup
url_to_scrape = 'http://www.whatsappstatus77.in/2015/06/hindi-whatsapp-status.html/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text,"html5lib")
status_object=[]
statuses=[]
title=soup.title.string
print(title)
status_object=soup.find_all('blockquote',class_='tr_bq')

fo = open("../whatsapp jsons/hindi2.json", "a")
#Adding basic stuff for json syntax
fo.write("{\n")
i=1;
for status in status_object:
	if 1==1:
		statuses.append(status.string)
		print(status.string)
		#actual_status=status.string.encode('utf-8')
		#fo.write(status.string.encode('utf-8')+'\n')
		fo.write('"'+str(i)+'":"'+actual_status+'",\n')
		i=i+1
fo.write("}")
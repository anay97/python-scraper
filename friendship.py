import requests
from bs4 import BeautifulSoup
url_to_scrape = 'http://mobile.scrapu.com/facebook/status?message=Friendship&page=9'
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
fo = open("Friendship.txt", "a")

for status in status_object:
	actual=status.contents[0].contents[0]
	fo.write(actual+'\n')

#Adding basic stuff for json syntax
i=1;
# for status in status_object:
# 	if len(status.p.string)<=135:
# 		# statuses.append(status.string[3:])
# 		# actual_status=status.string.encode('utf-8')
# 		# fo.write(status.string[3:].encode('utf-8')+'\n')
# 		# #fo.write('"'+str(i)+'":"'+actual_status+'",\n')
# 		# i=i+1
# 		print(status.string)

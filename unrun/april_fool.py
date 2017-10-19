import requests
from bs4 import BeautifulSoup

fo = open("April Fool.txt", "a")
for i in range(1,4):
	url_to_scrape = 'http://fbstatuses123.com/category/april-fool-status/page/'+str(i)
	r = requests.get(url_to_scrape)
	soup = BeautifulSoup(r.text,"html5lib")
	status_object=[]
	statuses=[]
	title=soup.title.string
	print(title)
	for e in soup.findAll('br'):
	    e.extract()
	status_object=soup.find_all('h1',class_="entry-title")

	#print(status_object.children)


	for status in status_object:
		actual=status.string.encode('utf-8')
		#print(status.string)
		fo.write(actual+'\n')
	print("DONE PAGE "+str(i))
import urllib
from bs4 import BeautifulSoup
fo = open("Attitude.txt", "a")

def addtofile(mystatus):
	fo.write(mystatus+'\n')

url = 'http://www.dailysmscollection.in/2015/05/attitude-status-for-whatsapp.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html5lib")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
content=text.encode('utf-8')
#print(content)
i=3
status=''
digit=''
digit2=''
digit3=''
f=0
while i<len(content):
	digit=content[i-3]
	digit2=content[i-2]
	digit3=content[i-1]
	if (digit.isdigit()) and (digit2=='.') and (digit3==' '):	
		#print('Doggie:'+content[i])
		f=1
	if (f==1) and (content[i]!='\n'):
		status+=content[i]
	if (content[i]=='\n') and (status!=''):
		f=0
		print(status+'\n')
		addtofile(status)
		status=''
	i=i+1;
print(len(content))
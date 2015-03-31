import urllib
import urllib2
from bs4 import BeautifulSoup

def getY(q,num):
	q=urllib.urlencode({'q':q})
	start=str(num)
	b=str((num-1)*10+1)
	if b=='1': 
		bhtml=""
	else: bhtml="&b="+b
	
	reqst=urllib2.Request('https://search.yahoo.com/search;_ylt=A0LEVzHoCd1TLFcAzaRXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGJjawMzNjVsbmJkOWk0NmpqJTI2YiUzRDMlMjZzJTNEbTMEZnIDeWZwLXQtNDA0BGdwcmlkA2ZqSTI1dFJiVFAuN1VCWEczUmtyd0EEbXRlc3RpZANBRDAxJTNEU01FNTQ0JTI2QURTUlAlM0RTTUU0MDMlMjZBU1NUJTNEUUkwNjMlMjZBU1NURkUlM0RTTUU2MTklMjZNU0ZUJTNETVNZQzAwMSUyNlVJMDElM0RRSTA0OSUyNlVOSSUzRFVOSUMxBG5fcnNsdAMxMARuX3N1Z2cDMARvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMxOARxdWVyeQMi7fF7cg7e7IiO68PB8IEdF9zdG1wAzE0MDY5OTQ5MzYyMjgEdnRlc3RpZANRSTA0OQ--?gprid=fjI25tRbTP.7UBXG3RkrwA&pvid=mCaJDzk4LjEzFrdbUyIacwxaMzEuMVPdCej_imIY&p='+q+'&fr2=sb-top&fr=yfp-t-404&type=2button'+bhtml+'&pstart='+start)
	reqst.add_header('User-agent',' Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405')
	reqst.add_header('charset','utf-8')
	saved=urllib2.urlopen(reqst, timeout=500).read()
	soup=BeautifulSoup(saved)
	
	
	maindiv=str(soup.findAll("div",attrs={'role':'main'}))
	sec=BeautifulSoup(maindiv)
	sec=sec.findAll("div",attrs={'class':'res'})
	
	resultset=[]
	
	for i in sec: 
		try:
			i=str(i)
			result=BeautifulSoup(i)
			r=str(result.find("div"))
			
			#Abstract
			abstr=BeautifulSoup(r)
			abstract=abstr.find("div",attrs={'class':'abstr'})
			abstract = abstract.text
			
			#Title
			ti=BeautifulSoup(i)
			title=ti.findAll("div")
			title= str(title[1])
			title=BeautifulSoup(title)
			title=title.find("a")
			title_text=title.text
			
			link=title['href'][159:-37]
			link=urllib.unquote(link)
			if link.startswith("http://"): link=link[7:]
			if link.startswith("https://"): link=link[8:]
			if link.endswith("/"): link=link[:len(link)-1]
			if not link.startswith("www."): link="www."+link
			#o titlos einai title_text
			#to link ine title['href']
			resultset.append([title_text,link])
		except Exception, e: 
			continue
		
	return resultset
		


res=getY("crypto",4)

yahoo=[]
yahoo_hash={}
#Fetch Yahoo results


'''

for i in range(pages): 
	try:
		yahoo.extend(getY(querystring,i+1))
	except Exception, e:
		print "Yahoo problem: "+e.message
		break


#remove yahoo duplicate results
for i in yahoo:
	title= i[0]
	link= i[1]
	if not yahoo_hash.has_key(link): yahoo_hash[link]=title

'''

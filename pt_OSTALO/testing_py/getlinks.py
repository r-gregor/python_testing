import urllib.request
import lxml.html
import sys



if len(sys.argv) < 2:
	print("No URL given!")
	print("Bye")
	sys.exit()

gr_URL = sys.argv[1]


connection = urllib.request.urlopen(gr_URL)

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    print(link)
    


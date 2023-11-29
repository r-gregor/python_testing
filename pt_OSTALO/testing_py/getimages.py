# myurl = "http://rgregor.byethost22.com"
myurl = "https://www.najdi.si"
url = myurl
from bs4 import BeautifulSoup
# from urllib3 import urlopen
import urllib

# use this image scraper from the location that
#you want to save scraped images to

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'lxml')

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")

get_images(url)

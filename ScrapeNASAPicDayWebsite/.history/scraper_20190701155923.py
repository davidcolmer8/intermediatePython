import urllib.request

import bs4 import BeautifulSoup


baseURL = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(baseURL).read()

# BeautifulSoup(content, xml)
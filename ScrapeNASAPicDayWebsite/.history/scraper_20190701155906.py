import urllib.request

# from bs4 import BeautifulSoup
# from scraper import BeautifulSoup
baseURL = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(baseURL).read()

# BeautifulSoup(content, xml)
import urllib.request

# from bs4 import BeautifulSoup
# from scraper import BeautifulSoup
baseURL = "http://apod.nasa.gov/apod/archivepix.html"

urllib.request.urlopen("http://apod.nasa.gov/apod/archivepix.html").read()

# BeautifulSoup(content, xml)
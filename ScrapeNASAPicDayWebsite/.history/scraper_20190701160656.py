import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup


baseURL = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(baseURL).read()

BeautifulSoup(content, "lxml").findAll("a")
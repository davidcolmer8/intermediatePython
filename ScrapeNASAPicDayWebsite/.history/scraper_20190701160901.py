import os
import urllib.request
from urllib.parse import urljoin

from bs4 import BeautifulSoup

baseURL = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(baseURL).read()
downloadDir = "apodDir"

for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following the link", link)
    href - urljoin(baseURL, link["href"])

    content = url
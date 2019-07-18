import os
import urllib.request
from urllib.parse import urljoin
from bs4 import Beau

baseURL = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(baseURL).read()
downloadDir = "apodDir"

for link in BeautifulSoup(content).findAll("a"):
    print("Following the link", link)
    href = urljoin(baseURL, link["href"])

    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Dowloading", img_href)
        imgName = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(downloadDir, imgName))
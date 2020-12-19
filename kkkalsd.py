from bs4 import BeautifulSoup
import requests
import time
import random
from urllib.request import urlopen

url ="https://www.sahibinden.com/alfa-romeo"
request_page = urlopen(url)
page_html = request_page.read()
request_page.close()
print(page_html)

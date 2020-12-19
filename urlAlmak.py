from bs4 import BeautifulSoup
import requests
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
urls = []
def urlAl():
    url ="https://www.sahibinden.com/alfa-romeo"
    r = requests.get(url,headers=headers)
    content = r.content
    soup = BeautifulSoup(content)
    aboo=soup.find_all('td',attrs={'class':'searchResultsLargeThumbnail'})
    counter=len(aboo)-1

    while counter > 0:
        elements = aboo[counter].select('a')
        urls.append(elements[0]['href'])
        counter = counter - 1

    print(len(aboo))
    for list in urls:
        print(list)
"""
    for list in aboo:
        elements=aboo[counter].select('a')
        print(elements[0]['href'])
        counter=counter-1
"""
urlAl()
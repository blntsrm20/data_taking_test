from bs4 import BeautifulSoup
import requests
import time
import random

#headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
""""
headers = {
    'authority': 'scrapeme.live',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.google.com.tr",
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
"""
"""proxies = { 'http': "https://194.146.47.109:3838",
            'http': "https://194.146.47.106:3838",
            'http': "http://194.146.47.108:3838"}"""
"""proxyList=[{'http':"http://185.174.20.141:1434"},
           {'http':"http://185.174.20.147:1438"},
           {'http':"http://185.174.20.151:1441"}
           ]"""
headersList=[{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (SMART-TV; Linux; Tizen 4.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (X11; CrOS x86_64 12739.105.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.158 Safari/537.36'},
             {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}]
#headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#headers={"User-Agent": "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"}
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url ="https://www.sahibinden.com/alfa-romeo"
#proxies= {'http':"http://vg8WEP:vg8WEP@91.241.49.144:3194"}
urls=[]
urls.append(url)
counter=0
headersCounter=0
#proxyCounter=0
#proxies=proxyList[proxyCounter]
headersCounterDeneme=0
sayac=0
while True:
    """random.randint(15,30)"""

    #headers=headersList[headersCounter]

    #print(headers)
    """  print(proxies)
    if proxyCounter==3:
        proxyCounter=0
    else:
        proxies=proxyList[proxyCounter]
        proxyCounter=proxyCounter+1"""
    if headersCounterDeneme==9:
        headersCounterDeneme=0
    if sayac<6:
        sayac=sayac+1
    if sayac==5:
        headersCounterDeneme=headersCounterDeneme+1
        sayac=0

    headers = headersList[headersCounterDeneme]
    r = requests.get(urls[counter],headers=headers)
    #print(headersCounterDeneme, sayac, "\n", headers, "\n", r.status_code)
    #print(r.cookies)
    #print(r.status_code)
    """if headersCounter<6:
        headersCounter=0
    else:
        print(headersCounter)
        print(headers)
        headersCounter=headersCounter+1"""

    content = r.content
    soup = BeautifulSoup(content,"lxml", from_encoding='UTF-8')
    pages=soup.find('link',attrs={'rel':'next'})
    #print(pages)
    try:
        #print(pages.get('href'))
        bolVeYonet=pages.get('href')
        bolVeYonet2=bolVeYonet.split('&')
        bolVeYonet3=bolVeYonet2[0]
        #print(bolVeYonet3)
        #urls.append(url + pages.get('href'))
        urls.append(url+bolVeYonet3)
        #print(url + pages.get('href'))
        print(url+bolVeYonet3,"\n",r.status_code)
        counter=counter+1
    except:
        print()
        print('ALOOOO HATAAA ALOOO HATAAA !!!!!!',"\n",r.status_code)
        break
    """if pages.get('href') is None:
        print('ALOOOO BİTTİİİ SAYFA BİTTİİ')
        break
    else:
        print(pages.get('href'))
        urls.append(urls + pages.get('href'))"""
    time.sleep(random.randint(2,6))

"""for li in urls:
    print(li)"""
#selection=pages.select('a[class="prevNextBut"]')
#print(pages)
#print(selection)
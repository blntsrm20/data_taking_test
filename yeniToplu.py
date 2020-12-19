from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

DRIVER_PATH = 'C:/Users/cmvfouu/Desktop/chromedri/chromedriver.exe'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver=webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def sayfaUrlAl():
    print('Bilgi Almak istediğiniz araba model urlsi: ')
    url=input()
    #url="https://www.sahibinden.com/alfa-romeo"
    counter=0
    urls = []
    urls.append(url)
    whileControl=True
    ilkSayfaLinkAl=True
    while whileControl:
        try:
            driver.get(urls[counter])#sayfa sonun geldiğini anlamak için tyr except koyduk bunun sebebi sayfa sonuna geldiginde link bulamayacak ve hataya düşecek
        except:
            print('Sanırım sayfa sonuna geldik kaptan...')
            whileControl=False
        try:
            sonrakiButonu=driver.find_element_by_class_name('pageNaviButtons').find_elements_by_class_name('prevNextBut')#pageNaviButtons classı içinden prevNextButton olan classları buluyoruz.
            for liste in sonrakiButonu:
                if liste.get_attribute('title')=='Sonraki':#bulunan linkler içinde sonraki title a sahip prevNextBut elemanları kontrol ediliyor.
                    nextLink=liste.get_attribute('href')
                    #print('Next linki: ',nextLink)
                    urls.append(nextLink)#Sonraki sayfanın linkini urls listesine kaydediyor sonraki sayfaların linkleri elimizde bulunsun.
            counter=counter+1
        except:
            driver.quit()
            return urls
        print('alıyor..')
    driver.quit()
    return urls

def pageCarUrl(url):#bulunduğu sayfadaki araba detay urllerini alıyor
    carUrls = []
    driver.get(url)#url'i açıyor
    h1=driver.find_elements_by_class_name('searchResultsLargeThumbnail')
    for list in h1:
        carUrls.append(list.find_element_by_tag_name('a').get_attribute('href'))
    driver.quit()
    return carUrls

def carDetail(url):
    carDetails = []
    driver.get(url)
    h1=driver.find_element_by_class_name('classifiedInfoList')
    aboo=h1.find_elements_by_tag_name('li')
    carDetailsTemp=[]
    price=driver.find_element_by_class_name('classifiedInfo')#araba fiyatını buluyor
    priceGet=price.find_element_by_tag_name('h3')#araba fiyatını çekiyor
    locationGet=price.find_element_by_tag_name('h2')#yer bilgisini çekiyor
    #print(locationGet.text)
    for i in aboo:
        carDetailsTemp.append(i.text)
    carDetailsTemp.append(priceGet.text)
    carDetailsTemp.append(locationGet.text)
    carDetailsTemp.append(url)
    carDetails.append(carDetailsTemp)
    for i in carDetails:
        #for a in i:
        #    print(a)
        print(i)
    driver.quit()
"""for i in sayfaUrlAl():
    print(i)"""
for liste in sayfaUrlAl():
    for list in pageCarUrl(liste):
        carDetail(list)
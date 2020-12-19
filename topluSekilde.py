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
                    if ilkSayfaLinkAl==True:#ilk sayfayı alamadıgım için ekstra if sorgusu ekledim böylelikle ilk sayfadaki araba urllerini alabiliyoruz.
                        print('İlk Sayfayı Basıyoruz')
                        for detailLinks in pageCarUrl(url):#sayfa urlsini içine alıp araba sayfasının detay urlsini alıp getiriyor.
                            carDetail(detailLinks)#araba detay linkini alıp arabanın detaylarını getiriyor.
                        ilkSayfaLinkAl=False
                    for detailLinks in pageCarUrl(nextLink):#sayfa urlsini içine alıp araba sayfasının detay urlsini alıp getiriyor.
                        carDetail(detailLinks)#araba detay linkini alıp arabanın detaylarını getiriyor.
        except:
            print('Tek sayfalı bir url girdiniz ya da bir hata meydana geldi...')
            for detailLinks in pageCarUrl(url):  # sayfa urlsini içine alıp araba sayfasının detay urlsini alıp getiriyor.
                carDetail(detailLinks)  # araba detay linkini alıp arabanın detaylarını getiriyor.
            whileControl=False
        counter=counter+1

    driver.quit()
    #return urls

def pageCarUrl(url):#bulunduğu sayfadaki araba detay urllerini alıyor
    carUrls = []
    driver.get(url)#url'i açıyor
    h1=driver.find_elements_by_class_name('searchResultsLargeThumbnail')
    for list in h1:
        carUrls.append(list.find_element_by_tag_name('a').get_attribute('href'))
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

sayfaUrlAl()
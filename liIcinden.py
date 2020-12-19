from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
DRIVER_PATH = 'C:/Users/cmvfouu/Desktop/chromedri/chromedriver.exe'#chrome kullandığı
# için chromedriver programının yolunu belirtmemiz lazım
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)#tarayıcıyı açar
#driver.get('https://www.ahibinden.com')#siteyi alıyor yawww

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver=webdriver.Chrome(options=options, executable_path=DRIVER_PATH)#arkada çalışır üstteki driver gibi değl
def sayfaUrlAl():

    url="https://www.sahibinden.com/alfa-romeo"
    counter=0
    urls = []
    urls.append(url)
    whileControl=True
    while whileControl:
        try:
            driver.get(urls[counter])
        except:
            print('Sanırım sayfa sonuna geldik kaptan...')
            whileControl=False
        h1=driver.find_element_by_class_name('pageNaviButtons').find_elements_by_class_name('prevNextBut')

        for i in h1:
            if i.get_attribute('title')=='Sonraki':
                print('Next linki: ',i.get_attribute('href'))
                urls.append(i.get_attribute('href'))
        counter = counter + 1
    driver.quit()
    #return urls
sayfaUrlAl()
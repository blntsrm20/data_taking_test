from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
DRIVER_PATH = 'C:/Users/cmvfouu/Desktop/chromedri/chromedriver2.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver=webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def carDetail(url):
    time.sleep(1)
    carDetails = []
    driver.get(url)
    h1=driver.find_element_by_class_name('classifiedInfoList')
    aboo=h1.find_elements_by_tag_name('li')
    carDetailsTemp=[]
    for i in aboo:
        carDetailsTemp.append(i.text)
    carDetails.append(carDetailsTemp)
    for i in carDetails:
        print(i)
    driver.quit()
#carDetail('https://www.sahibinden.com/ilan/vasita-otomobil-alfa-romeo-memurdan-bir-yaris-arabasi-suv-takasli-783021245/detay')
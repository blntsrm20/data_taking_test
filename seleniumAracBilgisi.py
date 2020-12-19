from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
DRIVER_PATH = 'C:/Users/cmvfouu/Desktop/chromedri/chromedriver1.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver=webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def pageCarUrl(url):
    time.sleep(1)
    carUrls = []
    driver.get(url)
    h1=driver.find_elements_by_class_name('searchResultsLargeThumbnail')
    for list in h1:
        #print(list.find_element_by_tag_name('a').get_attribute('href'))
        carUrls.append(list.find_element_by_tag_name('a').get_attribute('href'))
        print(list.find_element_by_tag_name('a').get_attribute('href'))
        #print(list.find_element_by_tag_name('a').get_attribute('href'))
    #print(h1.find_elements_by_tag_name('a').get_attribute('href'))
    driver.quit()
    return carUrls
pageCarUrl('https://www.sahibinden.com/alfa-romeo')
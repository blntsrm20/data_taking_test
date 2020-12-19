from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
DRIVER_PATH = 'C:/Users/cmvfouu/Desktop/chromedri/chromedriver.exe'


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver=webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
def sayfaUrlAl():

    url="https://www.sahibinden.com/alfa-romeo"
    counter=0
    urls = []
    urls.append(url)
    control=True
    while True:

        driver.get(urls[counter])

        h1=driver.find_elements_by_class_name('pageNaviButtons')
        for i in h1:
            print(i.find_element_by_class_name('prevNextBut').text)
            if (i.find_element_by_class_name('prevNextBut').text)=='Sonraki':
                urls.append(i.find_element_by_class_name('prevNextBut').get_attribute('href'))
                print(i.find_element_by_class_name('prevNextBut').get_attribute('href'))


            else:
                #print('Next tuşu yok'," ",i.find_element_by_class_name('prevNextBut').get_attribute('href'))
                print('ab')

        if urls[-1]=='https://www.sahibinden.com/alfa-romeo?pagingOffset=820':
            break
        counter = counter + 1
    driver.quit()
sayfaUrlAl()
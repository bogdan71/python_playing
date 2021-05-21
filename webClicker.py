from selenium import webdriver
#from decouple import config

import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:\\Users\\bbucz\\Downloads\\chromedriver.exe', chrome_options=options)
driver.get('https://cnet.com')

newvid = driver.find_element_by_xpath('//*[@id="rbWrapper"]/header/nav/div[1]/div[1]/a')
time.sleep(3)
newvid.click()


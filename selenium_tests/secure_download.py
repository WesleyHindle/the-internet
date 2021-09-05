from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  

#username and password are both admin

driver.get('http://the-internet.herokuapp.com/download_secure')
time.sleep(2)
driver.quit

driver.get("http://admin:admin@the-internet.herokuapp.com/download_secure")
driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]').click()          #This downloads the file at index [1]. Expected output may change if the 

time.sleep(3)
driver.quit()
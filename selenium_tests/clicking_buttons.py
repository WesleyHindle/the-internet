from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.

#Clicking Buttons

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
#driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click() #This is another way of doing the below. Probably a better way if you're only clicking on it and don't need to input anything 

button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
time.sleep(1)
for i in range (3):
    button.click() #This  creates 3 buttons
    time.sleep(1)

for i in range(3): #This deleted the buttons one by one. Works slightly different to normal as each button is identical the xpath becomes button[n], whereas normally it would just be button
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/button').click()
    time.sleep(1)

time.sleep(2)
driver.quit()
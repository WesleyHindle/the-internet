from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  

driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()

time.sleep(1)

driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[1]/div/input').send_keys("tomsmith")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/input').send_keys("SuperSecretPassword!")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
time.sleep(2)

driver.find_element_by_class_name('icon-signout').click()               #Selecting by xpath isn't always possible so may need to select by another element. Here it's class name. Below is a copy of the class info and there's two classes so sometimes may have to check.
                                                                        #  <a class="button secondary radius" href="/logout"><i class="icon-2x icon-signout">                
time.sleep(2)
driver.quit()


##########
#Can also get selenium to do stupid stuff like this: 

# for i in range(5):
#     driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[1]/div/input').send_keys("tomsmith")
#     driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/div/input').send_keys("SuperSecretPassword!")
#     driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
#     driver.find_element_by_class_name('icon-signout').click()   

# driver.quit()
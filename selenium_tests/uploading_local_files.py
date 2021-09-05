## Finding the actual file path can be a nightmare!




from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  
driver.get("http://the-internet.herokuapp.com/upload")
driver.maximize_window()
 
upload = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[1]').send_keys("/Users/Student/Desktop/beagle1.jpeg")            #This uses the absolute path of a local file. Can use relative, but may run into issues if dirs change


time.sleep(3)
upload = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[2]').click()                     #Upload button

time.sleep(3)   
driver.quit()


#########
# Way 2

from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.
import os    #Library that allows you to interact with OS functionality

file = '/Users/Student/Desktop/beagle1.jpeg'         #This can be relative or absolute. We have given it the absolute here, so this is for demo purposes.    
path = os.path.abspath(file)                        #This finds the absolute path (abspath) of the file you have specified. 
print(path)                                         #Demo purposes

upload = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[1]').send_keys(path)         #Built in Python upload feature means you can select the upload button and give it the path in one action without seeing the upload popup

time.sleep(3)
upload = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/input[2]').click()                     #Upload button

time.sleep(3)   
driver.quit()
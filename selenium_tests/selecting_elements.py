from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.



driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")              #Need to specify where chromdriver is and assign it to a variable. This is then used to control selenium. 
# driver.get("http://the-internet.herokuapp.com/inputs")                          #This opens the site you want it to. Always give the http part. 

# search = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/input')   #This specifies the item to be selected. Ideally you want to use element ID as this is unique, but xpath is also fine. 
# search.send_keys("10")                                                             #This then types 10 into the element you have created on the page 

# time.sleep(1)                                                                       #Delays the next action by 1 second

# search = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/input')   #This is the same element as above
# search.send_keys(Keys.ARROW_UP)                                                    # This then presses the up arrow once. 

# time.sleep(1) #Delays the next action by 1 second

# for i in range (10):  #We don't need to select the same element again as the browser is already focussed on it. 
#     search.send_keys(Keys.ARROW_DOWN) #Here the down arrow is pressed 10 times. 
 
# time.sleep(3) #Delays closing the window by 3 seconds.

# driver.quit()



##########


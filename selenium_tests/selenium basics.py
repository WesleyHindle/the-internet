from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver") #Need to specify where chromdriver is and assign it to a variable. This is then used to control selenium. 
driver.get("http://the-internet.herokuapp.com/") #This opens the site you want it to. Always give the http part. 





print(search)

print(driver.title) #This prints the title of the page of the site you've just opened (usually stated in the tab)
driver.close() #This closes the tab (not the window) and will do so immediately. You can delay this by using...



#driver.quit() #This will close the entire window. 
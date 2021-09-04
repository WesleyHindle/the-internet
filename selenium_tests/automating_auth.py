from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  


#driver.get("https://the-internet.herokuapp.com/basic_auth") When you go to this URL you can automate login by embedding the credentials into the URL
#driver.get("https://USERNAME:PASSWORD@rest_of_the_URL.com")

username = "admin"
password = "admin"

driver.get("https://" + username + ":" + password + "@the-internet.herokuapp.com/basic_auth")  #You can also sign in using variables
#driver.get(f"https//{username}:{password}@the-internet.herokuapp.com/basic_auth")

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


time.sleep(2)
driver.quit()
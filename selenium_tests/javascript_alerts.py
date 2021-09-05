from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#https://www.lambdatest.com/blog/how-to-handle-javascript-alert-in-selenium-webdriver/

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  

driver.get('http://the-internet.herokuapp.com/javascript_alerts')
time.sleep(1)

# driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[1]/button').click()
# time.sleep(1)
# driver.switch_to_alert().accept()                       #.accept() is like clicking the okay button. To selenium there is no 'Okay' button to click. 
# time.sleep(1)

# driver.refresh()                                        #This refreshes the page
# driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[1]/button').click()
# time.sleep(1)
# driver.switch_to_alert().dismiss()                      #Dismisses the alert and returns focus to the main window.



# #We can do the same with the second button too. 
# driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[2]/button').click()
# time.sleep(1)
# driver.switch_to_alert().accept()                       #.accept() is like clicking the okay button. To selenium there is no 'Okay' button to click. 
# time.sleep(1)

# driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[2]/button').click()
# time.sleep(1)
# driver.switch_to_alert().dismiss()

driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li[3]/button').click()


#WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for prompt alert to appear')
alert = driver.switch_to.alert
alert.send_keys(Keys.EQUALS)





#driver.switch_to_alert.accept()



#print(alert)
#driver.quit()
# time.sleep(3)
# driver.send_keys(Keys.RETURN)
# driver.sw

from selenium import webdriver #Libraries needed
from selenium.webdriver.common.keys import Keys #This gives you access to keys you so you can use things like the esc or return key. This is different to being able to type.
import time #Here we use this to delay selenium from executing by the number of seconds specified.
import requests #This allows us to send requests to URLs
#from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL

driver = webdriver.Chrome("/Users/Student/Downloads/chromedriver")  

# driver.get("http://the-internet.herokuapp.com/broken_images")


# image_list = driver.find_element_by_xpath('/html/body/div[2]/div/div/img[1]') #You're selecting specifically which image you want to check if it's broken or not
# response = requests.get(image_list.get_attribute('src'), stream=True)    #This checks the url of the image

# if (response.status_code != 200):     #If the response code for image is NOT 200 then the image is not broken. Other issues could cause it not to display though.
#     print("Image is broken")

# driver.quit()

###Searching through all images on a page

driver.get("http://the-internet.herokuapp.com/broken_images")

iBrokenImageCount = 0  
image_list = driver.find_elements_by_tag_name("img")        #This finds every image on the pages and stores in a list
print('Total number of images on is ' + str(len(image_list))) #Just for demo purposes

for img in image_list:                      #Searches through each image in the list
    response = requests.get(img.get_attribute('src'), stream=True)          #src holds the URL the image is stored on
    
    if (response.status_code != 200):                       #This URL is then checked for its status code. 
            print(img.get_attribute('outerHTML') + " is broken.")
            iBrokenImageCount = (iBrokenImageCount + 1)

print(f"The number of broken images is {iBrokenImageCount}")
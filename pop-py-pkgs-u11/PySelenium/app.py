from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #This will help to keep the browser open
import time #This is go give us time to see what is happening with the 
            # Browser
chrome_options = Options() #This will help to keep the browser open
chrome_options.add_experimental_option("detach", True) #This will help to keep the browser open
browser = webdriver.Chrome(options=chrome_options) #Included options

browser.get("https://github.com/")
time.sleep(1) #Let us actually see something

#Section of the code to find element
signin_link =  browser.find_element(By.LINK_TEXT,"Sign in")
signin_link.click()
time.sleep(1) #Let us actually see something

#Section to introduce the user
username_box = browser.find_element(By.ID,"login_field")
username_box.send_keys("edjose2206@gmail.com")

#Section to introduce the password
password_box = browser.find_element(By.ID,"password")
password_box.send_keys("Bass_2206")
password_box.submit()
time.sleep(2) #Let us actually see something

#Section of the code to check user
assert "edjose182" in browser.page_source

#More specific assertion
#profile_link = browser.find_element(By.CLASS_NAME, "Truncate-text")
#link_label = profile_link.get_attribute("innerHTML")
#print(link_label)
#assert "edjose182" in link_label #This is not working

#It is necessary to end the browser
#browser.quit() #Commented out the quit() to mantain the browser open
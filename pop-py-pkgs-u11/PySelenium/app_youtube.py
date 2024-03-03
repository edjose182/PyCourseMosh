from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #This will help to keep the browser open
import time #This is go give us time to see what is happening with the 

chrome_options = Options() #This will help to keep the browser open
chrome_options.add_experimental_option("detach", True) #This will help to keep the browser open
browser = webdriver.Chrome(options=chrome_options) #Included options

browser.get("https://youtube.com/")
#time.sleep(1) #Let us actually see something

search_box = browser.find_element(By.CSS_SELECTOR,"ytd-searchbox")
search_box.send_keys("Hakari dance")
#time.sleep(4)

search_button = browser.find_element(By.ID,"search-icon-legacy")
search_button.click()
#time.sleep(4)

#browser.quit()
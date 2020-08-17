from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# Insert name of your target between the "" (Must be in your contacts list!)
contact = ""
# Insert the text you want to send them between the ""
text = ""
# Change to driver = webdriver.Firefox() if you dont want to use Chrome
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then hit Enter in the console")
input()
print("Logged In")
input_box_search = WebDriverWait(driver, 10).until(
    lambda driver: driver.find_element_by_class_name('_3FRCZ'))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(1)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
for i in range(25):  # specify number of messages here
    input_box.send_keys(text + Keys.ENTER)
time.sleep(10)
driver.quit()

# driver = webdriver.Chrome(
#     r'C:\Users\Luuk\Desktop\whatsapp bot\chromedriver.exe')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
contact = "Valerie"
text = "Hi Val hahaha"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
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
for i in range(25):
    #input_box.send_keys(text + str(i) + Keys.ENTER)
    input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
driver.quit()

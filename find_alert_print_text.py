from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

link_url = str(math.ceil(math.pow(math.pi, math.e)*10000))
#print(link_url)

try:
    browser = webdriver.Chrome()
    #time.sleep(3)
    browser.get(link)
    #time.sleep(3)
    link2 = browser.find_element(By.LINK_TEXT, link_url)
    link2.click()
    #time.sleep(0.5)
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Max")
    first_name = browser.find_element(By.NAME, "last_name")
    first_name.send_keys("Xam")
    first_name = browser.find_element(By.CLASS_NAME, "city")
    first_name.send_keys("MSK")
    first_name = browser.find_element(By.ID, "country")
    first_name.send_keys("RUS")
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    if "Congrats, you've passed the task! Copy this code as the answer for Stepik quiz:" in alert_text:
        print("----------------------------------")
        print("Код:", alert_text[alert_text.find(" 25."):])
        print("Test 1 - Passed")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("Test 1 - Failed")
        print("----------------------------------")
    #time.sleep(10)

finally:
    browser.quit()
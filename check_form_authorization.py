from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    time.sleep(3)
    browser.get(link)
    time.sleep(3)
    #time.sleep(0.5)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Max")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Xam")
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("max@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)
    text_congr_el = browser.find_element(By.CSS_SELECTOR, "h1")
    text_congr = text_congr_el.text
    if text_congr == "Congratulations! You have successfully registered!":
        print("----------------------------------")
        print("Test 1 - Passed")
        print("ФР:", text_congr)
        print("ОР:", "Congratulations! You have successfully registered!")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("Test 1 - Failed")
        print("----------------------------------")
        print(text_congr)
    time.sleep(5)

finally:
    browser.quit()
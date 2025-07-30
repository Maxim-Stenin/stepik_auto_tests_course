from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Max")
    first_name = browser.find_element(By.NAME, "last_name")
    first_name.send_keys("Xam")
    first_name = browser.find_element(By.CLASS_NAME, "city")
    first_name.send_keys("MSK")
    first_name = browser.find_element(By.ID, "country")
    first_name.send_keys("RUS")
    time.sleep(1)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(10)

finally:
# закрываем браузер после всех манипуляций
    browser.quit()
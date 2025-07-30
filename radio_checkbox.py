from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Комментарий для проверки работы с ветками - Stepik

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    time.sleep(1)
    browser.get(link)
    time.sleep(1)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print("calc(x)= ", y)
    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(y)
    time.sleep(1)
    chekbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox.form-check-input")
    chekbox1.click()
    time.sleep(1)
    radio1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio1.click()
    time.sleep(1)
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button1.click()
    time.sleep(10)

finally:
    browser.quit()

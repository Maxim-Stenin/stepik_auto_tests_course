from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    time.sleep(0.5)
    browser.get(link)
    time.sleep(0.5)
    x_el = browser.find_element(By.ID, "input_value")
    x = x_el.text
    x = int(x)
    print("x = ", x)
    time.sleep(0.5)
    y = math.log(abs(12*math.sin(x)))
    print("y =", y)
    input_el = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_el)
    input_el.send_keys(y)
    chbx_el = browser.find_element(By.ID, "robotCheckbox")
    chbx_el.click()
    rdbtn_el = browser.find_element(By.ID, "robotsRule")
    rdbtn_el.click()
    btn_el = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn_el.click()
    time.sleep(10)

finally:
    browser.quit()
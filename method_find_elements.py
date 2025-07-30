from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Max")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    if ": 2" in alert_text:
        print("----------------------------------")
        print("Код:", alert_text[alert_text.find(": 2"):])
        print("Test 1 - Passed")
        print("----------------------------------")
    else:
        print("----------------------------------")
        print("Test 1 - Failed")
        print("----------------------------------")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        time.sleep(1)
        browser.get(link1)
        time.sleep(1)
        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name.send_keys("Max")
        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Xam")
        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        email.send_keys("max@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        text_congr_el = browser.find_element(By.CSS_SELECTOR, "h1")
        text_congr = text_congr_el.text
        self.assertEqual("Congratulations! You have successfully registered!", text_congr, "Текст не совпадает")
    
    def test_registration2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        time.sleep(1)
        browser.get(link2)
        time.sleep(1)
        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name.send_keys("Max")
        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Xam")
        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        email.send_keys("max@mail.ru")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        text_congr_el = browser.find_element(By.CSS_SELECTOR, "h1")
        text_congr = text_congr_el.text
        self.assertEqual("Congratulations! You have successfully registered!", text_congr, "Текст не совпадает")
   
if __name__ == "__main__":
    unittest.main()

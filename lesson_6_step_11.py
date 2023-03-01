from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
    input1.send_keys("FirstName")
    input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
    input2.send_keys("LastName")
    input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
    input3.send_keys("Email")
    input4 = browser.find_element(By.CLASS_NAME, "second_block .form-control.first")
    input4.send_keys("Phone")
    input5 = browser.find_element(By.CLASS_NAME, "second_block .form-control.second")
    input5.send_keys("Address")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

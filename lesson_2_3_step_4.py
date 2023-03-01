from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc_function(x):
        return str(math.log(abs(12 * math.sin(x))))

    num = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc_function(int(num)))

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(30)
    browser.quit()

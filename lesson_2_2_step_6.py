from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc_function(x):
        return str(math.log(abs(12 * math.sin(x))))

    num = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc_function(int(num)))

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("window.scrollBy(0, 100);", option2)
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    print(x)
    y = calc(x)

    input_y = browser.find_element(By.TAG_NAME, "input")
    input_y.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

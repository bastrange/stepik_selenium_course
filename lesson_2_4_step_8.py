from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    def calc_function(x):
        return str(math.log(abs(12 * math.sin(x))))

    num = browser.find_element(By.ID, "input_value").text
    browser.execute_script("window.scrollBy(0, 100);", num)
    browser.find_element(By.ID, "answer").send_keys(calc_function(int(num)))

    browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(30)
    browser.quit()

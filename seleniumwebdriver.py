from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_css_selector('.btn')

price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

button.click()

formula = browser.find_element_by_id('input_value')
x = formula.text
y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
submit.click()


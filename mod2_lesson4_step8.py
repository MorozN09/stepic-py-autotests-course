from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser,9).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))
button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
input_field = browser.find_element_by_class_name('form-control')
_ = input_field.location_once_scrolled_into_view
input_field.send_keys(y)
submit = browser.find_element_by_id('solve')
submit.click()

from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")
browser.find_element_by_id("button")
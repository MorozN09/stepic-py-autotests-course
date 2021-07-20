from selenium import webdriver


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

btn = browser.find_element_by_id("verify")
btn.click()
message = browser.find_element_by_id("verify_message")
assert "successful" in message.text
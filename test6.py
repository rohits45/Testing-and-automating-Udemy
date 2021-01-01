from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

forgot = driver.find_element_by_css_selector("#login-form > div.form-actions > div > a")
forgot.click()


time.sleep(2)
driver.__exit__()
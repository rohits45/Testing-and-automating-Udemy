from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

email = driver.find_element_by_id("email--1")
email.clear()
email.send_keys("seleniumtesting@gmail.com")


password = driver.find_element_by_id("id_password")
password.clear()
password.send_keys("Testing@123")

login = driver.find_element_by_id("submit-id-submit")
login.click()




time.sleep(2)

driver.__exit__()
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(2)

signup = driver.find_element_by_css_selector("#udemy > div.main-content-wrapper > div.udlite-in-udheavy.udlite-header.ud-app-loader.ud-component--header-v6--udlite-header.ud-app-loaded > div.udlite-text-sm.header--header--3sK1h.header--flex-middle--2Xqjv > div:nth-child(9) > a")
signup.click()
time.sleep(2)
driver.__exit__()
from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://www.udemy.com/")


time.sleep(2)

driver.__exit__()
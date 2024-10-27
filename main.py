from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os
import time

# É necessário especificar o geckdriver do snap no Ubuntu 24.04
# https://github.com/mozilla/geckodriver/issues/2010
service = Service(executable_path="/snap/bin/firefox.geckodriver")
driver = webdriver.Firefox(service=service)

file_path = os.path.abspath("sample-exercise.html")
driver.get("file://" + file_path)

time.sleep(5)
driver.quit()
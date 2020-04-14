# -*- coding: utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://reddit.com")
cookies = browser.get_cookies()
for cookie in cookies:
    print(cookie)
    
browser.quit()

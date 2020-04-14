# -*- coding: utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://reddit.com")
print(browser.get_cookies())
browser.add_cookie({"name":"python","domain":"reddit.com","value":"python"})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()
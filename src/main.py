
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config import USERNAME, PASSWORD

s=Service("C:\\Users\\user\\PycharmProjects\\pythonInstaTry1\\chromedriver\\chromedriver")

users = ['jasim_ak']

browser = webdriver.Chrome(service=s)

browser.get('https://www.instagram.com/')

time.sleep(2)

username_field = browser.find_element_by_name('username')
#username_field = browser.find_element(by=By.NAME )
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(5)

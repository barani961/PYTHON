from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
try:
    service=Service(r"C:\Users\admi\Desktop\set\chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    driver.get("https://www.linkedin.com/login")
    user=os.getenv('LINKEDIN_USERNAME')
    pass_=os.getenv('LINKEDIN_PASSWORD')
    driver.find_element(By.ID,"username").send_keys(user)
    driver.find_element(By.ID,"password").send_keys(pass_)
    driver.find_element(By.ID,"password").send_keys(keys.RETURN)
except Exception as e:
    print(f"{e}")
finally:
    driver.quit()

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstaLoginTest(unittest.TestCase):
    def setUp(self):
        chromedriver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        
    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.linkedin.com/login")
        
        wait = WebDriverWait(driver, 10)
        
        # Correcting the element selectors
        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        # Retrieve the insta username and password from environment variables
        username = os.getenv('LINKEDIN_USERNAME')
        password = os.getenv('LINKEDIN_PASSWORD')
        
        if not username or not password:
            raise ValueError("Username or password environment variable not set")
            
        # Send the username and password to the respective fields
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        # Submit the form
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        
        # Wait for the navigation to complete and verify the URL
        wait.until(EC.url_contains("https://www.linkedin.com/feed/"))
        time.sleep(5)
        
        # Printing the current URL after login
        print(driver.current_url)
        
        # Add an assertion to verify successful login
        self.assertIn("linkedin.com", driver.current_url)
        
    def tearDown(self):
        self.driver.quit()
unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(r"C:\Users\admi\Desktop\set\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
          # Implicit wait for finding elements
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)  # Explicit wait for conditions

    def test_login(self):
        driver = self.driver
        driver.get("http://www.instagram.com/")  # URL of the login page

        # Find the username, password fields, and login button
        driver.find_element(By.NAME, "username").send_keys("baranib812@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("zenithpoo123$")
        driver.find_element(By.NAME, "password").submit()  # Submit the form

        # Wait for login and verify URL
        self.wait.until(EC.url_contains("instagram.com"))
        print(driver.current_url)
        self.assertIn("instagram.com", driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

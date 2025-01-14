import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsite(unittest.TestCase):
    try:
        

        @classmethod
        def setUp(cls):
            service = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe"
            cls.driver = webdriver.Chrome(service=service)
            cls.wait = WebDriverWait(cls.driver, 10)

        def test_log(self):
            driver = self.driver
            driver.get("https://www.instagram.com/")
            driver.find_element(By.NAME, 'username').send_keys("baranib812@gmail.com")
            driver.find_element(By.NAME, 'password').send_keys("zenithpoo123$")
            driver.find_element(By.NAME, 'password').submit()
            self.wait.until(EC.url_contains("instagram.com"))
            print(driver.current_url)
            self.assertIn("instagram.com", driver.current_url)

        @classmethod
        def tearDown(cls):
            cls.driver.quit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    unittest.main()

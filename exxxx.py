import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestInstagramLogin:
    @pytest.fixture(autouse=True)
    def open_browser(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

    def test_login(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            
            username = os.getenv('INSTAGRAM_USERNAME')
            password = os.getenv('INSTAGRAM_PASSWORD')

            assert username is not None and password is not None, "Missing credentials"
            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
        except Exception as e:
            print(f"Error during login: {e}")
            assert False, "Login failed"

    def test_post_login(self):
        time.sleep(5)
        current_url = self.driver.current_url
        assert "https://www.instagram.com/" in current_url, "Login Failed"

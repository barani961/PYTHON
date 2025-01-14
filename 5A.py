import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="class")
def setup(request):
    # Setup Chrome WebDriver
    chromedriver_path = "C:\\Users\\chromedriver.exe"

    # Create a new instance of the Chrome driver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    # Maximize the window
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLinkedInLogin:

    @pytest.fixture(autouse=True)
    def open_browser(self):
        # Open LinkedIn login page before every test
        self.driver.get("https://www.linkedin.com/login")

    def test_login(self):
        # Perform login actions
        try:
            # Wait for the username and password fields to be present
            wait = WebDriverWait(self.driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

            # Get credentials from environment variables
            username = os.getenv('LINKEDIN_USERNAME')
            password = os.getenv('LINKEDIN_PASSWORD')

            # Validate credentials presence
            assert username is not None, "LinkedIn username environment variable not set"
            assert password is not None, "LinkedIn password environment variable not set"

            # Input credentials
            username_field.send_keys(username)
            password_field.send_keys(password)

            # Simulate pressing Enter to log in
            password_field.send_keys(Keys.RETURN)

        except Exception as e:
            print(f"Error during login: {e}")
            assert False, "Login failed due to an exception."

    def test_post_login(self):
        # Wait for the URL to change to the feed or checkpoint page
        time.sleep(5)  # Give time for the login process to complete
        current_url = self.driver.current_url
        print(f"Current URL after login: {current_url}")
        assert "feed" in current_url or "checkpoint" in current_url, "Login failed, check credentials or page redirection"

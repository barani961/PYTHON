
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
load_dotenv()
try:
    # Provide the path to your ChromeDriver executable
    chromedriver_path = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    # Navigate to Instagram's login page
    driver.get("https://www.facebook.com/")

    time.sleep(5)  # Wait for the page to load

    # Locate the username and password fields
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")

    # Retrieve the username and password from environment variables
    username = os.getenv('FACEBOOK_USERNAME')
    password = os.getenv('FACEBOOK_PASSWORD')

    print("Username:", username)  # Optional: Print username for debugging
    print("Password:", password)  # Optional: Print password for debugging

    if not username or not password:
        raise ValueError("Username or password environment variable not set")

    # Enter the username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Press Enter to submit the form
    password_field.send_keys(Keys.RETURN)

    time.sleep(10)  # Wait for the login process to complete

    # Verify that login was successful by checking the URL
    expected_url_contains = "https://www.facebook.com/"
    actual_url = driver.current_url

    if expected_url_contains in actual_url.lower():
        print("Test passed")
    else:
        print("Test failed")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser window
    driver.quit()

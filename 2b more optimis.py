 
import os 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try: 
    # Set the path to the chromedriver executable 
    chromedriver_path = "D:\\barani code\\set\\chromedriver.exe" 
 
    # Create a new instance of the Chrome driver 
    service = Service(chromedriver_path) 
    driver = webdriver.Chrome(service=service) 
 
    # Maximize the window 
    driver.maximize_window() 
 
    # Navigate to the LinkedIn login page 
    driver.get("https://www.instagram.com/") 
 
    # Locate the username and password fields 
    username_field = driver.find_element(By.NAME, "username") 
    password_field = driver.find_element(By.NAME, "password") 
 
    # Retrieve the LinkedIn username and password from environment variables 
    username = os.getenv('INSTA_USERNAME') 
    password = os.getenv('INSTA_PASSWORD') 
 
    # Debugging: Print the retrieved username and password 
    print("Username:", username) 
    print("Password:", password) 
 
    if not username or not password: 
        raise ValueError("Username or password environment variable not set") 
 
    # Send the username and password to the respective fields 
    username_field.send_keys(username) 
    password_field.send_keys(password) 
 
    # Submit the form 
    password_field.send_keys(Keys.RETURN) 
 
    # Wait for the page to load after login 
    time.sleep(5) 
 
    # Check if the login was successful by comparing URLs 
    expected_url = "https://www.instagram.com/feed/" 
    actual_url = driver.current_url 
 
    if expected_url.lower() == actual_url.lower(): 
        print("Test passed")
    else: 
        print("Test failed") 
 
except Exception as e: 
    print("Error:", e) 
 
finally: 
    # Close the browser 
    driver.quit() 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


chrome_driver_path = "D:\\barani code\\set\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/")

try:
    # Find the username and password input fields (update locators if necessary)
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    # Enter your credentials
    username_field.send_keys("________baran_")
    password_field.send_keys("zenith32*A$")
    time.sleep(5)

    # Find and click the login button (update locator if necessary)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Handle CAPTCHAs or additional actions here (manual interaction might be needed)

except TimeoutException as e:
    print("Error: Element not found within 10 seconds.", e)

finally:
    # Close the browser (optional)
    driver.quit()

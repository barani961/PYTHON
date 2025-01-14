from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def open_instagram_login():
    try:
        # Set up the path to the ChromeDriver executable
        chrome_driver_path = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
        
        # Initialize Chrome WebDriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        
        # Step 1: Navigate to Instagram login page
        driver.get("https://www.instagram.com/accounts/login/")
        print("Navigated to Instagram login page")
        
        # Optional: Wait to observe the page
        time.sleep(5)
        
        # Step 2: Close the browser
        driver.quit()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_instagram_login()

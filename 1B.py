from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def main():
    try:
        
        chrome_driver_path = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe"
        
        # Initialize Chrome WebDriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        
        # Function to navigate to a URL and print a message
        def navigate_to(url, name):
            driver.get(url)
            print(f"Navigated to {name}")
            # Wait for 5 seconds to observe the page
            time.sleep(4)
        
        # Step 1: Navigate to Google
        navigate_to("https://www.google.com", "Google")
        time.sleep(3)
        
        # Step 2: Navigate to Pinterest
        navigate_to("https://www.pinterest.com", "Pinterest")
        
        # Step 3: Navigate to Zoho
        navigate_to("https://www.zoho.com", "Zoho")
        time.sleep(2)
    
        # Close the browser
        driver.quit()
        print("Browser closed successfully")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

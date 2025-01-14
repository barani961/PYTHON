from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import time 
try: 
    # Set up the ChromeDriver path 
    chrome_driver_path = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe"
    # Initialize Chrome WebDriver 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service) 
    # Navigate to javatpoint.com 
    driver.get("https://www.javatpoint.com") 
                             
    # Navigate back 
    driver.back() 
    time.sleep(3) 
                             
    # Navigate forward 
    driver.forward() 
    time.sleep(3) 
                             
    # Navigate to google.com 
    driver.get("https://www.google.com") 
                             
    # Refresh the page 
    driver.refresh() 
                             
    # Close the browser 
    driver.quit() 
except Exception as e: 
        print(e)

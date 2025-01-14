from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
import time 
def incognito():
    
    options = Options() 
    options.add_argument("--incognito") 
    chrome_driver_path = "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.get("http://google.co.in") 
    print("Page Title:", driver.title) 
    driver.quit() 
 
def headless(): 
    options = Options() 
    options.add_argument("--headless") 
    chrome_driver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.get("https://smvec.ac.in/") 
    time.sleep(5) 
    print("Title of website is", driver.title) 
    driver.quit() 
 
def maximize(): 
    options = Options() 
    options.add_argument("--start-maximized") 
    chrome_driver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.get("https://smvec.ac.in/") 
    driver.quit() 
 
def disable_extensions(): 
    options = Options() 
    options.add_argument("--disable-extensions") 
    chrome_driver_path = 'D:\\barani code\\set\\chromedriver.exe' 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.get("http://google.co.in") 
    driver.quit() 
 
def disable_notifications(): 
    prefs = {"profile.default_content_setting_values.notifications": 1} 
    options = Options() 
    options.add_experimental_option("prefs", prefs) 
    chrome_driver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
    service = Service(chrome_driver_path) 
    driver = webdriver.Chrome(service=service, options=options)  
    driver.get("http://google.co.in") 
    driver.quit() 
 
while True: 
    print("Choose an option for ChromeDriver:") 
    print("1. Incognito") 
    print("2. Headless") 
    print("3. Maximize") 
    print("4. Disable Extensions") 
    print("5. Disable Notifications") 
    print("6. Exit") 
    choice = input("Enter your choice (1-6): ") 
    if choice == '1': 
        incognito() 
    elif choice == '2': 
        headless() 
    elif choice == '3': 
        maximize() 
    elif choice == '4': 
        disable_extensions() 
    elif choice == '5': 
        disable_notifications() 
    elif choice == '6':
        print("Exiting...") 
        break 
    else: 
        print("Invalid choice. Please enter a number between 1 and 6.") 

import os 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time 
 
try: 
    # Set the path to the chromedriver executable 
    chromedriver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 
 
    # Create a new instance of the Chrome driver 
    service = Service(chromedriver_path) 
    driver = webdriver.Chrome(service=service) 
 
    # Maximize the window 
    driver.maximize_window() 
 
    # Navigate to the LinkedIn login page 
    driver.get("https://www.linkedin.com/login") 
 
    # Locate the username and password fields 
    username_field = driver.find_element(By.ID, "username") 
    password_field = driver.find_element(By.ID, "password") 
 
    # Retrieve the LinkedIn username and password from environment variables 
    username = os.getenv('LINKEDIN_USERNAME') 
    password = os.getenv('LINKEDIN_PASSWORD') 
 
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
    expected_url = "https://www.linkedin.com/feed/" 
    actual_url = driver.current_url
    result = "Test passed" if expected_url.lower() == actual_url.lower() else "Test failed" 
    print(result) 
 
    # Generate HTML content with the result 
    html_content = f""" 
    <!DOCTYPE html> 
    <html> 
    <head> 
        <title>LinkedIn Login Test Result</title> 
    </head> 
    <body> 
        <h1>{result}</h1> 
    </body> 
    </html> 
    """ 
 
    # Write the HTML content to a file 
    with open("test_result.html", "w") as file: 
        file.write(html_content) 
 
    # Open the generated HTML file in the browser 
    driver.get("file://" + os.path.abspath("test_result.html")) 
 
    # Wait for a few seconds to view the result 
    time.sleep(5) 
 
except Exception as e: 
    print("Error:", e) 
 
finally: 
    # Close the browser 
    driver.quit()

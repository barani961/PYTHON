import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

try:
    # Provide the path to your ChromeDriver executable
    chromedriver_path =  "C:\\Users\\admi\\Desktop\\set\\chromedriver.exe" 

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    # Navigate to Instagram's login page
    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(5)  # Wait for the page to load

    # Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Retrieve the username and password from environment variables
    username = os.getenv('INSTA_USERNAME')
    password = os.getenv('INSTA_PASSWORD')

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
    expected_url_contains = "instagram.com/"
    actual_url = driver.current_url

    result = "Test passed" if expected_url_contains in actual_url else "Test failed"
    print(result)
    
    # Generate HTML content with the result
    html_content = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Instagram Login Test Result</title>
        </head>
        <body>
            <h1>{result}</h1>
        </body>
    </html>'''
    
    
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

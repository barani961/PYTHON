from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Define the URL for Wikipedia and YouTube
wikipedia_url = "https://www.wikipedia.org"
youtube_url = "https://www.youtube.com"

# Set the duration to stay on each page (in seconds)
timer = 10  # Stay 5 seconds on each page

# Start WebDriver (adjust to your browser)
# For Chrome:
driver=webdriver.Chrome()

# Function to navigate and wait
def navigate_to_page(url, duration):
    driver.get(url)
    print(f"Navigated to {url}. Staying for {duration} seconds.")
    time.sleep(duration)

try:
    # Navigate to Wikipedia
    navigate_to_page(wikipedia_url, timer)
    
    # Navigate to YouTube
    navigate_to_page(youtube_url, timer)

finally:
    # Close the browser after navigation
    driver.quit()
    print("Browser closed.")


<<<<<<< HEAD
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
=======
#prime or not prime
start=int(input("enter the start number:"))
end=int(input("enter the end of range:"))
prime=[]
non_prime=[]
for num in range(start,end+1):
    is_prime=1
    for i in range(2,(num//2)+1):
        if num%i==0:
            is_prime=0
            break;

    if is_prime and num>1:
        prime.append(num)
    else:
        non_prime.append(num)
print("prime numbers are:",prime)
print("non prime numbers are:",non_prime)
>>>>>>> 2862771b139c929db618195d23986244a1884af3

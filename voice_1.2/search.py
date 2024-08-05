from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def search_google(query):
    try:
        # Set up the ChromeDriver path using Service with raw string
        service = Service(executable_path=r'C:/Users/HP/drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.maximize_window()
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.click()
        search_box.send_keys(query)
        search_box.submit()
        
        input("Press Enter to close the browser...")  # Keep browser open until Enter is pressed
        driver.quit()

    except Exception as e:
        print(f"An error occurred during Google search: {e}")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Music:
    def __init__(self):
        service = Service(executable_path=r'C:/Users/HP/drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        
    def play(self, query):
        self.query = query
        self.driver.get('https://www.youtube.com/results?search_query=' + query)
        
        self.driver.implicitly_wait(10)
        
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        
        time.sleep(5)

        try:
            skip_button = WebDriverWait(self.driver, 11).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Skip")]'))
            )
            skip_button.click()
        except Exception as e:
            print("No skip button found or the ad is not skippable. Error:", e)
        
       
        input("Press Enter to close the browser...") 

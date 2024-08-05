from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class infow:
    def __init__(self):
        # Set up the ChromeDriver path using Service with raw string
        service = Service(executable_path=r'C:/Users/HP/drivers/chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        
    def get_info(self, query):
        self.query = query
        self.driver.maximize_window()
        self.driver.get(url='https://www.wikipedia.org')
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
        input("Press Enter to close the browser...") 



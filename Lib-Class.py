from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SvFunctions :
    
    def __init__(self, driver):
        self.driver = driver

    def login(self, url, user, password, title):
        driver.maximize_window()
        driver.get(self.url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "html/body/div[3]/div[2]/div/div[2]/div/div[3]/div/div/form/fieldset/div[2]/input")))
        assert self.title in driver.title
        elem1 = driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div/div[3]/div/div/form/fieldset/div[1]/input")
        elem1.send_keys("bill")
        elem2 = driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div/div[3]/div/div/form/fieldset/div[2]/input")
        elem2.send_keys("Nart@123")
        elem3 = driver.find_element_by_xpath("//*[contains(text(), 'Sign In')]")
        elem3.click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Sample EU Dashboard Content')]")))
        assert "SupportVantage" in driver.title
        print ("done")
        return 1







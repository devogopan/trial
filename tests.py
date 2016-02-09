from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class loginTests(unittest.TestCase):
        def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_valid(self):
        driver = self.driver
        url = "http://acme.supportvantage.com:8080/SVWeb/index.html"
        user = "bill"
        password = "Nart@123"
        
        

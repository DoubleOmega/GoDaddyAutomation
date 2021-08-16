import unittest
from selenium import webdriver
import time


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/browser_drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://godaddy.com")
        # # Will throw an error if the page doesn't load in (time)
        self.driver.set_page_load_timeout(20)

    def tearDown(self):
        print("***Test environment cleanup***")
        self.driver.close()
        self.driver.quit()

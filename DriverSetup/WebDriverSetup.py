import unittest
from selenium import webdriver
import time


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/browser_drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        print("***Test environment cleanup***")
        self.driver.close()
        self.driver.quit()

import unittest
import time import sleep
from GodaddyProject.UsernamePassword.Users import Users
from GodaddyProject.Pages.LoginPage import loginpage


class LoginSetup(unittest.TestCasease):


    def setup(self):
        def test_valid_login(self):
            driver = self.driver
            login = loginpage(driver)
            login.click_sign_in_dropdown()
            sleep(3)
            login.click_sign_in_link()
            sleep(3)
            with open(Users.path, 'r') as file:
                credentials = file.readlines()
                username = credentials[0]
                password = credentials[1]
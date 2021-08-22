import unittest
from time import sleep
from GodaddyProject.UsernamePassword.Users import Users
from GodaddyProject.Pages.LoginPage import loginpage


class LoginSetup(unittest.TestCase):

    def login(self):
        driver = self.driver
        self.driver = loginpage(driver)
        self.driver.click_sign_in_dropdown()
        sleep(3)
        self.driver.click_sign_in_link()
        sleep(3)
        with open(Users.path, 'r') as file:
            credentials = file.readlines()
            username = credentials[0]
            password = credentials[1]

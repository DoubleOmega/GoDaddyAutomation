import unittest
from selenium import webdriver
from time import sleep

from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
from GodaddyProject.Locators.Locators import Locators
from GodaddyProject.Pages.LoginPage import loginpage
from GodaddyProject.Pages.HomePage import homepage
from GodaddyProject.UsernamePassword.Users import Users


class Login(WebDriverSetup):

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

        login.click_sign_in_username(username)
        login.click_sign_in_password(password)
        login.click_remember_me_checkbox()
        login.click_sign_in_submit_button()
        sleep(3)


if __name__ == '__main__':
    unittest.main()

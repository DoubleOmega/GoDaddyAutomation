import unittest
from time import sleep

from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
from GodaddyProject.Pages.LoginPage import loginpage
from GodaddyProject.UsernamePassword.Users import Users
from GodaddyProject.UsernamePassword.Credentials import Credentials


class LaunchWebPage(WebDriverSetup):

    def test_valid_login(self):
        driver = self.driver
        login = loginpage(driver)
        login.click_sign_in_dropdown()
        sleep(3)
        login.click_sign_in_link()
        sleep(3)
        # with open(Users.path, 'r') as file:
        #     credentials = file.readlines()
        #     username = credentials[0]
        #     password = credentials[1]

        login.click_sign_in_username(Credentials.username)
        login.click_sign_in_password(Credentials.password)
        login.click_remember_me_checkbox()
        login.click_sign_in_submit_button()
        sleep(3)


if __name__ == '__main__':
    unittest.main()

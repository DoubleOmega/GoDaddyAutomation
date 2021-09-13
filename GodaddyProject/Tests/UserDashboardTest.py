import unittest
from time import sleep

from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
from GodaddyProject.Pages.LoginPage import loginpage
from GodaddyProject.UsernamePassword.Users import Users
from GodaddyProject.UsernamePassword.Credentials import Credentials


class LaunchWebPage(WebDriverSetup):

    def test_label_verification(self):
        driver = self.driver

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

    def test_invalid_login(self):
        driver = self.driver
        login = loginpage(driver)
        login.click_sign_in_dropdown()
        sleep(3)
        login.click_sign_in_link()
        sleep(3)

        self.assertIn("Sign in", login.get_login_title_text())
        self.assertIn("Username or Customer #", login.get_username_label().text)
        self.assertIn("Password", login.get_password_label().text)
        login.click_sign_in_submit_button()
        self.assertIn("Username is required", login.get_username_required_text())
        self.assertIn("Password is required", login.get_password_required_text())




if __name__ == '__main__':
    unittest.main()

import unittest
from selenium import webdriver
from time import sleep
from GodaddyProject.Locators.Locators import Locators
from GodaddyProject.Pages.LoginPage import loginpage
from GodaddyProject.Pages.HomePage import homepage
from GodaddyProject.UsernamePassword.Users import users


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/users/admin/desktop/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_user_dashboard_valid(self):
        driver = self.driver

        driver.get("https://godaddy.com")

        login = loginpage(driver)
        login.click_sign_in_dropdown()
        login.click_sign_in_link()
        login.click_sign_in_username().sendkeys(users.username1)
        login.click_sign_in_password().sendkeys(users.password1)
        sleep(2)
        login.click_sign_in_submit_button()

        home = homepage(driver)
        home.click_bell_icon_button()
        home.sign_out_dropdown_xpath
        home.click_sign_out_link_button()
        sleep(3)

    @classmethod
    def test_teardown(cls):
        cls.driver.close()

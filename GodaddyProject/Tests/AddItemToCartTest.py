import unittest
from time import sleep
from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
from GodaddyProject.DriverSetup.LoginSetup import LoginSetup
from GodaddyProject.Pages.ProductsTab import productstab



class LaunchWebPage(WebDriverSetup):

    def test_add_item_to_cart(self):
        #LoginSetup.login(LoginSetup)
        class login(LoginSetup):
         driver = self.driver
         prod = productstab(driver)
         prod.search_new_domain()
         sleep(5)
         print('success')
         prod.click_search_button()


if __name__ == '__main__':
    unittest.main()

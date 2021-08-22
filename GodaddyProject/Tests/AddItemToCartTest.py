from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
from GodaddyProject.DriverSetup.LoginSetup import LoginSetup
from GodaddyProject.Pages.MyProductsTabPage import MyProductsTabPage


class LaunchWebPage(WebDriverSetup):
    class Login(LoginSetup):

        def test_add_item_to_cart(self):
            driver = self.driver
            mptp = MyProductsTabPage(driver)
            mptp.search_new_domain()





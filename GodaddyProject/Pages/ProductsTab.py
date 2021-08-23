from GodaddyProject.Locators.Locators import Locators


# 1. this class creates all the objects on the home page - objects meaning buttons and text fields
# 2. this class also creates all the actions that will be needed to be performed on all the objects - such as click the button

class productstab():

    def __init__(self, driver):
        self.driver = driver

        self.search_new_domain = Locators.search_for_a_new_domain_xpath
        self.click_search_button = Locators.search_button_xpath

    def search_new_domain(self):
        self.driver.find_element_by_xpath(self.search_new_domain).sendkeys('cccccccccccc')

    def click_search_button(self):
        self.driver.find_element_by_xpath(self.click_search_button).click()

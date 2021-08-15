from GodaddyProject.Locators.Locators import Locators

# 1. this class creates all the objects on the home page - objects meaning buttons and text fields
# 2. this class also creates all the actions that will be needed to be performed on all the objects - such as click the button
class homepage():

    def __init__(self, driver):
        self.driver = driver

        self.bell_icon_button_xpath = Locators.bell_icon_button_xpath
        self.sign_out_dropdown_xpath = Locators.sign_out_dropdown_xpath
        self.sign_out_link_button_xpath = Locators.sign_out_link_button_xpath

    def click_bell_icon_button(self):
        self.driver.find_element_by_xpath(self.bell_icon_button_xpath).click()

    def click_sign_out_dropdown(self):
        self.driver.find_element_by_xpath(self.sign_out_dropdown_xpath).click()

    def click_sign_out_link_button(self):
        self.driver.find_element_by_xpath(self.sign_out_link_button_xpath).click()

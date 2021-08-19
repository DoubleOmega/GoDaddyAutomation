from GodaddyProject.Locators.Locators import Locators

# 1. this class creates all the objects on the home page - objects meaing buttons and text fields
# 2. this class also creats all the actions that will be needed to be performed on all the objects - such as click the button


class loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_dropdown_xpath = Locators.sign_in_dropdown_xpath
        # self.sign_in_link_class = Locators.sign_in_link_class
        self.sign_in_link_text = Locators.sign_in_link_link_text
        self.sign_in_username_id = Locators.sign_in_username_id
        self.sign_in_password_id = Locators.sign_in_password_id
        self.sign_in_submit_button_id = Locators.sign_in_submit_button_id
        self.remember_me_checkbox = Locators.remember_me_checkbox_id

    def click_sign_in_dropdown(self):
        self.driver.find_element_by_xpath(self.sign_in_dropdown_xpath).click()

    def click_sign_in_link(self):
        # self.driver.find_element_by_id(self.sign_in_link_class).click()
        self.driver.find_element_by_link_text(self.sign_in_link_text).click()

    def click_sign_in_username(self, username):
        self.driver.find_element_by_id(self.sign_in_username_id).send_keys(username)

    def click_sign_in_password(self, password):
        self.driver.find_element_by_id(self.sign_in_password_id).send_keys(password)

    def click_remember_me_checkbox(self):
        self.driver.find_element_by_id(self.remember_me_checkbox).click()

    def click_sign_in_submit_button(self):
        self.driver.find_element_by_id(self.sign_in_submit_button_id).click()

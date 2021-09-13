from GodaddyProject.Locators.Locators import Locators

# 1. this class creates all the objects on the home page - objects meaing buttons and text fields
# 2. this class also creates all the actions that will be needed to be performed on all the objects - such as click the button


class loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_dropdown_xpath = Locators.sign_in_dropdown_xpath
        # self.sign_in_link_class = Locators.sign_in_link_class
        self.sign_in_link_text = Locators.sign_in_link_link_text
        self.sign_in_username_id = Locators.sign_in_username_id
        self.sign_in_password_id = Locators.sign_in_password_id
        self.sign_in_submit_button_id = Locators.sign_in_submit_button_id
        self.remember_me_checkbox_id = Locators.remember_me_checkbox_id
        self.invalid_login_alert_msg_xpath = Locators.invalid_login_alert_msg_xpath
        self.username_required_text_xpath = Locators.username_required_text_xpath
        self.password_required_text_xpath = Locators.password_required_text_xpath
        self.username_label_id = Locators.username_label_id
        self.title_xpath = Locators.title_xpath
        self.password_label_id = Locators.password_label_id

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
        self.driver.find_element_by_id(self.remember_me_checkbox_id).click()

    def click_sign_in_submit_button(self):
        self.driver.find_element_by_id(self.sign_in_submit_button_id).click()

    def get_invalid_login_msg_text(self):
        self.driver.find_element_by_xpath(self.invalid_login_alert_msg_xpath).text

    def get_username_label(self):
        return self.driver.find_element_by_id(self.username_label_id)

    def get_username_required_text(self):
        return self.driver.find_element_by_xpath(self.username_required_text_xpath).text

    def get_login_title_text(self):
        return self.driver.find_element_by_xpath(self.title_xpath).text

    def get_login_title(self):
        return self.driver.find_element_by_xpath(self.title_xpath)

    def get_password_label(self):
        return self.driver.find_element_by_id(self.password_label_id)

    def get_password_required_text(self):
        return self.driver.find_element_by_xpath(self.password_required_text_xpath).text



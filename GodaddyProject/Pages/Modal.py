from GodaddyProject.Locators.Locators import Locators

class Modal():

    def __init__(self, driver):
        self.driver = driver

        self.modal_okay_btn_css = Locators.modal_okay_btn_css

    def click_modal_okay(self):
        self.driver.find_element_by_css_selector(self.modal_okay_btn_css).click()

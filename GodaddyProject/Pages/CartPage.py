from GodaddyProject.Locators.Locators import Locators

# 1. this class creates all the objects on the home page - objects meaning buttons and text fields
# 2. this class also creates all the actions that will be needed to be performed on all the objects - such as click the button
class cartpage():

    def __init__(self, driver):
        self.driver = driver
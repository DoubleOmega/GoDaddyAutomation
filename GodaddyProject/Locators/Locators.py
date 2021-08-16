class Locators():
     #sign in locators
    sign_in_dropdown_xpath = "//span[normalize-space()='Sign In']"
    sign_in_link_class = "//a[normalize-space()='Sign In']"
    sign_in_username_id = 'username'
    sign_in_password_id = 'password'
    sign_in_submit_button_id = 'submitBtn'

    #homepage locators(once signed in)
    sign_out_dropdown_xpath = "//span[@class='chevron-down open']//*[local-name()='svg']"
    sign_out_link_button_xpath = "//a[normalize-space()='Sign Out']"
    bell_icon_button_class ="//button[@id='notifications-bell']//*[local-name()='svg']"



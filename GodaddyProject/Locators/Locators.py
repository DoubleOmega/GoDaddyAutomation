class Locators():
    #sign in locators
    sign_in_dropdown_xpath = "//span[normalize-space()='Sign In']"
    # sign_in_link_class = "//a[normalize-space()='Sign In']"
    sign_in_link_link_text = 'Sign In'
    sign_in_username_id = 'username'
    sign_in_password_id = 'password'
    remember_me_checkbox_id = 'remember-me'
    sign_in_submit_button_id = 'submitBtn'
    invalid_login_alert_css = "div[role='alert']"
    invalid_login_alert_msg_xpath = "//div[@class='ux-alert-message']"
    invalid_login_error_icon_class_name = "svg[class='uxicon-svg-container ux-alert-icon']"
    username_label_id = 'label-username'
    password_label_id = 'label-password'
    username_required_text_xpath = "//span[contains(text(),'Username is required')]"
    password_required_text_xpath = "//span[contains(text(), 'Password is required')]"
    title_xpath = '//*[@id="title"]'

    #homepage locators(once signed in)
    sign_out_dropdown_xpath = "//span[@class='chevron-down open']//*[local-name()='svg']"
    sign_out_link_button_xpath = "//a[normalize-space()='Sign Out']"
    bell_icon_button_xpath = "//button[@id='notifications-bell']//*[local-name()='svg']"

    #my products page tab locators
    search_for_a_new_domain_xpath = "//input[@id='search-box']"
    search_button_xpath = "//button[@aria-label='Search button']"

    #cart locators
    get_it_button_xpath = "//span[normalize-space()='Get It']"
    looks_good_keep_going_button_xpath = "//span[normalize-space()='Looks Good, Keep Going']"

    #modal locators ie: pop ups
    # I received a popup when I log in with my ad blocker enabled
    modal_okay_btn_css = "button[aria-label='Okay']"

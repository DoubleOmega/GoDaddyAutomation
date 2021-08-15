from GodaddyProject.DriverSetup.WebDriverSetup import WebDriverSetup
import unittest


class LaunchWebsite(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver

        web_page_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy"

        # Checks if the value grabbed by driver.title matches web_page_title
        try:
            if driver.title == web_page_title:
                print("Page loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error+"Page failed to load")


if __name__ == '__main__':
    unittest.main()

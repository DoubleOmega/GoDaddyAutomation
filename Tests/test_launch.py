from selenium import webdriver

from DriverSetup.WebDriverSetup import WebDriverSetup
from Pages.homepage import HomePage
import unittest


class LaunchWebsite(WebDriverSetup):

    def test_Home_Page(self):
        # driver = self.driver

        web_page_title = "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy"

        # Checks if the value grabbed by driver.title matches web_page_title
        try:
            if self.driver.title == web_page_title:
                print(self.driver.title + "Page loaded successfully")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "Page failed to load")

    def test_current_url(self):
        url = self.driver.current_url
        print(url)

    def test_page_source(self):
        # pagesource = self.driver.page_source
        with open('page_source.html', 'r', encoding='utf-8') as f:
            if self.driver.title in f.read():
                print("Page title is in page source")

        # self.assertIn(self.driver.title, "page_source.html")
        # fw = open("page_source.html", "w", encoding="utf-8")
        # fw.write(pagesource)
        # fw.close()
        # fr = open("page_source.html", "r", encoding="utf-8")
        # self.assertIn(self.driver.title, fr)
        # fr.close()


if __name__ == '__main__':
    unittest.main()

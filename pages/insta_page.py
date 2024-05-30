from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

insta_btn = (By.XPATH, "//span[text()='Instagram']")


class InstaPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://us.loropiana.com/')

    def insta_find(self):
        return self.find(insta_btn)

    def insta_click(self):
        return self.insta_find().click()

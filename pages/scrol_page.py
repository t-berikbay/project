from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

coockie = (By.ID, "onetrust-accept-btn-handler")
btn = (By.ID, "cross")
btn2 = (By.XPATH, "//div[@class='CAFFEINA-FooterSub_language']//a[@class='CAFFEINA-statusbar__link btn-shipping']")


class ScrollingPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://us.loropiana.com/')

    def coockies(self):
        self.find(coockie)

    def coockies_click(self):
        self.find(coockie).click()

    def cross_find(self):
        return self.find(btn)

    def cross_click(self):
        return self.cross_find().click()

    def scroll(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def btn_find(self):
        return self.find(btn2)

    def btn_click(self):
        return self.btn_find().click()

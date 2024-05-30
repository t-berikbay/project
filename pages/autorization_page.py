from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

login = (By.XPATH, "//div[@class='menu-account-button']")
email = (By.ID, "currentEmail")
password = (By.ID, "j_password")
btn1 = (By.XPATH, "//button[@class='main-button t-cta']")
coockie = (By.ID, "onetrust-accept-btn-handler")
btn2= (By.ID, "cross")


class AutorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://us.loropiana.com/')

    def coockie(self):
        self.find(coockie)
    def coockie_click(self):
        self.find(coockie).click()

    def cross(self):
        self.find(btn2).click()

    def autorization_find(self):
        return self.find(login)

    def autorization_click(self):
        return self.autorization_find().click()

    def autorization_email_find(self):
        return self.find(email)

    def autorization_email_click(self):
        return self.autorization_email_find().click()

    def autorization_email_input(self):
        return  self.autorization_email_find().send_keys('testersportal@gmail.com')  #Here send the your email

    def log_in(self):
        self.browser.implicitly_wait(10)
        return self.find(btn1)

    def continue_click(self):
        self.log_in().click()
        sleep(1.5)

    def password_find(self):
        return self.find(password)

    def password_click(self):
        return self.password_find().click()

    def password_input(self):
        return self.password_find().send_keys('Madiyar2011')  #Here send the your password


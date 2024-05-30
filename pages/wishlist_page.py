from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

coockie = (By.ID, "onetrust-accept-btn-handler")
btn1 = (By.XPATH, "//button[@class='CAFFEINA-Header__button search-icon js-search-trigger js-quicksearch-trigger']")
product_btn = (By.XPATH, "//a[@class='CAFFEINA-image-link CAFFEINA-image-link--text-under js-gtm-product-click js-quick-search-prod']")
favourites_btn2 = (By.ID, "favorites-star-button-sticky")
view_wishlist = (By.XPATH, "//button[@aria-label='View Wishlist']")
send_search = (By.XPATH, "//input[@type='text']")


class WishlistPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://us.loropiana.com/')

    def coockies(self):
        self.find(coockie)

    def coockies_click(self):
        self.find(coockie).click()

    def btn_find(self):
        return self.find(btn1)

    def btn_click(self):
        return self.btn_find().click()

    def send_search_find(self):
        return self.find(send_search)

    def send_search_click(self):
        return self.send_search_find().click()

    def send_search_input(self):
        return self.send_search_find().send_keys('Zita Hat')

    def product_find(self):
        sleep(5)
        return self.find(product_btn)

    def product_click(self):
        return self.product_find().click()

    def faworits_find(self):
        return self.find(favourites_btn2)

    def faworits_click(self):
        return self.faworits_find().click()

    def wishlist_find(self):
        return self.find(view_wishlist)

    def wishlist_click(self):
        return self.wishlist_find().click()




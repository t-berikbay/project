from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

coockie = (By.ID, "onetrust-accept-btn-handler")
btn1 = (By.XPATH, "//button[@class='CAFFEINA-Header__button search-icon js-search-trigger js-quicksearch-trigger']")
product_btn = (By.XPATH, "//a[@class='CAFFEINA-image-link CAFFEINA-image-link--text-under js-gtm-product-click js-quick-search-prod']")
select_color=(By.XPATH, "//button[@aria-label='Kokuto Sugar']")
select_size = (By.XPATH, "//div[@class='sizevalue t-sub-h3-med a-kummel-hover' and text()='Select Size']")
size_btn = (By.XPATH, "//button[@value='M']")
add_shopping_bag = (By.XPATH, "//span[text()='Add to Shopping Bag']")
send_search = (By.XPATH, "//input[@type='text']")
viev_shopping_bag = (By.XPATH, "//button[@aria-label='View Shopping Bag']")


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://us.loropiana.com/')

    def coockies(self):
        self.find(coockie)

    def coockies_click(self):
        self.find(coockie).click()

    def prod_btn_find(self):
        return self.find(btn1)

    def prod_btn_click(self):
        return self.prod_btn_find().click()

    def prod_send_search_find(self):
        return self.find(send_search)

    def prod_send_search_click(self):
        return self.prod_send_search_find().click()

    def prod_send_search_input(self):
        sleep(0.5)
        return self.prod_send_search_find().send_keys('Zita')

    def prod_find(self):
        sleep(5)
        return self.find(product_btn)

    def product_click(self):
        return self.prod_find().click()

    def select_size_find(self):
        return self.find(select_size)

    def select_color_find(self):
        return self.find(select_color)

    def select_color_click(self):
        return self.select_color_find().click()


    def select_size_click(self):
        return self.select_size_find().click()

    def size_btn_find(self):
        return self.find(size_btn)

    def size_btn_click(self):
        return self.size_btn_find().click()

    def add_shopping_bag_find(self):
        return self.find(add_shopping_bag)

    def add_shopping_bag_click(self):
        return self.add_shopping_bag_find().click()

    def viev_shopping_bag(self):
        return self.find(viev_shopping_bag)

    def viev_shopping_bag_click(self):
        return self.viev_shopping_bag().click()

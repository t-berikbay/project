from time import sleep

from pages.insta_page import InstaPage

import allure

def test_insta(self):
    with allure.step('Open browser'):
        insta_page = InstaPage(self)

    with allure.step('open browser'):
        insta_page.open()

    with allure.step('insta_find'):
        insta_page.insta_find()
    with allure.step('insta_click'):
        insta_page.insta_click()
        sleep(2)
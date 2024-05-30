from time import sleep

from pages.wishlist_page import WishlistPage

import allure


def test_wishlist(browser):
    with allure.step('Open browser'):
        wishlist_page = WishlistPage(browser)
    with allure.step('open browser'):
        wishlist_page.open()
        browser.implicitly_wait(10)

    with allure.step('coockies'):
        wishlist_page.coockies()
        wishlist_page.coockies_click()

    with allure.step('btn_find'):
        wishlist_page.btn_find()
    with allure.step('btn_click'):
        wishlist_page.btn_click()
        sleep(2)

    with allure.step('send_search_find'):
        wishlist_page.send_search_find()
    with allure.step('send_search_click'):
        wishlist_page.send_search_click()
    with allure.step('send_search_input'):
        wishlist_page.send_search_input()
        sleep(2)
######################################################
    with allure.step('product_find'):
        wishlist_page.product_find()
    with allure.step('product_click'):
        wishlist_page.product_click()
        sleep(2)
##############################################
    with allure.step('faworits_find'):
        wishlist_page.faworits_find()
    with allure.step('faworits_click'):
        wishlist_page.faworits_click()

        sleep(6)

    with allure.step('close_wishlist'):
        wishlist_page.wishlist_find()
    with allure.step('close_wishlist_click'):
        wishlist_page.wishlist_click()
        sleep(2)





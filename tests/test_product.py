from time import sleep

from pages.product_page import ProductPage

import allure


def test_product(browser):
    with allure.step('Open browser'):
        product_page = ProductPage(browser)
    with allure.step('open browser'):
        product_page.open()

    with allure.step('coockies'):
        product_page.coockies()
        product_page.coockies_click()

    with allure.step('prod_btn_find'):
        product_page.prod_btn_find()
    with allure.step('prod_btn_click'):
        product_page.prod_btn_click()
        sleep(2)

    with allure.step('prod_send_search_find'):
        product_page.prod_send_search_find()
    with allure.step('send_search_click'):
        product_page.prod_send_search_click()
    with allure.step('send_search_input'):
        product_page.prod_send_search_input()
        sleep(2)

    with allure.step('prod_find'):
        product_page.prod_find()
    with allure.step('product_click'):
        product_page.product_click()
        sleep(2)

    with allure.step('select_color_find'):
        product_page.select_color_find()
    with allure.step('select_color_click'):
        product_page.select_color_click()
        sleep(2)

    with allure.step('select_size_find'):
        product_page.select_size_find()
    with allure.step('select_size_click'):
        product_page.select_size_click()
        sleep(2)

    with allure.step('size_btn_find'):
        product_page.size_btn_find()
    with allure.step('size_btn_click'):
        product_page.size_btn_click()
        sleep(2)

    with allure.step('add_shopping_bag_find'):
        product_page.add_shopping_bag_find()
    with allure.step('add_shopping_bag_click'):
        product_page.add_shopping_bag_click()
        sleep(5)


    with allure.step('viev_shopping_bag'):
        product_page.viev_shopping_bag()

    with allure.step('viev_shopping_bag_click'):
        product_page.viev_shopping_bag_click()
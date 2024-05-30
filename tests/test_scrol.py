from time import sleep

from pages.scrol_page import ScrollingPage

import allure


def test_scroll(browser):
    with allure.step('Open browser'):
        scroll_page = ScrollingPage(browser)
    with allure.step('open browser'):
        scroll_page.open()

    with allure.step('coockies'):
        scroll_page.coockies()
        scroll_page.coockies_click()

    with allure.step('scroll'):
        scroll_page.scroll()
        sleep(5)

    with allure.step('find countrys'):
        scroll_page.btn_find()
        sleep(2)

    with allure.step('open countrys'):
        scroll_page.btn_click()
        sleep(2)


import allure
from pages.autorization_page import AutorizationPage




def test_autorization(browser):

    with allure.step('Open browser'):
        autorization_page = AutorizationPage(browser)

    with allure.step('open browser'):
        autorization_page.open()

    with allure.step('coockie'):
        autorization_page.coockie()
        autorization_page.coockie_click()

    with allure.step('cross'):
        autorization_page.cross()

    with allure.step('autorization_find'):
        autorization_page.autorization_find()

    with allure.step('autorization_click'):
        autorization_page.autorization_click()

    with allure.step('email_find'):
        autorization_page.autorization_email_find()

    with allure.step('email_click'):
        autorization_page.autorization_email_click()

    with allure.step('email_input'):
        autorization_page.autorization_email_input()

    with allure.step('continue'):
        autorization_page.log_in()
        autorization_page.continue_click()

    with allure.step('password_find'):
        autorization_page.password_find()

    with allure.step('password_click'):
        autorization_page.password_click()

    with allure.step('password_input'):
        autorization_page.password_input()

    with allure.step('continue'):
        autorization_page.log_in()
        autorization_page.continue_click()

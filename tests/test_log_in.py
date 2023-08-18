from locators import log_in_locators
from selenium.webdriver.support import expected_conditions as EC
from helpers import automation_log_in

class Tests_log_in:
    def test_log_in_main(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        wait = browser.wait

        log_in_box = wait.until(
            EC.element_to_be_clickable(log_in_locators.log_in_box)
        )
        log_in_box.click()

        automation_log_in(browser, wait)

        order_box_text = wait.until(
            EC.presence_of_element_located(log_in_locators.order_box_text)).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через кнопку на главной странице"


    def test_log_in_personal_area(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        wait = browser.wait

        personal_area = wait.until(
            EC.element_to_be_clickable(log_in_locators.personal_area)
        )
        personal_area.click()

        automation_log_in(browser, wait)

        order_box_text = wait.until(
            EC.presence_of_element_located(log_in_locators.order_box_text)).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через личный кабинет"


    def test_log_in_register_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        wait = browser.wait

        log_in_box = wait.until(
            EC.element_to_be_clickable(log_in_locators.log_in_box_register_form)
        )
        log_in_box.click()

        automation_log_in(browser, wait)

        order_box_text = wait.until(
            EC.presence_of_element_located(log_in_locators.order_box_text)).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через форму регистрации"


    def test_log_in_forgot_pass(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/forgot-password")
        wait = browser.wait

        log_in_box = wait.until(
            EC.element_to_be_clickable(log_in_locators.log_in_box_forgot_pass_form)
        )
        log_in_box.click()

        automation_log_in(browser, wait)

        order_box_text = wait.until(
            EC.presence_of_element_located(log_in_locators.order_box_text)).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через форму восстановления пароля"


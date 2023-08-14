from selenium.webdriver.common.keys import Keys
import time
from locators import log_in_locators


class Tests_log_in:
    def test_log_in_main(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        log_in_box = browser.find_element(*log_in_locators.log_in_box)
        log_in_box.click()
        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)

        time.sleep(1)
        order_box_text = browser.find_element(*log_in_locators.order_box_text).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через кнопку на главной странице"
        browser.quit()

    def test_log_in_personal_area(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        personal_area = browser.find_element(*log_in_locators.personal_area)
        personal_area.click()

        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)

        time.sleep(1)
        order_box_text = browser.find_element(*log_in_locators.order_box_text).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через личный кабинет"
        browser.quit()

    def test_log_in_register_form(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/register")
        log_in_box = browser.find_element(*log_in_locators.log_in_box_register_form)
        log_in_box.click()

        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)

        time.sleep(1)
        order_box_text = browser.find_element(*log_in_locators.order_box_text).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через форму регистрации"
        browser.quit()

    def test_log_in_forgot_pass(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/forgot-password")
        log_in_box = browser.find_element(*log_in_locators.log_in_box_forgot_pass_form)
        log_in_box.click()

        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)

        time.sleep(1)
        order_box_text = browser.find_element(*log_in_locators.order_box_text).text
        assert "Оформить заказ" in order_box_text, "Не удалось войти в аккаунт через форму восстановления пароля"
        browser.quit()


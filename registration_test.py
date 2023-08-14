import time
from locators import register_locators


class Tests_registration:
    def test_registration(self, browser):
        login = "1test_user"
        email = "1test@example.com"
        password = "test_password"

        browser.get("https://stellarburgers.nomoreparties.site/register")
        username_input = browser.find_element(*register_locators.username_input)
        username_input.send_keys(login)
        email_input = browser.find_element(*register_locators.email_input)
        email_input.send_keys(email)
        password_input = browser.find_element(*register_locators.password_input)
        password_input.send_keys(password)

        confirm_box = browser.find_element(*register_locators.confirm_box)
        confirm_box.click()
        time.sleep(1)

        log_in_text = browser.find_element(*register_locators.log_in_text).text
        assert "Вход" in log_in_text, "Не удалось пройти регистрацию"
        browser.quit()


    def test_incorrect_pass(self, browser):
        login = "test_user"
        email = "test@example.com"
        password = "6asds"

        browser.get("https://stellarburgers.nomoreparties.site/register")
        username_input = browser.find_element(*register_locators.username_input)
        username_input.send_keys(login)
        email_input = browser.find_element(*register_locators.email_input)
        email_input.send_keys(email)
        password_input = browser.find_element(*register_locators.password_input)
        password_input.send_keys(password)
        email_input.click()
        time.sleep(1)

        incorrect_pass_text = browser.find_element(*register_locators.incorrect_pass_text).text
        assert "Некорректный пароль" in incorrect_pass_text, "Удалось создать некорректный пароль"
        browser.quit()



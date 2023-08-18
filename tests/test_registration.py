from locators import register_locators
from selenium.webdriver.support import expected_conditions as EC
from helpers import automation_registration


class Tests_registration:
    def test_registration(self, browser):
        login = "test_user"
        email = "tesssssst@example.com"
        password = "test_password"

        browser.get("https://stellarburgers.nomoreparties.site/register")
        wait = browser.wait

        automation_registration(browser, wait, login, email, password)

        log_in_text = wait.until(
            EC.presence_of_element_located(register_locators.log_in_text)).text
        assert "Войти" in log_in_text, "Не удалось пройти регистрацию"

    def test_incorrect_pass(self, browser):
        login = "test_user"
        email = "test@example.com"
        password = "6asds"

        browser.get("https://stellarburgers.nomoreparties.site/register")
        wait = browser.wait

        automation_registration(browser, wait, login, email, password)

        incorrect_pass_text = wait.until(
            EC.presence_of_element_located(register_locators.incorrect_pass_text)).text
        assert "Некорректный пароль" in incorrect_pass_text, "Удалось создать некорректный пароль"



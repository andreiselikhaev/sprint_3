from locators import constructor_locators
from selenium.webdriver.support import expected_conditions as EC

class Tests_constructor:
    def test_constructor_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/feed")
        wait = browser.wait

        constructor_box = wait.until(
            EC.element_to_be_clickable(constructor_locators.constructor_box)
        )
        constructor_box.click()

        create_burger_text = wait.until(
            EC.presence_of_element_located(constructor_locators.create_burger_text)).text
        assert "Соберите бургер" in create_burger_text, "Не удалось перейти в конструктор по кнопке 'Конструктор'"

    def test_logo_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/feed")
        wait = browser.wait

        logo_box = wait.until(
            EC.element_to_be_clickable(constructor_locators.logo_box)
        )
        logo_box.click()

        create_burger_text = wait.until(
            EC.presence_of_element_located(constructor_locators.create_burger_text)).text
        assert "Соберите бургер" in create_burger_text, "Не удалось перейти в конструктор нажав на логотип'"

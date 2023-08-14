import time
from locators import constructor_locators

class Tests_constructor:
    def test_constructor_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/feed")
        constructor_box = browser.find_element(*constructor_locators.constructor_box)
        constructor_box.click()
        time.sleep(1)
        create_burger_text = browser.find_element(*constructor_locators.create_burger_text).text
        assert "Соберите бургер" in create_burger_text, "Не удалось перейти в конструктор по кнопке 'Конструктор'"
        browser.quit()

    def test_logo_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/feed")
        logo_box = browser.find_element(*constructor_locators.logo_box)
        logo_box.click()
        time.sleep(1)
        create_burger_text = browser.find_element(*constructor_locators.create_burger_text).text
        assert "Соберите бургер" in create_burger_text, "Не удалось перейти в конструктор нажав на логотип'"
        browser.quit()

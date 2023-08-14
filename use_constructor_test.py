import time
from locators import use_constructor_locators

class Tests_use_constructor():
    def test_selector_click(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        chapter_list = []
        sauce_box = browser.find_element(*use_constructor_locators.sauce_box)
        sauce_box.click()
        chapter_list.append(browser.find_element(*use_constructor_locators.sauce_text).text)
        time.sleep(1)

        filling_box = browser.find_element(*use_constructor_locators.filling_box)
        filling_box.click()
        chapter_list.append(browser.find_element(*use_constructor_locators.filling_text).text)
        time.sleep(1)

        bun_box = browser.find_element(*use_constructor_locators.bun_box)
        bun_box.click()
        chapter_list.append(browser.find_element(*use_constructor_locators.bun_text).text)
        time.sleep(1)

        assert ['Соусы', 'Начинки', 'Булки'] == chapter_list, "Не удалось проверить переход к разделам"
        browser.quit()

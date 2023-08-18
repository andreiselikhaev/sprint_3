from selenium.webdriver.support import expected_conditions as EC
from locators import use_constructor_locators

class Tests_use_constructor():
    def test_selector_click(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        wait = browser.wait
        chapter_list = []

        sauce_box = wait.until(
            EC.element_to_be_clickable(use_constructor_locators.sauce_box)
        )
        sauce_box.click()
        chapter_list.append(wait.until(
            EC.presence_of_element_located(use_constructor_locators.sauce_text)).text)

        filling_box = wait.until(
            EC.element_to_be_clickable(use_constructor_locators.filling_box)
        )
        filling_box.click()
        chapter_list.append(wait.until(
            EC.presence_of_element_located(use_constructor_locators.filling_text)).text)

        bun_box = wait.until(
            EC.element_to_be_clickable(use_constructor_locators.bun_box)
        )
        bun_box.click()
        chapter_list.append(wait.until(
            EC.presence_of_element_located(use_constructor_locators.bun_text)).text)

        assert ['Соусы', 'Начинки', 'Булки'] == chapter_list, "Не удалось проверить переход к разделам"

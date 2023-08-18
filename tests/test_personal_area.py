from locators import log_in_locators, personal_area_locators
from selenium.webdriver.support import expected_conditions as EC
from helpers import automation_log_in

class Tests_personal_area:
    def test_personal_area_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        wait = browser.wait

        log_in_box = wait.until(
            EC.element_to_be_clickable(log_in_locators.log_in_box)
        )
        log_in_box.click()

        automation_log_in(browser, wait)

        personal_area = wait.until(
            EC.element_to_be_clickable(personal_area_locators.personal_area)
        )
        personal_area.click()

        save_box = wait.until(
            EC.presence_of_element_located(personal_area_locators.save_box)).text
        assert "Сохранить" in save_box, "Не удалось перейти в личный кабинет"



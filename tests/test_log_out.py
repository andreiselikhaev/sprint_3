from selenium.webdriver.support import expected_conditions as EC
from locators import log_in_locators, personal_area_locators, register_locators, log_out_locators
from helpers import automation_log_in


class Tests_log_out:
    def test_log_out_in_personal_area(self, browser):
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

        log_out_box = wait.until(
            EC.element_to_be_clickable(log_out_locators.log_out_box)
        )
        log_out_box.click()

        log_in_text = wait.until(
            EC.presence_of_element_located(register_locators.log_in_text)
        ).text
        assert "Войти" in log_in_text, "Не удалось выйти из аккаунта в личном кабинете"

from selenium.webdriver.common.keys import Keys
import time
from locators import log_in_locators, personal_area_locators, register_locators, log_out_locators

class Tests_log_out:
    def test_log_out_in_personal_area(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        log_in_box = browser.find_element(*log_in_locators.log_in_box)
        log_in_box.click()
        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)
        time.sleep(1)

        personal_area = browser.find_element(*personal_area_locators.personal_area)  # Кнопка личный кабинет
        personal_area.click()
        time.sleep(1)

        log_out_box = browser.find_element(*log_out_locators.log_out_box)
        log_out_box.click()
        time.sleep(1)

        log_in_text = browser.find_element(*register_locators.log_in_text).text
        assert "Вход" in log_in_text, "Не удалось выйти из аккаунта в личном кабинете"
        browser.quit()

import time
from selenium.webdriver.common.keys import Keys
from locators import log_in_locators, personal_area_locators

class Tests_personal_area:
    def test_personal_area_box(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        log_in_box = browser.find_element(*log_in_locators.log_in_box)
        log_in_box.click()
        login_fild = browser.find_element(*log_in_locators.login_fild)
        login_fild.send_keys("123456789@gmail.com")
        password_fild = browser.find_element(*log_in_locators.password_fild)
        password_fild.send_keys("Qwe12345")
        password_fild.send_keys(Keys.RETURN)
        time.sleep(1)

        personal_area = browser.find_element(*personal_area_locators.personal_area)
        personal_area.click()
        time.sleep(1)

        save_box = browser.find_element(*personal_area_locators.save_box).text
        assert "Сохранить" in save_box, "Не удалось перейти в личный кабинет"
        browser.quit()



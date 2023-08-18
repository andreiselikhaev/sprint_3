from selenium.webdriver.common.keys import Keys
from locators import log_in_locators, register_locators
from selenium.webdriver.support import expected_conditions as EC

def automation_log_in(browser, wait):
    login_fild = wait.until(
        EC.presence_of_element_located(log_in_locators.login_fild)
    )
    login_fild.send_keys("123456789@gmail.com")
    password_fild = browser.find_element(*log_in_locators.password_fild)
    password_fild.send_keys("Qwe12345")
    password_fild.send_keys(Keys.RETURN)


def automation_registration(browser, wait, login, email, password):
    username_input = wait.until(
        EC.presence_of_element_located(register_locators.username_input)
    )
    username_input.send_keys(login)
    email_input = browser.find_element(*register_locators.email_input)
    email_input.send_keys(email)
    password_input = browser.find_element(*register_locators.password_input)
    password_input.send_keys(password)

    confirm_box = wait.until(
        EC.element_to_be_clickable(register_locators.confirm_box)
    )
    confirm_box.click()
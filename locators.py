from selenium.webdriver.common.by import By

class register_locators():
    username_input = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")   # Поле для ввода username
    email_input = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")  # Поле для ввода email
    password_input = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input")   # Поле для ввода password
    confirm_box = (By.XPATH, "/html/body/div/div/main/div/form/button")   # Кнопка зарегистрироваться
    log_in_text = (By.XPATH, "/html/body/div/div/main/div/h2")  # Элемент хранящий текст "Вход"
    incorrect_pass_text = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")   # Элемент хранящий текст "Некорректный пароль"

class log_in_locators():
    log_in_box = (By.CLASS_NAME, "button_button__33qZ0")    # Кнопка войти в аккаунт
    log_in_box_register_form = (By.XPATH, "/html/body/div/div/main/div/div/p/a")   # Кнопка войти в аккаунт в форме регистрации
    log_in_box_forgot_pass_form = (By.XPATH, "/html/body/div/div/main/div/div/p/a")   # Кнопка войти в аккаунт в форме восстановления пароля
    login_fild = (By.NAME, "name")  # Поле логин
    password_fild = (By.NAME, "Пароль")  # Поле пароль
    order_box_text = (By.CLASS_NAME, "button_button__33qZ0")    # Кнопка Оформить заказ
    personal_area = (By.XPATH, "/html/body/div/div/header/nav/a")   # Кнопка личный кабинет

class personal_area_locators():
    personal_area = (By.XPATH, "/html/body/div/div/header/nav/a")  # Кнопка личный кабинет
    save_box = (By.XPATH, "/html/body/div/div/main/div/div/div/div/button[2]")  # Кнопка "Сохранить" в личном кабинете

class constructor_locators():
    constructor_box = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p")  # Кнопка конструктор
    create_burger_text = (By.XPATH, "/html/body/div/div/main/section[1]/h1")    # Текст "Соберите бургер" в конструкторе
    logo_box = (By.XPATH, "/html/body/div/div/header/nav/div")   # Кнопка в логотипе

class log_out_locators():
    log_out_box = (By.XPATH, "//li[@class='Account_listItem__35dAP']/button[contains(text(), 'Выход')]") # Кнопка "Выход"

class use_constructor_locators():
    sauce_box = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]")  # Кнопка соусы
    sauce_text = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[2]")   # Текст "соусы"
    filling_box = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")  # Кнопка начинки
    filling_text = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[3]")   # Текст "начинки"
    bun_box = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]")    # Кнопка булки
    bun_text = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/h2[1]")   # Текст "булки"
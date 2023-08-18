from selenium.webdriver.common.by import By

class register_locators():
    username_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")   # Поле для ввода username
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле для ввода email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")   # Поле для ввода password
    confirm_box = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']")   # Кнопка зарегистрироваться
    log_in_text = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")  # Элемент хранящий текст "Вход"
    incorrect_pass_text = (By.XPATH, "//p[contains(@class, 'input__error text_type_main-default')]")   # Элемент хранящий текст "Некорректный пароль"

class log_in_locators():
    log_in_box = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка войти в аккаунт
    log_in_box_register_form = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")  # Кнопка войти в аккаунт в форме регистрации
    log_in_box_forgot_pass_form = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj')]")  # Кнопка войти в аккаунт в форме восстановления пароля
    login_fild = (By.NAME, "name")  # Поле логин
    password_fild = (By.NAME, "Пароль")  # Поле пароль
    order_box_text = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка Оформить заказ
    personal_area = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")   # Кнопка личный кабинет

class personal_area_locators():
    personal_area = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Личный Кабинет']")  # Кнопка личный кабинет
    save_box = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]")  # Кнопка "Сохранить" в личном кабинете

class constructor_locators():
    constructor_box = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Конструктор']")  # Кнопка конструктор
    create_burger_text = (By.XPATH, "//h1[contains(@class, 'text text_type_main-large mb-5 mt-10') and text()='Соберите бургер']")    # Текст "Соберите бургер" в конструкторе
    logo_box = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")   # Кнопка в логотипе

class log_out_locators():
    log_out_box = (By.XPATH, "//li[@class='Account_listItem__35dAP']/button[contains(text(), 'Выход')]") # Кнопка "Выход"

class use_constructor_locators():
    sauce_box = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Соусы']")  # Кнопка соусы
    sauce_text = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and text()='Соусы']")   # Текст "соусы"
    filling_box = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Начинки']")  # Кнопка начинки
    filling_text = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and text()='Начинки']")   # Текст "начинки"
    bun_box = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Булки']")    # Кнопка булки
    bun_text = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and text()='Булки']")   # Текст "булки"
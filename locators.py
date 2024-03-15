header_logo = ".//div[contains(@class, 'AppHeader_header__logo')]"  # Логотип в хэдере страницы сайта

login_button_on_main_page = ".//section[contains(@class, 'BurgerConstructor_basket')]//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"

auth_form = ".//button[text()='Войти']/parent::form[contains(@class, 'Auth_form')]"  # Форма аутентификации для входа в личный кабинет

registration_link = ".//a[@href='/register' and text()='Зарегистрироваться']"  # Ссылка для входа на страницу регистрации

registration_form = ".//button[text()='Зарегистрироваться']/parent::form[contains(@class, 'Auth_form')]"  # Форма регистрации

name_input = ".//label[(text()='Имя')]/parent::div/input"  # Поле ввода имени

email_input = ".//label[(text()='Email')]/parent::div/input"  # Поле ввода email

password_input = ".//input[@name='Пароль']"  # Поле ввода пароля

registration_button = ".//form[contains(@class, 'Auth_form')]/button[text()='Зарегистрироваться']"  # Кнопка 'Зарегистрироваться' в форме регистрации

login_button_on_auth_page = ".//form[contains(@class, 'Auth_form')]/button[text()='Войти']"  # - Кнопка 'Войти' на странице авторизации

profile_link_on_main_page = ".//header//a/p[text()='Личный Кабинет']"  # Ссылка на страницу Профиля пользователя

user_data_on_profile_page = ".//main/div[contains(@class, 'Account_account')]"  # Блок с данными пользователя в Профиле пользователя

name_filed_on_profile_page = ".//ul[contains(@class, 'Profile_profileList')]//input[@name='Name']"  # Поле имя в профиле пользователя

login_field_on_profile_page = ".//label[text()='Логин']/parent::div/input"  # Поле логин в профиле пользователя

error_message_element = ".input__error"  # Элемент с сообщением об ошибке (пароля)

ingredients_section = ".//section[contains(@class, 'BurgerIngredients_ingredients')]"  # Секция с ингредиентами бургера на главной странице

button_in_burger_section = ".//section[contains(@class, 'BurgerConstructor_basket')]//button"  # Кнопка в секции корзины с бургером

login_link_element = ".//a[@href='/login' and text()='Войти']"  # Ссылка для перехода на страницу логина

forgot_password_link = ".//a[@href='/forgot-password']"  # Ссылка для перехода на страницу восстановления пароля

recovery_password_form = ".//form[contains(@class, 'Auth_form')]/button[text()='Восстановить']"  # Форма восстановления пароля

paragraph_in_profile = ".//p[contains(@class, 'Account_text')]"  # Абзац с текстом в профиле пользователя

constructor_link_element = ".//header//a/p[text()='Конструктор']"  # Ссылка на переход в Конструктов в Хэдере

ingredients_section_header = ".//section[contains(@class, 'BurgerIngredients_ingredients')]/h1"

exit_button = ".//ul[contains(@class, 'Account_list')]/li/button[(text()='Выход')]"  #- Кнопка 'Выйти' в профиле пользователя

login_header_element = ".//div[contains(@class, 'Auth_login')]/h2"  # - Заголовок на странице логина

fillings_section_element = ".//section[contains(@class, 'BurgerIngredients_ingredients')]//span[text()='Начинки']/parent::div" #- Переход к разделу 'Начинки' в Конструкторе

sauces_section_element = ".//section[contains(@class, 'BurgerIngredients_ingredients')]//span[text()='Соусы']/parent::div" #- Переход к разделу 'Начинки' в Конструкторе

loaves_section_element = ".//section[contains(@class, 'BurgerIngredients_ingredients')]//span[text()='Булки']/parent::div" #- Переход к разделу 'Начинки' в Конструкторе


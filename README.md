# Sprint_5

В файле locators.py - Список используемых локаторов

В файле data.py - Логин и пароль пользователя

В файле coftests - Логика открытия и закрытия экземпляра браузера для страницы "https://stellarburgers.nomoreparties.site/"

Список тестов:

1. Регистрация:
   
tests/test_registration.py

registration_success - Успешная регистрацию

test_registration_incorrect_password - Регистрация, сообщение c некорректном пароле

3. Вход

tests/test_login.py

test_login_use_button_on_main_page - Вход по кнопке «Войти в аккаунт» на главной

test_login_use_profile_button - Вход через кнопку «Личный кабинет»

test_login_use_button_on_registration_page - Вход через кнопку в форме регистрации

test_login_use_button_on_password_recovery_page - вход через кнопку в форме восстановления пароля

5. Переход в личный кабинет

tests/test_transition_profile.py

test_transition_to_profile - Переход по клику на «Личный кабинет»


7. Переход из личного кабинета в конструктор
   
tests/test_transition_to_constructor.py

test_transition_to_constructor_click_constructor.py - Переход по клику на «Конструктор»

test_transition_to_constructor_click_logo.py - Переход по клику на логотип Stellar Burgers


9. Выход из аккаунта
    
test_logout.py

test_logout_button_in_profile - Выход по кнопке «Выйти» в личном кабинете

11. Раздел «Конструктор»

tests/test_transitions_to_constructor_sections.py

test_transition_to_fillings - Переход к разделу «Начинки»

test_transition_to_sauces - Переход к разделу «Соусы»

test_transition_to_loaves - Переход к разделу «Булки»

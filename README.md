# Sprint_5

В файле locators.txt - Список используемых локаторов

Список тестов:

1. Регистрация:

tests/test_registration_success.py - Успешная регистрацию
tests/test_registration_incorrect_password.py - Регистрация, сообщение c некорректном пароле

2. Вход

tests/test_login_use_button_on_main_page.py - Вход по кнопке «Войти в аккаунт» на главной
tests/test_login_use_profile_button.py - Вход через кнопку «Личный кабинет»
tests/test_login_use_button_on_registration_page.py - Вход через кнопку в форме регистрации
tests/test_login_use_button_on_password_recovery_page.py - вход через кнопку в форме восстановления пароля

3. Переход в личный кабинет

tests/test_transition_profile.py - Переход по клику на «Личный кабинет»

4. Переход из личного кабинета в конструктор

tests/test_transition_to_constructor_click_constructor.py - Переход по клику на «Конструктор»
tests/test_transition_to_constructor_click_logo.py - Переход по клику на логотип Stellar Burgers

5. Выход из аккаунта

python tests/test_logout_button_in_profile.py - Выход по кнопке «Выйти» в личном кабинете

6. Раздел «Конструктор»

tests/test_transitions_to_constructor_sections.py - Переходы к разделам: «Булки», «Соусы» «Начинки»

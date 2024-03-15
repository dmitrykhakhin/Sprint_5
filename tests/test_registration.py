from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import *


class TestRegistration:
    def test_registration_success(self, driver):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        login_button = driver.find_element(
            By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        register_link = driver.find_element(By.XPATH, registration_link)
        register_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, registration_form)))
        # Заполняем форму регистрации
        name_input_field = driver.find_element(By.XPATH, name_input)
        new_user_name = 'Дмитрий'
        name_input_field.send_keys(new_user_name)
        email_input_field = driver.find_element(By.XPATH, email_input)
        new_login = 'dmitry' + str(random.randint(1000, 9999)) + '@ya.ru'
        email_input_field.send_keys(new_login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        new_password = str(random.randint(100000, 999999))
        password_input_field.send_keys(new_password)
        register_button = driver.find_element(
            By.XPATH, registration_button)
        register_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, auth_form)))
        # Входим в аккаунт под созданным пользователем
        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(new_login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(new_password)
        login_button = driver.find_element(
            By.XPATH, login_button_on_auth_page)
        login_button.click()

        # Входим на страницу профиля пользователя
        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, profile_link_on_main_page)))
        profile_link = driver.find_element(By.XPATH, profile_link_on_main_page)
        profile_link.click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, user_data_on_profile_page)))

        user_name = driver.find_element(By.XPATH, name_filed_on_profile_page).get_attribute("value")

        login_name = driver.find_element(By.XPATH, login_field_on_profile_page).get_attribute("value")

        assert user_name == new_user_name and login_name == new_login

    def test_registration_incorrect_password(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        login_button = driver.find_element(By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, auth_form)))

        register_link = driver.find_element(By.XPATH, registration_link)
        register_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, registration_form)))
        # Заполняем форму регистрации
        name_input_field = driver.find_element(By.XPATH, name_input )
        new_user_name = 'Дмитрий'
        name_input_field.send_keys(new_user_name)
        email_input_field = driver.find_element(By.XPATH, email_input)
        new_login = 'dmitry' + str(random.randint(1000, 9999)) + '@ya.ru'
        email_input_field.send_keys(new_login)

        # Вводим некорректный пароль
        password_input_field = driver.find_element(By.XPATH, password_input)
        short_password = str(random.randint(10000, 99999))
        password_input_field.send_keys(short_password)
        register_button = driver.find_element(
            By.XPATH, registration_button)
        register_button.click()

        password_error_notification = driver.find_element(By.CSS_SELECTOR, error_message_element)

        assert password_error_notification.text == 'Некорректный пароль'

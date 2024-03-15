from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *
from data import *


class TestLogin:
    def test_login_use_button_on_main_page(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        login_button = driver.find_element(By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, login_button_on_auth_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        create_order_button = driver.find_element(By.XPATH, button_in_burger_section)

        assert create_order_button.text == 'Оформить заказ'

    def test_login_use_profile_button(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, profile_link_on_main_page)))
        profile_link = driver.find_element(By.XPATH, profile_link_on_main_page)
        profile_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, login_button_on_auth_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        create_order_button = driver.find_element(By.XPATH, button_in_burger_section)

        assert create_order_button.text == 'Оформить заказ'

    def test_login_use_button_on_registration_page(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        login_button = driver.find_element(By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        register_link = driver.find_element(By.XPATH, registration_link)
        register_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, registration_form)))

        login_link = driver.find_element(By.XPATH, login_link_element)
        login_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, auth_form)))

        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(password)
        login_button = driver.find_element(
            By.XPATH, login_button_on_auth_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        create_order_button = driver.find_element(
            By.XPATH, button_in_burger_section)

        assert create_order_button.text == 'Оформить заказ'

    def test_login_use_button_on_password_recovery_page(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, header_logo)))

        login_button = driver.find_element(By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        recovery_password_link = driver.find_element(By.XPATH, forgot_password_link)
        recovery_password_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, recovery_password_form)))

        login_link = driver.find_element(By.XPATH, login_link_element)
        login_link.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, login_button_on_auth_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        create_order_button = driver.find_element(By.XPATH, button_in_burger_section)

        assert create_order_button.text == 'Оформить заказ'

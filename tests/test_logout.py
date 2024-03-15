from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *
from data import *


class TestLogout:
    def test_logout_button_in_profile(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, header_logo)))

        login_button = driver.find_element(By.XPATH, login_button_on_main_page)
        login_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        email_input_field = driver.find_element(By.XPATH, email_input)
        email_input_field.send_keys(login)
        password_input_field = driver.find_element(By.XPATH, password_input)
        password_input_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, login_button_on_auth_page)
        login_button.click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, profile_link_on_main_page)))
        profile_link = driver.find_element(By.XPATH, profile_link_on_main_page)
        profile_link.click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, user_data_on_profile_page)))

        logout_button = driver.find_element(By.XPATH,exit_button)
        logout_button.click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, auth_form)))

        login_header = driver.find_element(By.XPATH, login_header_element)

        assert login_header.text == 'Вход'

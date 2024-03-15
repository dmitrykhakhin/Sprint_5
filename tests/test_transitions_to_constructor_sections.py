from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *
from data import *


class TestTransitionToConstructorSections:
    def test_transition_to_fillings(self, driver):
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

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        filling_section = driver.find_element(
            By.XPATH,
            fillings_section_element)
        filling_section.click()

        assert 'current' in filling_section.get_attribute('class')

    def test_transition_to_sauces(self, driver):
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

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        sauces_section = driver.find_element(
            By.XPATH,
            sauces_section_element)
        sauces_section.click()

        assert 'current' in sauces_section.get_attribute('class')

    def test_transition_to_loaves(self, driver):
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

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ingredients_section)))

        filling_section = driver.find_element(
            By.XPATH,
            fillings_section_element)
        filling_section.click()

        loaves_section = driver.find_element(
            By.XPATH,
            loaves_section_element)
        loaves_section.click()

        assert 'current' in loaves_section.get_attribute('class')

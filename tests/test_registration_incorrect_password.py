from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import random

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")))

login_button = driver.find_element(
    By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]//button[text()='Войти в аккаунт']")
login_button.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, ".//button[text()='Войти']/parent::form[contains(@class, 'Auth_form')]")))

register_link = driver.find_element(By.XPATH, ".//a[@href='/register' and text()='Зарегистрироваться']")
register_link.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, ".//button[text()='Зарегистрироваться']/parent::form[contains(@class, 'Auth_form')]")))
# Заполняем форму регистрации
name_input_field = driver.find_element(By.XPATH, ".//label[(text()='Имя')]/parent::div/input")
new_user_name = 'Дмитрий'
name_input_field.send_keys(new_user_name)
email_input_field = driver.find_element(By.XPATH, ".//label[(text()='Email')]/parent::div/input")
new_login = 'dmitry'+str(random.randint(1000, 9999)) + '@ya.ru'
email_input_field.send_keys(new_login)

# Вводим некорректный пароль
password_input_field = driver.find_element(By.XPATH, ".//input[@name='Пароль']")
short_password = str(random.randint(10000, 99999))
password_input_field.send_keys(short_password)
register_button = driver.find_element(
    By.XPATH, ".//form[contains(@class, 'Auth_form')]/button[text()='Зарегистрироваться']")
register_button.click()


password_error_notification = driver.find_element(By.CSS_SELECTOR, ".input__error")
assert password_error_notification.text == 'Некорректный пароль'

driver.quit()

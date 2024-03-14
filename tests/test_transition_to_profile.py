from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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

email_input_field = driver.find_element(By.XPATH, ".//label[(text()='Email')]/parent::div/input")
login = 'dmitry_qa06@ya.ru'
email_input_field.send_keys(login)
password = 'abc123'
password_input_field = driver.find_element(By.XPATH, ".//input[@name='Пароль']")
password_input_field.send_keys(password)
login_button = driver.find_element(
    By.XPATH, ".//form[contains(@class, 'Auth_form')]/button[text()='Войти']")
login_button.click()

WebDriverWait(driver, 5).until(
    expected_conditions.element_to_be_clickable((By.XPATH, ".//header//a/p[text()='Личный Кабинет']")))
profile_link = driver.find_element(By.XPATH, ".//header//a/p[text()='Личный Кабинет']")
profile_link.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, ".//main/div[contains(@class, 'Account_account')]")))

information_text = driver.find_element(By.XPATH, ".//p[contains(@class, 'Account_text')]")

assert information_text.text == 'В этом разделе вы можете изменить свои персональные данные'

driver.quit()

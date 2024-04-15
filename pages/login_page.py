import allure
import os

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class LoginPageLocators(object):
    # xpath кнопки принятия куки
    COOKIES_ACCEPT_BUTTON = (By.XPATH, "//button[text()='Принять']")
    # xpath кнопки "личный кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath кнопки "Вход"
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Вход']")
    # xpath поля Email
    EMAIL_LOGIN_INPUT = (By.XPATH, "//input[@id='input-auth1']")
    # xpath поля Password
    PASSWORD_LOGIN_INPUT = (By.XPATH, "//input[@id='input-auth2']")
    # xpath кнопки Sign in
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # xpath алерта при попытке логина с неправильными email и password
    INCORRECT_LOGIN_ALERT = (By.XPATH, "//div[@class='invalid-feedback' and text()='Неверный e-mail или пароль']")
    # xpath дропдауна аккаунта
    ACCOUNT_BUTTON_DROPDOWN = (By.XPATH, "//a[@class='head-bar__link' and contains(@href, '/my/')]")
    # xpath кнопки Sign in
    LOGOUT_BUTTON = (By.XPATH, "//span[text()='Выход']")


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    load_dotenv()
    email = os.environ.get("EMAIL")
    password = os.environ.get("PASSWORD")

    @allure.step("Принимаем куки")
    def accept_cookie(self):
        self.wait_and_click(*LoginPageLocators.COOKIES_ACCEPT_BUTTON)

    @allure.step("Логин в приложение: почта - {email}, пароль - {password} ")
    def login_user(self, email=email, password=password):
        self.accept_cookie()
        self.wait_and_click(*LoginPageLocators.ACCOUNT_BUTTON)
        self.wait_and_click(*LoginPageLocators.LOGIN_BUTTON)
        self.clear_and_set_value(*LoginPageLocators.EMAIL_LOGIN_INPUT, email)
        self.clear_and_set_value(*LoginPageLocators.PASSWORD_LOGIN_INPUT, password)
        self.wait_and_click(*LoginPageLocators.SIGN_IN_BUTTON)

    @allure.step("Logout пользователя")
    def logout_user(self):
        self.wait_and_click(*LoginPageLocators.ACCOUNT_BUTTON_DROPDOWN)
        self.wait_and_click(*LoginPageLocators.LOGOUT_BUTTON)

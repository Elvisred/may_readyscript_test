import time

import allure
import pytest

from pages.login_page import LoginPage, LoginPageLocators
from tests.base_test import BaseTest
from tests.conftest import random_string
from utils.sreenshooter import ScreenShooter


@allure.epic("Login tests")
class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.loginpage = LoginPage(browser, BaseTest.baseurl)
        self.loginpage.open(BaseTest.baseurl)
        self.screenshooter = ScreenShooter(browser)

    @allure.story("Login")
    @allure.title("Проверка успешного логина")
    def test_correct_login(self, browser):
        self.loginpage.login_user()

        self.loginpage.open_account_dropdown()

        self.screenshooter.compare_screenshots('./screenshots/login/account_dropdown.png')
        with allure.step("Скриншоты сверены корректно"):
            pass

    @allure.story("Negative Login")
    @allure.title("Негативные тесты авторизации")
    @pytest.mark.parametrize(
        "case_index, email, password",
        [
            (0, f"not_exist_email_{random_string(5)}@gmail.com", random_string(12)),  # несуществующие логин и пароль
            (0, LoginPage.email, "random_string(12)"),  # реальный логин, неправильный пароль
            (1, f"no_password_{random_string(5)}@gmail.com", ""),  # валидный логин, пустой пароль
            (1, "", random_string(12)),  # пустой логин
            (1, f"short_password_{random_string(5)}@gmail.com", random_string(6)),  # короткий пароль
            (1, f"short_password_{random_string(5)}gmail.com", random_string(12)),  # невалидный логин
        ],
    )
    def test_negative_login(self, browser, case_index, email, password):
        self.loginpage.login_user(email=email, password=password)

        with allure.step("Проверяем сообщение об ошибке"):
            assert self.loginpage.is_element_present(*LoginPageLocators.INCORRECT_LOGIN_ALERT)

    @allure.story("Logout")
    @allure.title("Тест разлогина")
    def test_logout(self, browser):
        self.loginpage.login_user()

        self.loginpage.logout_user()

        with allure.step("Проверяем наличие элемента личного кабинета, что указывает на успешный разлогин"):
            assert self.loginpage.is_element_present(*LoginPageLocators.ACCOUNT_BUTTON)

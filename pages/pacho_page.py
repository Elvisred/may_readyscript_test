import time

import allure
import os

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class LoginPachoPageLocators(object):
    # xpath кнопки принятия куки
    COOKIES_ACCEPT_BUTTON = (By.XPATH, "//span[@class='custom-button__title' and @data-title='Accept all']")
    # xpath выбора английского языка
    ENGLISH_SELECTOR = (By.XPATH, "//img[@alt='English']")
    # xpath кнопки "Log in" на главной
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")
    # xpath кнопки "Login" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Log In']")
    # xpath первой игры в топе
    FIRST_TOP_GAME = (By.XPATH, "(//a[@href='/en/game/mr-pacho?mode=real'])")


class PachoPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(PachoPage, self).__init__(*args, **kwargs)
        self._web_driver = None

    load_dotenv()
    login = os.environ.get("PACHO_LOGIN")
    password = os.environ.get("PACHO_PASSWORD")

    @allure.step("Логин в приложение: почта - {login}, пароль - {password} ")
    def login_pacho_user(self, login=login, password=password):

        time.sleep(2)
        self.press_enter()
        time.sleep(3)
        self.wait_and_click(*LoginPachoPageLocators.MAIN_PAGE_LOGIN_BUTTON)
        time.sleep(2)
        self.enter_text(login)
        time.sleep(1)
        self.press_tab()
        self.enter_text(password)
        time.sleep(2)
        self.wait_and_click(*LoginPachoPageLocators.LOGIN_BUTTON)
        time.sleep(2)
        self.wait_and_click(*LoginPachoPageLocators.COOKIES_ACCEPT_BUTTON)

# тут костыльно слегка пока, лень нормально сделать
    @allure.step("Скролл до топа игр")
    def scroll_to_top_games(self):
        time.sleep(2)
        self.scroll_by_pixels(1300)

    @allure.step("Клик по кнопке по порядковому номеру - {number}")
    def click_top_game_by_order_number(self, number):
        time.sleep(2)
        self.hover_and_click(By.XPATH, f"(//a[@class='game-tile--btn _play'])[{number}]")

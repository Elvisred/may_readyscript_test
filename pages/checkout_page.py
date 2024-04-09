import allure
import os

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPageLocators(object):
    # кнопка корзины
    CHECKOUT_BUTTON = (By.XPATH, "//a[@id='rs-cart']")
    # кнопка "Вернуться на главную"
    BACK_TO_MAIN_SCREEN_BUTTON = (By.XPATH, "//a[@href='/' and contains(@class, 'btn-primary')]")


class CheckoutPage(BasePage):
    pass

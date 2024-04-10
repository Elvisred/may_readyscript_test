import allure


from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPageLocators(object):
    # кнопка корзины
    CART_BUTTON = (By.XPATH, "//a[@id='rs-cart']")
    # кнопка "Очистить"
    EMPTY_CART_BUTTON = (By.XPATH, "//a[contains(@class, 'rs-clean')]")
    # удаление первого товара из корзины
    FIRST_CART_ITEM_DELETE_BUTTON = (By.XPATH, "//a[contains(@class,'cart-checkout-item__del')]")


class CheckoutPage(BasePage):

    @allure.step("Переход в корзину")
    def move_to_cart(self):
        self.wait_and_click(*CheckoutPageLocators.CART_BUTTON)

    @allure.step("Очистка корзины")
    def empty_cart(self):
        self.wait_and_click(*CheckoutPageLocators.EMPTY_CART_BUTTON)

    @allure.step("Удаление из корзины первого товара")
    def delete_first_item(self):
        self.wait_and_click(*CheckoutPageLocators.FIRST_CART_ITEM_DELETE_BUTTON)

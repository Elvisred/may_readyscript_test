import time

import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


@allure.epic("Checkout tests")
class TestCheckout(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.loginpage = LoginPage(browser, BaseTest.baseurl)
        self.loginpage.open(BaseTest.baseurl)
        self.checkoutpage = CheckoutPage(browser, BaseTest.baseurl)
        self.catalogpage = CatalogPage(browser, BaseTest.baseurl)

    @allure.story("Checkout")
    @allure.title("Проверка добавления товаров в корзину и их удаление")
    def test_add_and_remove_products_from_cart(self, browser):
        self.loginpage.login_user()

        self.catalogpage.select_main_catalog_category(CatalogPage.MainCatalogCategory.LAPTOPS)
        self.catalogpage.add_to_cart_by_order_number(1)
        self.catalogpage.back_to_catalog()
        self.catalogpage.add_to_cart_by_order_number(2)
        self.catalogpage.back_to_catalog()
        self.catalogpage.add_to_cart_by_order_number(3)
        self.catalogpage.back_to_catalog()
        self.catalogpage.open_product_page_by_order_number(4)
        self.catalogpage.add_to_cart_from_product_page()
        self.catalogpage.proceed_to_checkout_from_product_page()



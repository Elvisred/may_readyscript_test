import time

import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


@allure.epic("Catalog tests")
class TestCatalog(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.loginpage = LoginPage(browser, BaseTest.baseurl)
        self.loginpage.open(BaseTest.baseurl)
        self.catalogpage = CatalogPage(browser, BaseTest.baseurl)

    @allure.story("Catalog")
    @allure.title("Проверка страницы каталога планшетов марки Digma. Переход через дропдаун меню")
    def test_digma_tablets_page(self, browser):
        self.loginpage.login_user()

        self.catalogpage.click_catalog_dropdown()
        self.catalogpage.hover_dropdown_catalog_category(CatalogPage.DropdownCatalogCategory.ELECTRONICS)
        self.catalogpage.hover_dropdown_catalog_subcategory(CatalogPage.ElectronicsSubCategory.TABLETS)
        self.catalogpage.select_dropdown_tablets_brand(CatalogPage.TabletsCategoryBrands.DIGMA)

        time.sleep(1)

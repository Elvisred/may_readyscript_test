import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.sreenshooter import ScreenShooter


@allure.epic("Catalog tests")
class TestCatalog(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.loginpage = LoginPage(browser, BaseTest.baseurl)
        self.loginpage.open(BaseTest.baseurl)
        self.catalogpage = CatalogPage(browser, BaseTest.baseurl)
        self.screenshooter = ScreenShooter(browser)

    @allure.story("Catalog")
    @allure.title("Проверка страницы каталога планшетов марки Digma. Переход через дропдаун меню")
    def test_digma_tablets_page(self, browser):
        self.loginpage.login_user()

        self.catalogpage.click_catalog_dropdown()
        self.catalogpage.hover_dropdown_catalog_category(CatalogPage.DropdownCatalogCategory.ELECTRONICS)
        self.catalogpage.hover_dropdown_catalog_subcategory(CatalogPage.ElectronicsSubCategory.TABLETS)
        self.screenshooter.compare_screenshots('./screenshots/catalog/tablets_dropdown.png')
        self.catalogpage.select_dropdown_tablets_brand(CatalogPage.TabletsCategoryBrands.DIGMA)

        self.screenshooter.compare_screenshots('./screenshots/catalog/digma_tablets_catalog_screen.png')
        with allure.step("Скриншоты сверены корректно"):
            pass

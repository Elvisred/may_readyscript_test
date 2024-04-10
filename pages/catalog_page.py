from enum import Enum

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPageLocators(object):
    # xpath дропдауна каталога
    CATALOG_DROPDOWN = (By.XPATH, "//button[contains(@class, 'head-catalog-btn')]")
    # xpath "Вернуться к покупкам" из окна добавления товара в корзину
    BACK_TO_CATALOG_BUTTON = (By.XPATH, "//a[@aria-label='Close']")
    # xpath кнопки "В корзину" в карточке товара
    ADD_TO_CART_ON_PRODUCT_PAGE_BUTTON = (By.XPATH, "(//button[contains(@class, 'rs-buy')])[1]")
    # xpath кнопки "Перейти в корзину" в карточке товара
    PROCEED_TO_CHECKOUT_FROM_PRODUCT_PAGE_BUTTON = (By.XPATH, "//a[@href='/cart/']")


class CatalogPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CatalogPage, self).__init__(*args, **kwargs)

    class DropdownCatalogCategory(Enum):
        DEMO = "Демо-продукты"
        ELECTRONICS = "Электроника"
        CLOTHES = "Одежда, обувь"
        KIDS_PRODUCTS = "Детские товары"
        SPORT_PRODUCTS = "Спорт товары"
        GIFTS = "Подарки"

    class ElectronicsSubCategory(Enum):
        PROJECTORS = "Проекторы"
        TABLETS = "Планшеты"
        LAPTOPS = "Ноутбуки"
        PHONES = "Телефоны"
        SMARTPHONES = "Смартфоны"

    class TabletsCategoryBrands(Enum):
        DIGMA = "Digma"
        ARCHOS = "Archos"
        HTS = "HTS"
        VIEWSONIC = "ViewSonic"
        CREATIVE = "Creative"

    # Методы для работы с дродауном каталога

    @allure.step("Клик на дропдаун каталога")
    def click_catalog_dropdown(self):
        self.wait_and_click(*CatalogPageLocators.CATALOG_DROPDOWN)

    # значения категории в CatalogCategory
    @allure.step("Выбор категории товаров в дропдауне каталога - {category}")
    def select_dropdown_catalog_category(self, category):
        self.wait_and_click(By.XPATH, f"//span[text()='{category.value}']")

    # значения категории в DropdownCategory
    @allure.step("Ховер на категорию товаров в дропдауне каталога - {category}")
    def hover_dropdown_catalog_category(self, category):
        self.hover_to_element(By.XPATH, f"//span[text()='{category.value}']")

    # значения субкатегории в ElectronicsSubCategory
    @allure.step("Ховер в субкатегорию товаров в дропдауне каталога электоники - {subcategory}")
    def hover_dropdown_catalog_subcategory(self, subcategory):
        self.hover_to_element(By.XPATH, f"//a[text()='{subcategory.value}']")

    # значения бренда в TabletsCategoryBrands
    @allure.step("Ховер и клик на марку планшетов в дропдауне каталога планшетов - {brand}")
    def select_dropdown_tablets_brand(self, brand):
        self.hover_and_click(By.XPATH, f"//li/a[text()='{brand.value}']")

    # Методы для работы с основным каталогом на главной странице

    class MainCatalogCategory(Enum):
        TABLETS = "Планшеты"
        LAPTOPS = "Ноутбуки"
        PROJECTORS = "Проекторы"
        PHONES = "Телефоны"
        CLOTHES = "Одежда обувь"
        SMARTPHONES = "Смартфоны"
        KIDS_PRODUCTS = "Детские товары"
        GIFTS = "Подарки"
        SPORT_PRODUCTS = "Спорт товары"

    # значения категории в MainCatalogCategory
    @allure.step("Выбор категории товаров в каталоге - {category}")
    def select_main_catalog_category(self, category):
        self.wait_and_click(By.XPATH, f"//a[.//div[contains(@class, 'index-category__title') "
                                      f"and text()='{category.value}']]")

    # Методы для работы внутри категорий товаров

    @allure.step("Прямое добавление товара 'В корзину' по порядковому номеру - {number}")
    def add_to_cart_by_order_number(self, number):
        self.wait_and_click(By.XPATH, f"(//button[contains(@class, 'rs-buy')])[{number}]")

    @allure.step("Возврат к покупкам из окна выбранных товаров")
    def back_to_catalog(self):
        self.wait_and_click(*CatalogPageLocators.BACK_TO_CATALOG_BUTTON)

    @allure.step("Переход в карточку товара по порядковому номеру - {number}")
    def open_product_page_by_order_number(self, number):
        self.wait_and_click(By.XPATH, f"(//img[@class='rs-image'])[{number}]")

    @allure.step("Добавление товара в корзину из карточки товара")
    def add_to_cart_from_product_page(self):
        self.wait_and_click(*CatalogPageLocators.ADD_TO_CART_ON_PRODUCT_PAGE_BUTTON)

    @allure.step("Переход в корзину из окна выбранных товаров")
    def proceed_to_checkout_from_product_page(self):
        self.wait_and_click(*CatalogPageLocators.PROCEED_TO_CHECKOUT_FROM_PRODUCT_PAGE_BUTTON)

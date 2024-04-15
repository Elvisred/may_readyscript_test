import time

import allure
import pytest

from pages.pacho_page import PachoPage
from tests.base_test import BaseTest
from utils.sreenshooter import ScreenShooter


@allure.epic("Login tests")
class TestPachoGames(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.pachopage = PachoPage(browser, BaseTest.pachourl)
        self.pachopage.open(BaseTest.pachourl)
        self.screenshooter = ScreenShooter(browser)

    @allure.story("Login")
    @allure.title("Проверка успешного логина")
    def test_login_and_example_game_test_for_nastya(self, browser):
        self.pachopage.login_pacho_user()
        self.pachopage.scroll_to_top_games()
        self.pachopage.click_top_game_by_order_number(1)
        time.sleep(2000)
        self.screenshooter.compare_screenshots('./screenshots/mr_pacho_test/fish_and_spins_game_screen.png')
        self.screenshooter.compare_screenshots('./screenshots/mr_pacho_test/fish_and_spins_game_start.png')
        with allure.step("Скриншоты сверены корректно"):
            pass

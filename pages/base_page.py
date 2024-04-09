import os

from utils.selenium_wrapper import SeleniumWrapper


class BasePage(SeleniumWrapper):
    UI_URL = "https://mega.readyscript.ru/"
    baseurl = os.environ.get("UI_URL", UI_URL)

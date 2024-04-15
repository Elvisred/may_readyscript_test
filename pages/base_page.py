import os

from utils.selenium_wrapper import SeleniumWrapper


class BasePage(SeleniumWrapper):
    UI_URL = "https://mega.readyscript.ru/"
    baseurl = os.environ.get("UI_URL", UI_URL)

    PACHO_URL = "https://mrpacho1.com/en/"
    pachobaseurl = os.environ.get("UI_URL", PACHO_URL)

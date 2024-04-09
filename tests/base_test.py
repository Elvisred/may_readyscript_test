import os


class BaseTest:
    UI_URL = "https://mega.readyscript.ru/"
    baseurl = os.environ.get("UI_URL", UI_URL)

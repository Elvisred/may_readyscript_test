import os


class BaseTest:
    UI_URL = "https://mega.readyscript.ru/"
    baseurl = os.environ.get("UI_URL", UI_URL)

    PACHO_URL = "https://mrpacho1.com/en/"
    pachourl = os.environ.get("PACHO_URL", PACHO_URL)

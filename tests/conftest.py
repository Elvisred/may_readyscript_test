import os
import random
import pytest
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SELENOID_URL = "http://127.0.0.1:4444/wd/hub"
url = os.environ.get("SELENOID_URL", SELENOID_URL)


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    driver.quit()


def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def random_number(length):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

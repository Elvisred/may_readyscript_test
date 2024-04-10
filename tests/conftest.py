import os
import random
import pytest
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.configuration import Configuration

SELENOID_URL = "http://127.0.0.1:4444/wd/hub"
url = os.environ.get("SELENOID_URL", SELENOID_URL)


def pytest_addoption(parser):
    parser.addoption(
        "--disable-headless",
        action="store_true",
        default=False,
        help="Start selenium in windowed mode"
    )


def pytest_configure(config):
    disable_headless = config.getoption("--disable-headless")
    Configuration.instance().is_headless_disabled = disable_headless


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1512,982")
    if not Configuration.instance().is_headless_disabled:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    driver.quit()


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

import sys
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC


class SeleniumWrapper:

    browser: WebDriver

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    TIME_OUT = 10
    STEP = 0.3

    @allure.step("Нажимаем на элемент {what}")
    def wait_and_click(self, how, what, timeout=TIME_OUT, step=STEP, attempts=3):
        attempt = 0
        while attempt < attempts:
            try:
                with allure.step(f"Попытка нажать на элемент {what}, попытка {attempt + 1}"):
                    element = WebDriverWait(self.browser, timeout, step).until(
                        EC.visibility_of_element_located((how, what)))
                    element.click()
                    time.sleep(2)
                    return
            except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                error_type = "Не удалось нажать на элемент" if isinstance(e,
                                                                          ElementClickInterceptedException) \
                    else "Устаревшая ссылка на элемент"
                with allure.step(f"{error_type} {what}, ошибка: {e}. Повтор через 2 секунды"):
                    allure.attach(str(e), name=f"Ошибка при попытке {attempt + 1}",
                                  attachment_type=allure.attachment_type.TEXT)
                    time.sleep(2)
                    attempt += 1
        with allure.step(f"Элемент {what} не был кликабелен после {attempts} попыток"):
            raise ElementClickInterceptedException(f"Элемент {what} не был кликабелен после {attempts} попыток.")

    @allure.step("Ожидаем что элемент {what} присутствует на странице")
    def wait_for_presence(self, how, what, timeout=TIME_OUT, step=STEP):
        try:
            return WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            raise AssertionError(f"Элемент {what} отсутствует на странице")

    @allure.step("Проверяем что элемент {what} присутствует на странице")
    def is_element_present(self, how, what, timeout=TIME_OUT, step=STEP):
        try:
            WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step("Открываем страницу {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Очищаем значение и вводим {value} в текущем поле {what}")
    def clear_and_set_value(self, how, what, value=None):
        actions = ActionChains(self.browser)
        self.wait_and_click(how, what)
        element = self.browser.find_element(how, what)

        control_key = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL

        actions.move_to_element(element).click().key_down(control_key).send_keys("a").key_up(control_key).send_keys(
            Keys.DELETE).perform()

        if value:
            self.browser.find_element(how, what).send_keys(value)

    @allure.step("Переводим курсор мыши на элемент {what}")
    def hover_to_element(self, how, what, timeout=TIME_OUT, step=STEP):
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located((how, what)))
        element = self.wait_for_presence(how, what)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    @allure.step("Переводим курсор на элемент {what} и нажимаем на него")
    def hover_and_click(self, how, what, timeout=TIME_OUT, step=STEP):
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located((how, what)))
        time.sleep(2)
        element = self.wait_for_presence(how, what)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).click().perform()

    @allure.step("Ввод текста: {text}")
    def enter_text(self, text):
        actions = ActionChains(self.browser)
        actions.send_keys(text)
        actions.perform()

    @allure.step("Нажимаем на TAB")
    def press_tab(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.TAB)
        actions.perform()

    @allure.step("Нажимаем на ENTER")
    def press_enter(self):
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    @allure.step("Скролл до элемента {what}")
    def scroll_to_element(self, how, what):
        try:
            self.wait_for_visibility(how, what)
            element = self.browser.find_element(how, what)
            self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(2)
        except TimeoutException as e:
            allure.attach(str(e), name="Ошибка скролла", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(f"Не удалось проскроллить до элемента {what}: {e}")

    @allure.step("Ожидаем, что элемент {what} будет виден")
    def wait_for_visibility(self, how, what, timeout=TIME_OUT, step=STEP):
        try:
            return WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutException(f"Элемент {what} не стал виден после {timeout} секунд.")

    @allure.step("Прокрутка страницы на {pixels} пикселей")
    def scroll_by_pixels(self, pixels):
        self.browser.execute_script(f"window.scrollBy(0, {pixels});")

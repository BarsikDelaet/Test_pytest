import os
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(driver=self.browser, timeout=10, poll_frequency=0.5)

    def find(self, selector_find):
        """ Поиск элемента. """
        by, value = selector_find
        return self.browser.find_element(by, value)

    def find_list(self, selector_find):
        """ Поиск списка элементов. """
        by, value = selector_find
        return self.browser.find_elements(by, value)

    def wait_displayed_element(self, selector, msg_error):
        """ Принимает селектор элемента и сообщение об ошибке.
        Ищете элемент, если не находит, выводит сообщение об ошибке.
        Возвращает элемент если он нашелся. """
        self.wait.until(lambda b: self.find(selector).is_displayed, message=msg_error)
        return self.find(selector)

    def wait_enabled_element(self, selector, msg_error):
        """ Принимает селектор элемента и сообщение об ошибке.
        Проверяет элемент на функциональность, если не находит, выводит сообщение об ошибке.
        Возвращает элемент если он нашелся. """
        self.wait.until(lambda b: self.find(selector).is_enabled, message=msg_error)
        return self.find(selector)

    def wait_element_invisibility(self, selector, msg_error):
        """ Проверяет что элемент больше не виден """
        self.wait.until(EC.invisibility_of_element_located(selector), message=msg_error)

    def wait_url_is_open(self, url, msg_error):
        """ Принимает проверяемый url и сообщение об ошибке.
        Если текущий url != url, возвращает сообщение об ошибке. """
        self.wait.until(lambda b: url in self.browser.current_url, message=msg_error)

    def wait_title_is_open(self, title, msg_error):
        """ Принимает проверяемый title и сообщение об ошибке.
        Если текущий title != title, возвращает сообщение об ошибке. """
        self.wait.until(lambda b: self.browser.title == title, message=msg_error)

    def move_to_element(self, elem):
        """ Принимает элемент.
        Наводит мышку по элементу. """
        ActionChains(self.browser).move_to_element(elem).perform()

    def wait_change_text_element(self, element, new_text, msg_error):
        """ Принимает элемент и старый текст.
        Проверяет смену текста в элементе. """
        self.wait.until(lambda d: element.text == new_text, message=msg_error)

    def check_file_download(self, file_name):
        """ Проверяет что файл скачан в папку с тестом. """
        download = False
        start_time = datetime.now().strftime('%S')
        now_time = start_time
        path = os.getcwd()
        while not download or start_time != now_time:
            if file_name in os.listdir(path):
                download = True
                return download
            time.sleep(1)
            now_time = datetime.now().strftime('%S')
        return download

import os
import glob
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(driver=self.browser, timeout=10, poll_frequency=0.5)

    def find(self, selector_find):
        by, value = selector_find
        return self.browser.find_element(by, value)

    def find_list(self, selector_find):
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

    def wait_url_is_open(self, url, msg_error):
        """ Принимает проверяемый url и сообщение об ошибке.
        Проверяет url, если он не открылся, возвращает сообщение об ошибке. """
        self.wait.until(lambda b: self.browser.current_url == url, message=msg_error)

    def move_to_element(self, elem):
        """ Принимает элемент.
        Наводит мышку по элементу. """
        ActionChains(self.browser).move_to_element(elem).perform()

    def check_change_text_element(self, element, old_text):
        self.wait.until(lambda d: element.text != old_text,
                        'Регион не поменялся')

    def check_file_download(self):
        """ Проверяет что файл скачан в папку с тестом. """
        download = False
        max_time = 10
        time_count = 0
        path = os.getcwd()
        while not download or max_time != time_count:
            if 'sbisplugin-setup-web.exe' in os.listdir(path):
                download = True
                return True
            time.sleep(1)
            time_count += 1
        return False

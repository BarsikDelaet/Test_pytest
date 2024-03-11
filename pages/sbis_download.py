import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class SbisDownloadPage(BasePage):

    url_download_page = 'https://sbis.ru/download?tab=ereport&innerTab=ereport25'
    sbis_plugin_button = (By.CSS_SELECTOR, '[data-id="plugin"] .controls-tabButton__overlay')
    download_button = (By.XPATH, '//*[text()="Веб-установщик "]/../..//a[@href]')

    name_plugin_file = 'sbisplugin-setup-web.exe'
    size_plugin_file = 8.17

    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)

    def choice_sbis_plugin(self):
        self.wait.until(EC.url_changes(self.url_download_page))
        time.sleep(1)
        self.find(self.sbis_plugin_button).click()

    def download_file(self):
        download_button = self.wait.until(EC.presence_of_element_located(self.download_button))
        size_file = download_button.text.split(' ')[-2]
        download_button.click()
        time.sleep(5)
        return size_file

    def check_file_downloads(self, size_file):
        assert os.path.isfile(self.name_plugin_file), 'Плагин не скачался'

        file_size = round(os.path.getsize(self.name_plugin_file) / 1024**2, 2)
        assert file_size == size_file, 'Размер файлов не совпадает'





import os
import time

from selenium.webdriver.common.by import By
from pages.base import BasePage


class SbisDownloadPage(BasePage):
    """ Все взаимодействия и локаторы страницы https://sbis.ru/download """

    url_download_page = 'https://sbis.ru/download?tab=ereport&innerTab=ereport25'
    sbis_plugin_button = (By.CSS_SELECTOR, '[data-id="plugin"] .controls-tabButton__overlay')
    download_button = (By.CSS_SELECTOR,
                       'div[data-for="plugin"] div.sbis_ru-DownloadNew-block.sbis_ru-DownloadNew-flex a')
    name_plugin_file = 'sbisplugin-setup-web.exe'

    def __init__(self, browser):
        super().__init__(browser)

    def check_sbis_download(self):
        """ Проверяем что перешли на нужную страницу """
        self.wait_url_is_open(self.url_download_page,
                              'Переход на страницу "Скачать" не произошел')

    def choice_sbis_plugin(self):
        """ Находим кнопку "СБИС Плагины", нажимаем на неё. """
        sbis_plugin_button = self.wait_displayed_element(self.sbis_plugin_button,
                                                         'Кнопка "СБИС Плагины не найдена"')
        self.move_to_element(sbis_plugin_button)
        sbis_plugin_button.click()

    def download_file(self):
        """ Ищем кнопку Скачать(Веб-установщик) и нажимаем на неё.
        Сохраняем размер указанный на сайте и возвращаем его.
        Проверяем что файл докачался."""
        download_button = self.wait_displayed_element(self.download_button,
                                                      'Кнопка "Скачать" не нашлась')
        size_file = float(download_button.text.split(' ')[-2])
        file_list = os.listdir(os.getcwd())
        download_button.click()
        self.check_file_download(file_list)
        return size_file

    def check_file_size(self, size_file):
        """ Проверят размер скаченного фала. """
        download_size_file = round(os.path.getsize(self.name_plugin_file) / 1024**2, 2)
        assert download_size_file == size_file, 'Размер файлов не совпадает'

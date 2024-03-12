import os

from selenium.webdriver.common.by import By
from loguru import logger

from pages.base import BasePage


class SbisDownloadPage(BasePage):
    """ Все взаимодействия и локаторы страницы https://sbis.ru/download """

    url_download_page = 'https://sbis.ru/download?tab=ereport&innerTab=ereport25'
    sbis_plugin_button = (By.CSS_SELECTOR, '[data-id="plugin"] .controls-tabButton__overlay')
    download_button = (By.CSS_SELECTOR,
                       'div[data-for="plugin"] div.sbis_ru-DownloadNew-block.sbis_ru-DownloadNew-flex a')

    def __init__(self, browser):
        super().__init__(browser)

    def check_sbis_download(self):
        """ Проверяет что перешли на нужную страницу """
        self.wait_url_is_open(self.url_download_page,
                              'Переход на страницу "Скачать" не произошел')
        logger.info("Раздел \"Скачать\" открылся")

    def choice_sbis_plugin(self):
        """ Находим кнопку "СБИС Плагины", нажимаем на неё. """
        sbis_plugin_button = self.wait_displayed_element(self.sbis_plugin_button,
                                                         'Кнопка "СБИС Плагины не найдена"')
        logger.info("Кнопка \"СБИС Плагины\" найдена")
        self.move_to_element(sbis_plugin_button)
        sbis_plugin_button.click()
        logger.info("Передвинули курсор на кнопку \"СБИС Плагины\" и нажали")

    def download_file(self, name_plugin_file):
        """ Ищем кнопку Скачать(Веб-установщик) и нажимаем на неё.
        Сохраняем размер указанный на сайте и возвращаем его.
        Проверяет что файл докачался."""
        download_button = self.wait_displayed_element(self.download_button,
                                                      'Кнопка "Скачать" не нашлась')
        logger.info("Кнопка \"Скачать\" найдена")
        size_file = float(download_button.text.split(' ')[-2])
        logger.info(f"Вязи размер файла {size_file}")
        download_button.click()
        logger.info("Кликнули по кнопке \"Скачать\"")
        assert self.check_file_download(name_plugin_file), 'Файл не скачался'
        logger.info("Файл скачался")
        return size_file

    def check_file_size(self, size_file, name_plugin_file):
        """ Проверят размер скаченного фала. """
        download_size_file = round(os.path.getsize(name_plugin_file) / 1024**2, 2)
        assert download_size_file == size_file, f'Размер файлов не совпадает {download_size_file} != {size_file}'
        logger.info("Файлы равны по размеру")

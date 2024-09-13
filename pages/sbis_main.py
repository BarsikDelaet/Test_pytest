from selenium.webdriver.common.by import By
from loguru import logger

from pages.base import BasePage


class SbisMainPage(BasePage):
    """ Все взаимодействия и локаторы страницу https://Sbis.ru """

    contact_button = (By.LINK_TEXT, 'Контакты')

    sbis_footer = (By.CLASS_NAME, 'sbisru-Footer')
    sbis_download = (By.LINK_TEXT, 'Скачать локальные версии')

    def __init__(self, browser):
        super().__init__(browser)

    def open_contact(self):
        """ Находит и нажимает кнопку Контакты. """
        contact_button = self.wait_displayed_element(self.contact_button,
                                                     'Кнопка "Контакты" не найдена')
        logger.info("Кнопка Контакты найдена")

        self.move_to_element(contact_button)
        contact_button.click()

        logger.info("Нажали на кнопку Контакты")
 
    def open_sbis_download(self):
        """ Находит раздел Footer, спускается до него.
        Ищет кнопку "Скачать локальные версии" и нажимает. """
        sbis_footer = self.wait_displayed_element(self.sbis_footer, 'Раздел "Footer" не обнаружился')
        self.browser.execute_script("arguments[0].scrollIntoView();", sbis_footer)

        logger.info("Раздел Footer найден, передвинулись к нему.")

        sbis_download = (self.wait_enabled_element(self.sbis_download,
                                                   'Кнопка "Скачать локальные версии" не найдена'))
        logger.info("Кнопка скачать найдена.")
        sbis_download.click()
        logger.info("Кликнули по кнопке скачать.")

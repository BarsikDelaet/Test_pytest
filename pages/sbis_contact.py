import time

from selenium.webdriver.common.by import By
from loguru import logger

from pages.base import BasePage


class SbisContactsPage(BasePage):
    """ Все взаимодействия и локаторы страницы https://Sbis.ru/contacts """

    url_sbis_contacts = "https://sbis.ru/contacts"
    banner_tensor = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')

    region_chooser = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')
    partners_list = (By.CSS_SELECTOR, 'div.sbisru-Contacts-List__col-1 div[title]')
    window_choice_region = (By.CLASS_NAME, 'sbis_ru-Region-Panel.sbis_ru-Region-Panel-l')
    desired_region = (By.CSS_SELECTOR, '[title="Камчатский край"].sbis_ru-link')

    def __init__(self, browser):
        super().__init__(browser)

    def check_sbis_contacts(self):
        """ Проверяет что раздел Sbis.ru/contacts открылся. """
        self.wait_url_is_open(self.url_sbis_contacts, 'Сбис раздел "Контакты" не открылся')

        logger.info("Раздел Контакты открылся.")

    def search_banner_tensor_and_click(self):
        """ Поиск банера Тензор и нажатие на него.
        Возвращаем последнее открывшуюся вкладку. """
        banner_tensor = self.wait_displayed_element(self.banner_tensor,
                                                    'Банер "Тензор" не найден')
        logger.info("Банер Тензор найден")

        banner_tensor.click()

        logger.info("Кликнули по банеру Тензор")

        return self.browser.window_handles[-1]

    def switch_to_tensor(self, window):
        """ Переход на новую вкладку Тензор. """
        self.browser.switch_to.window(window)

        logger.info("Перешли на открывшуюся вкладку Тензор")

    def check_home_region(self, your_region):
        """ Проверяет определившейся регион. """
        current_region = self.wait_displayed_element(self.region_chooser,
                                                     'Кнопка текущего региона не найдена').text

        logger.info("Кнопка региона найдена")

        assert current_region == your_region, f'Определился неверный регион {current_region}'

        logger.info(f"Регион определился верно, {current_region}")

    def check_list_partners(self):
        """ Проверяет наличие раздела списков партнеров. """
        partner = self.wait_displayed_element(self.partners_list,
                                              'Список партнеров не найде')
        logger.info("Список партнеров найден")
        return partner.get_attribute('title')

    def open_window_choice_region(self):
        """ Открывает окно выбора регионов. """
        region_chooser = self.wait_enabled_element(self.region_chooser,
                                                   'Кнопка выбора регионов не найдена')

        logger.info("Кнопка региона найдена")

        region_chooser.click()

        logger.info("Кликнули по кнопке региона")

        self.wait_displayed_element(self.window_choice_region,
                                    'Окно выбора региона не открылось')

        logger.info("Открылось окно выбора регионов")

    def choice_other_region(self):
        """ Находит кнопку нужного региона и переключает на него.  """
        desired_region = self.wait_enabled_element(self.desired_region,
                                                   'Кнопка "Камчатский край" не найдена')

        logger.info("Кнопка нужного региона найдена")

        self.move_to_element(desired_region)

        desired_region.click()

        logger.info("Передвинули на неё курсор и кликнули")

        self.wait_element_invisibility(self.window_choice_region, 'Окно не закрылось')

        logger.info("Дождались закрытия окна")

    def check_new_region(self, new_region):
        """ Проверят что регион поменялся на новый. """
        self.wait_displayed_element(self.region_chooser,
                                    'Регион не виден')

        logger.info("Кнопка региона найдена")

        current_region = self.find(self.region_chooser)

        self.wait_change_text_element(current_region, new_region, 'Регион не поменялся')

        logger.info("Регион поменялся на нужный")

    def check_new_partners_list(self, old_partners):
        """ Проверяет наличия списка партнеров """
        new_partners = self.wait_displayed_element(self.partners_list,
                                                   'Список партнеров не найден')
        logger.info("Список партнеров найден")

        new_partners = new_partners.get_attribute('title')
        logger.info(f'Новый список партнеров {new_partners}')

        assert old_partners != new_partners, 'Список партнеров не поменялся'

        logger.info(f"Список партнеров поменялся на {new_partners}")

    def check_url_title(self, new_url, new_title_text):
        """ Проверят url и title на соответствующий выбранному региону """
        self.wait_url_is_open(new_url,
                              'Url не поменялся на предполагаемый')
        logger.info(f"Url поменялся на {new_url}")

        self.wait_title_is_open(new_title_text,
                                'Title не поменялся на предполагаемый')
        logger.info(f"Title поменялся на {new_title_text}")

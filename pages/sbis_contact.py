import time

from selenium.webdriver.common.by import By

from pages.base import BasePage


class SbisContactsPage(BasePage):
    """ Все взаимодействия и локаторы страницы https://Sbis.ru/contacts """

    url_sbis_contacts = "https://sbis.ru/contacts"
    banner_tensor = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')

    region_chooser = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')
    partners_list = (By.NAME, 'itemsContainer')
    window_choice_region = (By.NAME, 'dialog')
    desired_region = (By.CSS_SELECTOR, '[title="Камчатский край"].sbis_ru-link')
    new_partners_list = (By.XPATH, '//*[@name="itemsContainer"]//*[@title="СБИС - Камчатка"]')

    your_region = 'Ярославская обл.'
    new_region = 'Камчатский край'
    new_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    new_title_text = 'СБИС Контакты — Камчатский край'

    def __init__(self, browser):
        super().__init__(browser)

    def check_sbis_contacts(self):
        """ Проверяет что раздел Sbis.ru/contacts открылся. """
        self.wait_url_is_open(self.url_sbis_contacts, 'Сбис раздел "Контакты" не открылся')

    def search_banner_tensor_and_click(self):
        """ Поиск банера Тензор и нажатие на него.
        Возвращаем последнее открывшуюся вкладку. """
        banner_tensor = self.wait_enabled_element(self.banner_tensor, 'Банер "Тензор" не найден')
        banner_tensor.click()

        return self.browser.window_handles[-1]

    def switch_to_tensor(self, window):
        """ Переход на новую вкладку Тензор. """
        self.browser.switch_to.window(window)

    def check_home_region(self):
        """ Проверяем определившейся регион. """
        current_region = self.wait_displayed_element(self.region_chooser,
                                                     'Кнопка текущего региона не найдена').text
        assert current_region == self.your_region, 'Определился неверный регион'

    def check_list_partners(self):
        """ Проверяет наличие раздела списков партнеров. """
        self.wait_displayed_element(self.partners_list,
                                    'Список партнеров не найде')

    def open_window_choice_region(self):
        """ Открывает окно выбора регионов. """
        self.find(self.region_chooser).click()
        window_choice_region = self.find(self.window_choice_region)
        assert window_choice_region.is_displayed(), 'Окно выбора региона не открылось'

    def choice_other_region(self):
        """ Находит кнопку нужного региона и переключает на него.  """
        desired_region = self.wait_enabled_element(self.desired_region,
                                                   'Кнопка "Камчатский край" не найдена')
        self.move_to_element(desired_region)
        desired_region.click()

    def check_new_region(self):
        """ Проверят что регион поменялся на новый. """
        self.wait_displayed_element(self.region_chooser, 'Регион не виден')
        current_region = self.find(self.region_chooser)
        self.check_change_text_element(current_region, self.your_region)

    def check_new_partners_list(self):
        """ Проверка наличия списка партнеров """
        assert self.find(self.new_partners_list).is_displayed(), 'Список партнеров не поменялся'

    def check_url_title(self):
        """ Проверка url и title на соответствующий выбранному региону """
        assert self.browser.current_url == self.new_url, 'Url не поменялся на предполагаемый'
        assert self.browser.title == self.new_title_text, 'Title не поменялся на предполагаемый'

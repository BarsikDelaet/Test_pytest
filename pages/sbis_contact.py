import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class SbisContactsPage(BasePage):

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
    # desired_region = (By.XPATH, '//*[contains(text(), "41 Камчатский край")]/..')



    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)

    def check_sbis_contacts(self):
        self.wait.until(EC.url_changes(self.url_sbis_contacts))
        assert self.url_sbis_contacts in self.browser.current_url, 'Сбис раздел "Контакты" не открылся'

    def search_banner_tensor_and_click(self):
        banner_tensor = self.find(self.banner_tensor)
        assert banner_tensor.is_displayed(), 'Банер "Тензор" не найден'
        banner_tensor.click()
        return self.browser.window_handles[-1]

    def switch_to_tensor(self, window):
        self.browser.switch_to.window(window)

    def check_home_region(self):
        current_region = self.find(self.region_chooser).text
        assert current_region == self.your_region, 'Определился неверный регион'

    def check_list_partners(self):
        assert self.find(self.partners_list).is_displayed, 'Список партнеров не найде'

    def open_window_choice_region(self):
        self.find(self.region_chooser).click()
        window_choice_region = self.find(self.window_choice_region)
        assert window_choice_region.is_displayed(), 'Окно выбора региона не открылось'

    def choice_other_region(self):
        desired_region = self.find(self.desired_region)
        assert desired_region.is_displayed(), 'Кнопка "Камчатский край" не найдена'
        time.sleep(1)
        desired_region.click()
        time.sleep(1)

    def check_new_region(self):
        current_region = self.find(self.region_chooser).text
        assert current_region == self.new_region, f'Определился неверный регион'

    def check_new_partners_list(self):
        assert self.find(self.new_partners_list).is_displayed(), 'Список партнеров не поменялся'

    def check_url_title(self):
        assert self.browser.current_url == self.new_url, 'Url не поменялся предполагаемый'
        assert self.browser.title == self.new_title_text, f'Title не поменялся на предполагаемый, {self.browser.title}'


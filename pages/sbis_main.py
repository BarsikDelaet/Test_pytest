import time
from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisMainPage(BasePage):

    contact_button = (By.LINK_TEXT, 'Контакты')

    sbis_footer = (By.CLASS_NAME, 'sbisru-Footer')
    sbis_download = (By.LINK_TEXT, 'Скачать локальные версии')

    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)

    def open_contact(self):
        self.wait.until(EC.visibility_of_element_located(self.contact_button)).click()

    def open_sbis_download(self):
        sbis_footer = self.wait.until(EC.presence_of_element_located(self.sbis_footer))
        self.browser.execute_script("arguments[0].scrollIntoView();", sbis_footer)

        self.wait.until(EC.element_to_be_clickable(self.sbis_download)).click()

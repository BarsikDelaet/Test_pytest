from selenium.webdriver.common.by import By

from pages.base import BasePage


class TensorPage(BasePage):
    """ Все взаимодействия и селекторы страницы https://Tensor.ru """

    tensor_url = "https://tensor.ru/"
    block_power_in_people = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
    about_button = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content a')
    
    def __init__(self, browser):
        super().__init__(browser)

    def check_link_tensor(self):
        """ Проверяет переход на страницу Тензор """
        self.wait_url_is_open(self.browser.current_url, 'Страница Тензор не открыта')

    def check_block_power_in_people(self):
        """ Проверяет наличия блока "Сила в людях".
        Скрол до этого блока."""
        block_power_in_people = self.wait_displayed_element(self.block_power_in_people,
                                                            'Блок "Сила в людях" не найден')
        self.browser.execute_script("arguments[0].scrollIntoView();", block_power_in_people)

    def open_tensor_about(self):
        """ Поиск кнопки "Подробнее" блока "Сила в людях" и нажатие по ней. """
        button_about = self.wait_enabled_element(self.about_button,
                                                 'Кнопка "Подробнее" не найдена')
        button_about.click()



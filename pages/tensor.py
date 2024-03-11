from pages.base import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    
    tensor_url = "https://tensor.ru/"
    block_power_in_people = (By.CLASS_NAME, 'tensor_ru-Index__block4-content')
    about_button = (By.CSS_SELECTOR, 'a.tensor_ru-Index__link.tensor_ru-link')
    
    def __init__(self, browser):
        super().__init__(browser)

    def check_link_tensor(self):
        current_page = self.browser.current_url
        assert self.tensor_url == current_page, 'Страница Тензор не открыта'

    def check_block_power_in_people(self):
        block_power_in_people = self.find(self.block_power_in_people)
        assert block_power_in_people.is_displayed(), f'Блок "Сила в людях" не найден, {block_power_in_people}'

    def open_tensor_about(self):
        button_about = self.find_list(self.about_button)[1]
        assert button_about.is_displayed(), 'Кнопка "Подробнее" не найдена'
        self.browser.execute_script("arguments[0].scrollIntoView();", button_about)
        button_about.click()



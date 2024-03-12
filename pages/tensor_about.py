from selenium.webdriver.common.by import By

from pages.base import BasePage


class TensorAboutPage(BasePage):
    """ Все взаимодействия и селекторы страницы https://Tensor.ru/about """

    tensor_about_url = "https://tensor.ru/about"
    block_working = (By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    img_in_block_working = (By.CLASS_NAME, 'tensor_ru-About__block3-image.new_lazy.loaded')

    def __init__(self, browser):
        super().__init__(browser)

    def check_tensor_about(self):
        """ Проверят открытие страницы "https://tensor.ru/about" """
        self.wait_url_is_open(self.tensor_about_url,
                              'Раздел Тензор "О компании" не открылся')

    def check_block_working(self):
        """ Проверка наличия блока "Работаем"
        Скрол до него. """
        block_working = self.wait_displayed_element(self.block_working,
                                                    'Блок "Работаем" не найден')
        self.browser.execute_script("arguments[0].scrollIntoView();", block_working)

    def check_size_photo(self):
        """ Проверка размерности фото раздела "Работаем"
        Ищем первое фото и берем его размеры.
        Поочередно сравниваем с другими фото."""
        self.wait_displayed_element(self.img_in_block_working,
                                    'Фото раздела "Работаем" не найдены')
        img_elements = self.find_list(self.img_in_block_working)
        size_img = img_elements[0].get_attribute('height'), img_elements[0].get_attribute('width')
        for img in img_elements:
            assert size_img == (img.get_attribute('height'), img.get_attribute('width')), \
                'Размеры фотографий не совпадают'

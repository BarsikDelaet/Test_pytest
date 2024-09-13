from selenium.webdriver.common.by import By
from loguru import logger

from pages.base import BasePage


class TensorAboutPage(BasePage):
    """ Все взаимодействия и селекторы страницы https://Tensor.ru/about """

    tensor_about_url = "https://tensor.ru/about"
    block_working = (By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    img_in_block_working = (By.CLASS_NAME, 'tensor_ru-About__block3-image.new_lazy.loaded')

    def __init__(self, browser):
        super().__init__(browser)

    def check_tensor_about(self):
        """ Проверяет открытие страницы "https://tensor.ru/about" """
        self.wait_url_is_open(self.tensor_about_url,
                              'Раздел Тензор "О компании" не открылся')

        logger.info("Раздел \"О компании\" открылся")

    def check_block_working(self):
        """ Проверяет наличия блока "Работаем"
        Скрол до него. """
        block_working = self.wait_displayed_element(self.block_working,
                                                    'Блок "Работаем" не найден')

        logger.info("Блок \"Работаем\" открылся")

        self.browser.execute_script("arguments[0].scrollIntoView();", block_working)

        logger.info("Передвинулись к \"Работаем\"")

    def check_size_photo(self):
        """ Проверяет размерности фото раздела "Работаем"
        Ищем первое фото и берем его размеры.
        Поочередно сравниваем с другими фото."""
        self.wait_displayed_element(self.img_in_block_working,
                                    'Фото блока "Работаем" не найдены')

        logger.info("Фото блока \"Работаем\" найдены")

        img_elements = self.find_list(self.img_in_block_working)
        size_img = img_elements[0].get_attribute('height'), img_elements[0].get_attribute('width')

        logger.info(f"Взяли размеры первой фотографии h:{size_img[0]} w:{size_img[1]}")

        for img in img_elements[1:]:
            assert size_img == (img.get_attribute('height'), img.get_attribute('width')), \
                'Размеры фотографий не совпадают'
        logger.info("Размеры фотографий совпадают")

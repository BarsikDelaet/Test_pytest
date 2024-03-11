from pages.base import BasePage
from selenium.webdriver.common.by import By


class TensorAboutPage(BasePage):

    tensor_about_url = "https://tensor.ru/about"
    block_working = (By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    img_block_working = (By.CLASS_NAME, 'tensor_ru-About__block3-image.new_lazy.loaded')

    def __init__(self, browser):
        super().__init__(browser)

    def check_tensor_about(self):
        assert self.browser.current_url == self.tensor_about_url, 'Раздел Тензор "О компании" не открылся'

    def check_block_working(self):
        block_working = self.find(self.block_working)
        assert block_working.is_displayed(), 'Блок "Работаем" не найден'
        self.browser.execute_script("arguments[0].scrollIntoView();", block_working)

    def check_size_photo(self):
        img_elements = self.find_list(self.img_block_working)
        size_img = img_elements[0].get_attribute('height'), img_elements[0].get_attribute('width')
        for img in img_elements:
            assert size_img == (img.get_attribute('height'), img.get_attribute('width')), \
                "Размеры фотографий не совпадают"

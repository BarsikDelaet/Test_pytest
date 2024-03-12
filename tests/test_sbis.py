from loguru import logger

from pages.tensor import TensorPage
from pages.sbis_main import SbisMainPage
from pages.tensor_about import TensorAboutPage
from pages.sbis_contact import SbisContactsPage
from pages.sbis_download import SbisDownloadPage


def test_01(browser):

    logger.info("_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.\nЗапуск теста 01")

    sbis_main = SbisMainPage(browser)

    # Зайти на Sbis.ru/contacts.
    sbis_main.open_contact()

    sbis_contact = SbisContactsPage(browser)
    sbis_contact.check_sbis_contacts()

    # Найти банер тензор и кликнуть по нему
    next_window = sbis_contact.search_banner_tensor_and_click()

    # Переход на открывшееся окно
    sbis_contact.switch_to_tensor(window=next_window)

    tensor = TensorPage(browser)

    # Проверить страницу.
    tensor.check_link_tensor()

    # Проверить наличие блока "Сила в людях"
    tensor.check_block_power_in_people()

    # Перейти в этом блоке в "Подробнее"
    tensor.open_tensor_about()

    tensor_about = TensorAboutPage(browser)

    # Проверить что открывается 'https://tensor.ru/about'
    tensor_about.check_tensor_about()

    # Проверить наличие блока "Работаем"
    tensor_about.check_block_working()

    # Поверить размерность фото в разделе "Работаем"
    tensor_about.check_size_photo()


def test_02(browser):

    logger.info("_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.\nЗапуск теста 02")

    your_region = 'Ярославская обл.'
    new_region = 'Камчатский край'

    new_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    new_title_text = 'СБИС Контакты — Камчатский край'

    sbis_main = SbisMainPage(browser)
    # Зайти на Sbis.ru/contacts.
    sbis_main.open_contact()

    sbis_contact = SbisContactsPage(browser)
    sbis_contact.check_sbis_contacts()

    # Проверить регион определения
    sbis_contact.check_home_region(your_region)

    # Проверить наличие списка партнеров
    old_partners = sbis_contact.check_list_partners()

    # Изменить регион на Камчатский край
    sbis_contact.open_window_choice_region()
    sbis_contact.choice_other_region()

    # Проверить что подставился верный регион
    sbis_contact.check_new_region(new_region)

    # Список партнеров изменился
    sbis_contact.check_new_partners_list(old_partners)

    # Изменился url и title
    sbis_contact.check_url_title(new_url, new_title_text)


def test_03(browser):

    logger.info("_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.\nЗапуск теста 03")

    name_plugin_file = 'sbisplugin-setup-web.exe'

    # Зайти на Sbis.ru
    sbis_main = SbisMainPage(browser)

    # Найти и перейти "Скачать СБИС" *Скачать локальные версии*
    sbis_main.open_sbis_download()

    sbis_download = SbisDownloadPage(browser)

    # Проверить переход на страницу "Скачать"
    sbis_download.check_sbis_download()

    # Открыть раздел "СБИС Плагины"
    sbis_download.choice_sbis_plugin()

    # Скачать СБИС для Windows в папку с тестом и проверяем что он скачался
    size_file = sbis_download.download_file(name_plugin_file)

    # Сравнить размер скаченного файла с указанным на сайте
    sbis_download.check_file_size(size_file, name_plugin_file)

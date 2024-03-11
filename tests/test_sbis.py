from pages.tensor import TensorPage
from pages.sbis_main import SbisMainPage
from pages.tensor_about import TensorAboutPage
from pages.sbis_contact import SbisContactsPage
from pages.sbis_download import SbisDownloadPage


def test_01(browser):

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

    sbis_main = SbisMainPage(browser)
    # Зайти на Sbis.ru/contacts.
    sbis_main.open_contact()

    sbis_contact = SbisContactsPage(browser)
    sbis_contact.check_sbis_contacts()

    # Проверить регион определения
    # sbis_contact.check_home_region()

    # Проверить наличие списка партнеров
    sbis_contact.check_list_partners()

    # Изменить регион на Камчатский край
    sbis_contact.open_window_choice_region()
    sbis_contact.choice_other_region()

    # Проверить что подставился верный регион
    sbis_contact.check_new_region()

    # Список партнеров изменился
    sbis_contact.check_new_partners_list()

    # Изменился url и title
    sbis_contact.check_url_title()


def test_03(browser):

    # Зайти на Sbis.ru
    sbis_main = SbisMainPage(browser)

    # Найти и перейти "Скачать СБИС" *Скачать локальные версии*
    sbis_main.open_sbis_download()

    sbis_download = SbisDownloadPage(browser)

    # Открыть раздел "СБИС Плагины"
    sbis_download.choice_sbis_plugin()

    # Скачать СБИС для Windows в папку с тестом
    sbis_download.download_file()

    # Проверить что плагин скачался

    # Сравнить размер скаченного файла с указанным на сайте
    sbis_download.check_file_downloads()

import os

from selenium import webdriver
from loguru import logger
import pytest


@pytest.fixture()
def browser():
    # SetUp
    logger.add("info_logging.log",
               format="{time:DD-MM-YYYY HH:mm:ss}| {level: <5} | {name}:{function}: {line} - {message}")
    options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': f'{os.getcwd()}',
        'safebrowsing.enabled': True
    }  #
    options.add_experimental_option("prefs", prefs)

    sbis_url = 'https://sbis.ru/'

    chrom_browser = webdriver.Chrome(options=options)
    chrom_browser.maximize_window()
    chrom_browser.implicitly_wait(10)
    logger.info("Тест запускается")
    chrom_browser.get(sbis_url)

    yield chrom_browser
    # for window in chrom_browser.window_handles:
    #     chrom_browser.switch_to.window(window)
    #     chrom_browser.close()
    chrom_browser.quit()

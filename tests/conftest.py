import os

from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    # SetUp
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

    chrom_browser.get(sbis_url)

    yield chrom_browser
    for window in chrom_browser.window_handles:
        chrom_browser.switch_to.window(window)
        chrom_browser.close()
    chrom_browser.quit()

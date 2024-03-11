class BasePage(object):
    def __init__(self, browser):
        self.browser = browser

    def find(self, selector_find):
        by, value = selector_find
        return self.browser.find_element(by, value)

    def find_list(self, selector_find):
        by, value = selector_find
        return self.browser.find_elements(by, value)

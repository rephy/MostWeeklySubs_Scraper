from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

class ChromeDriver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=options)

    def cooldown(self, secs):
        sleep(secs)

    def get(self, link):
        self.driver.get(link)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def find_XPATH(self, XPATH):
        element = self.driver.find_element(By.XPATH, XPATH)
        return element

    def extract_text_XPATH(self, XPATH):
        element = self.find_XPATH(XPATH)
        return element.text

    def input_XPATH(self, XPATH, *args):
        element = self.find_XPATH(XPATH)
        for arg in args:
            element.send_keys(*arg)

    def click_XPATH(self, XPATH):
        element = self.find_XPATH(XPATH)
        element.click()

    def find_selector(self, selector):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element

    def finds_selector(self, selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return elements

    def extract_text_selector(self, selector):
        element = self.find_selector(selector)
        return element.text

    def input_selector(self, selector, *args):
        element = self.find_selector(selector)
        for arg in args:
            element.send_keys(*arg)

    def click_selector(self, selector):
        element = self.find_selector(selector)
        element.click()

    def click_element(self, element):
        element.click()

    def input_element(self, element, *args):
        for arg in args:
            element.send_keys(arg)

    def extract_text_element(self, element):
        return element.text

    def quit(self):
        self.driver.quit()

    def current_url(self):
        return self.driver.current_url
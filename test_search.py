from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def test_search(self):
        search_request = 'Навушники'
        url = 'https://www.olx.ua/uk/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[id="headerSearch"]').send_keys(search_request)
        browser.find_element_by_css_selector('[id="headerSearch"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="inline selected"]').text

        expectedResult = "Навушники"

        assert expectedResult in actualResult
        browser.close()

        search_request = 'Audi A6'
        url = 'https://www.olx.ua/uk/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[id="headerSearch"]').send_keys(search_request)
        browser.find_element_by_css_selector('[id="headerSearch"]').send_keys(Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="inline selected"]').text

        expectedResult = "Audi A6"

        assert expectedResult in actualResult

        browser.close()

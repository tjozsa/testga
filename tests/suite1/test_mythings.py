from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultPage

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    # driver = Chrome()
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver
    driver.close()


def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()

    time.sleep(3)

    search_page.search(PHRASE)
    time.sleep(3)

    result_page = DuckDuckGoResultPage(browser)

    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE

def test_basic_duckduckgo_search1(browser):
    PHRASE = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()

    time.sleep(3)

    search_page.search(PHRASE)
    time.sleep(3)

    result_page = DuckDuckGoResultPage(browser)

    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE

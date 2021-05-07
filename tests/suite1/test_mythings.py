from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import Chrome, ChromeOptions
import time
from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultPage


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    options = ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = Chrome(options)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    return driver


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


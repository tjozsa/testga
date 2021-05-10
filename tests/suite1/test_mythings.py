from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import Chrome, ChromeOptions, Remote, DesiredCapabilities
import time
from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultPage


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # driver = Chrome(options=options)
    # Create a desired capabilities object as a starting point.
    capabilities = DesiredCapabilities.FIREFOX.copy()

    driver = Remote('http://hub:4444/wd/hub', desired_capabilities=capabilities)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    return driver

@pytest.fixture
def browser2():
    # Initialize ChromeDriver
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # driver = Chrome(options=options)
    # Create a desired capabilities object as a starting point.
    capabilities = DesiredCapabilities.CHROME.copy()

    driver = Remote('http://hub:4444/wd/hub', desired_capabilities=capabilities)
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    return driver

  
def basic_duckduckgo_search(browser):
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

def test_chrome_basic_duckduckgo_search(browser2):
    basic_duckduckgo_search(browser2)

def test_ffox_basic_duckduckgo_search(browser):
    basic_duckduckgo_search(browser)
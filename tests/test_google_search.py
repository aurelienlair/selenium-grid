import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope='module')
def setup(request):
    # Check if the BROWSER environment variable is present and use it if available
    browser = os.environ.get("BROWSER")
    if browser:
        browser = browser.lower()
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # Set additional Chrome options if needed
            driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
                                      options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            # Set additional Firefox options if needed
            driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
                                      options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    else:
        # If BROWSER environment variable not set, use local Firefox WebDriver
        driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    driver.maximize_window()

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver


def test_google_search(setup):
    driver = setup
    driver.get('https://www.google.co.uk/?hl=en')

    try:
        driver.find_element(
            By.XPATH, "//div[normalize-space()='Reject all']").click()
        print("Cookie banner found!")
    except NoSuchElementException:
        print("Cookie banner not found.")

    search_box = driver.find_element(by=By.NAME, value='q')
    search_box.send_keys('Automation step by step')
    search_box.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is("Automation step by step - Google Search"))

    # Collect and print the search results
    search_results = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']")
    print(f"Collected {len(search_results)} items:")
    for result in search_results:
        print(result.text)

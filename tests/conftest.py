import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but received {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute test (chrome/firefox)"
    )

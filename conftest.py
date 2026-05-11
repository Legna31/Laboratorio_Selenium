import os
import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")
        
        if driver is not None:
            screenshot = driver.get_screenshot_as_base64()

            html = f'''
            <div>
                <img src="data:image/png;base64,{screenshot}"
                style="width:400px;height:250px;"
                onclick="window.open(this.src)"
                align="right"/>
            </div>
            '''

            extras.append(pytest_html.extras.html(html))

    report.extras = extras


@pytest.fixture
def driver(request):

    options = Options()

    headless_option = request.config.getoption("--headless")
    headless_env = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
    if headless_option or headless_env:
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    yield driver

    driver.quit()
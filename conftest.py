import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import datetime
import os
import allure

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'headlessfirefox':
        ff_options = FFOptions()
        ff_options.add_argument("--disable-gpu")
        ff_options.add_argument("--no-sandbox")
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(options=ff_options)

    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()

# Hook that takes a screenshot of the web browser for failed tests and adds it to the HTML report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
   pytest_html = item.config.pluginmanager.getplugin('html')
   outcome = yield
   report = outcome.get_result()
   extra = getattr(report, 'extra', [])
   if report.when == 'call':
        #always add url to report
       extra.append(pytest_html.extras.url(f'http://localhost:63342/tests/{item}'))
       xfail = hasattr(report, 'wasxfail')
       if (report.skipped and xfail) or (report.failed and not xfail):
           # only add additional html on failure
           is_frontend_test = True if 'init_driver' in item.fixturenames else False
           # if is_frontend_test:
           #     results_dir = os.environ.get("RESULTS_DIR")
           #     if not results_dir:
           #         raise Exception("Environment variable 'RESULTS_DIR' must be set.")
           #
           #     screen_shot_path = os.path.join(results_dir, item.name + '.png')
           #     driver_fixture = item.funcargs['request']
           #     driver_fixture.cls.driver.save_screenshot(screen_shot_path)
           #     # only add additional html on failure
           #     # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
           extra.append(pytest_html.extras.image("/home/yevhenk/tests/registration_COM_confirm_EN_2023-03-21 10:33:18.900899.png"))
           #     allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
           #                   name='screenshot',
           #                   attachment_type=allure.attachment_type.PNG)
       report.extra = extra

### FOR: generating only pytest-html report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#    pytest_html = item.config.pluginmanager.getplugin("html")
#    outcome = yield
#    report = outcome.get_result()
#    extra = getattr(report, 'extra', [])
#    if report.when == "call":
#        # always add url to report
#        extra.append(pytest_html.extras.url(f'http://localhost:63342/tests/{item}'))
#        xfail = hasattr(report, "wasxfail")
#        # check if test failed
#        if (report.skipped and xfail) or (report.failed and not xfail):
#            is_frontend_test = True if 'init_driver' in item.fixturenames else False
#            if is_frontend_test:
#                results_dir = os.environ.get("RESULTS_DIR")
#                if not results_dir:
#                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")
#
#                screen_shot_path = os.path.join(results_dir, item.name + '.png')
#                driver_fixture = item.funcargs['request']
#                driver_fixture.cls.driver.save_screenshot(screen_shot_path)
#                # only add additional html on failure
#                # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
#                extra.append(pytest_html.extras.image("/home/yevhenk/tests/registration_COM_confirm_EN_2023-03-21 10:33:18.900899.png"))
#                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
#                              name='screenshot',
#                              attachment_type=allure.attachment_type.PNG)
#        report.extra = extra
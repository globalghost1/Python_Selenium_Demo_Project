import pytest as pytest
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager())
    driver.implicity_wait(10)
    driver.maximize_window()
    driver.execute_script("arguments[0].scrollIntoView(true):", driver.find_element())
    request.cls.driver = driver
    before_failed = request.session.testfailed
    yield
    driver.quit()

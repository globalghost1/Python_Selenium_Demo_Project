from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from locators.locators import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:


    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self, driver)
        my_account_page.open_page()
        my_account_page.log_in("softwaretester@gmail.com", "softwaretester")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self, driver)
        my_account_page.open_page()
        my_account_page.log_in("softwaretester@vp.com", "softwaretester")

        self.driver.find_element(By.ID, "username").send_keys("softwaretester@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("softwaretester")
        self.driver.find_element(By.ID, "password").send_kesy(Keys.ENTER)

        assert "ERROR: Incorrect username or password" in my_account_page.get_error_msg()





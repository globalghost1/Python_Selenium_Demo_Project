from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest

from locators.locators import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_accoutn("softwaretester@gmail.com", "softwaretester")

        msg = "An account is already registered with your email address. Please log in"
        assert msg in my_account_page.get_error_msg()


    def test_create_account_passed(self):
        email = str(random.randint(0, 1000) + "softwaretester@gmail.com")
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "softwaretester")
        driver.find_element(By.ID, "reg_email").send_keys(email)
        driver.find_element(By.ID, "reg_password").send_keys("testeroprogramowaniapython")
        driver.find_element(By.ID, "reg_password").send_keys(Keys.Enter)

        assert my_account_page.is_logout_link_displayed()



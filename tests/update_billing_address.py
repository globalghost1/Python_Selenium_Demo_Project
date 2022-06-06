import email

import self as self
from selenium.webdriver.common.by import By
from webdriver_manager import driver
import pytest
from locators.locators import MyAccountPage
import random

from locators.pages.billing_address_page import BillingAddressPage


class TestUpdateBillingAddress:


@pytest.mark.usefixtures("setup")

def test_update_billing_address():
    my_account_page = MyAccountPage()
    my_account_page.open_page()
    my_account_page.create_account(email, "softwaretester@gmail.com")
    billing_address_page = BillingAddressPage(self.driver)
    billing_address_page.open_page()
    billing_address_page.set_personal_data("John", "Doe")
    billing_address_page.select_country("Poland")
    billing_address_page.set_address("Kwiatowa 1", "01-202", "Warsaw")
    billing_address_page.set_phone_number("283940392")
    billing_address_page.save_address()
    assert "Address changed successfully" in billing_address_page.get_message_text()
    assert 'Address changed successfully' in driver.find_element(By.XPATH, "//div[@class= 'woocommerce-message']").text

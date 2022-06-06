from selenium.webdriver.support.select import Select

from locators.locators import BillingAddressLocators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        #Billing Address Page elements
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.addresses_link = BillingAddressLocators.addresses_link
        self.edit_lint = BillingAddressLocators.edit_link
        self.country_select = BillingAddressLocators.country_select
        self.addresses_input = BillingAddressLocators.address_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.msg_div = BillingAddressLocators.message_div

    def open_edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()


    def set_personal_data(self,first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.driver.find_elemen(*self.addresses_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, number):
        self.driver.execute_script("arguments[0].scrollIntoView(true):", self.driver.find_element(*self.phone_input))
        self.driver.find_element(*self.phone_input).send_keys(number)

    def save_address(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true):", self.driver.find_element(*self.save_address_button))
        self.driver.find_element(*self.save_address_button()).click()

    def get_message_text(self):
        return self.driver.find(*self.msg_div).text

    




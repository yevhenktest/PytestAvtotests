
from pages.locators.RegistrationUALocator import RegistrationUALocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class RegistrationUA(RegistrationUALocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def clicking_localization_dropdown(self):
        logger.debug("Clicking localization dropdown.")
        self.sl.wait_and_click(self.LOCALIZATION_DROPDOWN)

    def select_ua_in_localization_dropdown(self):
        logger.debug("Clicking 'Ua' link.")
        self.sl.wait_and_click(self.UA_IN_LOCALIZATION_DROPDOWN)

    def go_to_registrationform(self):
        base_url = get_base_url()
        my_url = base_url
        logger.info(f"Going to: {my_url}")

        self.driver.get(my_url)

    def click_registration_button(self):
        logger.debug("Clicking 'Registration' button.")
        self.sl.wait_and_click(self.REGISTRATION_UA_BTN)

    def click_registration_link(self):
        logger.debug("Clicking 'Registration' link.")
        self.sl.wait_and_click(self.REGISTRATION_UA_LINK)

    def input_firstname(self, firstname):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_FIRSTNAME, firstname)

    def input_lastname(self, lastname):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_LASTNAME, lastname)

    def input_patronymic(self, patronymic):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_PATRONYMIC, patronymic)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_TELEPHONE, telephone)

    def input_country_dropdown_click(self):
        self.sl.wait_and_click(self.REGISTRATION_UA_COUNTRY_DROPDOWN_CLICK)

    def input_selectregion(self):
        self.sl.wait_and_click(self.REGISTRATION_UA_REGION_SELECT)

    def input_sity(self, sity):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_CITY, sity)

    def input_address(self, address):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_ADDRESS, address)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_EMAIL, email)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_PASSWORD, password)

    def input_confirmpassword(self, confirmpassword):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_CONFIRMPASSWORD, confirmpassword)

    def click_checkbox1(self):
        logger.debug("Clicking checkbox 1.")
        self.sl.wait_and_click(self.REGISTRATION_UA_CHECKBOX1)

    def click_checkbox2(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.REGISTRATION_UA_CHECKBOX2)

    def click_checkbox3(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_CHECKBOX3)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.REGISTRATION_UA_BTN_SUBMIT)
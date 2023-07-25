
from pages.locators.RegistrationUALocator import RegistrationUALocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class RegistrationUAlegal(RegistrationUALocator):

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

    def click_tab(self):
        self.sl.wait_and_click(self.REGISTRATION_UA_TAB_B2B)

    def input_institution(self, institution):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_INSTITUTION, institution)

    def input_firstname(self, firstname):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_FIRSTNAME, firstname)

    def input_lastname(self, lastname):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_LASTNAME, lastname)

    def input_patronymic(self, patronymic):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_PATRONYMIC, patronymic)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_TELEPHONE, telephone)

    def input_country_dropdown_click(self):
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_COUNTRY_DROPDOWN_CLICK)

    def input_selectregion(self):
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_REGION_SELECT)

    def input_sity(self, sity):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_CITY, sity)

    def input_address(self, address):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_ADDRESS, address)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_EMAIL, email)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_PASSWORD, password)

    def input_confirmpassword(self, confirmpassword):
        self.sl.wait_and_input_text(self.REGISTRATION_UA_B2B_CONFIRMPASSWORD, confirmpassword)

    def scroll_page_up(self):
        self.sl.scroll_page_up(self.REGISTRATION_UA_B2B_INSTITUTION)

    def click_checkbox1(self):
        logger.debug("Clicking checkbox 1.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX1)

    def click_checkbox2(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX2)

    def click_checkbox3(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX3)

    def click_checkbox4(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX4)

    def click_checkbox5(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX5)

    def click_checkbox6(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX6)

    def click_checkbox7(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX7)

    def click_checkbox8(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX8)

    def click_checkbox9(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_CHECKBOX9)

    def click_conditions_checkbox(self):
        logger.debug("Clicking 'Сonditions' checkbox.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_QAZBTN)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.REGISTRATION_UA_B2B_BTN_SUBMIT)
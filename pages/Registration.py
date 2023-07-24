
from pages.locators.RegistrationLocator import RegistrationLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class Registration(RegistrationLocator):

    endpoint = '/registration'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_registrationform(self):
        base_url = get_base_url()
        my_url = base_url + self.endpoint
        logger.info(f"Going to: {my_url}")

        self.driver.get(my_url)

    def clicking_localization_dropdown(self):
        logger.debug("Clicking localization dropdown.")
        self.sl.wait_and_click(self.LOCALIZATION_DROPDOWN)

    def select_ua_in_localization_dropdown(self):
        logger.debug("Clicking 'Ua' link.")
        self.sl.wait_and_click(self.UA_IN_LOCALIZATION_DROPDOWN)

    def select_en_in_localization_dropdown(self):
        logger.debug("Clicking 'En' link.")
        self.sl.wait_and_click(self.EN_IN_LOCALIZATION_DROPDOWN)

    def select_pl_in_localization_dropdown(self):
        logger.debug("Clicking 'Pl' link.")
        self.sl.wait_and_click(self.PL_IN_LOCALIZATION_DROPDOWN)

    def select_es_in_localization_dropdown(self):
        logger.debug("Clicking 'Es' link.")
        self.sl.wait_and_click(self.ES_IN_LOCALIZATION_DROPDOWN)

    def select_ru_in_localization_dropdown(self):
        logger.debug("Clicking 'Ru' link.")
        self.sl.wait_and_click(self.RU_IN_LOCALIZATION_DROPDOWN)

    def click_confirm_popup_window(self):
        logger.debug("Clicking 'Confirm' button in popup window on Pl localization.")
        self.sl.wait_and_click(self.REGISTRATION_POPUP_BTN)

    def click_registration_link(self):
        logger.debug("Clicking 'Products' main menu.")
        self.sl.wait_and_click(self.REGISTRATION_LINK)

    def click_checkbox1(self):
        logger.debug("Clicking checkbox 1.")
        self.sl.wait_and_click(self.REGISTRATION_CH1)

    def click_checkbox2(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.REGISTRATION_CH2)

    def click_checkbox3(self):
        logger.debug("Clicking checkbox 3.")
        self.sl.wait_and_click(self.REGISTRATION_CH3)

    def click_checkbox4(self):
        logger.debug("Clicking checkbox 4.")
        self.sl.wait_and_click(self.REGISTRATION_CH4)

    def input_education(self, education):
        self.sl.wait_and_input_text(self.REGISTRATION_EDUCATION, education)

    def input_firstname(self, firstname):
        self.sl.wait_and_input_text(self.REGISTRATION_FIRSTNAME, firstname)

    def input_lastname(self, lastname):
        self.sl.wait_and_input_text(self.REGISTRATION_LASTNAME, lastname)

    def input_country(self, country):
        self.sl.wait_and_input_text(self.REGISTRATION_COUNTRY, country)

    def input_city(self, city):
        self.sl.wait_and_input_text(self.REGISTRATION_CITY, city)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.REGISTRATION_TELEPHONE, telephone)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.REGISTRATION_EMAIL, email)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.REGISTRATION_PASSWORD, password)

    def input_confirmpassword(self, confirmpassword):
        self.sl.wait_and_input_text(self.REGISTRATION_CONFIRMPASSWORD, confirmpassword)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.REGISTRATION_BTN_SUBMIT)
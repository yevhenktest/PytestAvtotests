
from pages.locators.ContactsLocator import ContactsLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class Question(ContactsLocator):

    endpoint = '/contacts'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_question_form(self):
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

    def click_contacts_link_main_menu(self):
        logger.debug("Clicking 'Contacts' link in main menu.")
        self.sl.wait_and_click(self.QUESTION_LINK_MENU)

    def input_fullname(self, fullname):
        self.sl.wait_and_input_text(self.QUESTION_FULLNAME, fullname)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.QUESTION_TELEPHONE, telephone)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.QUESTION_EMAIL, email)

    def click_dropdown(self):
        logger.debug("Clicking Country dropdown.")
        self.sl.wait_and_click(self.QUESTION_DROPDOWN)

    def input_country(self, country):
        self.sl.wait_and_input_text(self.QUESTION_COUNTRY, country)

    def input_town(self, town):
        self.sl.wait_and_input_text(self.QUESTION_TOWN, town)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.QUESTION_BTN_SUBMIT)
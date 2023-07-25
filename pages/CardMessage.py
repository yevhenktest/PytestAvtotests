
from pages.locators.CardMessageLocator import CardMessageLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class CardMessage(CardMessageLocator):

    endpoint = '/medicalReview'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cardmessage(self):
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

    def click_cardmessage_main_menu(self):
        logger.debug("Click on the 'Product feedback' link in the main menu.")
        self.sl.wait_and_click(self.CARDMESSAGE_LINK_MENU)

    def click_cardmessage_button(self):
        logger.debug("Clicking 'Card-message' button.")
        self.sl.wait_and_click(self.CARDMESSAGE_FORM_BTN)

    def input_fullnamenotifier(self, fullnamenotifier):
        self.sl.wait_and_input_text(self.CARDMESSAGE_FULLNAME_NOTIFIER, fullnamenotifier)

    def input_institution(self, institution):
        self.sl.wait_and_input_text(self.CARDMESSAGE_INSTITUTION_NOTIFIER, institution)

    def input_telephonenotifier(self, telephonenotifier):
        self.sl.wait_and_input_text(self.CARDMESSAGE_TELEPHONE_NOTIFIER, telephonenotifier)

    def input_emailnotifier(self, emailnotifier):
        self.sl.wait_and_input_text(self.CARDMESSAGE_EMAIL_NOTIFIER, emailnotifier)

    def input_countrynotifier(self, countrynotifier):
        self.sl.wait_and_input_text(self.CARDMESSAGE_COUNTRY_NOTIFIER, countrynotifier)

    def click_checkbox1(self):
        logger.debug("Clicking checkbox 1.")
        self.sl.wait_and_click(self.CARDMESSAGE_CH1)

    def click_checkbox2(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.CARDMESSAGE_CH2)

    def click_checkbox3(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.CARDMESSAGE_CH3)

    def scroll_page(self):
        self.sl.scroll_page(self.PAGE_DOWN)

    def input_fullnamecustomer(self, fullnamecustomer):
        self.sl.wait_and_input_text(self.CARDMESSAGE_FULLNAME_CUSTOMER, fullnamecustomer)

    def input_emailcustomer(self, emailcustomer):
        self.sl.wait_and_input_text(self.CARDMESSAGE_EMAIL_CUSTOMER, emailcustomer)

    def input_telephonecustomer(self, telephonecustomer):
        self.sl.wait_and_input_text(self.CARDMESSAGE_TELEPHONE_CUSTOMER, telephonecustomer)

    def input_countrycustomer(self, countrycustomer):
        self.sl.wait_and_input_text(self.CARDMESSAGE_COUNTRY_CUSTOMER, countrycustomer)

    def input_medicalproduct(self, medicalproduct):
        self.sl.wait_and_input_text(self.CARDMESSAGE_PRODUCTNAME, medicalproduct)

    def input_sku(self, sku):
        self.sl.wait_and_input_text(self.CARDMESSAGE_SKU, sku)

    def input_manufacturer(self, manufacturer):
        self.sl.wait_and_input_text(self.CARDMESSAGE_MANUFACTURER, manufacturer)

    def input_description(self, description):
        self.sl.wait_and_input_text(self.CARDMESSAGE_DESCRIPTION, description)

    def click_agreecheckbox(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.CARDMESSAGE_AGREE_CH)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.CARDMESSAGE_BTN_SUBMIT)

    def click_popup_window_close(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.CARDMESSAGE_CLOSE_POPUP_WINDOW)
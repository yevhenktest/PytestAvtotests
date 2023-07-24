
from pages.locators.FeedbackLocator import FeedbackLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class Feedback(FeedbackLocator):

    endpoint = '/catalogue/product/128-alexa-volume'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_products_page(self):
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

    def click_products_main_menu(self):
        logger.debug("Clicking 'Products' main menu.")
        self.sl.wait_and_click(self.PRODUCTS_BTN_MENU)

    def click_login_btn(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN_CLICK)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def click_alexa_volume_en(self):
        logger.debug("Clicking 'Alexa volume' product.")
        self.sl.wait_and_click(self.FEEDBACK_ALEXA_VOLUME_PRODUCT_EN)

    def click_alexa_volume_localization(self):
        logger.debug("Clicking 'Alexa volume' product.")
        self.sl.wait_and_click(self.FEEDBACK_ALEXA_VOLUME_PRODUCT_LOCALIZATION)

    def click_discounts_constructor(self):
        logger.debug("click on the discounts constructor block.")
        self.sl.wait_and_click(self.FEEDBACK_DISCOUNTS_CONSTRUCTOR)

    def input_name(self, name):
        self.sl.wait_and_input_text(self.FEEDBACK_FULLNAME, name)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.FEEDBACK_EMAIL, email)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.FEEDBACK_TELEPHONE, telephone)

    def input_comment(self, comment):
        self.sl.wait_and_input_text(self.FEEDBACK_COMMENT, comment)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.FEEDBACK_BTN_SUBMIT)

    def click_Signout_link(self):
        logger.debug("Clicking 'Sign out' link.")
        self.sl.wait_and_click(self.FEEDBACK_SIGNOUT_LINK)
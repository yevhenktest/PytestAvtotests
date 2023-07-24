
from pages.locators.MyAccountSignInLocator import MyAccountSignInLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger


class MyAccountSignIn(MyAccountSignInLocator):

    endpoint = '/login'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")

        self.driver.get(my_account_url)

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

    def click_login_link(self):
        logger.debug("Clicking 'login' link.")
        self.sl.wait_and_click(self.LOGIN_LINK_CLICK)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def click_products_main_menu(self):
        logger.debug("Clicking 'Products' main menu.")
        self.sl.wait_and_click(self.PRODUCTS_BTN_MENU)

    def click_discounts_constructor(self):
        logger.debug("click on the discounts constructor block.")
        self.sl.wait_and_click(self.CHECKOUT_DISCOUNTS_CONSTRUCTOR)

    def input_quantity(self, quantity):
        self.sl.wait_and_input_text(self.INPUT_QUANTITY, quantity)

    def click_add_to_card_button(self):
        logger.debug("Clicking 'Add to card' button.")
        self.sl.wait_and_click(self.ADD_TO_CARD)

    def click_signout_link(self):
        logger.debug("Clicking 'Sign out' link.")
        self.sl.wait_and_click(self.LOGIN_SIGNOUT_LINK)

    def click_signout_link_ua(self):
        logger.debug("Clicking 'Sign out' link.")
        self.sl.wait_and_click(self.LOGIN_SIGNOUT_LINK_UA)

    def wait_until_element_is_visible(self):
        self.sl.wait_until_element_is_visible(self)


    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)



from pages.locators.MedicalTrainersLocator import MedicalTrainersLocator
from SeleniumExtended import SeleniumExtended
from config_helpers import get_base_url
import logging as logger

class MedicalTrainer(MedicalTrainersLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_medical_trainer(self):
        base_url = get_base_url()
        logger.info(f"Going to: {base_url}")

        self.driver.get(base_url)

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

    def click_trainer_main_menu(self):
        logger.debug("Click on the 'Medical Trainers' link in the main menu.")
        self.sl.wait_and_click(self.TRAINER_BTN_MENU)

    def click_join_button(self):
        logger.debug("Clicking 'Join' button.")
        self.sl.wait_and_click(self.TRAINER_BTN_JOIN)

    def scroll_page(self):
        logger.debug("Scroll the page.")
        self.sl.scroll_page(self.TRAINER_TELEPHONE)

    def input_fullname(self, fullname):
        self.sl.wait_and_input_text(self.TRAINER_FULLNAME, fullname)

    def input_telephone(self, telephone):
        self.sl.wait_and_input_text(self.TRAINER_TELEPHONE, telephone)

    def click_checkbox1(self):
        logger.debug("Clicking checkbox 1.")
        self.sl.wait_and_click(self.TRAINER_CH1)

    def click_checkbox2(self):
        logger.debug("Clicking checkbox 2.")
        self.sl.wait_and_click(self.TRAINER_CH2)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.TRAINER_EMAIL, email)

    def input_country(self, country):
        self.sl.wait_and_input_text(self.TRAINER_COUNTRY, country)

    def click_submit_button(self):
        logger.debug("Clicking 'Submit' button.")
        self.sl.wait_and_click(self.TRAINER_BTN_SUBMIT)

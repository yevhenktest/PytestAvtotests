from selenium.webdriver.common.by import By

class MedicalTrainersLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    TRAINER_BTN_MENU = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[5]')
    TRAINER_BTN_JOIN = (By.XPATH, '/html/body/div[1]/main/div[4]/div[2]/a')
    TRAINER_FULLNAME = (By.ID, 'appbundle_become_an_expert_credentials')
    TRAINER_CH1 = (By.CSS_SELECTOR,
           'body > div.page-l__content > main > div.overflow-hidden-bae > div.expert-form-wrapper > form > div.isclient-block > div:nth-child(3) > label')
    TRAINER_CH2 = (By.CSS_SELECTOR,
           'body > div.page-l__content > main > div.overflow-hidden-bae > div.expert-form-wrapper > form > div.expert-type-block.become-expert-form-contact-mobile > div > div > div:nth-child(1) > div:nth-child(3) > label')
    TRAINER_TELEPHONE = (By.ID, 'appbundle_become_an_expert_phone')
    TRAINER_EMAIL = (By.ID, 'appbundle_become_an_expert_email')
    TRAINER_COUNTRY = (By.ID, 'appbundle_become_an_expert_location')
#    driver.get_screenshot_as_file(f'trainerform_{local}_valid_{datetime.datetime.now()}.png')
#    btn = (By.CSS_SELECTOR, 'form button,button_submit')
    TRAINER_BTN_SUBMIT = (By.XPATH, '/html/body/div[1]/main/div[4]/div[5]/form/div[4]/button')
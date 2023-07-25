from selenium.webdriver.common.by import By

class ContactsLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    QUESTION_LINK_MENU = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[8]')
    QUESTION_FULLNAME = (By.CSS_SELECTOR, '#appbundle_contact_us_message_userName')
    QUESTION_TELEPHONE = (By.ID, 'appbundle_contact_us_message_phone')
    QUESTION_EMAIL = (By.ID, 'appbundle_contact_us_message_email')
    QUESTION_DROPDOWN = (By.CSS_SELECTOR,
                     'body > div.page-l__content.al-contact-page > main > div.b-contanct.b-contact_global > div.b-contanct-row > div.b-contact__feedback > form > fieldset:nth-child(2) > div > div:nth-child(1) > div.custom-combobox.al-pos-relative > div.al-custom-combobox-container > a')
    QUESTION_COUNTRY = (By.CSS_SELECTOR,
                     'body > div.page-l__content.al-contact-page > main > div.b-contanct.b-contact_global > div.b-contanct-row > div.b-contact__feedback > form > fieldset:nth-child(2) > div > div:nth-child(1) > div.custom-combobox.al-pos-relative > div.al-custom-combobox-container > input')
    QUESTION_TOWN = (By.ID, 'appbundle_contact_us_message_city')
    QUESTION_DESCRIPTION = (By.ID, 'appbundle_contact_us_message_message')
    QUESTION_BTN_SUBMIT = (By.CSS_SELECTOR, 'button[type = "submit"]')
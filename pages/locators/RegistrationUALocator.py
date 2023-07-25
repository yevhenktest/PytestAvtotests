from selenium.webdriver.common.by import By

class RegistrationUALocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_UA_LINK = (By.CSS_SELECTOR, 'body > div.page-l__content > header > div.header__content > div.header__manage > div.userbar > ul > li.auth-nav__item.auth-nav__item-registration')
    # Вкладка для фізичних осіб
    REGISTRATION_UA_BTN = (By.CSS_SELECTOR, '#tabs > ul > li:nth-child(1)')
    REGISTRATION_UA_FIRSTNAME = (By.ID, 'my_userclient__registration_form_username')
    REGISTRATION_UA_LASTNAME = (By.ID, 'my_userclient__registration_form_lastName')
    REGISTRATION_UA_PATRONYMIC = (By.ID, 'my_userclient__registration_form_patronymic')
    REGISTRATION_UA_TELEPHONE = (By.ID, 'my_userclient__registration_form_phone')
    REGISTRATION_UA_COUNTRY_DROPDOWN_CLICK = (By.CSS_SELECTOR, '#clientRegistrationForm > div.registration-wrap > div.widtch-lg-5.left-tab-registration.col-tab > fieldset.inform-user > div:nth-child(5) > div > div.al-custom-combobox-container > a > span.ui-button-icon.ui-icon.ui-icon-triangle-1-s')
    REGISTRATION_UA_REGION_SELECT = (By.XPATH, '/html/body/div[1]/main/div[6]/div[1]/form/div[1]/div[1]/fieldset[1]/div[5]/div/div[2]/ul/li[2]/div')
    REGISTRATION_UA_CITY = (By.ID, 'my_userclient__registration_form_city')
    REGISTRATION_UA_ADDRESS = (By.ID, 'my_userclient__registration_form_address')
    REGISTRATION_UA_EMAIL = (By.ID, 'my_userclient__registration_form_email')
    REGISTRATION_UA_PASSWORD = (By.ID, 'my_userclient__registration_form_plainPassword_first')
    REGISTRATION_UA_CONFIRMPASSWORD = (By.ID, 'my_userclient__registration_form_plainPassword_second')
    REGISTRATION_UA_CHECKBOX1 = (By.CSS_SELECTOR,
           '#clientRegistrationForm > div.registration-wrap > div.widtch-lg-5.right-tab-registration.col-tab > div.education.education-background-non > div:nth-child(1) > label')
    REGISTRATION_UA_CHECKBOX2 = (By.CSS_SELECTOR,
           '#clientRegistrationForm > div.registration-wrap > div.widtch-lg-5.right-tab-registration.col-tab > div.education.education-background-non > div:nth-child(2) > label')
    REGISTRATION_UA_CHECKBOX3 = (By.CSS_SELECTOR,
           '#clientRegistrationForm > div.registration-wrap > div.widtch-lg-5.right-tab-registration.col-tab > div.education.education-background-non > div:nth-child(3) > label')
    REGISTRATION_UA_BTN_SUBMIT = (By.CSS_SELECTOR, 'form button,button_submit')
    # Вкладка для юридичних осіб
    REGISTRATION_UA_TAB_B2B = (By.CSS_SELECTOR, '#tabs > ul > li:nth-child(2)')
    REGISTRATION_UA_B2B_INSTITUTION = (By.ID, 'my_usercompany__registration_form_username')
    REGISTRATION_UA_B2B_FIRSTNAME = (By.ID, 'my_usercompany__registration_form_contactPersonFirstName')
    REGISTRATION_UA_B2B_LASTNAME = (By.ID, 'my_usercompany__registration_form_lastName')
    REGISTRATION_UA_B2B_PATRONYMIC = (By.ID, 'my_usercompany__registration_form_patronymic')
    REGISTRATION_UA_B2B_TELEPHONE = (By.ID, 'my_usercompany__registration_form_phone')
    REGISTRATION_UA_B2B_COUNTRY_DROPDOWN_CLICK = (By.CSS_SELECTOR, '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.left-tab-registration > fieldset.inform-user > div:nth-child(6) > div > div.al-custom-combobox-container > a > span.ui-button-icon.ui-icon.ui-icon-triangle-1-s')
    REGISTRATION_UA_B2B_REGION_SELECT = (By.XPATH, '/html/body/div[1]/main/div[6]/div[2]/form/div[1]/div[1]/fieldset[1]/div[6]/div/div[2]/ul/li[1]/div')
    REGISTRATION_UA_B2B_CITY = (By.ID, 'my_usercompany__registration_form_city')
    REGISTRATION_UA_B2B_ADDRESS = (By.ID, 'my_usercompany__registration_form_address')
    REGISTRATION_UA_B2B_EMAIL = (By.ID, 'my_usercompany__registration_form_email')
    REGISTRATION_UA_B2B_PASSWORD = (By.ID, 'my_usercompany__registration_form_plainPassword_first')
    REGISTRATION_UA_B2B_CONFIRMPASSWORD = (By.ID, 'my_usercompany__registration_form_plainPassword_second')
    REGISTRATION_UA_B2B_CHECKBOX1 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(1) > label')
    REGISTRATION_UA_B2B_CHECKBOX2 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(2) > label')
    REGISTRATION_UA_B2B_CHECKBOX3 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(3) > label')
    REGISTRATION_UA_B2B_CHECKBOX4 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(4) > label')
    REGISTRATION_UA_B2B_CHECKBOX5 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(5) > label')
    REGISTRATION_UA_B2B_CHECKBOX6 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(6) > label')
    REGISTRATION_UA_B2B_CHECKBOX7 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(7) > label')
    REGISTRATION_UA_B2B_CHECKBOX8 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(8) > label')
    REGISTRATION_UA_B2B_CHECKBOX9 = (By.CSS_SELECTOR,
           '#companyRegistrationForm > div.registration-wrap > div.widtch-lg-5.col-tab.right-tab-registration > div.education.al-education-reg.education-background-non > div:nth-child(9) > label')
    # privacy_Policy
    REGISTRATION_UA_B2B_QAZBTN = (By.CSS_SELECTOR, 'input[name="my_usercompany__registration_form[privacyPolicy]"][value="1"]')
    REGISTRATION_UA_B2B_BTN_SUBMIT = (
        By.CSS_SELECTOR,
        '#companyRegistrationForm > div.wrapper-btn-registr.ripple-effect-prevent-error-wrapper > button')
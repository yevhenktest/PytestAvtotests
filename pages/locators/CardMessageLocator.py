from selenium.webdriver.common.by import By

class CardMessageLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    CARDMESSAGE_LINK_MENU = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[7]/a/small')
    CARDMESSAGE_FORM_BTN = (By.XPATH, '/html/body/div[1]/main/div[5]/div[2]/div[1]/a')
    CARDMESSAGE_FULLNAME_NOTIFIER = (By.ID, 'appbundle_medicalreview_notifierName')
    CARDMESSAGE_INSTITUTION_NOTIFIER = (By.ID, 'appbundle_medicalreview_notifierInstitution')
    CARDMESSAGE_TELEPHONE_NOTIFIER = (By.ID, 'appbundle_medicalreview_notifierPhone')
    CARDMESSAGE_COUNTRY_NOTIFIER = (By.ID, 'appbundle_medicalreview_notifierLocation')
    CARDMESSAGE_EMAIL_NOTIFIER = (By.ID, 'appbundle_medicalreview_notifierEmail')
    CARDMESSAGE_CH1 = (
        By.CSS_SELECTOR,
        '#al-popup-wrapper > form > fieldset.user-information > div.form-radio-wrap > label:nth-child(2)')
    CARDMESSAGE_CH2 = (
        By.CSS_SELECTOR,
        '#al-popup-wrapper > form > fieldset.user-information > div.form-radio-wrap > label:nth-child(4)')
    CARDMESSAGE_CH3 = (
        By.CSS_SELECTOR,
        '#al-popup-wrapper > form > fieldset.user-information > div.form-radio-wrap > label:nth-child(6)')
    CARDMESSAGE_FULLNAME_CUSTOMER = (By.ID, 'appbundle_medicalreview_clientName')
    CARDMESSAGE_EMAIL_CUSTOMER = (By.ID, 'appbundle_medicalreview_clientEmail')
    CARDMESSAGE_TELEPHONE_CUSTOMER = (By.ID, 'appbundle_medicalreview_clientPhone')
    CARDMESSAGE_COUNTRY_CUSTOMER = (By.ID, 'appbundle_medicalreview_clientLocation')
    CARDMESSAGE_PRODUCTNAME = (By.ID, 'appbundle_medicalreview_productName')
    CARDMESSAGE_SKU = (By.ID, 'appbundle_medicalreview_productSeries')
    CARDMESSAGE_MANUFACTURER = (By.ID, 'appbundle_medicalreview_productManufacturer')
    PAGE_DOWN = (By.TAG_NAME, 'body')
    CARDMESSAGE_DESCRIPTION = (By.ID, 'appbundle_medicalreview_productDescription')
    CARDMESSAGE_AGREE_CH = (By.XPATH, '//*[@id="al-popup-wrapper"]/form/div[3]/label')
    # Button Submit
    CARDMESSAGE_BTN_SUBMIT = (By.XPATH, '/html/body/div[1]/main/div[5]/div[3]/form/div[4]/div/button')
    # Close popup window
    CARDMESSAGE_CLOSE_POPUP_WINDOW = (By.CSS_SELECTOR, '#al-popup-wrapper > div.close-medical-review-form')
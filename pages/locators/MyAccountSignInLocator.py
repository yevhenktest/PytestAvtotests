
from selenium.webdriver.common.by import By

class MyAccountSignInLocator:
    LOCALIZATION_DROPDOWN = (By.CSS_SELECTOR, 'div.lswitcher__current-locale')
    EN_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'En')
    UA_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ua')
    PL_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Pl')
    ES_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Es')
    RU_IN_LOCALIZATION_DROPDOWN = (By.LINK_TEXT, 'Ru')
    REGISTRATION_POPUP_BTN = ("id", 'pl-button-submit')
    # btn = (By.CSS_SELECTOR, 'a[class="auth-nav__link"]')
    LOGIN_LINK_CLICK = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div[3]/ul/li[1]/a/span')
    #LOGIN_LINK_CLICK = (By.CSS_SELECTOR, 'ul[class="auth-nav"]')
    #LOGIN_LINK_CLICK = ('/html/body/div[1]/header/div[1]/div[1]/div[3]/ul/li[1]/a')
    LOGIN_USER_NAME = (By.CSS_SELECTOR, 'input[data-action-type="phone-change"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[class="form-control custom-required-validation-message"]')
    LOGIN_BTN = (By.CLASS_NAME, 'al-login-form__btn')
    PRODUCTS_BTN_MENU = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[2]/a')
    CHECKOUT_DISCOUNTS_CONSTRUCTOR = (By.XPATH, '/html/body/div[1]/main/div[5]/div/div[3]/a[2]')
    INPUT_QUANTITY = (By.XPATH, '/html/body/div[1]/main/article/div[1]/div[1]/div/div[3]/div[1]/div[4]/div/span[1]/input')
    ADD_TO_CARD = (By.XPATH, '/html/body/div[1]/main/article/div[1]/div[1]/div/div[4]/div[2]/div/a')
    CHECKOUT_CLICK_1 = (By.XPATH, '/html/body/aside/div[2]/div/nav/ul/li[2]/a')
    CHECKOUT_CLICK_2 = (By.XPATH, '/html/body/div[1]/main/div[5]/div[1]/div/div/div[4]')
    LOGIN_SIGNOUT_LINK = (By.XPATH, '/html/body/div[1]/header/div[3]/div[3]/ul/li/a')
    LOGIN_SIGNOUT_LINK_UA = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div[3]/div[3]/ul/li/a')
    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

#    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')

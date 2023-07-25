import time

import pytest
from pages.RegistrationUAlegal import RegistrationUAlegal
import datetime

@pytest.mark.usefixtures("init_driver")
class TestRegistrationUAlegal:

    @pytest.mark.reg_ua_legal
    @pytest.mark.smoke
    def test_registration_ua_legal(self):
        print("*******")
        print("THE TEST FOR COMPLETING THE REGISTRATION FORM ON THE TAB FOR LEGAL ENTITIES PASSED")
        print("*******")
        registrationUAlegal = RegistrationUAlegal(self.driver)
        registrationUAlegal.go_to_registrationform()
        registrationUAlegal.clicking_localization_dropdown()
        registrationUAlegal.select_ua_in_localization_dropdown()
        registrationUAlegal.click_registration_link()
        registrationUAlegal.click_tab()
        registrationUAlegal.input_institution('Test12345!@#$%')
        registrationUAlegal.input_firstname('Test')
        registrationUAlegal.input_lastname('Test')
        registrationUAlegal.input_patronymic('Test')
        registrationUAlegal.input_telephone(+380987654321)
        registrationUAlegal.input_country_dropdown_click()
        registrationUAlegal.input_selectregion()
        registrationUAlegal.input_sity('Cherkasy')
        registrationUAlegal.input_address('Cherkasy')
        registrationUAlegal.input_email('a@a.')
        registrationUAlegal.input_password('Test12345')
        registrationUAlegal.input_confirmpassword('Test12345')
        registrationUAlegal.scroll_page_up()
        time.sleep(3)
        registrationUAlegal.click_checkbox1()
        registrationUAlegal.click_checkbox2()
        registrationUAlegal.click_checkbox3()
        registrationUAlegal.click_checkbox4()
        registrationUAlegal.click_checkbox5()
        registrationUAlegal.click_checkbox6()
        registrationUAlegal.click_checkbox7()
        registrationUAlegal.click_checkbox8()
        registrationUAlegal.click_checkbox9()
        screen_valid_name = f'registration_UA_legal_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        registrationUAlegal.click_submit_button()
        screen_confirm_name = f'registration_UA_legal_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
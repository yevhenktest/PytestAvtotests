import pytest
from pages.RegistrationUA import RegistrationUA
import datetime

@pytest.mark.usefixtures("init_driver")
class TestRegistrationUA:

    @pytest.mark.reg_ua
    @pytest.mark.smoke
    def test_registrationUA(self):
        print("*******")
        print("THE TEST FOR COMPLETING THE REGISTRATION FORM ON THE TAB FOR INDIVIDUALS PASSED")
        print("*******")

        registrationUA = RegistrationUA(self.driver)
        registrationUA.go_to_registrationform()
        registrationUA.clicking_localization_dropdown()
        registrationUA.select_ua_in_localization_dropdown()
        registrationUA.click_registration_link()
        registrationUA.input_firstname('Test')
        registrationUA.input_lastname('Test')
        registrationUA.input_patronymic('Test')
        registrationUA.input_telephone(+380987654321)
        registrationUA.input_country_dropdown_click()
#        import pdb; pdb.set_trace()
        registrationUA.input_selectregion()
        registrationUA.input_sity('Cherkasy')
        registrationUA.input_address('Cherkasy')
        registrationUA.input_email('a@')
        registrationUA.input_password('Test12345')
        registrationUA.input_confirmpassword('Test12345')
        registrationUA.click_checkbox1()
        registrationUA.click_checkbox2()
        registrationUA.click_checkbox3()
        screen_valid_name = f'registration_UA_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        registrationUA.click_submit_button()
        screen_confirm_name = f'registration_UA_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
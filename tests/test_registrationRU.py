import pytest
from pages.Registration import Registration
import datetime


@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.reg
    @pytest.mark.reg_ru
    @pytest.mark.smoke
    def test_medicalform_ru(self):
        print("*******")
        print("TEST THE REGISTRATION FORM IN RU INSTANCE PASSED")
        print("*******")
        registration = Registration(self.driver)
        registration.go_to_registrationform()
        registration.clicking_localization_dropdown()
        registration.select_ru_in_localization_dropdown()
        registration.click_registration_link()
        registration.click_checkbox1()
        registration.click_checkbox2()
        registration.click_checkbox3()
        registration.click_checkbox4()
        registration.input_education('Doctor')
        registration.input_firstname('Test')
        registration.input_lastname('Test')
        registration.input_country('Ukraine')
        registration.input_city('Cherkasy')
        registration.input_telephone(+380987654326)
        registration.input_email('abru@gmail.com')
        registration.input_password('Test12345')
        registration.input_confirmpassword('Test12345')
        screen_valid_name = f'registration_COM_valid_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        registration.click_submit_button()
        screen_confirm_name = f'registration_COM_confirm_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
import pytest
from pages.Registration import Registration
import datetime


@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.reg
    @pytest.mark.regen
    @pytest.mark.smoke
    def test_medicalform(self):
        print("*******")
        print("TEST THE REGISTRATION FORM PASSED")
        print("*******")
        registration = Registration(self.driver)
        registration.go_to_registrationform()
        registration.click_checkbox1()
        registration.click_checkbox2()
        registration.click_checkbox3()
        registration.click_checkbox4()
        registration.input_education('Doctor')
        registration.input_firstname('Test')
        registration.input_lastname('Test')
        registration.input_country('Ukraine')
        registration.input_city('Cherkasy')
        registration.input_telephone(+380987654322)
        registration.input_email('aen@gmail.com')
        registration.input_password('Test12345')
        registration.input_confirmpassword('Test12345')
        screen_name = f'registration_COM_valid_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
        registration.click_submit_button()
        screen_name = f'registration_COM_confirm_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
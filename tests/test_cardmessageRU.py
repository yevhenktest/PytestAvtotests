import pytest
from pages.CardMessage import CardMessage
import datetime

@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.cardmessage_ru
    @pytest.mark.cardmessage
    @pytest.mark.smoke
    def test_cardmessageform_ru(self):
        print("*******")
        print("TEST THE CARD MESSAGE FORM IN RU INSTANCE PASSED")
        print("*******")
        cardmessage = CardMessage(self.driver)
        cardmessage.go_to_cardmessage()
        cardmessage.clicking_localization_dropdown()
        cardmessage.select_ru_in_localization_dropdown()
        cardmessage.click_cardmessage_main_menu()
        cardmessage.click_cardmessage_button()
        cardmessage.input_fullnamenotifier('Test')
        cardmessage.input_institution('Test_institution123 4567 <>=!@#$%')
        cardmessage.input_telephonenotifier(+380987654321)
        cardmessage.input_emailnotifier('a@a.')
        cardmessage.input_countrynotifier('Ukraine')
        cardmessage.click_checkbox1()
        cardmessage.click_checkbox2()
        cardmessage.click_checkbox3()
        cardmessage.scroll_page()
        cardmessage.input_fullnamecustomer('Test')
        cardmessage.input_emailcustomer('a@a.')
        cardmessage.input_telephonecustomer(+380987654321)
        cardmessage.input_countrycustomer('Ukraine')
        cardmessage.input_medicalproduct('Test_Product123 4567 <>=!@#$%')
        cardmessage.input_sku(1234567890)
        cardmessage.input_manufacturer('Test_manufacturer123 4567 <>=!@#$%')
        cardmessage.input_description('Test_description123 4567 <>=!@#$%')
        cardmessage.click_agreecheckbox()
        screen_valid_name = f'cardmessage_COM_valid_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        cardmessage.click_submit_button()
        screen_confirm_name = f'cardmessage_COM_confirm_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
        cardmessage.click_popup_window_close()
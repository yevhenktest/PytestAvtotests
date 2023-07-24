import pytest
from pages.Contacts import Question
import datetime


@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.question_ua
    @pytest.mark.question
    @pytest.mark.smoke
    def test_questionform_ua(self):
        print("*******")
        print("TEST THE ASK YOUR QUESTION FORM IN UA INSTANCE PASSED")
        print("*******")
        questionform = Question(self.driver)
        questionform.go_to_question_form()
        questionform.clicking_localization_dropdown()
        questionform.select_ua_in_localization_dropdown()
        questionform.click_contacts_link_main_menu()
        # questionform.input_fullname('Test Test')
        questionform.input_telephone(+380987654321)
        questionform.input_email('a@a.')
        questionform.input_town('Cherkasy')
        screen_valid_name = f'questionform_UA_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        questionform.click_submit_button()
        screen_confirm_name = f'questionform_UA_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
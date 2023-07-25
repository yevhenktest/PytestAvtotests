import pytest
from pages.Contacts import Question
import datetime


@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.question_es
    @pytest.mark.question
    @pytest.mark.smoke
    def test_questionform_es(self):
        print("*******")
        print("TEST THE ASK YOUR QUESTION FORM IN ES INSTANCE PASSED")
        print("*******")
        questionform = Question(self.driver)
        questionform.go_to_question_form()
        questionform.clicking_localization_dropdown()
        questionform.select_es_in_localization_dropdown()
        questionform.click_contacts_link_main_menu()
        questionform.input_fullname('Test Test')
        questionform.input_telephone(+380987654321)
        questionform.input_email('a@a.')
        questionform.click_dropdown()
        questionform.input_country('Ukraine')
        screen_valid_name = f'questionform_COM_valid_ES_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        questionform.click_submit_button()
        screen_confirm_name = f'questionform_COM_confirm_ES_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
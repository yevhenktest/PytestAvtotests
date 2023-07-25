import pytest
from pages.Contacts import Question
import datetime


@pytest.mark.usefixtures("init_driver")
class TestMedicalTrainer:

    @pytest.mark.question_en
    @pytest.mark.question
    @pytest.mark.smoke
    def test_questionform_en(self):
        print("*******")
        print("TEST THE ASK YOUR QUESTION FORM IN EN INSTANCE PASSED")
        print("*******")
        questionform = Question(self.driver)
        questionform.go_to_question_form()
        questionform.input_fullname('Test Test')
        questionform.input_telephone(+380987654321)
        questionform.input_email('a@a.')
        questionform.click_dropdown()
        questionform.input_country('Ukraine')
        screen_valid_name = f'questionform_COM_valid_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        questionform.click_submit_button()
        screen_confirm_name = f'questionform_COM_confirm_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
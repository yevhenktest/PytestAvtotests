import pytest
from pages.Feedback import Feedback
import datetime

@pytest.mark.usefixtures("init_driver")
class TestFeedback:

    @pytest.mark.feedback_es
    @pytest.mark.feedback
    @pytest.mark.smoke
    def test_feedbackform_es(self):
        print("*******")
        print("TEST THE FEEDBACK FORM ON THE PRODUCT PAGE ON THE ES INSTANCE PASSED")
        print("*******")
        feedback = Feedback(self.driver)
        feedback.go_to_products_page()
        feedback.clicking_localization_dropdown()
        feedback.select_es_in_localization_dropdown()
        feedback.input_name('Test')
        feedback.input_telephone(+380987654321)
        feedback.input_email('a@a.')
        feedback.input_comment('TestTest TestTest')
        screen_valid_name = f'feedback_COM_valid_ES_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        feedback.click_submit_button()
        screen_confirm_name = f'feedback_COM_confirm_ES_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
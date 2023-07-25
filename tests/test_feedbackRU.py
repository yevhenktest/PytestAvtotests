import pytest
from pages.Feedback import Feedback
import datetime

@pytest.mark.usefixtures("init_driver")
class TestFeedback:

    @pytest.mark.feedback_ru
    @pytest.mark.feedback
    @pytest.mark.smoke
    def test_feedbackform_ru(self):
        print("*******")
        print("TEST THE FEEDBACK FORM ON THE PRODUCT PAGE ON THE RU INSTANCE PASSED")
        print("*******")
        feedback = Feedback(self.driver)
        feedback.go_to_products_page()
        feedback.clicking_localization_dropdown()
        feedback.select_ru_in_localization_dropdown()
        feedback.input_name('Test')
        feedback.input_telephone(+380987654321)
        feedback.input_email('a@a.')
        feedback.input_comment('TestTest TestTest')
        screen_valid_name = f'feedback_COM_valid_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        feedback.click_submit_button()
        screen_confirm_name = f'feedback_COM_confirm_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
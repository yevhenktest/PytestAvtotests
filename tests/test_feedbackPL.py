import pytest
from pages.Feedback import Feedback
import datetime

@pytest.mark.usefixtures("init_driver")
class TestFeedback:

    @pytest.mark.feedback_pl
    @pytest.mark.feedback
    @pytest.mark.smoke
    def test_feedbackform_pl(self):
        print("*******")
        print("TEST THE FEEDBACK FORM ON THE PRODUCT PAGE ON THE PL INSTANCE PASSED")
        print("*******")
        feedback = Feedback(self.driver)
        feedback.go_to_products_page()
        feedback.clicking_localization_dropdown()
        feedback.select_pl_in_localization_dropdown()
        feedback.click_confirm_popup_window()
        feedback.input_name('Test')
        feedback.input_telephone(+380987654321)
        feedback.input_email('a@a.')
        feedback.input_comment('TestTest TestTest')
        screen_valid_name = f'feedback_COM_valid_PL_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        feedback.click_submit_button()
        screen_confirm_name = f'feedback_COM_confirm_PL_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
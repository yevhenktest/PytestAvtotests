import time

import pytest
from pages.Feedback import Feedback
import datetime


@pytest.mark.usefixtures("init_driver")
class TestFeedbackUA:

    @pytest.mark.feedback_ua
    @pytest.mark.feedback
    @pytest.mark.smoke
    def test_feedbackform_ua(self):
        print("*******")
        print("TEST THE FEEDBACK FORM ON THE PRODUCT PAGE ON THE UA INSTANCE PASSED")
        print("*******")
        feedback = Feedback(self.driver)
        feedback.go_to_products_page()
        feedback.clicking_localization_dropdown()
        feedback.select_ua_in_localization_dropdown()
        feedback.click_products_main_menu()
        feedback.click_login_btn()
        feedback.input_login_username(+380982707258)
        feedback.input_login_password('Test12345')
        feedback.click_login_button()
        time.sleep(5)
        feedback.click_products_main_menu()
        feedback.click_discounts_constructor()
        feedback.input_comment('TestTest TestTest')
        screen_name = f'feedback_UA_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
        feedback.click_submit_button()
        screen_name = f'feedback_UA_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
        feedback.click_Signout_link()

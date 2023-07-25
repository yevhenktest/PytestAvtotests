import time
import pytest
from pages.MyAccountSignIn import MyAccountSignIn
import datetime

@pytest.mark.usefixtures("init_driver")
class TestFeedbackUA:

    @pytest.mark.signin_checkout_ua
    @pytest.mark.smoke
    def test_feedbackform_ua(self):
        print("*******")
        print("TEST THE CHECKOUT ON THE UA INSTANCE PASSED")
        print("*******")
        signin = MyAccountSignIn(self.driver)
        signin.go_to_my_account()
        signin.clicking_localization_dropdown()
        signin.select_ua_in_localization_dropdown()
        signin.click_login_link()
        signin.input_login_username(+380982707258)
        signin.input_login_password('Test12345')
        signin.click_login_button()
        time.sleep(5)
        signin.click_products_main_menu()
        signin.click_discounts_constructor()
        signin.input_quantity(1)
        signin.click_add_to_card_button()

        screen_name = f'feedback_UA_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
#        signin.click_submit_button()
        screen_name = f'feedback_UA_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_name)
        signin.click_Signout_link()

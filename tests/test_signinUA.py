import pytest
from pages.MyAccountSignIn import MyAccountSignIn
import datetime
import time

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.signin_ua
    @pytest.mark.signin
    @pytest.mark.smoke
    def test_login_ua(self):
        print("*******")
        print("TEST THE SIGNIN FORM ON THE UA INSTANCE PASSED")
        print("*******")
        my_account = MyAccountSignIn(self.driver)
        my_account.go_to_my_account()
        my_account.clicking_localization_dropdown()
        my_account.select_ua_in_localization_dropdown()
        my_account.click_login_link()
        my_account.input_login_username(+380982707258)
        my_account.input_login_password('Test12345')
        screen_valid_name = f'signin_UA_valid_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        my_account.click_login_button()
        time.sleep(5)
        screen_confirm_name = f'signin_UA_confirm_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
        my_account.click_signout_link_ua()

        # verify error message
#        expected_err = 'Unknown username. Check again or try your email address.'
#        my_account.wait_until_element_is_visible()
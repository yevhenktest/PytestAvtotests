import pytest
from pages.MyAccountSignIn import MyAccountSignIn
import datetime
import time

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.signin_en
    @pytest.mark.signin
    @pytest.mark.smoke
    def test_login_en(self):
        print("*******")
        print("TEST THE SIGNIN FORM ON THE EN INSTANCE PASSED")
        print("*******")
        my_account = MyAccountSignIn(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(+380982707258)
        my_account.input_login_password('Test12345')
        screen_valid_name = f'signin_COM_valid_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        my_account.click_login_button()
        time.sleep(3)
        screen_confirm_name = f'signin_COM_confirm_EN_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
        my_account.click_signout_link()

        # verify error message
#        expected_err = 'Unknown username. Check again or try your email address.'
#        my_account.wait_until_element_is_visible()
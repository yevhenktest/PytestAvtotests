import pytest
from pages.MyAccountSignIn import MyAccountSignIn
import datetime
import time

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.signin_ru
    @pytest.mark.signin
    @pytest.mark.smoke
    def test_login_ru(self):
        print("*******")
        print("TEST THE SIGNIN FORM ON THE RU INSTANCE PASSED")
        print("*******")
        my_account = MyAccountSignIn(self.driver)
        my_account.go_to_my_account()
        my_account.clicking_localization_dropdown()
        my_account.select_ru_in_localization_dropdown()
        my_account.input_login_username(+380982707258)
        my_account.input_login_password('Test12345')
        screen_valid_name = f'signin_COM_valid_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_valid_name)
        my_account.click_login_button()
        time.sleep(3)
        screen_confirm_name = f'signin_COM_confirm_RU_{datetime.datetime.now()}.png'
        self.driver.get_screenshot_as_file(screen_confirm_name)
        my_account.click_signout_link()
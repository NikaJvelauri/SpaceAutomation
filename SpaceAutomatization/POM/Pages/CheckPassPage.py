import time
from appium.webdriver.common.appiumby import AppiumBy
from SpaceAutomatization.POM.Locators.Locators import Locators


class CheckPassword:
    def __init__(self, driver):
        self.driver = driver

        self.activity_back_btn_id = Locators.activity_back_btn_id
        self.log_out_btn_id = Locators.log_out_btn_id
        self.input_password_id = Locators.input_password_id

    def goBackToProfileSettings(self):
        goBack_btn = self.driver.find_element(AppiumBy.ID, self.activity_back_btn_id)
        time.sleep(3)
        goBack_btn.click()

    def logOut(self):
        logOut_btn = self.driver.find_element(AppiumBy.ID, self.log_out_btn_id)
        logOut_btn.click()

    def resign(self):
        with open('../Passwords/password.txt') as f:
            new_pass = f.read()
        checkPasscode_btn = self.driver.find_element(AppiumBy.ID, "ge.space.app:id/loginPinEntryEditText")
        checkPasscode_btn.send_keys(new_pass)

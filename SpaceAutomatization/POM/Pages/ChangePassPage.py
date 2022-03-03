import time

import random as rand
from appium.webdriver.common.appiumby import AppiumBy
from SpaceAutomatization.POM.Locators.Locators import Locators


class ChangePass:
    def __init__(self, driver):
        self.driver = driver

        self.profile_png_id = Locators.profile_png_id
        self.security_btn_id = Locators.security_btn_id
        self.change_password_btn_id = Locators.change_password_btn_id
        self.input_old_password_id = Locators.input_old_password_id
        self.input_new_password_id = Locators.input_new_password_id
        self.input_new_password_again_id = Locators.input_new_password_again_id

    def goToProfile(self):
        time.sleep(1.5)
        profile_btn = self.driver.find_element(AppiumBy.ID, self.profile_png_id)
        profile_btn.click()

    def clickOnSecurity(self):
        time.sleep(2)
        security_btn = self.driver.find_element(AppiumBy.ID, self.security_btn_id)
        security_btn.click()

    def changePassword(self):
        changePass_btn = self.driver.find_element(AppiumBy.ID, self.change_password_btn_id)
        changePass_btn.click()

    def sendOldPass(self, password):
        send_oldPasscode = self.driver.find_element(AppiumBy.ID, self.input_old_password_id)
        send_oldPasscode.send_keys(password)



    def sendNewPass(self):
        new_password = rand.randint(99999, 999999)
        enter_newPasscode = self.driver.find_element(AppiumBy.ID, self.input_new_password_id)
        enter_newPasscode.send_keys(new_password)

        repeat_passcode = self.driver.find_element(AppiumBy.ID, self.input_new_password_again_id)
        repeat_passcode.send_keys(new_password)

        time.sleep(2)

        file_Object = open(r"../Passwords/password.txt", "w")
        file_Object.write(str(new_password))



    def goBack(self):
        time.sleep(4)
        self.driver.press_keycode(4);



from appium.webdriver.common.appiumby import AppiumBy
from SpaceAutomatization.POM.Locators.Locators import Locators


class LoginPage:

    
    def __init__(self, driver):
        self.driver = driver

        self.demo_btn_id = Locators.demo_btn_id
        self.number_input_class_name = Locators.number_input_class_name
        self.password_input_id = Locators.password_input_id
        self.alert_negative_btn_id = Locators.alert_negative_btn_id

    def clickOnDemoBtn(self):
        self.driver.implicitly_wait(20)
        begin_btn = self.driver.find_element(AppiumBy.ID, self.demo_btn_id)
        begin_btn.click()

    def inputNumber(self, number):
        number_btn = self.driver.find_element(AppiumBy.CLASS_NAME, self.number_input_class_name)
        number_btn.send_keys(number)

    def inputPassword(self, password):
        send_passcode = self.driver.find_element(AppiumBy.ID, self.password_input_id)
        send_passcode.send_keys(password)

    def alertNegativeBtnClick(self):
        no_btn = self.driver.find_element(AppiumBy.ID, self.alert_negative_btn_id)
        no_btn.click()

from appium import webdriver
from SpaceAutomatization.POM.Pages.SignInPage import LoginPage
from SpaceAutomatization.POM.Pages.ChangePassPage import ChangePass
from SpaceAutomatization.POM.Pages.CheckPassPage import CheckPassword
import unittest


class Login(unittest.TestCase):

    def test_LogIn(self):
        with open('../Passwords/password.txt') as f:
            last_pass = f.read()
        desired_cap = {
            "appium:deviceName": "RF8M22HQA2B",
            "platformName": "Android",
            "appium:app": "C:\\Users\\ninja\\Downloads\\ge.space.app_2022-01-18.apk",
        }
        driver = webdriver.Remote("http://192.168.40.1:4723/wd/hub", desired_cap)

        login = LoginPage(driver)
        login.clickOnDemoBtn()
        login.inputNumber("571860087")
        login.inputPassword(last_pass)
        login.alertNegativeBtnClick()

        changePassword = ChangePass(driver)
        changePassword.goToProfile()
        changePassword.clickOnSecurity()
        changePassword.changePassword()
        changePassword.sendOldPass(last_pass)
        changePassword.sendNewPass()
        changePassword.goBack()
        # changePassword.saveNewPassword()

        checkPassword = CheckPassword(driver)
        checkPassword.goBackToProfileSettings()
        checkPassword.logOut()
        checkPassword.resign()


if __name__ == '__main__':
    unittest.main()

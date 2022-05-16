from appium import webdriver


class AppStart:
    @classmethod
    def start(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "platformVersion": "12.0",
            "app": "/Users/robinzhang/Downloads/hko.MyObservatory_v1_0_2022-05-10.apk",
            "autoAcceptAlerts": True,
            # 'newCommandTimeout': 50000,
            # 'noReset': True,
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)
        return self.driver

    @classmethod
    def quit(self):
        self.driver.quit()

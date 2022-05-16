class APPSetupPage:
    def __init__(self, driver):
        self.driver = driver
        self.disclaimer_agree_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]"
        self.privacy_policy_statements_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]"
        self.background_access_to_location_information_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button"
        self.allow_location_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
        self.back_button_xpath = "//android.widget.ImageButton[@content-desc='Back']"
        self.next_button_xpath = "//android.widget.ImageView[@content-desc='Next page']"
        self.close_button_xpath = "//android.widget.ImageView[@content-desc='Close']"

    def setup_app_steps(self):
        self.driver.find_element_by_xpath(self.disclaimer_agree_button_xpath).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(self.privacy_policy_statements_button_xpath).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(self.background_access_to_location_information_xpath).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(self.allow_location_button_xpath).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath(self.back_button_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(self.close_button_xpath).click()
        self.driver.implicitly_wait(10)

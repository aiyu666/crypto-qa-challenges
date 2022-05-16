class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.hamberger_list_button_xpath = "//android.widget.ImageButton[@content-desc='Navigate up']"

    def open_the_hambuger_list(self):
        self.driver.find_element_by_xpath(self.hamberger_list_button_xpath).click()
        self.driver.implicitly_wait(5)

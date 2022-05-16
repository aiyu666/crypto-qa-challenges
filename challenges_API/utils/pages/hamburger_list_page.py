import time


class HamburgerListPage:
    def __init__(self, driver):
        self.driver = driver
        self.nine_day_forecast_item = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[10]/android.view.ViewGroup/android.widget.TextView"

    def scroll_the_list(self):
        time.sleep(3)
        self.driver.swipe(300, 1800, 300, 1500, 500)
        self.driver.implicitly_wait(2)

    def go_to_nine_day_forecast_page(self):
        self.driver.find_element_by_xpath(self.nine_day_forecast_item).click()

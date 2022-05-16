from utils.pages.app_setup_page import APPSetupPage
from utils.pages.app_init import AppStart
from utils.pages.home_page import HomePage
from utils.pages.hamburger_list_page import HamburgerListPage


class TestClass(object):
    def setup_class(self):
        self.driver = AppStart.start()

    def teardown_class(self):
        AppStart.quit()

    def test_user_can_go_to_nine_day_forecast(self):
        APPSetupPage(self.driver).setup_app_steps()
        HomePage(self.driver).open_the_hambuger_list()
        HamburgerListPage(self.driver).scroll_the_list()
        HamburgerListPage(self.driver).go_to_nine_day_forecast_page()

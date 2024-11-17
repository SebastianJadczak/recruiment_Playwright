from allure import step

from src.modals.data import CookieModal, ActionInModal, CookieSettingsData
from src.pages.common.enums import PageName
from src.pages.main_site.data import MainSitePageData
from src.pages.main_site.locators import MainSiteLocators
from utils.base_page import BasePage


class MainSiteBasePage(BasePage):
    PAGE_NAME = PageName.MAIN_SITE

    @property
    def locators(self) -> MainSiteLocators:
        return MainSiteLocators()

    @step(f'Wypełnij page: {PAGE_NAME}')
    def fill(self, data: MainSitePageData):
        if data.cookie_modal:
            self.__fill_cookie_modal(data.cookie_modal)

    @step('Wypełnij modal z cookie')
    def __fill_cookie_modal(self, data: CookieModal):
        self.page.wait_for_selector(self.locators.action_cookie_modal_button_by_xpath(data.action))
        self.page.locator(f'xpath={self.locators.action_cookie_modal_button_by_xpath(data.action)}').click()
        if data.action is ActionInModal.ADJUST:
            self.__set_cookie_settings(data.cookie_settings)

    @step('Ustaw interesujące cookie')
    def __set_cookie_settings(self, data: CookieSettingsData):
        if data.analytical_cookies:
            self.page.locator(self.locators.ANALYTICAL_COOKIE_CHECKBOX_XPATH).check()
        self.page.locator(f'xpath={self.locators.set_cookie_button_by_xpath(data.action)}').click()

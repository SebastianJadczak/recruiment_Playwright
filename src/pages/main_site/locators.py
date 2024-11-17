from src.modals.data import ActionInModal, ActionInCookieSettingsModal


class MainSiteLocators:
    ANALYTICAL_COOKIE_CHECKBOX_XPATH = '//input[@id="CpmAnalyticalOption"]'

    def action_cookie_modal_button_by_xpath(self, action: ActionInModal) -> str:
        return f'//div[@class="cookie-policy-btn-wrapper"]/button[text()="{action}"]'

    def set_cookie_button_by_xpath(self, action: ActionInCookieSettingsModal) -> str:
        return f'//div[2]/div//div[2]//div//div//div[2]/div/button[text()="{action}"]'

from playwright.async_api import Page

from flow.ing import IngContainer
from src.pages.data import IngData
from utils.cookies import Cookies


class CommonPath:

    def __init__(self, page: Page):
        self.page = page
        self.flow = IngContainer(self.page)

    def set_cookie(self, data: IngData):
        self.flow.open_ing_website()
        self.flow.main_site_page.fill(data.main_site_page)
        self.flow.refresh_website()
        cookies = self.page.context.cookies()
        result = Cookies(cookies).check_type_of_cookies_accepted()
        assert result in '4' or result == '3', f"Niezaznoczono odpiewiedniej zgody: {result}"

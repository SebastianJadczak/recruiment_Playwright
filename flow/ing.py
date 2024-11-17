from playwright.sync_api import Page

from src.pages.main_site.page import MainSiteBasePage


class IngContainer:

    def __init__(self, page: Page):
        self.page = page

    @property
    def main_site_page(self) -> MainSiteBasePage:
        return MainSiteBasePage(self.page)

    # implementacja property poszczególnych Page

    def open_ing_website(self):
        # todo: zmienna środowiskowa sterująca linkiem do strony
        self.page.goto('https://www.ing.pl')

    def refresh_website(self):
        self.page.reload()

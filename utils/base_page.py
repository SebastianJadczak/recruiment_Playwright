# elementy stąd najlepiej byłoby przenieść do oddzielnej biblioteki a tu w proekcie jedynie
# implementować gotowe rozwiązania :)
from playwright.async_api import Page


class BasePage:
    PAGE_NAME = ...

    def __init__(self, page:Page):
        self.page = page


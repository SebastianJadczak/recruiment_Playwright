from pathlib import PurePath
import pytest
from playwright.sync_api import Playwright

from src.pages.data import IngData
from src.paths import Paths
from tests.ing.common_path import CommonPath
from utils.utils import get_test_data_from_json


def get_path_to_test_data(test_data: str) -> PurePath:
    return Paths.test_data(test_data=test_data)


@pytest.fixture
def data_01_set_cookie():
    return get_test_data_from_json(IngData, get_path_to_test_data('data_01_set_cookie'))


class TestSpecialCases:

    @pytest.fixture(autouse=True)
    def setup(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], )
        context = browser.new_context()
        self.page = context.new_page()
        yield
        self.page.close()

    def test_01_set_cookie(self, data_01_set_cookie: IngData):
        CommonPath(self.page).set_cookie(data=data_01_set_cookie)

from dataclasses import dataclass

from src.modals.data import CookieModal


@dataclass
class MainSitePageData:
    cookie_modal: CookieModal

from dataclasses import dataclass
from enum import StrEnum
from typing import Optional


class ActionInModal(StrEnum):
    ADJUST = 'Dostosuj'
    DISCARD_ALL = 'Odrzuć wszystkie'
    ACCEPT_ALL = 'Zaakceptuj wszystkie'


class ActionInCookieSettingsModal(StrEnum):
    REJECT_ALL = 'Odrzuć wszystkie'
    ACCEPT_SELECTED_ONES = 'Zaakceptuj wybrane'


@dataclass
class CookieSettingsData:
    action: ActionInCookieSettingsModal
    technical_cookies: Optional[bool] = None
    analytical_cookies: Optional[bool] = None
    marketing_cookies: Optional[bool] = None


@dataclass
class CookieModal:
    action: ActionInModal
    cookie_settings: Optional[CookieSettingsData] = None

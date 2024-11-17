from typing import Any


class Cookies:
    def __init__(self, cookies):
        self.cookies = cookies

    def get_cookie_policy_gdpr(self) -> dict | None:
        target_name = 'cookiePolicyGDPR'
        return next((cookie for cookie in self.cookies if cookie['name'] == target_name), None)

    def check_type_of_cookies_accepted(self):
        match self.get_cookie_policy_gdpr()['value']:
            case '1':
                print('Cookie techniczne')
                return '1'
            case '2':
                print('Cookie techniczne i marketingowe')
                return '2'
            case '3':
                print('Cookie techniczne i analityczne')
                return '3'
            case '4':
                print('Wszystkie cookie')
                return '4'
            case _:
                return None

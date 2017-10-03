import sys

import getpass
import requests
from halo import Halo
from colorclass import Color
from bs4 import BeautifulSoup
from terminaltables import AsciiTable

from browser import Browser


class Faceboss:

    URL = 'https://en-gb.facebook.com/'
    CHECKPOINT = 'https://en-gb.facebook.com/checkpoint/'

    def __init__(self):
        self.session = requests.Session()
        self.browser = Browser()

    def login(self, email, password):
        spinner = Halo({'text': 'Logging in', 'spinner': 'dots'})
        spinner.start()

        self.browser.login(self.URL, email, password)

        response = self.browser.get_response()
        if 'Two-Factor Authentication' in response:
            code = raw_input(Color('{autocyan}Please enter verification code: {/autocyan}'))
            self.browser.submit_verification_code(self.CHECKPOINT, code)
            self.browser.save_browser(self.CHECKPOINT)
        elif 'Create a Post' not in response:
            spinner.fail('Wrong credentials, please verify')
            sys.exit()

        self.browser.set_cookies()
        spinner.succeed('Successfully logged in')

    def get_notifications_table(self):

        def _get_span_value_by_id(elem_id):
            return parsed_html.body.find('span', attrs={'id': elem_id}).text

        def _get_headers_color(header):
            return 'autored' if header else 'autocyan'

        def _get_notifs_count():
            return int(_get_span_value_by_id('requestsCountValue')),\
                   int(_get_span_value_by_id('mercurymessagesCountValue')),\
                   int(_get_span_value_by_id('notificationsCountValue'))

        cookies = self.browser.get_cookies()

        response = self.session.get(self.URL, cookies=cookies)
        parsed_html = BeautifulSoup(response.content, 'html.parser')
        friend_requests_count, messages_count, notifications_count = _get_notifs_count()

        table_data = [
            [Color('{{{0}}}Friend Requests{{/{0}}}'.format(_get_headers_color(friend_requests_count))),
             Color('{{{0}}}Messages{{/{0}}}'.format(_get_headers_color(messages_count))),
             Color('{{{0}}}Notifications{{/{0}}}'.format(_get_headers_color(notifications_count)))],
            [friend_requests_count, messages_count, notifications_count]
        ]

        return AsciiTable(table_data).table


def main():
    fb = Faceboss()
    if not fb.browser.has_cookies():
        email = raw_input(Color('{autocyan}Please enter your email: {/autocyan}'))
        password = getpass.getpass(Color('{autocyan}Please enter your password: {/autocyan}'))
        fb.login(email, password)

    print fb.get_notifications_table()

if __name__ == '__main__':
    main()

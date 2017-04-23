# -*- coding: utf-8 -*-
import json
import getpass
import os.path

import mechanize
from colorclass import Color


class Browser:

    CKS = '.cks'

    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        # 😈
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                                             'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def login(self, url):
        self.br.open(url)
        self.br.select_form(nr=0)

        email = raw_input(Color('{autocyan}Please enter your email: {/autocyan}'))
        self.br.form['email'] = email
        password = getpass.getpass(Color('{autocyan}Please enter your password: {/autocyan}'))
        self.br.form['pass'] = password
        self.br.submit()

    def get_response(self):
        return self.br.response().read()

    def set_cookies(self):
        cookies = self.br._ua_handlers['_cookies'].cookiejar
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie.name] = cookie.value

        with open(self.CKS, 'w') as f:
            json.dump(cookie_dict, f)

    def get_cookies(self):
        with open(self.CKS) as f:
            cookies = json.load(f)

        return cookies

    def has_cookies(self):
        return os.path.exists(self.CKS)

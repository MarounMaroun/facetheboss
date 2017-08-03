import unittest

from faceboss.faceboss import Faceboss


class BaseTest(unittest.TestCase):

    def test_html_structure(self):
        """Verify the HTML structure is valid.

         By passing fake credentials, we can verify that we have attempted to login
         successfully by not getting an error and gracefully exit the application.
        """
        faceboss = Faceboss()
        with self.assertRaises(SystemExit):
            faceboss.login('fakemail', 'fakepass')

if __name__ == '__main__':
    unittest.main()

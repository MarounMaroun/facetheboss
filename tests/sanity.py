import uuid
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
            faceboss.login(BaseTest._get_random_str(), BaseTest._get_random_str())

    @staticmethod
    def _get_random_str():
        return str(uuid.uuid4().get_hex().upper()[:8])

if __name__ == '__main__':
    unittest.main()

import unittest

from run import create_app
from service.ResellerService import ResellerService


class Reseller(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()
        self.reseller_service = ResellerService()

    def test_01_add(self):
        reseller = {"cpf": ""}
        self.reseller_service.add(reseller)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

import unittest

from run import create_app
from util.CustomException import NotFoundException
from util.ResponseUtil import get_response, get_error_response


class ResponseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("config")
        ctx = self.app.app_context()
        ctx.push()

    def test_get_response(self):
        data = get_response("body", 200)
        assert data.data != ""
        assert data.status_code == 200

    def test_get_error_response(self):
        data = get_error_response(NotFoundException, 400)
        assert data.data != ""
        assert data.status_code == 400

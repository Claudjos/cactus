import unittest, logging
from ddt import ddt, file_data
from fir.wsgi import WSGIClient
from fir.http import Request
from cactus.flask import build_app_v2


logger = logging.getLogger("TEST")


@ddt
class TestFlaskV2(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.client = WSGIClient(build_app_v2("examples/v2/FunctionApp"))

	@file_data("data_v2.yaml")
	def test_requests(self, request, response):
		r = self.client.request(Request(**request))
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

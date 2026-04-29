import unittest, logging
from ddt import ddt, file_data
from fir.asgi import ASGIClient
from fir.http import Request
from cactus.fastapi import build_app_v2


logger = logging.getLogger("TEST")


@ddt
class TestFastAPI(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.client = ASGIClient(build_app_v2("examples/v2-fastapi/FunctionApp"))

	@file_data("data_v2-fastapi.yaml")
	def test_requests(self, request, response):
		r = self.client.request(Request(**request))
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

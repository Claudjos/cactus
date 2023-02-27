import unittest
from ddt import ddt, file_data
from fir.wsgi import Client
from fir.http import Request
from cactus.flask import build_app_v2
import logging


logger = logging.getLogger("TEST")
client = Client(build_app_v2("examples/v2/FunctionApp"))


@ddt
class TestCases(unittest.TestCase):

	@file_data("data_v2.yaml")
	def test_requests(self, request, response):
		r = client.request(Request(**request))
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

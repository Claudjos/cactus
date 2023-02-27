import unittest
from ddt import ddt, file_data
from fir.wsgi import Client
from fir.http import Request
from cactus.appfactory import build_app
import logging


logger = logging.getLogger("TEST")
client = Client(build_app("examples/v1/FunctionApp"))


@ddt
class TestCases(unittest.TestCase):

	@file_data("data.yaml")
	def test_requests(self, request, response):
		r = client.request(Request(**request))
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

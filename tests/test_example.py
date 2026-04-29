import unittest, logging
from ddt import ddt, file_data
from fir.wsgi import WSGIClient
from fir.http import Request
from cactus.appfactory import build_app


logger = logging.getLogger("TEST")


@ddt
class TestWebAppV1(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.client = WSGIClient(build_app("examples/v1/FunctionApp"))

	@file_data("data.yaml")
	def test_requests(self, request, response):
		r = self.client.request(Request(**request))
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

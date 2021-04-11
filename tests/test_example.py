import unittest
from ddt import ddt, file_data
from cactus.testing import CactusClient
from cactus.appfactory import build_app
import logging


logger = logging.getLogger("TEST")
app = build_app("examples/FunctionApp")
client = CactusClient(app)


@ddt
class TestCases(unittest.TestCase):

	@file_data("data.yaml")
	def test_requests(self, request, response):
		r = client.request(**request)
		logger.debug(r.get_body())
		assert r.status_code == response["status"]

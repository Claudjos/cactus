"""
Client to test the WSGI Application.
"""
from io import BytesIO
from typing import Union
from urllib.parse import urlparse
import azure.functions as func


class CactusClient:

	def __init__(self, app):
		self.app = app

	def request(self, method: str, url: str, headers: dict = None, 
		body: Union[bytes, str] = None) -> func.HttpResponse:
		if headers is None:
			headers = {}
		if body is None:
			body = b''
		if isinstance(body, str):
			body = body.encode()
		parsed = urlparse(url)
		environ = {
			"wsgi.input": BytesIO(body),
			"REQUEST_METHOD": method,
			"PATH_INFO": parsed.path,
			"RAW_URI": url,
			"QUERY_STRING": parsed.query,
		}
		for header in headers:
			key = "HTTP_{}".format(header.upper().replace("-", "_"))
			environ[key] = headers[header]
		if body != b'':
			environ["CONTENT_LENGTH"] = len(body)

		return self.app.process(environ)
		
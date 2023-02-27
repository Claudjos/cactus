import azure.functions as func
from json import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
	return func.HttpResponse(
		status_code=200,
		headers={
			"access-control-allow-origin": "fancy-site.com",
			"content-type": "application/json"
		},
		body=dumps({
			"endpoint": "info",
			"headers": {k: v for k, v in req.headers.items()},
			"params": {k: v for k, v in req.params.items()},
			"route_params": {k: v for k, v in req.route_params.items()},
			"body": req.get_body().decode()
		}).encode()
	)

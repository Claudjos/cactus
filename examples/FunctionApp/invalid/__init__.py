import azure.functions as func
from json import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
	return func.HttpResponse(
		status_code=200,
		body="A string value!"
	)

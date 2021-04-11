import azure.functions as func


def main(req: func.HttpRequest, msg) -> func.HttpResponse:
	return func.HttpResponse(status_code=200)

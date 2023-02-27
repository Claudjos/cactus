import azure.functions as func


app = func.FunctionApp()


@app.function_name(name="hello_world")
@app.route(route="hello_world")
def _hello_world(req: func.HttpRequest) -> func.HttpResponse:
	return func.HttpResponse(status_code=200, body="Hello World!")


@app.function_name(name="suggestions")
@app.route(route="suggestions", methods=["POST"])
def _suggestion(req: func.HttpRequest) -> func.HttpResponse:
	return func.HttpResponse(status_code=200, body="Noted!")

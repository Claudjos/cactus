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


@app.function_name(name="books")
@app.route(route="books/{book?}", methods=["GET"])
def _books(req: func.HttpRequest) -> func.HttpResponse:
	output = "Fetch: " + req.route_params.get("book", "all")
	return func.HttpResponse(status_code=200, body=output)


@app.function_name(name="files")
@app.route(route="files/{*file}", methods=["GET"])
def _file(req: func.HttpRequest) -> func.HttpResponse:
	output = "Path: " + req.route_params.get("file")
	return func.HttpResponse(status_code=200, body=output)

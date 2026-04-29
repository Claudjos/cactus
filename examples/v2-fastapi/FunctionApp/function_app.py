import azure.functions as func
from azurefunctions.extensions.http.fastapi import Request, StreamingResponse, JSONResponse


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


async def hello_world_generator():
	for word in ["Hello", " ", "World", "!"]:
		yield word


@app.function_name(name="stream_hello_world")
@app.route(route="stream_hello_world", methods=[func.HttpMethod.GET])
async def stream_hello_world(req: Request) -> StreamingResponse:
	return StreamingResponse(hello_world_generator(), media_type="text/plain")


@app.function_name(name="json_hello_world")
@app.route(route="json_hello_world", methods=[func.HttpMethod.GET])
async def json_hello_world(req: Request) -> JSONResponse:
	return JSONResponse({"message": "Hello World!"})

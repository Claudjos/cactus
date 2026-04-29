from typing import Union
from fastapi import FastAPI, APIRouter
from .route_info import ROUTE_INFO, parse_project_v2


def build_api_router(name: str, route_infos: list[ROUTE_INFO], prefix: str = "") -> APIRouter:
	router = APIRouter(prefix=prefix)
	for path, methods, handler, input_name in route_infos:
		adjusted_path = path if path.startswith("/") else f"/{path}"
		router.api_route(adjusted_path, methods=methods)(handler)
	return router


def build_app_v2(app: Union[str, "azure.functions.FunctionApp"]) -> FastAPI:
	if isinstance(app, str):
		return _build_app(parse_project_v2(app))
	else:
		return _build_app(from_app(app))


def _build_app(route_infos: list[ROUTE_INFO], name: str = "app") -> FastAPI:
	app = FastAPI()
	app.include_router(build_api_router(f"FunctionApp <{name}>", route_infos))
	return app

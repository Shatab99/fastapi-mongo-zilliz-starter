from fastapi import APIRouter, Depends
from controllers.user_controllers import router as user_router
from controllers.auth_controllers import router as auth_router

api_v1 = APIRouter()


routers = [
    {"controllers": user_router, "prefix": "/users", "tags": ["users"], "dependencies": []},
    {"controllers": auth_router, "prefix": "/auth", "tags": ["auth"], "dependencies": []},
]

for router in routers:
    api_v1.include_router(
        router["controllers"],
        prefix=router["prefix"],
        tags=router["tags"],
        dependencies=router["dependencies"]
    )

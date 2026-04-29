from fastapi import APIRouter
from services.auth_services import login_service

router = APIRouter()

router.post("/login")(login_service)
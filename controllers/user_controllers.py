from services.user_services import (
    getProfileService,
    register_user_service,
)
from fastapi import APIRouter, Depends
from contexts.middleware import verify_token

router = APIRouter()

router.post("/register") (register_user_service)
router.get("/me", dependencies=[Depends(verify_token("user"))])(getProfileService)

# testing public route
router.get("/public-posts")(
    lambda: {
        "posts": [
            {"id": 1, "title": "Public Post 1"},
            {"id": 2, "title": "Public Post 2"},
        ]
    }
)

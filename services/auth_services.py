from fastapi import HTTPException

from models.user_schemas import userLoginRequest
from contexts.collections import User
from helpers.auth_helpers import (
    create_access_token as create_unique_token,
    verify_access_token,
)
from helpers.security_utils import verify_password
from helpers.mongo_utils import format_one_with_password


async def login_service(request: userLoginRequest):
    email = request.email
    password = request.password
    user = format_one_with_password(await User().find_one({"email": email}))

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.get("is_active", False):
        raise HTTPException(status_code=403, detail="User account is not active")
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    

    uniqueToken = create_unique_token(
        {
            "_id": str(user["_id"]),
            "email": email,
            "name": user["name"],
            "role": user["role"],
        }
    )
    return {"message": "Login successful", "token": uniqueToken, "user": user}


async def verify_token_service(token: str):
    user = verify_access_token(token)
    return user

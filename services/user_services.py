from fastapi import HTTPException
from datetime import datetime, timezone
from models.user_schemas import userRegistrationRequest
from helpers.security_utils import hash_password
from contexts.collections import User 
from helpers.mongo_utils import format_one
from models.user_schemas import  UserModel



async def register_user_service(request: userRegistrationRequest):
    newUser = request.dict()
    
    existing_user = await User().find_one({"email": newUser["email"]})  
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    newUser["password"] = hash_password(newUser["password"])
    
    db_user = UserModel(**newUser)
    
    result = await User().insert_one(db_user.model_dump())
    
    return {
        "message": "User registered successfully",
        "user_id": str(result.inserted_id),
    }


async def getProfileService(decoded_payload: dict):
    user = format_one(await User().find_one({"email": decoded_payload["email"]}) )
    return {"user": user}

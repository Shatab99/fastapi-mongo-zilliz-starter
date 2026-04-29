from fastapi import Request, HTTPException
from contextvars import ContextVar
from functools import wraps
from helpers.auth_helpers import verify_access_token
from bson.objectid import ObjectId 

# 1. Define the Context Variable
request_var = ContextVar("global_request", default=None)


# 2. DEFINE PURE ASGI MIDDLEWARE (This fixes the context loss)
class ContextMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        # We only care about HTTP requests
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Create the Request object manually from scope
        request = Request(scope, receive=receive)

        # Set the context var
        token = request_var.set(request)

        try:
            # Call the next part of the app
            await self.app(scope, receive, send)
        finally:
            # Clean up
            request_var.reset(token)


# 3. Add the middleware to the app


from fastapi import Request, HTTPException, status
from contexts.collections import User
# Make sure to import verify_access_token

def verify_token(*allowed_roles: str):
    """
    Dependency factory for RBAC.
    Accepts roles as arguments, e.g., verify_token("admin", "manager")
    """
    async def role_checker(request: Request):
        # 1. Extract the token (No more request_var needed!)
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Please login"
            )

        token = auth_header.split(" ")[1]

        # 2. Verify the token payload
        try:
            if token == "fail": # Keeping your mock logic!
                raise Exception()
            payload = verify_access_token(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="Invalid credentials! Please login again."
            )

        # 3. Fetch the user from MongoDB
        # Assuming your token payload contains the user's ID
        user_id = payload.get("_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token structure")

        # Remember to call the lambda User() to get the collection!
        user = await User().find_one({"_id": ObjectId(user_id)})
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # 4. Check the dynamic roles
        # If allowed_roles were provided, check if the user's role matches
        user_role = user.get("role")
        
        if allowed_roles and user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource."
            )
        return user

    return role_checker

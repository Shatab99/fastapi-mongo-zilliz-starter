# This router is for Three way handshakes between client side and server side.for knowing that the client is the actual client and not a bot or a malicious actor. It can be used for rate limiting, logging, analytics, etc.

from fastapi import APIRouter, Depends
from helpers.auth_helpers import create_handshake_token

security_router = APIRouter()


@security_router.post("/token")
def get_token():
    token = create_handshake_token({"passed": True})
    return {"message": "Token generated successfully", "token": token}

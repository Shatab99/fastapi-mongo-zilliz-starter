from fastapi import Request, HTTPException, status
import jwt
from helpers.auth_helpers import verify_access_token

async def check_client(request: Request):
    
    # Uncomment this line if you are in dev mode
    # return True
    client_token = request.headers.get("X-Client-Token")

    if not client_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Missing client handshake token. Bot activity suspected."
        )

    try:
        payload = verify_access_token(client_token)
        if not payload.get("passed"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid handshake token structure."
            )

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Handshake token expired. Request too slow."
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid client token."
        )
    return True
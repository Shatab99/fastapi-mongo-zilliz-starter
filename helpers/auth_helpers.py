from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_handshake_token(data: dict) -> str:
    """
    Strictly generates a handshake token that expires in exactly 5 seconds.
    Impossible to override the expiration time.
    """
    to_encode = data.copy()

    # Strictly enforce the 5-second expiration
    expire = datetime.now(timezone.utc) + timedelta(seconds=5)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

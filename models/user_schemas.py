from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone

def get_current_time():
    return datetime.now(timezone.utc)


class UserModel(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool = False
    is_admin: bool = False
    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)
    last_login: datetime = None

class userRegistrationRequest(BaseModel):
    name: str
    email: str
    password: str
    
class userLoginRequest(BaseModel):
    email: str
    password: str

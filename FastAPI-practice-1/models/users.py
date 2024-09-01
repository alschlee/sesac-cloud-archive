from typing import List, Optional
from pydantic import BaseModel, EmailStr
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]]

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
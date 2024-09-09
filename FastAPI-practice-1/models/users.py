from typing import TYPE_CHECKING, List, Optional
from pydantic import BaseModel, EmailStr
# from models.events import Event
from sqlmodel import Field, Relationship, SQLModel

# 타입 힌트를 사용하여 순환 참조 방지
if TYPE_CHECKING:
    from models.events import Event

# 사용자 정보를 저장하는 데이터 모델 정의
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str
    username: str
    events: Optional[List["Event"]] = Relationship(back_populates="user")

# 사용자 등록 시 전달되는 데이터 모델 정의
class UserSignUp(SQLModel):
    email: EmailStr
    password: str
    username: str

# 로그인 시 전달되는 데이터 모델 정의
class UserSignIn(SQLModel):
    email: EmailStr
    password: str
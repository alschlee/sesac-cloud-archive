from typing import List, Optional
#from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column, JSON

#class Event(BaseModel):
#    id: int
#    title: str
#    image: str
#    description: str
#    tags: List[str]
#    location: str

class Event(SQLModel, table = True):
    id: int = Field(default=None, primary_key = True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(default=[], sa_column=Column(JSON))

# 이벤트 수정했을 때 전달되는 데이터 모델 정의
class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None